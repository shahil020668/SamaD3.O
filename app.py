from firebase_admin import credentials
import firebase_admin
import streamlit as st
from auth import login, verify_token
import os, json

if 'flag' not in st.session_state:
    st.session_state.flag = False

if 'signedout' not in st.session_state:
    st.session_state.signedout = False
    st.session_state.show_auth = False

if 'signout' not in st.session_state:
    st.session_state.signout = False

if "user" not in st.session_state:
    st.session_state.user = None

from dotenv import load_dotenv


load_dotenv()

if not firebase_admin._apps:
    cred_dict = json.loads(st.secrets["FIREBASE_CREDENTIALS"])
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)


def app():

    if not st.session_state['signedout']:
        import streamlit_unsaved
        st.session_state.flag = True
        streamlit_unsaved.app()

    if st.session_state.signout:
        import streamlit_saved
        streamlit_saved.app()
        if st.session_state.flag:
            st.session_state.flag = False
            st.rerun()
        
app()