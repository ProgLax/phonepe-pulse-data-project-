
import streamlit as st
import plotly.graph_objects as go
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title='Overview', layout='wide', page_icon='📊')
st.markdown("""<style>
.main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
[data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
.stMarkdown h1, h2 { color: #2d3748 !important; font-weight: 700; }
</style>""", unsafe_allow_html=True)

if 'agg_trans_df' not in st.session_state:
    st.error("Data not loaded")
    st.stop()

agg_trans = st.session_state["agg_trans_df"]
map_trans = st.session_state["map_trans_df"]
map_user = st.session_state["map_user_df"]

st.title('📊 Overview')
add_vertical_space(2)

st.subheader("Transaction Distribution")
trans_type = agg_trans.groupby('Transaction_type')['Transaction_count'].sum().reset_index()

fig = go.Figure()
fig.add_trace(go.Pie(labels=trans_type['Transaction_type'], values=trans_type['Transaction_count'], hole=0.65))
fig.update_layout(height=500, paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, use_container_width=True)
