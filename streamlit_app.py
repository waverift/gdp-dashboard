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
# CUSTOM CSS - PROFESSIONAL COLOR SCHEME
# ============================================
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background - Professional Dark Blue */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
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
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        letter-spacing: -2px;
    }
    
    .hero-tagline {
        font-size: 1.4rem;
        color: #94a3b8;
        font-weight: 400;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Feature Cards */
    .feature-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 2.5rem 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.2);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #f1f5f9;
        margin-bottom: 0.75rem;
    }
    
    .feature-text {
        font-size: 1rem;
        color: #94a3b8;
        line-height: 1.6;
    }
    
    /* Stats Section */
    .stats-container {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 2.5rem 2rem;
        margin: 2rem 0;
    }
    
    .stat-box {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
    }
    
    .stat-label {
        font-size: 0.95rem;
        color: #cbd5e1;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    /* CTA Section */
    .cta-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 3rem 2.5rem;
        margin: 3rem 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        text-align: center;
    }
    
    .cta-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #f1f5f9;
        margin-bottom: 1rem;
    }
    
    .cta-subtitle {
        font-size: 1.15rem;
        color: #94a3b8;
        margin-bottom: 2rem;
        line-height: 1.7;
    }
    
    /* Section Title */
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #f1f5f9;
        text-align: center;
        margin: 3rem 0 2rem 0;
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #334155;
        background: #1e293b;
        color: #f1f5f9;
        padding: 1rem 1.25rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3b82f6;
        background: #0f172a;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #64748b;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.875rem 2.5rem;
        font-size: 1.05rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(59, 130, 246, 0.5);
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    }
    
    /* Success Message */
    .success-message {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        text-align: center;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }
    
    /* Contact Info */
    .contact-info {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 1.25rem 1.75rem;
        margin: 2rem auto;
        max-width: 400px;
        text-align: center;
    }
    
    .contact-email {
        color: #60a5fa;
        font-size: 1.1rem;
        font-weight: 500;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .contact-email:hover {
        color: #93c5fd;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 0 2rem 0;
        border-top: 1px solid #334155;
        margin-top: 4rem;
    }
    
    .footer-text {
        font-size: 0.9rem;
        color: #64748b;
    }
    
    .footer-links a {
        color: #94a3b8;
        text-decoration: none;
        margin: 0 1rem;
        transition: color 0.3s ease;
    }
    
    .footer-links a:hover {
        color: #60a5fa;
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
            font-size: 2.2rem;
        }
        .cta-title, .section-title {
            font-size: 1.8rem;
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
st.markdown("<br><br>", unsafe_allow_html=True)

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
st.markdown('<h2 class="section-title">How It Works</h2>', unsafe_allow_html=True)
st.markdown("""
<p style="text-align: center; color: #94a3b8; font-size: 1.1rem; margin-bottom: 2rem;">
    Simple, fast, and accurate audio diarization in three steps
</p>
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
st.markdown('<h2 class="section-title">Perfect For</h2>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

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
# CONTACT SECTION
# ============================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="contact-info">
    <p style="color: #94a3b8; margin-bottom: 0.5rem; font-size: 0.9rem;">Get in touch</p>
    <a href="mailto:hello@waverift.io" class="contact-email">hello@waverift.io</a>
</div>
""", unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown(f"""
<div class="footer">
    <p class="footer-text">
        Made with 💙 by WaveRift Team
    </p>
    <p class="footer-text" style="margin-top: 0.5rem;">
        © {datetime.now().year} WaveRift. All rights reserved.
    </p>
    <div class="footer-links" style="margin-top: 1.5rem;">
        <a href="#">Privacy Policy</a>
        <a href="#">Terms of Service</a>
        <a href="mailto:hello@waverift.io">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)