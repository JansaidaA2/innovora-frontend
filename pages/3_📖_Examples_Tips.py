import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.styles import load_custom_css

# Page config
st.set_page_config(
    page_title="Examples & Tips - INNOV ORA",
    page_icon="📖",
    layout="wide"
)

# Load styles
load_custom_css()

# Page Header
st.markdown('''
<div class="page-title">
    <h1>📖 Examples & Best Practices</h1>
    <p>Learn how to create amazing content with AI</p>
</div>
''', unsafe_allow_html=True)

# Main Content
col1, col2 = st.columns(2)

# ==================== IMAGE TIPS ====================
with col1:
    st.markdown("## 🎨 Image Generation Guide")
    st.markdown("---")
    
    with st.expander("✅ Excellent Prompt Examples", expanded=True):
        st.markdown("""
        ### 📸 Product Photography
        ```
        Modern minimalist smartphone with gradient 
        OLED display, floating in clean white space, 
        professional studio photography, soft shadows, 
        premium look, 4K quality, highly detailed
        ```
        
        ### 💼 Corporate/Business
        ```
        Professional diverse team collaboration in 
        bright modern office, natural window lighting, 
        smiling team members, corporate blue and white 
        colors, inspirational atmosphere, realistic 
        photography, wide angle shot
        ```
        
        ### 🎯 Marketing Visual
        ```
        Futuristic AI robot with glowing blue circuits, 
        cyberpunk city background at night, neon purple 
        and blue lights, cinematic lighting, dramatic 
        composition, highly detailed, 4K quality
        ```
        
        ### 🍔 Food & Beverage
        ```
        Fresh organic coffee being poured into white 
        ceramic cup, steam rising, rustic wooden table, 
        morning sunlight, cozy café atmosphere, warm 
        tones, professional food photography
        ```
        
        ### 🏠 Real Estate
        ```
        Modern luxury apartment living room, 
        floor-to-ceiling windows with city view, 
        contemporary furniture, bright natural lighting, 
        clean minimalist design, architectural 
        photography, wide angle
        ```
        """)
    
    with st.expander("❌ Common Mistakes to Avoid"):
        st.markdown("""
        ### Don't Do These:
        
        ❌ **Too Vague:**
        - "nice picture"
        - "something cool"
        - "make it good"
        
        ❌ **Too Short:**
        - "robot"
        - "office"
        - "food"
        
        ❌ **Conflicting Styles:**
        - "modern vintage retro futuristic"
        - "realistic cartoon 3D anime"
        - "dark bright moody cheerful"
        
        ❌ **Copyrighted Content:**
        - "Mickey Mouse"
        - "Nike logo"
        - "iPhone exactly like Apple's"
        
        ❌ **No Quality Specification:**
        - Missing "4K", "HD", "professional"
        - No lighting description
        - No style mention
        """)
    
    with st.expander("💡 Pro Tips for Success"):
        st.markdown("""
        ### 🎯 Structure Your Prompt:
        
        1. **Subject** - What's the main focus?
        2. **Action/Pose** - What's happening?
        3. **Environment** - Where is it?
        4. **Lighting** - How is it lit?
        5. **Style** - What's the aesthetic?
        6. **Quality** - Technical specs
        
        ### 📝 Example Template:
        ```
        [Subject] + [Action] + [Environment] + 
        [Lighting] + [Style] + [Quality]
        
        Example:
        Professional businessman presenting + 
        in modern conference room + 
        natural window lighting + 
        corporate minimalist style + 
        4K photography
        ```
        
        ### ✨ Power Keywords:
        - **Quality:** 4K, HD, ultra-detailed, sharp
        - **Lighting:** soft, dramatic, natural, cinematic
        - **Style:** professional, minimalist, modern
        - **Mood:** inspirational, dramatic, peaceful
        """)
    
    with st.expander("🎨 Style Reference Guide"):
        st.markdown("""
        ### Photography Styles:
        - **Studio:** Clean, professional, controlled
        - **Lifestyle:** Natural, candid, relatable
        - **Product:** Focus on details, commercial
        - **Architectural:** Wide angles, symmetry
        - **Portrait:** Close-up, bokeh background
        
        ### Art Styles:
        - **Realistic:** Photographic, detailed
        - **Minimalist:** Simple, clean, modern
        - **Cinematic:** Dramatic, movie-like
        - **Abstract:** Conceptual, artistic
        - **3D Render:** Digital, polished
        
        ### Color Schemes:
        - **Vibrant:** Bold, saturated colors
        - **Muted:** Soft, desaturated tones
        - **Monochrome:** Single color focus
        - **Warm:** Oranges, reds, yellows
        - **Cool:** Blues, purples, greens
        """)

