import streamlit as st

def load_custom_css():
    """Load custom CSS styles for the application"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Smooth transitions */
        * {
            transition: all 0.3s ease;
        }
        
        /* Sidebar Styling */
        .sidebar-brand {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem 1rem;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 1rem;
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
        }
        
        .sidebar-brand h1 {
            color: white;
            margin: 0;
            font-size: 1.8rem;
            font-weight: 800;
        }
        
        .sidebar-brand p {
            color: rgba(255, 255, 255, 0.9);
            margin: 0.5rem 0 0 0;
            font-size: 0.9rem;
        }
        
        /* Hero Section */
        .hero-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-size: 200% 200%;
            animation: gradientShift 8s ease infinite;
            padding: 4rem 2rem;
            border-radius: 24px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
        }
        
        .hero-section h1 {
            color: white;
            font-size: 3.5rem;
            font-weight: 800;
            margin: 0;
            text-shadow: 0 2px 20px rgba(0,0,0,0.2);
        }
        
        .hero-subtitle {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.5rem;
            font-weight: 500;
            margin: 1rem 0;
        }
        
        .hero-description {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1rem;
            max-width: 800px;
            margin: 1rem auto 0;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
            border: 2px solid rgba(102, 126, 234, 0.3);
            padding: 2rem 1rem;
            border-radius: 16px;
            text-align: center;
            transition: all 0.3s ease;
            height: 100%;
        }
        
        .metric-card:hover {
            transform: translateY(-8px);
            border-color: rgba(102, 126, 234, 0.6);
            box-shadow: 0 12px 32px rgba(102, 126, 234, 0.3);
        }
        
        .metric-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .metric-value {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        
        .metric-label {
            color: #999;
            font-size: 1rem;
            font-weight: 500;
        }
        
        /* Feature Cards */
        .feature-card {
            background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
            border: 2px solid rgba(102, 126, 234, 0.2);
            padding: 2.5rem;
            border-radius: 20px;
            height: 100%;
            transition: all 0.4s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            border-color: rgba(102, 126, 234, 0.5);
            box-shadow: 0 16px 48px rgba(102, 126, 234, 0.3);
        }
        
        .feature-card h3 {
            color: white;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        
        .feature-card p {
            color: #ccc;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }
        
        .feature-card ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .feature-card ul li {
            color: #aaa;
            padding: 0.5rem 0;
            font-size: 1rem;
        }
        
        /* Step Cards */
        .step-card {
            background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
            border: 2px solid rgba(102, 126, 234, 0.2);
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            height: 100%;
            transition: all 0.3s ease;
        }
        
        .step-card:hover {
            transform: translateY(-8px);
            border-color: rgba(102, 126, 234, 0.5);
            box-shadow: 0 12px 32px rgba(102, 126, 234, 0.3);
        }
        
        .step-number {
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            width: 60px;
            height: 60px;
            line-height: 60px;
            border-radius: 50%;
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }
        
        .step-card h4 {
            color: white;
            font-size: 1.5rem;
            font-weight: 600;
            margin: 1rem 0;
        }
        
        .step-card p {
            color: #aaa;
            font-size: 1rem;
        }
        
        /* Use Case Cards */
        .use-case-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem 1rem;
            border-radius: 16px;
            text-align: center;
            transition: all 0.3s ease;
            height: 100%;
        }
        
        .use-case-card:hover {
            transform: translateY(-8px) scale(1.05);
            box-shadow: 0 12px 32px rgba(102, 126, 234, 0.5);
        }
        
        .use-case-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .use-case-card h5 {
            color: white;
            font-size: 1.3rem;
            font-weight: 700;
            margin: 0.5rem 0;
        }
        
        .use-case-card p {
            color: rgba(255, 255, 255, 0.9);
            font-size: 0.9rem;
            margin: 0;
        }
        
        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            text-align: center;
            margin: 2rem 0;
        }
        
        .cta-section h2 {
            color: white;
            font-size: 2.5rem;
            font-weight: 800;
            margin: 0;
        }
        
        .cta-section p {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.2rem;
            margin: 1rem 0 0;
        }
        
        /* Enhanced Buttons */
        .stButton>button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            border-radius: 12px;
            padding: 0.8rem 2rem;
            font-weight: 600;
            font-size: 1rem;
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.5);
        }
        
        /* Input Fields */
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea,
        .stSelectbox>div>div>select {
            border-radius: 12px;
            border: 2px solid rgba(102, 126, 234, 0.2);
            transition: all 0.3s ease;
        }
        
        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        /* Info boxes */
        .stSuccess, .stWarning, .stError, .stInfo {
            border-radius: 12px;
            border-left-width: 4px;
        }
        
        /* Images and Videos */
        [data-testid="stImage"] {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        }
        
        video {
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        }
        
        /* Page Title Styling */
        .page-title {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 16px;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .page-title h1 {
            color: white;
            font-size: 2.5rem;
            font-weight: 800;
            margin: 0;
        }
        
        .page-title p {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1rem;
            margin: 0.5rem 0 0;
        }
    </style>
    """, unsafe_allow_html=True)