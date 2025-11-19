import streamlit as st
import sys
import os
import time

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.api_connect import generate_video_api, check_backend_health
from utils.styles import load_custom_css

# Page config
st.set_page_config(
    page_title="Video Generation - INNOV ORA",
    page_icon="🎬",
    layout="wide"
)

# Load styles
load_custom_css()

# Initialize backend status
if 'backend_status' not in st.session_state:
    st.session_state.backend_status = check_backend_health()

# Page Header
st.markdown('''
<div class="page-title">
    <h1>🎬 AI Video Generation</h1>
    <p>Create professional videos with realistic 3D avatars</p>
</div>
''', unsafe_allow_html=True)

# Quick Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("⚡ Speed", "1-3min", "Generation")
with col2:
    st.metric("🎥 Quality", "640x360", "HD Ready")
with col3:
    st.metric("🎭 Avatars", "3D", "Realistic")
with col4:
    st.metric("🔊 Voice", "AI TTS", "Natural")

st.markdown("---")

# Main Form
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Write Your Script")
    
    video_text = st.text_area(
        "🎤 Video Script",
        placeholder="Example: Hello! Welcome to Innovora AI. We help businesses create amazing marketing content using advanced artificial intelligence. Our platform generates professional images and engaging videos in minutes, not hours. Try Innovora today and transform your marketing!",
        height=250,
        help="Write a clear, engaging script. Best results with 50-150 words."
    )
    
    # Analytics
    char_count = len(video_text)
    word_count = len(video_text.split())
    estimated_duration = word_count / 2.5  # ~150 words per minute = 2.5 words per second
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if word_count < 10:
            st.metric("📝 Words", word_count, "⚠️ Too short")
        elif word_count > 150:
            st.metric("📝 Words", word_count, "⚠️ Too long")
        else:
            st.metric("📝 Words", word_count, "✅ Good")
    
    with col_b:
        st.metric("📊 Characters", char_count)
    
    with col_c:
        st.metric("⏱️ Est. Duration", f"{estimated_duration:.0f}s")
    
    if word_count > 150:
        st.warning("⚠️ Script is quite long. Consider keeping it under 150 words for optimal results on free tier.")
    elif word_count < 10:
        st.info("💡 Add more content to your script for a better video.")

with col2:
    st.markdown("### ⚙️ Video Settings")
    
    style = st.selectbox(
        "🎨 Avatar Style",
        ["business", "casual", "professional", "friendly"],
        help="Choose the avatar's appearance style"
    )
    
    background = st.selectbox(
        "🖼️ Background",
        ["professional", "gradient", "office", "modern"],
        help="Select background type"
    )
    
    st.markdown("---")
    
    st.info("""
    **✨ Video Features:**
    - 🎯 Realistic lip-sync
    - 👁️ Natural blinking
    - 💼 Professional look
    - 🎥 HD Quality output
    - 🔊 AI voice synthesis
    - ⚡ Fast generation
    """)
    
    st.markdown("---")
    
    st.warning("""
    **⚠️ Free Tier Limits:**
    - Max 150 words
    - 1-3 min generation
    - First request slower
    """)
    
    st.markdown("---")
    
    # Backend status
    health = st.session_state.backend_status
    if isinstance(health, dict):
        if health.get("status") is True:
            st.success("✅ Backend Online")
        elif health.get("status") is None:
            st.warning("⏱️ Cold Starting")
        else:
            st.error("❌ Backend Offline")

st.markdown("<br>", unsafe_allow_html=True)

