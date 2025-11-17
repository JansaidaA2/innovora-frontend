import streamlit as st
from utils.api_connect import generate_image_api, generate_video_api, check_backend_health
import time

st.set_page_config(
    page_title="INNOV ORA -The future of marketing content with AI",
    layout="wide",
    page_icon="🎯"
)

# ========================== ENHANCED CUSTOM CSS ==========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide default navigation */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Smooth animations */
    * {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Gradient header with animation */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 200% 200%;
        animation: gradientShift 8s ease infinite;
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .header-content {
        position: relative;
        z-index: 1;
    }
    
    .brand-title {
        color: white;
        margin: 0;
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 20px rgba(0,0,0,0.2);
    }
    
    .tagline {
        color: rgba(255, 255, 255, 0.95);
        margin-top: 1rem;
        font-size: 1.3rem;
        font-weight: 400;
        letter-spacing: 0.3px;
    }
    
    /* Enhanced stats card */
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.8rem 1.2rem;
        border-radius: 16px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.25);
        margin-bottom: 1rem;
        position: relative;
        overflow: hidden;
    }
    
    .stats-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .stats-card:hover::before {
        left: 100%;
    }
    
    .stats-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 32px rgba(102, 126, 234, 0.4);
    }
    
    .stats-number {
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    .stats-label {
        font-size: 0.95rem;
        opacity: 0.95;
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    /* Enhanced feature cards */
    .feature-card {
        background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
        border: 1px solid rgba(102, 126, 234, 0.2);
        padding: 2rem;
        border-radius: 16px;
        margin: 1rem 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        transform: scaleX(0);
        transition: transform 0.4s;
    }
    
    .feature-card:hover::before {
        transform: scaleX(1);
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 48px rgba(102, 126, 234, 0.35);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    /* Enhanced sidebar */
    .sidebar-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 16px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
    }
    
    .sidebar-brand {
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .sidebar-subtitle {
        font-size: 0.9rem;
        opacity: 0.9;
        font-weight: 500;
    }
    
    /* Enhanced button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1.05rem;
        letter-spacing: 0.3px;
        box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.5);
        background: linear-gradient(135deg, #7688f0 0%, #8659b0 100%);
    }
    
    .stButton>button:active {
        transform: translateY(-1px);
    }
    
    /* Enhanced metric cards */
    [data-testid="stMetricValue"] {
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    /* Smooth input fields */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    .stSelectbox>div>div>select {
        border-radius: 12px;
        border: 2px solid rgba(102, 126, 234, 0.2);
        transition: all 0.3s;
    }
    
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
    }
    
    /* Success/Warning/Error boxes */
    .stSuccess, .stWarning, .stError, .stInfo {
        border-radius: 12px;
        border-left-width: 4px;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        border-radius: 12px;
        font-weight: 600;
    }
    
    /* Image containers */
    [data-testid="stImage"] {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    
    /* Video containers */
    video {
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    }
    
    /* Status badges */
    .status-online {
        background: #4caf50;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .status-offline {
        background: #f44336;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ========================== CHECK BACKEND STATUS ==========================
if 'backend_status' not in st.session_state:
    st.session_state.backend_status = check_backend_health()

# ========================== ENHANCED SIDEBAR ==========================
with st.sidebar:
    st.markdown('''
    <div class="sidebar-card">
        <div class="sidebar-brand">🎯 INNOV ORA</div>
        <div class="sidebar-subtitle">The future of marketing content with AI</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Backend Status
    health = st.session_state.backend_status
    if isinstance(health, dict):
        status = health.get("status")
        message = health.get("message", "Unknown")
        response_time = health.get("response_time", 0)
        
        if status is True:
            st.markdown(f'<span class="status-online">✅ Online ({response_time:.1f}s)</span>', unsafe_allow_html=True)
        elif status is None:
            st.markdown('<span class="status-offline">⏱️ Cold Starting</span>', unsafe_allow_html=True)
            st.warning("⚠️ Backend is waking up (50-60s). Your first request will be slow.")
        else:
            st.markdown(f'<span class="status-offline">❌ {message}</span>', unsafe_allow_html=True)
            st.error("⚠️ Cannot connect to backend.")
    else:
        # Legacy boolean support
        if health:
            st.markdown('<span class="status-online">✅ Backend Online</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="status-offline">❌ Backend Offline</span>', unsafe_allow_html=True)
    
    if st.button("🔄 Refresh Status", use_container_width=True):
        with st.spinner("Checking backend..."):
            st.session_state.backend_status = check_backend_health()
        st.rerun()
    
    st.markdown("---")
    
    # Stats Section
    st.markdown("### 📊 Platform Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="stats-card">
            <p class="stats-number">2+</p>
            <p class="stats-label">AI Models</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="stats-card">
            <p class="stats-number">6+</p>
            <p class="stats-label">Ad Formats</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Guide
    st.markdown("### 📚 Quick Guide")
    with st.expander("📸 Image Generation", expanded=False):
        st.markdown("""
        **Steps:**
        1. Enter marketing text
        2. Choose ad format
        3. Click Generate!
        
        **Time:** ~10-30 seconds
        
        **Tip:** Clear, specific text = Better results
        """)
    
    with st.expander("🎬 Video Generation", expanded=False):
        st.markdown("""
        **Steps:**
        1. Write your script
        2. Choose avatar style
        3. Select background
        4. Generate video
        
        **Time:** ~1-3 minutes
        
        **Tip:** Scripts under 150 words work best
        """)
    
    st.markdown("---")
    
    # Features
    st.markdown("### ⚡ Features")
    st.success("✅ OpenAI DALL-E 3")
    st.success("✅ Google Gemini")
    st.success("✅ 3D Avatars")
    st.success("✅ Multiple Formats")
    st.success("✅ Instant Download")
    
    st.markdown("---")
    
    # Support
    st.markdown("### 💡 Need Help?")
    st.info("📧 support@innovora.ai\n\n🌐 innovora-backend.onrender.com")
    
    st.markdown("---")
    st.caption("Innovora © 2025 - All Rights Reserved")

# ========================== MAIN CONTENT ==========================
# Enhanced Hero Section
st.markdown("""
<div class="main-header">
    <div class="header-content">
        <h1 class="brand-title">🎯 INNOV ORA</h1>
        <p class="tagline">Multi-Model AI Generation: Images & Videos for Your Marketing Content</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Feature Highlights
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🎨 Models", "OpenAI", "Active")
with col2:
    st.metric("⚡ Speed", "10-30s", "Images")
with col3:
    st.metric("🎬 Video", "1-3min", "Generation")
with col4:
    st.metric("📊 Formats", "6+ Types", "Ready")

st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["🎨 Image Generation", "🎬 Video Generation", "📖 Examples & Tips"])

# ========================== IMAGE GENERATION TAB ==========================
with tab1:
    st.markdown("### 🎨 Create Marketing Visuals with AI")
    st.markdown("*Generate professional images powered by OpenAI DALL-E 3*")
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        brand = st.text_input("🏷️ Brand Name", placeholder="e.g., Innovora")
        brand_link = st.text_input("🔗 Brand Website Link", placeholder="https://innovora.ai")

        ad_text = st.text_area(
            "✍️ Describe Your Image", 
            placeholder="A futuristic AI robot in a cyberpunk city at night, neon lights, professional photography, 4K quality...", 
            height=150, 
            help="Be specific and detailed for best results"
        )
        
        # Character counter
        char_count = len(ad_text)
        st.caption(f"📊 Characters: {char_count} | Recommended: 50-500 characters")

    with col2:
        ad_format = st.selectbox(
            "📐 Ad Size / Format",
            [
                "Instagram Post (1080x1080)",
                "LinkedIn Post (1200x627)",
                "YouTube Thumbnail (1280x720)",
                "Facebook Ad (1200x628)",
                "Website Banner (1920x600)",
                "Poster (2480x3508)"
            ],
        )
        
        st.info("""
        **💡 Image Tips:**
        - Be specific and detailed
        - Mention style/mood
        - Include lighting details
        - Specify quality (4K, HD)
        - Use descriptive adjectives
        """)

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 Generate Image with AI", use_container_width=True, type="primary"):
        # Check backend status
        health = st.session_state.backend_status
        backend_offline = isinstance(health, dict) and health.get("status") is False
        
        if backend_offline:
            st.error("❌ Backend is offline. Please check the connection and try refreshing status.")
        elif not ad_text.strip():
            st.warning("⚠️ Please enter a description to generate an image.")
        elif char_count < 20:
            st.warning("⚠️ Please provide a more detailed description (at least 20 characters).")
        else:
            # Show cold start warning if needed
            if isinstance(health, dict) and health.get("status") is None:
                st.info("⏱️ Backend is cold starting. First request may take 60-90 seconds...")
            
            payload = {
                "brand_name": brand,
                "brand_link": brand_link,
                "prompt": ad_text,
                "ad_format": ad_format
            }

            
            start_time = time.time()
            
            with st.spinner("🎨 AI is creating your image... This takes 10-30 seconds"):
                result = generate_image_api(payload)
            
            elapsed_time = time.time() - start_time

            if result.get("status") == "success":
                st.success(f"✅ Image generated successfully in {elapsed_time:.1f} seconds!")
                
                st.markdown("---")
                st.markdown("#### 🖼️ Generated Image")

                res = result.get("results", {})
                openai_url = res.get("openai", "")
                
                if openai_url and not openai_url.startswith("OpenAI Error"):
                    col_img, col_info = st.columns([2, 1])
                    
                    with col_img:
                        st.image(openai_url, use_column_width=True, caption="Generated by DALL-E 3")
                    
                    with col_info:
                        st.markdown("#### 📊 Image Details")
                        st.write(f"**Model:** DALL-E 3")
                        st.write(f"**Format:** {ad_format}")
                        st.write(f"**Generation Time:** {elapsed_time:.1f}s")
                        st.markdown("---")
                        st.markdown(f"[⬇️ Download Image]({openai_url})")
                        st.caption("💡 Right-click and 'Save image as...'")
                        
                        # Show prompt
                        with st.expander("📝 View Prompt"):
                            st.code(ad_text)
                else:
                    st.error(f"❌ {openai_url}")
                
                # Show Gemini status
                gemini_msg = res.get("gemini", "")
                if gemini_msg:
                    st.info(f"ℹ️ Google Gemini: {gemini_msg}")
                    
            else:
                st.error(f"❌ Failed: {result.get('error', 'Unknown error occurred.')}")
                with st.expander("🔍 Error Details"):
                    st.json(result)

# ========================== VIDEO GENERATION TAB ==========================
with tab2:
    st.markdown("### 🎬 Generate AI Avatar Videos")
    st.markdown("*Create engaging video content with realistic 3D avatars*")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        video_text = st.text_area(
            "📝 Enter Your Script", 
            placeholder="Hello! Welcome to Innovora AI. We help businesses create amazing marketing content using advanced AI technology...",
            height=180,
            help="Write a clear, engaging script for your avatar"
        )
        
        # Character/word counter
        char_count = len(video_text)
        word_count = len(video_text.split())
        st.caption(f"📊 Characters: {char_count} | Words: {word_count} | Recommended: 50-150 words")
    
    with col2:
        st.markdown("#### 🎨 Video Settings")
        
        st.info("""
        **✨ Avatar Features:**
        - 🎯 Realistic lip-sync
        - 👁️ Natural blinking
        - 💼 Professional look
        - 🎥 HD Quality (640x360)
        - ⚡ Optimized generation
        - 🔊 Natural voice
        """)
        
        st.warning("""
        **⚠️ Free Tier Limits:**
        - Max 150 words
        - 1-3 min generation
        - First request: slower (cold start)
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🎞️ Generate Video", use_container_width=True, type="primary"):
        if not st.session_state.backend_status:
            st.error("❌ Backend is offline. Please check the connection.")
        elif not video_text.strip():
            st.warning("⚠️ Please enter text for video generation.")
        elif word_count > 150:
            st.warning(f"⚠️ Script is too long ({word_count} words). Please keep it under 150 words for optimal results.")
        elif word_count < 10:
            st.warning("⚠️ Script is too short. Please write at least 10 words.")
        else:
            start_time = time.time()
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("🎤 Generating audio...")
            progress_bar.progress(20)
            
            with st.spinner("🎬 Creating your AI avatar video... This may take 1-3 minutes..."):
                result = generate_video_api(video_text, "business", "professional")
                
            progress_bar.progress(100)
            elapsed_time = time.time() - start_time

            if result.get("status") == "success":
                status_text.empty()
                progress_bar.empty()
                
                st.success(f"✅ Video generated successfully in {elapsed_time:.1f} seconds!")
                
                st.markdown("---")
                
                col_video, col_info = st.columns([2, 1])
                
                with col_video:
                    st.markdown("#### 🎥 Your Generated Video")
                    video_url = result.get("video_url")
                    st.video(video_url)
                
                with col_info:
                    st.markdown("#### 📊 Video Details")
                    st.write(f"**Resolution:** 640x360")
                    st.write(f"**Frame Rate:** 15 FPS")
                    st.write(f"**Audio:** AI Voice (gTTS)")
                    st.write(f"**Generation Time:** {elapsed_time:.1f}s")
                    st.write(f"**Words:** {word_count}")
                    st.markdown("---")
                    st.markdown(f"[⬇️ Download Video]({video_url})")
                    st.caption("💡 Right-click and 'Save video as...'")
                    
                    # Show script
                    with st.expander("📝 View Script"):
                        st.text_area("Script:", video_text, height=150, disabled=True)

                # Show features
                features = result.get("features", [])
                if features:
                    st.markdown("#### ✨ Video Features")
                    for feature in features:
                        st.success(f"✅ {feature}")

            else:
                progress_bar.empty()
                status_text.empty()
                st.error(f"❌ Video generation failed: {result.get('error', 'Unknown error')}")
                
                if result.get('details'):
                    with st.expander("🔍 Technical Error Details"):
                        st.code(result.get('details'))

# ========================== EXAMPLES & TIPS TAB ==========================
with tab3:
    st.markdown("### 📖 Examples & Best Practices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎨 Image Generation Tips")
        
        with st.expander("✅ Good Examples", expanded=True):
            st.markdown("""
            **Example 1: Product Photography**
            ```
            Modern minimalist smartphone with gradient OLED display, 
            floating in clean white space, professional studio 
            photography, soft shadows, premium look, 4K quality
            ```
            
            **Example 2: Marketing Visual**
            ```
            Professional team collaboration in bright modern office, 
            diverse team members smiling, natural window lighting, 
            corporate blue and white colors, inspirational atmosphere
            ```
            
            **Example 3: Abstract/Creative**
            ```
            Futuristic AI robot with glowing blue circuits, 
            cyberpunk city background, neon purple and blue lights, 
            cinematic lighting, dramatic composition, highly detailed
            ```
            """)
        
        with st.expander("❌ What to Avoid"):
            st.markdown("""
            - ❌ Too vague: "nice picture"
            - ❌ Too short: "robot"
            - ❌ Conflicting styles: "modern vintage retro"
            - ❌ Copyrighted: "Mickey Mouse", "Nike logo"
            - ❌ Inappropriate content
            """)
        
        with st.expander("💡 Pro Tips"):
            st.markdown("""
            - ✅ Be specific about style (realistic, cartoon, 3D)
            - ✅ Mention lighting (soft, dramatic, natural)
            - ✅ Describe composition (close-up, wide angle)
            - ✅ Add quality keywords (4K, HD, professional)
            - ✅ Include mood/atmosphere
            """)
    
    with col2:
        st.markdown("#### 🎬 Video Script Tips")
        
        with st.expander("✅ Good Script Structure", expanded=True):
            st.markdown("""
            **Hook (5-10 seconds)**
            "Are you struggling with social media content?"
            
            **Problem (10-15 seconds)**
            "Most businesses waste hours creating content 
            that gets minimal engagement."
            
            **Solution (20-30 seconds)**
            "Innovora uses advanced AI to generate professional 
            marketing images and videos in seconds. No design 
            skills needed. Just describe what you want."
            
            **Call to Action (5-10 seconds)**
            "Try Innovora free today and transform your 
            marketing content!"
            
            **Total:** ~50-65 seconds, ~100 words ✅
            """)
        
        with st.expander("💡 Script Writing Tips"):
            st.markdown("""
            - ✅ Write conversationally (like talking to a friend)
            - ✅ Keep sentences short and clear
            - ✅ Use active voice ("We help" not "You are helped")
            - ✅ Include a clear call-to-action
            - ✅ Avoid jargon and complex terms
            - ✅ Test reading it out loud first
            """)
        
        with st.expander("⏱️ Timing Guide"):
            st.markdown("""
            - **10-20 words:** 5-10 seconds
            - **40-60 words:** 20-30 seconds
            - **80-100 words:** 40-50 seconds
            - **120-150 words:** 60-75 seconds
            
            💡 Speak at ~150 words per minute for clarity
            """)
    
    st.markdown("---")
    
    st.markdown("#### 🎯 Use Cases")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>📱 Social Media</h4>
            <p>Instagram posts, LinkedIn ads, Facebook campaigns, Twitter graphics, TikTok content</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🎬 Video Marketing</h4>
            <p>Product demos, explainer videos, testimonials, tutorials, announcements</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>💼 Business Content</h4>
            <p>Presentations, email campaigns, website banners, digital ads, reports</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sample Prompts
    st.markdown("#### 🎨 Ready-to-Use Prompts")
    
    with st.expander("Copy & Paste These Prompts"):
        st.markdown("""
        **Tech/Software:**
        ```
        Modern laptop displaying colorful code on screen, dark minimal workspace, 
        warm desk lamp, coffee mug, developer environment, professional photography
        ```
        
        **E-commerce:**
        ```
        Premium wireless headphones on marble surface, soft studio lighting, 
        luxury product photography, minimalist composition, matte black finish
        ```
        
        **Food & Beverage:**
        ```
        Fresh organic coffee being poured into white ceramic cup, steam rising, 
        rustic wooden table, morning sunlight, cozy café atmosphere, warm tones
        ```
        
        **Real Estate:**
        ```
        Modern luxury apartment living room, floor-to-ceiling windows, city view, 
        contemporary furniture, bright natural lighting, architectural photography
        ```
        
        **Fitness:**
        ```
        Athletic person doing yoga at sunrise, silhouette against orange sky, 
        peaceful outdoor setting, inspirational mood, cinematic composition
        ```
        """)
    
    st.markdown("---")
    
    st.info("""
    💡 **Pro Tip:** Experiment with different prompts and save the ones that work best! 
    The more specific you are, the better your results will be.
    """)
    
    st.success("🎉 Ready to create? Go to the Image or Video Generation tabs above!")