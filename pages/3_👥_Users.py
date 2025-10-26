
import streamlit as st
import plotly.express as px
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title='Users', layout='wide', page_icon='👥')

if 'agg_trans_df' not in st.session_state:
    st.error("❌ Data not loaded. Please go to Home page first.")
    st.stop()

st.title(':blue[Users Analysis]')
add_vertical_space(2)

# Add user-specific visualizations here
# This is a placeholder - you can add your Users page content

map_user = st.session_state["map_user_df"]
top_user_dist = st.session_state["top_user_dist_df"]

st.subheader(":blue[User Distribution Analysis]")

col1, col2 = st.columns(2)

with col1:
    user_state = map_user.groupby('State')['Registered_users'].sum().reset_index()
    user_state_sorted = user_state.sort_values(by='Registered_users', ascending=False).head(10)

    fig1 = px.bar(
        user_state_sorted, x='Registered_users', y='State', orientation='h',
        text='Registered_users', text_auto='.2s',
        title="Top 10 States by Registered Users"
    )
    fig1.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    user_district = top_user_dist.groupby('District')['Registered_users'].sum().reset_index()
    user_district_sorted = user_district.sort_values(by='Registered_users', ascending=False).head(10)

    fig2 = px.bar(
        user_district_sorted, x='Registered_users', y='District', orientation='h',
        text='Registered_users', text_auto='.2s',
        title="Top 10 Districts by Registered Users"
    )
    fig2.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig2, use_container_width=True)

st.info("💡 This is a sample Users page. You can customize it with your specific user analytics.")
