
import streamlit as st
import plotly.express as px
import json
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title='Overview', layout='wide', page_icon='📊')

if 'agg_trans_df' not in st.session_state:
    st.error("❌ Data not loaded. Please go to Home page first.")
    st.stop()

agg_trans = st.session_state["agg_trans_df"]
map_trans = st.session_state["map_trans_df"]
map_user = st.session_state["map_user_df"]

st.title(':blue[Overview]')
add_vertical_space(2)

# Chart 1: Transaction Breakdown by Type
st.subheader(":blue[Transaction Breakdown by Type]")
trans_type_count = agg_trans.groupby('Transaction_type')['Transaction_count'].sum()
total_trans_count = agg_trans['Transaction_count'].sum()
trans_type_perc = round(trans_type_count / total_trans_count * 100, 2).reset_index()

trans_type_fig = px.pie(
    trans_type_perc, names='Transaction_type', values='Transaction_count',
    hole=.65, hover_data={'Transaction_count': False}
)
trans_type_fig.update_layout(width=900, height=500)
st.plotly_chart(trans_type_fig, use_container_width=True)

add_vertical_space(2)

# Chart 2: Transaction Count by State
st.subheader(":blue[Transaction Count by State]")
trans_state = agg_trans.groupby('State')['Transaction_count'].sum().reset_index()
trans_state_sorted = trans_state.sort_values(by='Transaction_count', ascending=False).head(15)

trans_state_fig = px.bar(
    trans_state_sorted, x='Transaction_count', y='State', orientation='h',
    text='Transaction_count', text_auto='.2s',
    labels={'Transaction_count': "Transaction Count"}
)
trans_state_fig.update_layout(yaxis=dict(autorange="reversed"), width=900, height=500)
st.plotly_chart(trans_state_fig, use_container_width=True)

add_vertical_space(2)

# Chart 3: Transaction Count by District
st.subheader(":blue[Transaction Count by District]")
trans_district = map_trans.groupby(['State', 'District'])[['Transaction_count']].sum().reset_index()
trans_district_sorted = trans_district.sort_values(by='Transaction_count', ascending=False).head(15)

trans_district_fig = px.bar(
    trans_district_sorted, x='Transaction_count', y='District', orientation='h',
    text='Transaction_count', text_auto='.2s',
    labels={'Transaction_count': "Transaction Count"},
    hover_name='State', hover_data={'State': False, 'District': True}
)
trans_district_fig.update_layout(yaxis=dict(autorange="reversed"), width=900, height=500)
st.plotly_chart(trans_district_fig, use_container_width=True)

add_vertical_space(2)

# Chart 4: Registered User Count by State
st.subheader(':blue[Registered User Count by State]')
user_state = map_user.groupby('State')['Registered_users'].sum().reset_index()
user_state_sorted = user_state.sort_values(by='Registered_users', ascending=False).head(15)

user_state_fig = px.bar(
    user_state_sorted, x='Registered_users', y='State', orientation='h',
    text='Registered_users', text_auto='.2s',
    color='Registered_users', color_continuous_scale='Reds'
)
user_state_fig.update_layout(yaxis=dict(autorange="reversed"), height=600, width=900)
st.plotly_chart(user_state_fig, use_container_width=True)