# Generate Button
if st.button("🎞️ Generate Video", use_container_width=True, type="primary", key="generate_video_btn"):
    # Validation
    health = st.session_state.backend_status
    backend_offline = isinstance(health, dict) and health.get("status") is False
    
    if backend_offline:
        st.error("❌ Backend is offline. Please refresh the status and try again.")
    elif not video_text.strip():
        st.warning("⚠️ Please enter text for video generation.")
    elif word_count > 150:
        st.warning(f"⚠️ Script is too long ({word_count} words). Please keep it under 150 words.")
    elif word_count < 10:
        st.warning("⚠️ Script is too short. Please write at least 10 words.")
    else:
        # Show cold start warning
        if isinstance(health, dict) and health.get("status") is None:
            st.info("⏱️ Backend is cold starting. First request may take 2-4 minutes...")
        
        start_time = time.time()
        
        # Progress indicator
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("🎤 Generating audio...")
        progress_bar.progress(20)
        time.sleep(0.5)
        
        status_text.text("🎭 Creating avatar...")
        progress_bar.progress(40)
        time.sleep(0.5)
        
        status_text.text("🎬 Rendering video...")
        progress_bar.progress(60)
        
        with st.spinner("🎬 Creating your AI avatar video... This may take 1-3 minutes..."):
            result = generate_video_api(video_text, style, background)
        
        progress_bar.progress(100)
        elapsed_time = time.time() - start_time
        
        # Clear progress
        progress_bar.empty()
        status_text.empty()
        
        # Handle results
        if result.get("status") == "success":
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
                st.write(f"**Style:** {style.title()}")
                st.write(f"**Background:** {background.title()}")
                st.write(f"**Generation Time:** {elapsed_time:.1f}s")
                st.write(f"**Script Words:** {word_count}")
                
                st.markdown("---")
                
                st.markdown(f"[⬇️ Download Video]({video_url})")
                st.caption("💡 Right-click and 'Save video as...'")
                
                st.markdown("---")
                
                # Show script
                with st.expander("📝 View Script"):
                    st.text_area("Script:", video_text, height=150, disabled=True)
                
                # Share options
                with st.expander("📤 Share Options"):
                    st.code(video_url, language="text")
                    st.caption("Copy this URL to share")
            
            # Show features
            features = result.get("features", [])
            if features:
                st.markdown("---")
                st.markdown("#### ✨ Video Features")
                feature_cols = st.columns(len(features))
                for i, feature in enumerate(features):
                    with feature_cols[i]:
                        st.success(f"✅ {feature}")
        
        else:
            st.error(f"❌ Video generation failed: {result.get('error', 'Unknown error')}")
            
            if result.get('details'):
                with st.expander("🔍 Technical Details"):
                    st.code(result.get('details'))

# Tips Section
st.markdown("---")
st.markdown("### 💡 Script Writing Tips")

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("✅ Good Script Structure"):
        st.markdown("""
        **Hook (5-10s)**
        Start with a question or bold statement
        
        **Problem (10-15s)**
        Describe the challenge or pain point
        
        **Solution (20-30s)**
        Explain how your product/service helps
        
        **Call to Action (5-10s)**
        Clear next step for viewers
        
        **Total: ~50-65 seconds ✅**
        """)

with col2:
    with st.expander("💡 Writing Best Practices"):
        st.markdown("""
        - Write conversationally
        - Keep sentences short
        - Use active voice
        - Avoid jargon
        - Include a CTA
        - Test by reading aloud
        - ~150 words per minute
        """)

with col3:
    with st.expander("⏱️ Timing Guide"):
        st.markdown("""
        - **10-20 words:** 5-10 seconds
        - **40-60 words:** 20-30 seconds
        - **80-100 words:** 40-50 seconds
        - **120-150 words:** 60-75 seconds
        
        💡 Aim for clarity over speed
        """)

# Sample Scripts
st.markdown("---")
st.markdown("### 📝 Sample Scripts")

col1, col2 = st.columns(2)

with col1:
    with st.expander("🏢 Business Introduction"):
        sample1 = """Welcome to Innovora AI! We're revolutionizing marketing content creation. Our platform uses cutting-edge artificial intelligence to generate professional images and engaging videos in minutes. No design skills needed. Just describe what you want, and our AI brings it to life. Join thousands of businesses transforming their marketing. Try Innovora free today!"""
        st.text_area("Script:", sample1, height=150, disabled=True, key="sample1")
        if st.button("📋 Use This Script", key="use1"):
            st.session_state.script = sample1
            st.info("✅ Script copied! Scroll up to generate.")

with col2:
    with st.expander("🎯 Product Demo"):
        sample2 = """Struggling with social media content? Innovora AI has the solution. Our intelligent platform creates stunning visuals and videos automatically. Simply enter your text, choose a format, and watch as AI generates professional-quality content. Perfect for Instagram, LinkedIn, YouTube, and more. Start creating amazing content today. Visit innovora.ai to get started!"""
        st.text_area("Script:", sample2, height=150, disabled=True, key="sample2")
        if st.button("📋 Use This Script", key="use2"):
            st.session_state.script = sample2
            st.info("✅ Script copied! Scroll up to generate.")

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("🎨 Try Image Generation", use_container_width=True):
        st.switch_page("pages/1_🎨_Image_Generation.py")

with col3:
    if st.button("📖 View Examples", use_container_width=True):
        st.switch_page("pages/3_📖_Examples_Tips.py")