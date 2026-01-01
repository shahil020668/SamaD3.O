from firebase_admin import credentials
import firebase_admin
import streamlit as st
import streamlit as st

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
    cred = credentials.Certificate("/home/shahil/U23CS120/LANGGRAPH/samad-efcd8-37c743f3548a.json")
    firebase_admin.initialize_app(cred)


def app():
    

    if not st.session_state['signedout']:
        import streamlit_unsaved
        streamlit_unsaved.app()

    if st.session_state.signout:
        import streamlit_saved
        streamlit_saved.app()
        
app()