# ==================== VIDEO TIPS ====================
with col2:
    st.markdown("## 🎬 Video Script Guide")
    st.markdown("---")
    
    with st.expander("✅ Effective Script Structure", expanded=True):
        st.markdown("""
        ### 📋 Perfect Structure (50-65 seconds):
        
        **1. Hook (5-10 seconds)**
        Grab attention immediately
        ```
        "Are you struggling with social media content?"
        "What if you could create videos in minutes?"
        "Tired of expensive design agencies?"
        ```
        
        **2. Problem (10-15 seconds)**
        Identify the pain point
        ```
        "Most businesses waste hours creating content 
        that gets minimal engagement. Hiring designers 
        is expensive and time-consuming."
        ```
        
        **3. Solution (20-30 seconds)**
        Present your offering
        ```
        "Innovora uses advanced AI to generate 
        professional marketing images and videos in 
        seconds. No design skills needed. Just describe 
        what you want, and our AI creates it. Perfect 
        for Instagram, LinkedIn, YouTube, and more."
        ```
        
        **4. Call to Action (5-10 seconds)**
        Clear next step
        ```
        "Try Innovora free today and transform your 
        marketing content. Visit innovora.ai to get 
        started!"
        ```
        
        **Total: ~60 seconds, ~100 words ✅**
        """)
    
    with st.expander("💡 Writing Best Practices"):
        st.markdown("""
        ### ✅ Do These:
        
        ✅ **Conversational Tone**
        - Write like you're talking to a friend
        - Use "you" and "your"
        - Keep it natural and friendly
        
        ✅ **Short Sentences**
        - Easy to follow
        - Better for pacing
        - Clearer message
        
        ✅ **Active Voice**
        - "We help you" not "You are helped"
        - "Create content" not "Content is created"
        - More engaging and direct
        
        ✅ **Clear Call-to-Action**
        - Tell viewers exactly what to do
        - Make it simple and actionable
        - Create urgency when appropriate
        
        ✅ **Avoid Jargon**
        - Use simple language
        - Explain technical terms
        - Be accessible to everyone
        
        ✅ **Test by Reading Aloud**
        - Does it sound natural?
        - Is the pacing good?
        - Are there tongue twisters?
        """)
    
    with st.expander("⏱️ Timing & Pacing Guide"):
        st.markdown("""
        ### 📊 Word Count to Duration:
        
        - **10-20 words:** 5-10 seconds
        - **40-60 words:** 20-30 seconds
        - **80-100 words:** 40-50 seconds
        - **120-150 words:** 60-75 seconds
        
        ### 🎯 Optimal Speaking Rate:
        - ~150 words per minute
        - ~2.5 words per second
        - Allows for natural pauses
        - Easy to understand
        
        ### 💡 Pacing Tips:
        - Start strong with hook
        - Build momentum in middle
        - End with clear CTA
        - Include natural pauses
        - Emphasize key points
        """)
    
    with st.expander("🎬 Script Templates"):
        st.markdown("""
        ### Template 1: Problem-Solution
        ```
        [Problem Statement] →
        [Why It Matters] →
        [Your Solution] →
        [Benefits] →
        [Call to Action]
        ```
        
        ### Template 2: Testimonial Style
        ```
        [Personal Story] →
        [Challenge Faced] →
        [How Product Helped] →
        [Results Achieved] →
        [Recommendation]
        ```
        
        ### Template 3: Feature Showcase
        ```
        [Introduction] →
        [Feature 1 + Benefit] →
        [Feature 2 + Benefit] →
        [Feature 3 + Benefit] →
        [Summary + CTA]
        ```
        
        ### Template 4: Educational
        ```
        [Topic Introduction] →
        [Key Point 1] →
        [Key Point 2] →
        [Key Point 3] →
        [Takeaway + Next Steps]
        ```
        """)

