# login.py
import streamlit as st

VALID_USERS = {
    "user1": "password1",
    "admin": "admin123",
    "john": "doe456",
    "dev": "admin",
}

def application():
    
    
    # Custom title with center alignment and increased font size
    st.markdown("""
        <h1 style='text-align: center; font-size: 50px;'>✨RBPD</h1>
        <h3 style='text-align: center;'>Convert Your files into a BRD</h3>
    """, unsafe_allow_html=True)
    # st.title("RBPD")
    # st.subheader("Convert Your files into a BRD")
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in VALID_USERS and VALID_USERS[username] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("✅ Login successful")
            #st.experimental_set_query_params(page="main_wilson")
            #st.query_params["page"] = "wilson_main"
             # 👇 Set flag to reset thread in wilson_main
            st.session_state.just_logged_in = True
            st.session_state.page = "rbpd_main"
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

