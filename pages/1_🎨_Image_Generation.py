import streamlit as st
import sys
import os
import time

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.api_connect import generate_image_api, check_backend_health
from utils.styles import load_custom_css

# Page config
st.set_page_config(
    page_title="Image Generation - INNOV ORA",
    page_icon="🎨",
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
    <h1>🎨 AI Image Generation</h1>
    <p>Create stunning marketing visuals with OpenAI DALL-E 3</p>
</div>
''', unsafe_allow_html=True)

# Quick Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("⚡ Speed", "10-30s", "Fast")
with col2:
    st.metric("🤖 Model", "DALL-E 3", "Active")
with col3:
    st.metric("📐 Formats", "6 Types", "Available")
with col4:
    st.metric("✨ Quality", "HD/4K", "Premium")

st.markdown("---")

# Main Form
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### ✍️ Describe Your Image")
    
    brand = st.text_input(
        "🏷️ Brand Name (Optional)",
        placeholder="e.g., Innovora, TechCorp, MyBrand",
        help="Add your brand name to the image description"
    )
    
    brand_link = st.text_input(
        "🔗 Brand Website (Optional)",
        placeholder="https://example.com",
        help="Your brand website for reference"
    )
    
    ad_text = st.text_area(
        "🎨 Image Description",
        placeholder="Example: A futuristic AI robot in a cyberpunk city at night, neon purple and blue lights, professional photography, cinematic composition, 4K quality, highly detailed...",
        height=200,
        help="Be specific and detailed for best results. Mention style, lighting, mood, and quality."
    )
    
    # Character counter
    char_count = len(ad_text)
    word_count = len(ad_text.split())
    
    if char_count < 20:
        st.caption(f"📊 {char_count} characters | {word_count} words | ⚠️ Too short - add more details")
    elif char_count > 500:
        st.caption(f"📊 {char_count} characters | {word_count} words | ⚠️ Consider shortening")
    else:
        st.caption(f"📊 {char_count} characters | {word_count} words | ✅ Good length")

with col2:
    st.markdown("### ⚙️ Settings")
    
    ad_format = st.selectbox(
        "📐 Image Format",
        [
            "Instagram Post (1080x1080)",
            "LinkedIn Post (1200x627)",
            "YouTube Thumbnail (1280x720)",
            "Facebook Ad (1200x628)",
            "Website Banner (1920x600)",
            "Poster (2480x3508)"
        ],
        help="Choose the format that matches your needs"
    )
    
    st.markdown("---")
    
    st.info("""
    **💡 Pro Tips:**
    - Be specific about style
    - Mention lighting details
    - Include mood/atmosphere
    - Add quality keywords (4K, HD)
    - Use descriptive adjectives
    """)
    
    st.markdown("---")
    
    # Backend status indicator
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
if st.button("🚀 Generate Image with AI", use_container_width=True, type="primary", key="generate_btn"):
    # Validation
    health = st.session_state.backend_status
    backend_offline = isinstance(health, dict) and health.get("status") is False
    
    if backend_offline:
        st.error("❌ Backend is offline. Please refresh the status and try again.")
    elif not ad_text.strip():
        st.warning("⚠️ Please enter a description to generate an image.")
    elif char_count < 20:
        st.warning("⚠️ Please provide a more detailed description (at least 20 characters).")
    else:
        # Show cold start warning
        if isinstance(health, dict) and health.get("status") is None:
            st.info("⏱️ Backend is cold starting. First request may take 60-90 seconds...")
        
        # Prepare payload
        payload = {
            "brand_name": brand,
            "brand_link": brand_link,
            "prompt": ad_text,
            "ad_format": ad_format
        }
        
        start_time = time.time()
        
        # Progress indicator
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("🎨 Initializing AI model...")
        progress_bar.progress(20)
        
        with st.spinner("🎨 AI is creating your image..."):
            result = generate_image_api(payload)
        
        progress_bar.progress(100)
        elapsed_time = time.time() - start_time
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        # Handle results
        if result.get("status") == "success":
            st.success(f"✅ Image generated successfully in {elapsed_time:.1f} seconds!")
            
            st.markdown("---")
            
            res = result.get("results", {})
            openai_url = res.get("openai", "")
            
            if openai_url and not openai_url.startswith("OpenAI Error"):
                col_img, col_info = st.columns([2, 1])
                
                with col_img:
                    st.markdown("#### 🖼️ Your Generated Image")
                    st.image(openai_url, use_column_width=True, caption="Generated by DALL-E 3")
                
                with col_info:
                    st.markdown("#### 📊 Image Details")
                    st.write(f"**Model:** OpenAI DALL-E 3")
                    st.write(f"**Format:** {ad_format}")
                    st.write(f"**Generation Time:** {elapsed_time:.1f}s")
                    st.write(f"**Resolution:** High Quality")
                    
                    st.markdown("---")
                    
                    st.markdown(f"[⬇️ Download Image]({openai_url})")
                    st.caption("💡 Right-click and 'Save image as...'")
                    
                    st.markdown("---")
                    
                    # Show prompt used
                    with st.expander("📝 View Full Prompt"):
                        st.text_area("Prompt:", ad_text, height=150, disabled=True)
                    
                    # Share options
                    with st.expander("📤 Share Options"):
                        st.code(openai_url, language="text")
                        st.caption("Copy this URL to share")
            else:
                st.error(f"❌ Generation failed: {openai_url}")
            
            # Show Gemini info if available
            gemini_msg = res.get("gemini", "")
            if gemini_msg and not gemini_msg.startswith("Error"):
                st.info(f"ℹ️ Google Gemini: {gemini_msg}")
        
        else:
            st.error(f"❌ Generation failed: {result.get('error', 'Unknown error occurred')}")
            with st.expander("🔍 Error Details"):
                st.json(result)

# Tips Section
st.markdown("---")
st.markdown("### 💡 Quick Tips for Better Results")

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("✅ Good Prompt Examples"):
        st.markdown("""
        **Product Photo:**
        ```
        Premium wireless headphones on marble 
        surface, soft studio lighting, luxury 
        product photography, minimalist 
        composition, matte black finish, 4K
        ```
        
        **Marketing Visual:**
        ```
        Professional diverse team collaborating, 
        bright modern office, natural window 
        lighting, inspirational atmosphere, 
        corporate colors, realistic photography
        ```
        """)

with col2:
    with st.expander("❌ What to Avoid"):
        st.markdown("""
        - Too vague: "nice picture"
        - Too short: "robot"
        - Conflicting: "modern vintage"
        - Copyrighted content
        - Inappropriate content
        - No style specification
        """)

with col3:
    with st.expander("🎨 Style Keywords"):
        st.markdown("""
        **Photography:**
        - Professional, Studio, Natural
        - Cinematic, Dramatic, Soft
        
        **Art Styles:**
        - Realistic, Cartoon, 3D Render
        - Minimalist, Abstract, Modern
        
        **Quality:**
        - 4K, HD, Ultra-detailed
        - High-quality, Premium
        """)

# Navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("🎬 Try Video Generation", use_container_width=True):
        st.switch_page("pages/2_🎬_Video_Generation.py")

with col3:
    if st.button("📖 View Examples", use_container_width=True):
        st.switch_page("pages/3_📖_Examples_Tips.py")