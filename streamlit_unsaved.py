import streamlit as st
st.set_page_config(layout='centered')
from db_unsaved import chatbot
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import uuid
import firebase_admin
from firebase_admin import credentials
from auth import login, signup, verify_token
from dotenv import load_dotenv
# from streamlit_cookies_manager.cookie_manager import CookiesNotReady


load_dotenv()

def app():

    c1, c2 = st.columns([6, 1])
    with c2:
        if st.button("login/signup"):
            st.session_state.show_auth = True

    #***************************unsaves chat interface****************************************


    def generate_threadid():
        threadid = uuid.uuid4()
        return threadid

    if 'messages_history1' not in st.session_state:
        st.session_state['messages_history1'] = []

    if 'thread_id1' not in st.session_state:
        st.session_state['thread_id1'] = generate_threadid()

    if 'chat_threads1' not in st.session_state:
        st.session_state['chat_threads1'] = []

    def add_thread(thread_id1):
        if thread_id1 not in st.session_state['chat_threads1']:
            st.session_state['chat_threads1'].append(thread_id1)

    # when reloading 

    add_thread(st.session_state['thread_id1'])

    CONFIG = {"configurable": {"thread_id": st.session_state['thread_id1']}}

    def load_conversation(thread_id1):
        return chatbot.get_state(config={"configurable": {"thread_id": thread_id1}}).values['messages']

    def reset_chat():
        thread_id1 = generate_threadid()
        st.session_state['thread_id1'] = thread_id1
        add_thread(thread_id1)
        st.session_state['messages_history1'] = []

    st.sidebar.title("SamaD3.O")
    if st.sidebar.button("New chat"):
        reset_chat()
    st.sidebar.header("My conversation")



    for thread_id1 in st.session_state['chat_threads1'][::-1]:
        if st.sidebar.button(str(thread_id1)):
            st.session_state['thread_id1'] = thread_id1
            messages = load_conversation(thread_id1)
            if messages:
                st.session_state['messages_history1'] = messages
            else:
                st.session_state['messages_history1'] = []


    st.title("💬 SamaD3.O")

    for message in st.session_state['messages_history1']:
        if isinstance(message, HumanMessage):
            with st.chat_message('user'):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message('assistant'):
                st.write(message.content)

    user_input = st.chat_input('Ask anything')


    def stream_ai_response(chatbot, user_input, config):
        full_response = ""

        def generator():
            nonlocal full_response
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=config,
                stream_mode="messages"
            ):
                if isinstance(message_chunk, AIMessage):
                    full_response += message_chunk.content
                    yield message_chunk.content

        st.write_stream(generator())
        return AIMessage(content=full_response)



    if user_input:
        st.session_state['messages_history1'].append(HumanMessage(content=user_input))
        with st.chat_message('user'):
            st.write(user_input)
        
        # result = chatbot.invoke({'messages' : [HumanMessage (content = user_input)]},config=CONFIG)
        # ai_message = result['messages'][-1]

        with st.chat_message('assistant'):
            ai_message = stream_ai_response(chatbot, user_input, CONFIG)
        st.session_state['messages_history1'].append(ai_message)


    @st.dialog("🔐 Login / Signup")
    def auth_dialog():
        mode = st.radio(
            "Mode",
            ["Login", "Sign Up"],
            horizontal=True
        )

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # col1, col2 = st.columns(2)

        # with col1:
        #     if st.button("❌ Cancel"):
        #         st.session_state.show_auth = False
        #         # st.rerun()

        
        if st.button(mode):
            try:
                if mode == "Login":
                    data = login(email, password)
                    user = verify_token(data["idToken"])

                    st.session_state.user = user
                    st.session_state.logged_in = True
                    st.session_state.show_auth = False
                    st.session_state.signout = True
                    st.session_state.signedout = True
                    st.rerun()

                else:
                    signup(email, password)
                    st.success("Signup successful. Please login.")

            except Exception as e:
                st.error(e)

    if st.session_state.show_auth:
        auth_dialog()