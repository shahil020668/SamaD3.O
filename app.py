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
    raw_creds = os.getenv("FIREBASE_CREDENTIALS")
    
    if raw_creds:
        try:
            cred_dict = json.loads(raw_creds, strict=False)
            
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
        except json.JSONDecodeError as e:
            st.error(f"Failed to parse Firebase credentials: {e}")
    else:
        st.error("FIREBASE_CREDENTIALS environment variable not found.")


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