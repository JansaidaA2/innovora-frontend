# 🎯 Innovora.ai - Frontend

AI-powered marketing content generation platform. Create professional images and videos using OpenAI and custom avatars.

## Features
- 🎨 AI Image Generation (DALL-E 3)
- 🎬 AI Avatar Video Generation
- ⚡ Real-time backend health monitoring
- 📱 Responsive design

## Tech Stack
- **Frontend:** Streamlit 1.38.0
- **Backend:** Flask (deployed on Render)
- **APIs:** OpenAI DALL-E 3, gTTS

## Setup

### Prerequisites
- Python 3.9+
- Backend deployed at: https://innovora-backend.onrender.com

### Installation
```bash
# Clone repository
git clone <your-repo-url>
cd frontend

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

### Environment Variables
- `BACKEND_URL` - Backend API URL (default: https://innovora-backend.onrender.com)

## Deployment (Streamlit Community Cloud)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

## Project Structure
```
frontend/
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── utils/
│   └── api_connect.py       # Backend API connector
├── app.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## License
© 2025 Innovora.ai - All Rights Reserved