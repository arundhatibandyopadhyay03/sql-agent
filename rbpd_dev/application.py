import streamlit as st
# Set page config here as the first Streamlit command
st.set_page_config(page_title="Sql Agent", page_icon="📄")  # or a more generic title if needed

import login
import rbpd_main



if "page" not in st.session_state:
    st.session_state.page = "login"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
page = st.session_state.page

# Session safety check: block access to internal pages if not authenticated
protected_pages = ["rbpd_main"]
if page in protected_pages and not st.session_state.authenticated:
    st.warning("⚠️ Please log in to continue.")
    st.session_state.page = "login"
    st.rerun()
if page == "login":
    login.application()  # call login's app function to run the login UI
elif page == "rbpd_main":
    rbpd_main.application()
else:
    st.write("Page not found")
