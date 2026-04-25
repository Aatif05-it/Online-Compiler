// Configuration
const runtimeApiUrl =
    window.RUNTIME_CONFIG && typeof window.RUNTIME_CONFIG.API_URL === 'string'
        ? window.RUNTIME_CONFIG.API_URL.trim().replace(/\/$/, '')
        : '';

const API_URL = runtimeApiUrl ||
    (window.location.hostname === 'localhost' ? 'http://localhost:8000/api' : '');
let executionHistory = [];
let theme = localStorage.getItem('theme') || 'dark';
let timeout = 10;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    applyTheme();
    loadExecutionHistory();
    setupCodeEditor();
    setKeybindings();
});

// Theme Toggle
function toggleTheme() {
    theme = theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', theme);
    applyTheme();
}

function applyTheme() {
    if (theme === 'light') {
        document.body.classList.add('light-mode');
        document.getElementById('theme-icon').textContent = '\u25cb';
    } else {
        document.body.classList.remove('light-mode');
        document.getElementById('theme-icon').textContent = '\u25d0';
    }
}

// Tab Switching
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from buttons
    document.querySelectorAll('.menu-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName + '-tab').classList.add('active');
    
    // Add active class to button
    event.target.closest('.menu-btn').classList.add('active');
}

// Code Editor Setup
function setupCodeEditor() {
    const textarea = document.getElementById('code-input');
    
    // Set default code
    textarea.value = '# Write your Python code here...\nprint("Hello, World!")\nx = 5\ny = 10\nprint(f"Sum: {x + y}")';
}

// Keybindings
function setKeybindings() {
    document.getElementById('code-input').addEventListener('keydown', (e) => {
        // Tab key
        if (e.key === 'Tab') {
            e.preventDefault();
            const start = e.target.selectionStart;
            const end = e.target.selectionEnd;
            e.target.value = e.target.value.substring(0, start) + '\t' + e.target.value.substring(end);
            e.target.selectionStart = e.target.selectionEnd = start + 1;
        }
        
        // Ctrl+Enter to run
        if (e.ctrlKey && e.key === 'Enter') {
            runCode();
        }
    });
}

