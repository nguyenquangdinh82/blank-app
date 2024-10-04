import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

# Cấu hình chung cho ứng dụng
st.set_page_config(page_title="Ứng dụng AI", page_icon=":robot_face:")

nav = get_nav_from_toml("sidepage.toml")
pg = st.navigation(nav)

add_page_title(pg)

pg.run()