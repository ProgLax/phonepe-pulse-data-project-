
import io
import pandas as pd
import streamlit as st
from streamlit_player import st_player
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.add_vertical_space import add_vertical_space
import google.generativeai as genai
import os # Import os to access environment variables

st.set_page_config(
    page_title='PhonePe Pulse AI',
    layout='wide',
    page_icon='💜',
    initial_sidebar_state='expanded'
)

# ULTRA PREMIUM CSS WITH GLASSMORPHISM
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    * {
        font-family: 'Inter', -apple-system, sans-serif;
    }

    /* Animated Gradient Background */
    .main {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    /* Glassmorphism Header */
    [data-testid="stHeader"] {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Animated Title */
    .main-title {
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 50%, #ffffff 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s ease-in-out infinite;
        margin: 2rem 0;
        text-shadow: 0 0 40px rgba(255,255,255,0.5);
        letter-spacing: -2px;
    }

    @keyframes shimmer {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #ffffff;
        font-weight: 600;
        margin-bottom: 3rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        animation: fadeInUp 1s ease-out;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Premium Glassmorphism Cards */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 24px;
        padding: 28px;
        box-shadow:
            0 8px 32px 0 rgba(31, 38, 135, 0.37),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.5);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: slideInUp 0.8s ease-out backwards;
        position: relative;
        overflow: hidden;
    }

    div[data-testid="metric-container"]::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: rotate(45deg);
        animation: shine 3s infinite;
    }

    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }

    div[data-testid="metric-container"]:hover {
        transform: translateY(-12px) scale(1.03);
        box-shadow:
            0 20px 60px 0 rgba(31, 38, 135, 0.5),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.7);
        border-color: rgba(255, 255, 255, 0.5);
    }

    @keyframes slideInUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }

    div[data-testid="metric-container"]:nth-child(1) { animation-delay: 0.1s; }
    div[data-testid="metric-container"]:nth-child(2) { animation-delay: 0.2s; }
    div[data-testid="metric-container"]:nth-child(3) { animation-delay: 0.3s; }

    div[data-testid="metric-container"] label {
        color: #ffffff !important;
        font-weight: 700;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 2.8rem !important;
        font-weight: 900;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }

    div[data-testid="metric-container"] [data-testid="stMetricDelta"] {
        color: #34d399 !important;
        font-weight: 700;
        background: rgba(52, 211, 153, 0.2);
        padding: 4px 12px;
        border-radius: 20px;
    }

    /* Info Box Glassmorphism */
    .stAlert {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        color: #ffffff;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        animation: fadeIn 1s ease-out;
    }

    /* Headers with Glow */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #ffffff !important;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(255,255,255,0.5);
    }

    .stMarkdown h2 {
        border-left: 5px solid rgba(255,255,255,0.8);
        padding-left: 20px;
        margin: 2rem 0 1rem 0;
        animation: slideInLeft 0.6s ease-out;
    }

    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }

    .stMarkdown p {
        color: #ffffff;
        font-size: 1.1rem;
        line-height: 1.8;
        text-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }

    /* Premium Buttons */
    .stButton button {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 14px 32px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton button:hover {
        background: rgba(255, 255, 255, 0.3);
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        border-color: rgba(255, 255, 255, 0.5);
    }

    /* Chat Container Glassmorphism */
    .chat-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }

    /* Chat Messages */
    .user-message {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .ai-message {
        background: rgba(102, 126, 234, 0.3);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    /* Sidebar Glassmorphism */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 10px;
        border-radius: 20px;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        color: white;
        font-weight: 700;
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-2px);
    }

    .stTabs [aria-selected="true"] {
        background: rgba(255, 255, 255, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.5);
    }

    /* Text Input */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px;
        color: white;
        font-size: 1rem;
    }

    .stTextInput input::placeholder {
        color: rgba(255, 255, 255, 0.6);
    }

    /* Hide Streamlit Branding */
    #MainMenu, footer, header { display: none !important; }

    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
        margin: 3rem 0;
    }

    /* Video Player */
    .stVideo {
        border-radius: 25px;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load all CSV files"""
    try:
        data = {
            'agg_trans_df': pd.read_csv(r'/content/Miscellaneous/agg_trans.csv'),
            'agg_user_df': pd.read_csv(r'/content/Miscellaneous/agg_user.csv'),
            'map_trans_df': pd.read_csv(r'/content/Miscellaneous/map_trans.csv'),
            'map_user_df': pd.read_csv(r'/content/Miscellaneous/map_user.csv'),
            'top_trans_dist_df': pd.read_csv(r'/content/Miscellaneous/top_trans_dist.csv'),
            'top_trans_pin_df': pd.read_csv(r'/content/Miscellaneous/top_trans_pin.csv'),
            'top_user_dist_df': pd.read_csv(r'/content/Miscellaneous/top_user_dist.csv'),
            'top_user_pin_df': pd.read_csv(r'/content/Miscellaneous/top_user_pin.csv')
        }

        for key in data:
            if 'Year' in data[key].columns:
                data[key]['Year'] = data[key]['Year'].astype(str)

        return data
    except Exception as e:
        st.error(f"❌ Error: {e}")
        return None

def query_gemini(question): # Removed api_key parameter
    """Query Google Gemini AI"""
    try:
        # Get API key from environment variable
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            return "Error: Google Gemini API key not found. Please set the GOOGLE_API_KEY environment variable."

        genai.configure(api_key=api_key)
        # Use a potentially more compatible model
        model = genai.GenerativeModel('gemini-pro-latest') # Changed model name

        prompt = f"""You are a helpful AI assistant specialized in digital payments and PhonePe data analytics.
        Provide concise, accurate, and helpful answers.

        Question: {question}

        Answer:"""

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

# Load data
if 'agg_trans_df' not in st.session_state:
    data = load_data()
    if data:
        for key, value in data.items():
            st.session_state[key] = value
        st.session_state['states'] = st.session_state['agg_trans_df']['State'].unique()
        st.session_state['years'] = st.session_state['agg_trans_df']['Year'].unique()
        st.session_state['quarters'] = st.session_state['agg_trans_df']['Quarter'].unique()
    else:
        st.stop()

agg_trans_df = st.session_state['agg_trans_df']
map_user_df = st.session_state['map_user_df']
top_user_dist_df = st.session_state['top_user_dist_df']

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Animated Title
st.markdown('<h1 class="main-title">💜 PhonePe Pulse AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Digital Payments Analytics Dashboard</p>', unsafe_allow_html=True)

add_vertical_space(2)

# Description
description = """PhonePe Pulse is a comprehensive data analytics platform providing deep insights into digital payments in India.
With over **30 crore registered users** and **2000 crore transactions**, PhonePe commands **46% UPI market share**.
Explore interactive visualizations, trends, and ask our **Google Gemini AI** assistant anything about digital payments!"""

st.info(description)

add_vertical_space(2)

# Video Player
st_player(url="https://www.youtube.com/watch?v=c_1H6vivsiA", height=480)

add_vertical_space(2)

# Key Metrics
st.markdown("## 📊 Real-Time Metrics")
col1, col2, col3 = st.columns(3)

total_reg_users = top_user_dist_df['Registered_users'].sum()
col1.metric('🧑‍🤝‍🧑 REGISTERED USERS', f'{total_reg_users/100000000:.2f} Cr', '📈 +12.5%')

total_app_opens = map_user_df['App_opens'].sum()
col2.metric('📲 APP OPENS', f'{total_app_opens/100000000:.2f} Cr', '📈 +8.3%')

col3.metric('💳 TRANSACTIONS', '2000 Cr+', '📈 +15.2%')

add_vertical_space(3)

# AI CHATBOT SECTION
st.markdown("## 🤖 Google Gemini AI Assistant")

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Removed API Key Input Field

# Chat Input
user_input = st.text_input(
    "Ask about digital payments, UPI trends, or PhonePe data:",
    placeholder="e.g., What are the latest UPI payment trends in India?",
    key="user_question"
)

col1, col2 = st.columns([1, 5])

with col1:
    send_button = st.button("🚀 Ask AI", use_container_width=True)

with col2:
    clear_button = st.button("🗑️ Clear Chat", use_container_width=True)

if clear_button:
    st.session_state.chat_history = []
    st.rerun()

if send_button and user_input:
    # Removed API key check here
    with st.spinner("🤔 Gemini AI is thinking..."):
        response = query_gemini(user_input) # Removed api_key argument
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "ai", "content": response})

# Display Chat History
if st.session_state.chat_history:
    st.markdown("### 💬 Conversation")
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">👤 <strong>You:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="ai-message">🤖 <strong>Gemini AI:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)
else:
    st.markdown("### 💡 Try asking:")
    st.markdown("""
    - What are the top digital payment trends in India?
    - Explain UPI and its impact on Indian payments
    - What is PhonePe and how does it work?
    - Compare digital payment methods in India
    - What are the security features of UPI?
    """)

st.markdown('</div>', unsafe_allow_html=True)

add_vertical_space(3)

# Navigation
st.markdown("---")
st.markdown("## 🧭 Explore Dashboard")
st.info("💡 Navigate to **Overview**, **Transactions**, **Users**, **Trends**, and **Comparisons** using the sidebar!")