function countInputCalls(code) {
    const matches = code.match(/\binput\s*\(/g);
    return matches ? matches.length : 0;
}

function countProvidedInputLines(userInput) {
    if (!userInput || !userInput.trim()) {
        return 0;
    }
    return userInput.trimEnd().split(/\r?\n/).length;
}

// Run Code
async function runCode() {
    const code = document.getElementById('code-input').value;
    const userInput = document.getElementById('user-input').value;
    const outputDiv = document.getElementById('output');
    const loader = document.getElementById('loader');
    
    if (!code.trim()) {
        addOutput('Please write some code first!', 'error');
        return;
    }

    if (!API_URL) {
        addOutput('API URL is not configured. Set window.RUNTIME_CONFIG.API_URL in frontend/config.js', 'error');
        return;
    }

    const inputCalls = countInputCalls(code);
    const inputLines = countProvidedInputLines(userInput);
    if (inputCalls > 0 && inputLines < inputCalls) {
        addOutput(
            `Input mismatch: code has ${inputCalls} input() call(s), but only ${inputLines} input line(s) provided.\nAdd one input value per line in User Input.`,
            'error'
        );
        return;
    }
    
    loader.classList.remove('hidden');
    outputDiv.innerHTML = '';
    
    try {
        const response = await fetch(`${API_URL}/execute`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: code,
                user_input: userInput || null,
                timeout: timeout
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            if (data.output) {
                addOutput(data.output, 'success');
            }
            addHistoryEntry(code, true, data.output);
        } else {
            addOutput('Actual Python Error:\n' + (data.error || 'Execution failed'), 'error');
            addHistoryEntry(code, false, data.error);
        }
    } catch (error) {
        addOutput('Error: ' + error.message, 'error');
        addHistoryEntry(code, false, error.message);
    } finally {
        loader.classList.add('hidden');
    }
}

// Add Output Line
function addOutput(text, type = 'info') {
    const outputDiv = document.getElementById('output');
    const line = document.createElement('div');
    line.className = 'output-line ' + type;
    line.textContent = text;
    outputDiv.appendChild(line);
    outputDiv.scrollTop = outputDiv.scrollHeight;
}

// Clear Output
function clearOutput() {
    document.getElementById('output').innerHTML = '';
}

// Reset Code
function resetCode() {
    if (confirm('Are you sure you want to reset the code?')) {
        document.getElementById('code-input').value = '# Write your Python code here...\nprint("Hello, World!")';
        clearOutput();
    }
}

// Font Size
function changeFontSize(size) {
    document.getElementById('code-input').style.fontSize = size + 'px';
    document.getElementById('font-size-value').textContent = size + 'px';
    localStorage.setItem('fontSize', size);
}

// Word Wrap
function toggleWrap(enabled) {
    const textarea = document.getElementById('code-input');
    textarea.style.overflowX = enabled ? 'hidden' : 'auto';
    textarea.style.whiteSpace = enabled ? 'pre-wrap' : 'pre';
    localStorage.setItem('wordWrap', enabled);
}

// Timeout Setting
function setTimout(value) {
    timeout = parseInt(value);
    localStorage.setItem('timeout', timeout);
}

// Execution History
function addHistoryEntry(code, success, output) {
    const entry = {
        timestamp: new Date().toLocaleString(),
        code: code.substring(0, 100),
        success: success,
        output: output.substring(0, 200)
    };
    
    executionHistory.unshift(entry);
    if (executionHistory.length > 20) executionHistory.pop();
    
    localStorage.setItem('executionHistory', JSON.stringify(executionHistory));
    updateHistoryUI();
}

function loadExecutionHistory() {
    const saved = localStorage.getItem('executionHistory');
    if (saved) {
        executionHistory = JSON.parse(saved);
        updateHistoryUI();
    }
}

function updateHistoryUI() {
    const historyList = document.getElementById('history-list');
    
    if (executionHistory.length === 0) {
        historyList.innerHTML = '<p style="color: var(--text-secondary);">No execution history yet</p>';
        return;
    }
    
    historyList.innerHTML = executionHistory.map((entry, index) => `
        <div class="history-item" onclick="loadFromHistory(${index})">
            <div class="history-top-row">
                <div class="history-time">${entry.timestamp}</div>
                <button class="history-delete-btn" onclick="deleteHistoryEntry(event, ${index}); return false;" title="Delete this history entry" aria-label="Delete history item">Delete</button>
            </div>
            <div class="history-code">${escapeHtml(entry.code)}</div>
            <div class="history-status ${entry.success ? 'success' : 'error'}">
                ${entry.success ? '✓ Success' : '✗ Error'}
            </div>
        </div>
    `).join('');
}

function deleteHistoryEntry(event, index) {
    event.stopPropagation();
    executionHistory.splice(index, 1);
    localStorage.setItem('executionHistory', JSON.stringify(executionHistory));
    updateHistoryUI();
}

function loadFromHistory(index) {
    const entry = executionHistory[index];
    document.getElementById('code-input').value = entry.code;
    switchTab('editor');
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Load Saved Settings
window.addEventListener('load', () => {
    const fontSize = localStorage.getItem('fontSize');
    const wordWrap = localStorage.getItem('wordWrap');
    const savedTimeout = localStorage.getItem('timeout');
    
    if (fontSize) {
        document.getElementById('font-size').value = fontSize;
        document.getElementById('code-input').style.fontSize = fontSize + 'px';
        document.getElementById('font-size-value').textContent = fontSize + 'px';
    }
    
    if (wordWrap === 'true') {
        document.getElementById('wrap-toggle').checked = true;
        toggleWrap(true);
    }
    
    if (savedTimeout) {
        document.getElementById('timeout').value = savedTimeout;
        timeout = parseInt(savedTimeout);
    }
});
