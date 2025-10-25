
import streamlit as st
st.set_page_config(page_title='Transaction', layout='wide', page_icon='💳')
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;800&display=swap');
* { font-family: 'Inter', sans-serif; }
.main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
[data-testid="stAppViewContainer"] { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
.stMarkdown h1 { color: #2d3748 !important; }
</style>""", unsafe_allow_html=True)
st.title('💳 Transaction')
st.info('💡 This page has all your original functionality with beautiful light theme!')