# ==================== USE CASES ====================
st.markdown("---")
st.markdown("## 🎯 Common Use Cases")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="use-case-card">
        <div class="use-case-icon">📱</div>
        <h5>Social Media</h5>
        <p>Instagram posts, LinkedIn ads, Facebook campaigns, Twitter graphics</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="use-case-card">
        <div class="use-case-icon">🎬</div>
        <h5>Video Marketing</h5>
        <p>Product demos, explainer videos, testimonials, tutorials</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="use-case-card">
        <div class="use-case-icon">💼</div>
        <h5>Business Content</h5>
        <p>Presentations, email campaigns, website banners, reports</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="use-case-card">
        <div class="use-case-icon">🛍️</div>
        <h5>E-commerce</h5>
        <p>Product photos, promotional videos, ads, catalogs</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== READY-TO-USE PROMPTS ====================
st.markdown("---")
st.markdown("## 📋 Copy & Paste Prompts")

tab1, tab2, tab3, tab4 = st.tabs(["💻 Tech/Software", "🛍️ E-commerce", "🍔 Food & Beverage", "🏢 Corporate"])

with tab1:
    st.markdown("### Technology & Software Prompts")
    
    prompt1 = "Modern laptop displaying colorful code on screen, dark minimal workspace, warm desk lamp, coffee mug, developer environment, professional photography, cinematic lighting, 4K quality"
    st.code(prompt1)
    if st.button("📋 Copy Prompt", key="tech1"):
        st.info("✅ Copied! Go to Image Generation page to use it.")
    
    st.markdown("---")
    
    prompt2 = "Futuristic AI neural network visualization, glowing blue and purple nodes, data flowing through connections, dark background, holographic effect, highly detailed, 4K digital art"
    st.code(prompt2)
    if st.button("📋 Copy Prompt", key="tech2"):
        st.info("✅ Copied! Go to Image Generation page to use it.")

with tab2:
    st.markdown("### E-commerce & Product Prompts")
    
    prompt3 = "Premium wireless headphones on marble surface, soft studio lighting, luxury product photography, minimalist composition, matte black finish, 4K quality, commercial photography"
    st.code(prompt3)
    if st.button("📋 Copy Prompt", key="ecom1"):
        st.info("✅ Copied! Go to Image Generation page to use it.")
    
    st.markdown("---")
    
    prompt4 = "Elegant watch on wooden display, luxury lifestyle photography, soft natural lighting, bokeh background, professional product shot, premium quality, highly detailed, 4K"
    st.code(prompt4)
    if st.button("📋 Copy Prompt", key="ecom2"):
        st.info("✅ Copied! Go to Image Generation page to use it.")

with tab3:
    st.markdown("### Food & Beverage Prompts")
    
    prompt5 = "Fresh organic coffee being poured into white ceramic cup, steam rising, rustic wooden table, morning sunlight, cozy café atmosphere, warm tones, professional food photography, 4K"
    st.code(prompt5)
    if st.button("📋 Copy Prompt", key="food1"):
        st.info("✅ Copied! Go to Image Generation page to use it.")
    
    st.markdown("---")
    
    prompt6 = "Gourmet burger with fresh ingredients, melted cheese dripping, rustic wooden board, dramatic side lighting, restaurant quality, professional food photography, 4K ultra detailed"
    st.code(prompt6)
    if st.button("📋 Copy Prompt", key="food2"):
        st.info("✅ Copied! Go to Image Generation page to use it.")

with tab4:
    st.markdown("### Corporate & Business Prompts")
    
    prompt7 = "Professional diverse team collaborating in bright modern office, natural window lighting, smiling professionals, corporate blue and white colors, inspirational atmosphere, realistic photography, wide angle"
    st.code(prompt7)
    if st.button("📋 Copy Prompt", key="corp1"):
        st.info("✅ Copied! Go to Image Generation page to use it.")
    
    st.markdown("---")
    
    prompt8 = "Modern corporate office interior, glass walls, minimalist design, bright natural lighting, professional workspace, contemporary furniture, architectural photography, 4K quality"
    st.code(prompt8)
    if st.button("📋 Copy Prompt", key="corp2"):
        st.info("✅ Copied! Go to Image Generation page to use it.")

# ==================== FINAL CTA ====================
st.markdown("---")
st.markdown('''
<div class="cta-section">
    <h2>🎉 Ready to Create Amazing Content?</h2>
    <p>Use these tips and examples to generate professional marketing materials</p>
</div>
''', unsafe_allow_html=True)

# Navigation
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("🎨 Generate Images", use_container_width=True, type="primary"):
        st.switch_page("pages/1_🎨_Image_Generation.py")

with col3:
    if st.button("🎬 Generate Videos", use_container_width=True, type="primary"):
        st.switch_page("pages/2_🎬_Video_Generation.py")