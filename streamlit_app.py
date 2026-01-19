import streamlit as st
from datetime import datetime

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="WaveRift - Audio Diarization",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================
# CUSTOM CSS
# ============================================
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Main Container */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Hero Section */
    .hero {
        text-align: center;
        padding: 2rem 0 3rem 0;
        animation: fadeIn 1s ease-in;
    }
    
    .hero h1 {
        font-size: 4.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        letter-spacing: -2px;
    }
    
    .hero-tagline {
        font-size: 1.5rem;
        color: rgba(255,255,255,0.9);
        font-weight: 300;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Feature Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .feature-text {
        font-size: 1rem;
        color: #4a5568;
        line-height: 1.6;
    }
    
    /* Stats Section */
    .stats-container {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .stat-box {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        color: white;
        display: block;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .stat-label {
        font-size: 1rem;
        color: rgba(255,255,255,0.9);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.5rem;
    }
    
    /* CTA Section */
    .cta-box {
        background: white;
        border-radius: 20px;
        padding: 3rem;
        margin: 3rem 0;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        text-align: center;
    }
    
    .cta-title {
        font-size: 2rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 1rem;
    }
    
    .cta-subtitle {
        font-size: 1.1rem;
        color: #4a5568;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Success Message */
    .success-message {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        text-align: center;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 0 2rem 0;
        color: white;
    }
    
    .footer-text {
        font-size: 0.9rem;
        opacity: 0.8;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero h1 {
            font-size: 2.5rem;
        }
        .hero-tagline {
            font-size: 1.1rem;
        }
        .stat-number {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HERO SECTION
# ============================================
st.markdown("""
<div class="hero">
    <h1>🌊 WaveRift</h1>
    <p class="hero-tagline">
        Transform your audio into crystal-clear transcriptions<br>
        with AI-powered speaker identification
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# STATS SECTION
# ============================================
st.markdown('<div class="stats-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stat-box">
        <span class="stat-number">99%</span>
        <p class="stat-label">Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <span class="stat-number">&lt;5min</span>
        <p class="stat-label">Processing</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <span class="stat-number">50+</span>
        <p class="stat-label">Languages</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# FEATURES SECTION
# ============================================
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🎯</span>
        <h3 class="feature-title">Precision Diarization</h3>
        <p class="feature-text">
            Advanced AI algorithms identify and separate speakers 
            with industry-leading accuracy.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">⚡</span>
        <h3 class="feature-title">Lightning Fast</h3>
        <p class="feature-text">
            Process hours of audio in minutes. 
            Get your transcriptions when you need them.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🔒</span>
        <h3 class="feature-title">Secure & Private</h3>
        <p class="feature-text">
            Your audio files are encrypted and automatically 
            deleted after processing.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# HOW IT WORKS SECTION
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="cta-box">
    <h2 class="cta-title">How It Works</h2>
    <p class="cta-subtitle">
        Simple, fast, and accurate audio diarization in three steps
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card" style="text-align: center;">
        <span class="feature-icon">📤</span>
        <h3 class="feature-title">1. Upload</h3>
        <p class="feature-text">
            Upload your audio file<br>
            (MP3, WAV, M4A, FLAC)
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card" style="text-align: center;">
        <span class="feature-icon">🤖</span>
        <h3 class="feature-title">2. Process</h3>
        <p class="feature-text">
            Our AI analyzes and<br>
            identifies speakers
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card" style="text-align: center;">
        <span class="feature-icon">📊</span>
        <h3 class="feature-title">3. Download</h3>
        <p class="feature-text">
            Get timestamped<br>
            transcriptions instantly
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# WAITLIST SECTION
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="cta-box">
    <h2 class="cta-title">Join the Waitlist</h2>
    <p class="cta-subtitle">
        Be the first to know when WaveRift launches.<br>
        Limited early access spots available.
    </p>
</div>
""", unsafe_allow_html=True)

# Waitlist Form
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with st.form("waitlist_form", clear_on_submit=True):
        email = st.text_input(
            "Email Address",
            placeholder="your@email.com",
            label_visibility="collapsed"
        )
        
        submitted = st.form_submit_button("🚀 Join Waitlist")
        
        if submitted:
            if email and "@" in email:
                # Here you would save to database/spreadsheet
                st.markdown(f"""
                <div class="success-message">
                    ✅ You're on the list! We'll notify you at <strong>{email}</strong> when we launch.
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.error("⚠️ Please enter a valid email address")

# ============================================
# USE CASES SECTION
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="cta-box">
    <h2 class="cta-title">Perfect For</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🎙️</span>
        <h3 class="feature-title">Podcasters</h3>
        <p class="feature-text">
            Generate show notes and transcriptions automatically. 
            Save hours of manual work.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🎬</span>
        <h3 class="feature-title">Content Creators</h3>
        <p class="feature-text">
            Create subtitles and captions for videos with 
            accurate speaker labels.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📊</span>
        <h3 class="feature-title">Researchers</h3>
        <p class="feature-text">
            Analyze interviews and focus groups with 
            precise speaker identification.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">💼</span>
        <h3 class="feature-title">Businesses</h3>
        <p class="feature-text">
            Transcribe meetings and calls with 
            automatic speaker attribution.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="footer">
    <p class="footer-text">
        Made with 💜 by WaveRift Team<br>
        © {datetime.now().year} WaveRift. All rights reserved.
    </p>
    <p class="footer-text" style="margin-top: 1rem; font-size: 0.8rem;">
        <a href="#" style="color: white; text-decoration: none; margin: 0 1rem;">Privacy Policy</a>
        <a href="#" style="color: white; text-decoration: none; margin: 0 1rem;">Terms of Service</a>
        <a href="#" style="color: white; text-decoration: none; margin: 0 1rem;">Contact</a>
    </p>
</div>
""", unsafe_allow_html=True)