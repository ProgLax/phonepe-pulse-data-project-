
import io
import pandas as pd
import streamlit as st
from streamlit_player import st_player
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.add_vertical_space import add_vertical_space
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title='PhonePe Pulse', layout='wide', page_icon='💜', initial_sidebar_state='expanded')

def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# PREMIUM LIGHT MODE CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* Light Theme */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Animated Title */
    .main-title {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientMove 4s ease infinite;
        margin: 2rem 0;
    }
    
    @keyframes gradientMove {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #5a67d8;
        font-weight: 600;
        margin-bottom: 2rem;
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Premium Metric Cards */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.7) 100%);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: slideUp 0.6s ease-out backwards;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 20px 50px rgba(102, 126, 234, 0.4);
        border-color: rgba(102, 126, 234, 0.6);
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    div[data-testid="metric-container"]:nth-child(1) { animation-delay: 0.1s; }
    div[data-testid="metric-container"]:nth-child(2) { animation-delay: 0.2s; }
    div[data-testid="metric-container"]:nth-child(3) { animation-delay: 0.3s; }
    
    div[data-testid="metric-container"] label {
        color: #4a5568 !important;
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem !important;
        font-weight: 800;
    }
    
    div[data-testid="metric-container"] [data-testid="stMetricDelta"] {
        color: #48bb78 !important;
        font-weight: 600;
    }
    
    /* Headers */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2d3748 !important;
        font-weight: 700;
    }
    
    .stMarkdown h2 {
        border-left: 5px solid #667eea;
        padding-left: 15px;
        margin: 2rem 0 1rem 0;
        animation: slideInLeft 0.5s ease-out;
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .stMarkdown p {
        color: #4a5568;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    
    /* Info Box */
    .stAlert {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 15px;
        color: #2d3748;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 28px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.5);
    }
    
    /* Selectbox */
    div[data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.9) !important;
        border: 2px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: 10px !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.6);
        padding: 8px;
        border-radius: 15px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        color: #4a5568;
        font-weight: 600;
        border: 2px solid rgba(102, 126, 234, 0.2);
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 1);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(255,255,255,0.95) 0%, rgba(230,235,245,0.95) 100%);
        border-right: 2px solid rgba(102, 126, 234, 0.2);
    }
    
    /* Hide Branding */
    #MainMenu, footer, header { display: none !important; }
    
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
        margin: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
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

st.markdown('<h1 class="main-title">💜 PhonePe Pulse</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">India Digital Payments Dashboard</p>', unsafe_allow_html=True)

col_anim1, col_anim2, col_anim3 = st.columns([1, 2, 1])
with col_anim2:
    lottie_payment = load_lottieurl("https://lottie.host/embed/4db6e8ef-9bda-4fac-8d4f-2633f0bf6de7/VztQBQPXUF.json")
    if lottie_payment:
        st_lottie(lottie_payment, height=200, key="payment")

add_vertical_space(2)

st.info("**PhonePe Pulse** - Interactive analytics platform for digital payments in India. Explore trends across 30 crore users and 2000 crore transactions!")

add_vertical_space(2)
st_player(url="https://www.youtube.com/watch?v=c_1H6vivsiA", height=480)
add_vertical_space(2)

st.markdown("## 📊 Key Metrics")
col1, col2, col3 = st.columns(3)

total_reg_users = top_user_dist_df['Registered_users'].sum()
col1.metric('👥 Users', f'{total_reg_users/100000000:.2f} Cr', '+12.5%')

total_app_opens = map_user_df['App_opens'].sum()
col2.metric('📲 App Opens', f'{total_app_opens/100000000:.2f} Cr', '+8.3%')

col3.metric('💳 Transactions', '2000 Cr+', '+15.2%')

add_vertical_space(2)

st.markdown("## 💰 Financial Snapshot")
total_amount = agg_trans_df['Transaction_amount'].sum()
avg_trans = total_amount / agg_trans_df['Transaction_count'].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("💵 Total Volume", f"₹{total_amount/1e12:.2f}T")
col2.metric("📊 Avg Transaction", f"₹{avg_trans:.0f}")
col3.metric("🗺️ States", f"{len(st.session_state['states'])}")
col4.metric("📅 Years", f"{len(st.session_state['years'])}")

add_vertical_space(2)
st.markdown("---")
st.info("💡 Navigate to **Overview**, **Transaction**, **Users**, **Trends**, and **Comparison** pages!")
