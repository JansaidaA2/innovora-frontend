import streamlit as st
from utils.api_connect import check_backend_health
from utils.styles import load_custom_css

# Page config
st.set_page_config(
    page_title="INNOV ORA - AI Marketing Platform",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_custom_css()

# Initialize session state
if 'backend_status' not in st.session_state:
    st.session_state.backend_status = check_backend_health()

# ========================== SIDEBAR ==========================
with st.sidebar:
    st.markdown('''
    <div class="sidebar-brand">
        <h1>🎯 INNOV ORA</h1>
        <p>AI Marketing Platform</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Backend Status
    st.markdown("### 🔌 System Status")
    health = st.session_state.backend_status
    
    if isinstance(health, dict):
        status = health.get("status")
        response_time = health.get("response_time", 0)
        
        if status is True:
            st.success(f"✅ Online ({response_time:.1f}s)")
        elif status is None:
            st.warning("⏱️ Cold Starting (50-60s)")
        else:
            st.error(f"❌ {health.get('message', 'Offline')}")
    
    if st.button("🔄 Refresh Status", use_container_width=True):
        with st.spinner("Checking..."):
            st.session_state.backend_status = check_backend_health()
        st.rerun()
    
    st.markdown("---")
    
    # Quick Stats
    st.markdown("### 📊 Platform Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("AI Models", "2+", "OpenAI")
    with col2:
        st.metric("Formats", "6+", "Ready")
    
    st.markdown("---")
    
    # Features
    st.markdown("### ⚡ Features")
    st.info("🎨 DALL-E 3 Integration")
    st.info("🎬 AI Avatar Videos")
    st.info("📐 Multiple Ad Formats")
    st.info("⚡ Fast Generation")
    
    st.markdown("---")
    st.caption("© 2025 Innovora - All Rights Reserved")

# ========================== MAIN CONTENT ==========================

# Hero Section
st.markdown('''
<div class="hero-section">
    <h1>🎯 Welcome to INNOV ORA</h1>
    <p class="hero-subtitle">Transform Your Marketing with AI-Powered Content Generation</p>
    <p class="hero-description">
        Create professional images and engaging videos in minutes, not hours.
        Powered by cutting-edge AI technology.
    </p>
</div>
''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Key Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('''
    <div class="metric-card">
        <div class="metric-icon">🎨</div>
        <div class="metric-value">10-30s</div>
        <div class="metric-label">Image Generation</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="metric-card">
        <div class="metric-icon">🎬</div>
        <div class="metric-value">1-3min</div>
        <div class="metric-label">Video Creation</div>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="metric-card">
        <div class="metric-icon">📐</div>
        <div class="metric-value">6+</div>
        <div class="metric-label">Ad Formats</div>
    </div>
    ''', unsafe_allow_html=True)

with col4:
    st.markdown('''
    <div class="metric-card">
        <div class="metric-icon">⚡</div>
        <div class="metric-value">HD</div>
        <div class="metric-label">Quality Output</div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Features Section
st.markdown("## 🚀 What Can You Create?")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    <div class="feature-card">
        <h3>🎨 AI Image Generation</h3>
        <p>Create stunning marketing visuals using OpenAI's DALL-E 3</p>
        <ul>
            <li>✅ Instagram & Social Media Posts</li>
            <li>✅ YouTube Thumbnails</li>
            <li>✅ Facebook Ads</li>
            <li>✅ Website Banners</li>
            <li>✅ Professional Posters</li>
            <li>✅ Custom Ad Formats</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)
    
    if st.button("🎨 Start Creating Images", use_container_width=True, type="primary"):
        st.switch_page("pages/1_🎨_Image_Generation.py")

with col2:
    st.markdown('''
    <div class="feature-card">
        <h3>🎬 AI Video Generation</h3>
        <p>Generate professional avatar videos with realistic 3D characters</p>
        <ul>
            <li>✅ Realistic Lip-Sync</li>
            <li>✅ Natural Blinking & Gestures</li>
            <li>✅ Professional Avatars</li>
            <li>✅ Custom Backgrounds</li>
            <li>✅ AI Voice Synthesis</li>
            <li>✅ HD Quality Output</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)
    
    if st.button("🎬 Start Creating Videos", use_container_width=True, type="primary"):
        st.switch_page("pages/2_🎬_Video_Generation.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# How It Works
st.markdown("## 💡 How It Works")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
    <div class="step-card">
        <div class="step-number">1</div>
        <h4>📝 Describe</h4>
        <p>Write what you want to create. Be specific and detailed for best results.</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="step-card">
        <div class="step-number">2</div>
        <h4>⚡ Generate</h4>
        <p>Our AI processes your request and creates professional content in seconds.</p>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="step-card">
        <div class="step-number">3</div>
        <h4>⬇️ Download</h4>
        <p>Download your high-quality images or videos ready for immediate use.</p>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Use Cases
st.markdown("## 🎯 Perfect For")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('''
    <div class="use-case-card">
        <div class="use-case-icon">📱</div>
        <h5>Social Media</h5>
        <p>Instagram, LinkedIn, Facebook, Twitter</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="use-case-card">
        <div class="use-case-icon">💼</div>
        <h5>Marketing</h5>
        <p>Ads, Campaigns, Promotions</p>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="use-case-card">
        <div class="use-case-icon">🎓</div>
        <h5>Education</h5>
        <p>Tutorials, Explainers, Demos</p>
    </div>
    ''', unsafe_allow_html=True)

with col4:
    st.markdown('''
    <div class="use-case-card">
        <div class="use-case-icon">🏢</div>
        <h5>Business</h5>
        <p>Presentations, Reports, Content</p>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# CTA Section
st.markdown('''
<div class="cta-section">
    <h2>Ready to Transform Your Marketing?</h2>
    <p>Choose a tool from the sidebar to get started</p>
</div>
''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Quick Links
st.markdown("### 🔗 Quick Navigation")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎨 Image Generation →", use_container_width=True):
        st.switch_page("pages/1_🎨_Image_Generation.py")

with col2:
    if st.button("🎬 Video Generation →", use_container_width=True):
        st.switch_page("pages/2_🎬_Video_Generation.py")

with col3:
    if st.button("📖 Examples & Tips →", use_container_width=True):
        st.switch_page("pages/3_📖_Examples_Tips.py")