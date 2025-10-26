
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import os

st.set_page_config(page_title='About', layout='wide', page_icon='👤')

st.title(':blue[About Me]')
add_vertical_space(1)

# Define image paths
PROFILE_IMAGE_PATH = "/content/user.jpg"
COVER_IMAGE_PATH = "/content/cover photo.jpg"

# Cover Photo Section
if os.path.exists(COVER_IMAGE_PATH):
    st.image(COVER_IMAGE_PATH, use_container_width=True)
else:
    st.warning(f"Cover photo not found at {COVER_IMAGE_PATH}. Please upload it.")

add_vertical_space(1)

col1, col2 = st.columns([1, 3])

with col1:
    # Profile Photo
    if os.path.exists(PROFILE_IMAGE_PATH):
        st.image(PROFILE_IMAGE_PATH, caption="Laxman Rathod", width=150)
    else:
        st.warning(f"Profile photo not found at {PROFILE_IMAGE_PATH}. Please upload it.")


with col2:
    st.subheader("Laxman Rathod")
    st.markdown(f"- **LinkedIn:** [Laxman Rathod](https://www.linkedin.com/in/laxman-rathod-627264102)")
    st.markdown(f"- **GitHub:** [proglax](https://github.com/proglax)")
add_vertical_space(2)

st.subheader("📂 Project Repositories")
st.markdown("- [Walmart-time-series-and-online-Retail-Data-Analysis](https://github.com/ProgLax/Walmart-time-series-and-online-Retail-Data-Analysis-)")
st.markdown("- [covid-19](https://github.com/ProgLax/covid-19)")
st.markdown("- [Netflix-prediction-engine](https://github.com/ProgLax/Netflix-prediction-engine-)")
st.markdown("- [Wallmart](https://github.com/ProgLax/Walmart-python-)")
st.markdown("- [paisa bazaar banking fraud analysis](https://github.com/ProgLax/paisabazaarbankingfraudanalysis)")
st.markdown("- [phonepe pulse](https://github.com/ProgLax/phonepe-pulse-data-project-)")


