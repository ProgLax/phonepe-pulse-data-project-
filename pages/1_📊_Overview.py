
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title='Overview', layout='wide', page_icon='📊')

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    [data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    .stMarkdown h1, h2, h3 { color: #2d3748 !important; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

if 'agg_trans_df' not in st.session_state:
    st.error("❌ Data not loaded.")
    st.stop()

agg_trans = st.session_state["agg_trans_df"]
map_trans = st.session_state["map_trans_df"]
map_user = st.session_state["map_user_df"]

st.title('📊 Overview Dashboard')
add_vertical_space(2)

# Chart 1: Transaction Breakdown
st.subheader("🔄 Transaction Type Distribution")
trans_type_count = agg_trans.groupby('Transaction_type')['Transaction_count'].sum()
trans_type_perc = round(trans_type_count / trans_type_count.sum() * 100, 2).reset_index()

fig1 = go.Figure()
fig1.add_trace(go.Pie(
    labels=trans_type_perc['Transaction_type'],
    values=trans_type_perc['Transaction_count'],
    hole=0.65,
    marker=dict(colors=['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe'], line=dict(color='white', width=3)),
    textfont=dict(size=14, color='#2d3748'),
    textposition='outside'
))
fig1.update_layout(height=500, paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#2d3748'))
st.plotly_chart(fig1, use_container_width=True)

add_vertical_space(2)

# Chart 2: States
st.subheader("🏛️ Top 15 States by Transactions")
trans_state = agg_trans.groupby('State')['Transaction_count'].sum().reset_index()
trans_state_sorted = trans_state.sort_values(by='Transaction_count', ascending=False).head(15)

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=trans_state_sorted['Transaction_count'],
    y=trans_state_sorted['State'],
    orientation='h',
    marker=dict(color=trans_state_sorted['Transaction_count'], colorscale='Viridis', line=dict(color='white', width=1)),
    text=trans_state_sorted['Transaction_count'],
    texttemplate='%{text:.2s}'
))
fig2.update_layout(height=500, paper_bgcolor='rgba(0,0,0,0)', yaxis=dict(autorange="reversed"), font=dict(color='#2d3748'))
st.plotly_chart(fig2, use_container_width=True)

add_vertical_space(2)

# Chart 3: Districts
st.subheader("🏘️ Top 15 Districts")
trans_district = map_trans.groupby(['State', 'District'])[['Transaction_count']].sum().reset_index()
trans_district_sorted = trans_district.sort_values(by='Transaction_count', ascending=False).head(15)

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=trans_district_sorted['Transaction_count'],
    y=trans_district_sorted['District'],
    orientation='h',
    marker=dict(color=trans_district_sorted['Transaction_count'], colorscale='Plasma'),
    text=trans_district_sorted['Transaction_count'],
    texttemplate='%{text:.2s}',
    customdata=trans_district_sorted['State']
))
fig3.update_layout(height=500, paper_bgcolor='rgba(0,0,0,0)', yaxis=dict(autorange="reversed"), font=dict(color='#2d3748'))
st.plotly_chart(fig3, use_container_width=True)

add_vertical_space(2)

# Chart 4: Users
st.subheader('👥 Top 15 States by Users')
user_state = map_user.groupby('State')['Registered_users'].sum().reset_index()
user_state_sorted = user_state.sort_values(by='Registered_users', ascending=False).head(15)

fig4 = go.Figure()
fig4.add_trace(go.Bar(
    x=user_state_sorted['Registered_users'],
    y=user_state_sorted['State'],
    orientation='h',
    marker=dict(color=user_state_sorted['Registered_users'], colorscale='Reds'),
    text=user_state_sorted['Registered_users'],
    texttemplate='%{text:.2s}'
))
fig4.update_layout(height=550, paper_bgcolor='rgba(0,0,0,0)', yaxis=dict(autorange="reversed"), font=dict(color='#2d3748'))
st.plotly_chart(fig4, use_container_width=True)
