# Frontend Documentation

## 🎨 UI Components

### Layout
- **Sidebar**: Navigation and theme toggle
- **Header**: Title and action buttons
- **Editor**: Code input area with line numbers
- **Output**: Execution result display
- **Tabs**: Editor, History, Settings

### Features

#### 🖊️ Code Editor
- Syntax highlighting via highlight.js
- Line numbers
- Tab support
- Font size adjustment (12-24px)
- Word wrap toggle

#### ▶️ Execution
- Real-time code execution
- Output console
- Error display
- Timeout protection

#### ⏱️ History
- Saves last 20 executions
- Quick reload
- Local browser storage
- Show execution time

#### ⚙️ Settings
- Font size control
- Word wrap toggle
- Execution timeout (5-30s)
- Theme selection

#### 🌙 Dark/Light Theme
- Auto-switches
- Persists in localStorage
- Professional VS Code style

---

## 🛠️ Customization

### Change Colors
Edit `:root` in `styles.css`:
```css
:root {
    --primary-bg: #1e1e1e;      /* Main background */
    --secondary-bg: #252526;    /* Sidebar background */
    --accent: #007acc;          /* Blue accents */
    --success: #6a9955;         /* Green for success */
    --error: #f48771;           /* Red for errors */
}
```

### Add Custom Font
In `styles.css`:
```css
@import url('https://fonts.googleapis.com/css2?family=YourFont');

body {
    font-family: 'YourFont', sans-serif;
}
```

### Change Logo
In `index.html`:
```html
<span class="logo-icon">🐍</span>  <!-- Change emoji here -->
<h1>PyCompile</h1>                <!-- Change name here -->
```

---

## 📱 API Integration

### Backend URL
Edit `app.js`:
```javascript
const API_URL = 'http://localhost:8000/api';  // Local
// OR
const API_URL = 'https://backend.onrender.com/api';  // Production
```

### API Response Handling
```javascript
// Success: { success: true, output: "..." }
// Error: { success: false, error: "..." }
```

---

## 💾 Local Storage

Auto-saves:
- Theme preference
- Font size
- Word wrap setting
- Timeout value
- Execution history (last 20)

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+Enter | Run code |
| Tab | Indent code |
| Ctrl+A | Select all |

---

## 🎯 Browser Compatibility

✅ Chrome (latest)
✅ Firefox (latest)
✅ Safari (latest)
✅ Edge (latest)

---

## 📦 Dependencies

- **highlight.js**: Syntax highlighting
- No other dependencies! (Pure vanilla JS)

---

## 🚀 Performance Optimization

- Lazy loading
- Efficient DOM updates
- Debounced input handlers
- Minimal redraws

---

## 🔒 Security

- No sensitive data stored
- Local storage only
- XSS protection via textContent
- Input sanitization

---

## 📝 Debugging

Open browser DevTools:
- F12 or Right-click → Inspect
- Console tab for JavaScript errors
- Network tab for API calls
- Local Storage for saved data

---

## 🎨 Design System

### Colors
- Primary: Dark backgrounds (#1e1e1e)
- Secondary: Medium backgrounds (#252526)
- Accent: Blue highlights (#007acc)
- Text: Light gray (#e0e0e0)

### Typography
- Heading: 24px bold
- Body: 14px regular
- Code: 13px monospace

### Spacing
- Small: 8px
- Medium: 12px
- Large: 16px
- XL: 20px

---

## 🚨 Error Handling

```javascript
// Network errors
"Error: Connection refused"

// Execution errors
"SyntaxError: invalid syntax"

// Timeout
"Execution timeout: Code exceeded 10 seconds"
```

---

## 📊 Supported Python Features

✅ Variables & operators
✅ Loops & conditionals
✅ Functions
✅ Lists & dictionaries
✅ String operations
✅ Math operations
✅ Import standard library
❌ External packages
❌ File I/O
❌ Network requests

---

## 🔄 Update Frequency

- UI updates on every keystroke
- Line numbers update with input
- History updates after execution
- Settings save immediately

---

## 🎪 Animations

- Smooth color transitions (0.3s)
- Hover effects on buttons
- Loading spinner animation
- Slide transitions on tabs

---

## 📞 Support

For issues, check:
1. Browser console (F12)
2. Network requests (Network tab)
3. localStorage (Application tab)
4. Backend logs

