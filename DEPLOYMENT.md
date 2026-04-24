# PyCompile Deployment Guide

## 🚀 Step-by-Step Deployment

### Prerequisites
- GitHub account (for code hosting)
- Render/Railway account (for free hosting)

---

## 📦 OPTION 1: RENDER (Easiest for Beginners)

### Step 1: Prepare Code
```bash
git init
git add .
git commit -m "PyCompile Project"
git push origin main
```

### Step 2: Create Render Account
- Go to https://render.com
- Sign up with GitHub

### Step 3: Deploy Backend

1. Click "New +" → "Web Service"
2. Select your GitHub repository
3. Fill in:
   - **Name**: pycompile-backend
   - **Environment**: Python
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0`
4. Add Environment Variables:
   ```
   ALLOWED_ORIGINS=*.onrender.com
   DEBUG=False
   ```
5. Click "Deploy"

### Step 4: Deploy Frontend

1. Click "New +" → "Static Site"
2. Select your GitHub repository
3. Fill in:
   - **Name**: pycompile-frontend
   - **Build Command**: (leave empty)
   - **Publish directory**: `frontend`
4. Click "Deploy"

### Step 5: Connect Frontend to Backend

1. Get your backend URL from Render dashboard (e.g., https://pycompile-backend.onrender.com)
2. Edit `frontend/app.js`
3. Change: `const API_URL = 'http://localhost:8000/api'`
4. To: `const API_URL = 'https://pycompile-backend.onrender.com/api'`
5. Push changes - frontend will auto-redeploy

**✅ Done! Your app is live at the frontend URL**

---

## 🚂 OPTION 2: RAILWAY

### Step 1: Create Railway Account
- Go to https://railway.app
- Sign up

### Step 2: Deploy
1. Click "New Project" → "Deploy from GitHub"
2. Select repository
3. Railway auto-detects Python
4. Configure port as 8000
5. Deploy!

### Step 3: Update Frontend
- Get Railway URL
- Update `API_URL` in `frontend/app.js`

---

## 🐳 OPTION 3: DOCKER (Advanced)

### Deploy Backend on Any Cloud

```bash
docker build -f Dockerfile -t pycompile .
docker run -p 8000:8000 pycompile
```

### Deploy on Heroku
```bash
heroku create pycompile
heroku container:push web
heroku container:release web
```

---

## 🌐 CUSTOM DOMAIN

### Add Domain to Render
1. Go to Render Dashboard
2. Select your service
3. Settings → Custom Domain
4. Add your domain (e.g., compiler.yoursite.com)

---

## 🔒 Production Security Checklist

- [ ] Set `DEBUG=False`
- [ ] Update `ALLOWED_ORIGINS` with your domain
- [ ] Use HTTPS only
- [ ] Set execution timeout limits
- [ ] Monitor API usage
- [ ] Add rate limiting (coming soon)
- [ ] Enable CORS properly

---

## 📊 Monitoring & Logs

### Render Logs
1. Dashboard → Service → Logs

### Check Backend Health
```bash
curl https://your-backend-url.com/health
```

---

## 💰 Cost Breakdown

- **Render Free Tier**: $0/month (sleeps after 15 min inactivity)
- **Railway Free Tier**: ~$5 credit/month free
- **PythonAnywhere**: $0 for basic (with limitations)
- **Total**: **FREE** ✅

---

## 🆘 Troubleshooting

### Issue: CORS Error
**Solution**: 
```javascript
// In frontend/app.js, verify API_URL is correct
const API_URL = 'https://your-backend-url.com/api';
```

### Issue: Backend sleeping (Render)
**Solution**: Use Render Cron or upgrade for always-on

### Issue: Code execution fails
**Solution**: Check backend logs - might be Python module missing

---

## 📈 Next Steps

1. Add custom domain
2. Set up monitoring
3. Configure email alerts
4. Add rate limiting
5. Implement user authentication

---

**🎉 Congratulations! Your Python Compiler is live online!**
