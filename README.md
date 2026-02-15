# SamaD3.O

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://samad3ai.streamlit.app)

A Streamlit-based chatbot application that uses API of AI models (Google Gemini, HuggingFace) using LangGraph for state management. Features user authentication via Firebase and persistent conversation storage.

## 🌟 Features

- **Chat model**: like chat GPT, gemini 
- **User Authentication**: Firebase-based login/signup with session management
- **Dual Chat Modes**:
  - **Unsaved Chat**: Anonymous conversations (temporary, no login required)
  - **Saved Chat**: Persistent conversations with SQLite database for logged-in users
- **Conversation History**: Save and load multiple chat threads
- **LangGraph Integration**: Advanced state management and message routing
- **Streamlit UI**: Interactive web interface with session state management

## 📁 Project Structure

```
├── app.py                      # Main Streamlit entry point
├── auth.py                     # Firebase authentication
├── streamlit_unsaved.py        # Anonymous chat interface
├── streamlit_saved.py          # Authenticated chat with history
├── db_unsaved.py               # Unsaved chat backend (LangGraph)
├── db_saved.py                 # Saved chat backend with SQLite persistence
├── user_dbs/                   # User conversation databases (SQLite)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8+
- Firebase project with credentials
- API keys for HuggingFace and Google Gemini

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Chatbot2
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables**
   
   Create a `.env` file in the root directory:
   ```
   FIREBASE_CREDENTIALS='<your-firebase-json>'
   FIREBASE_API_KEY='<your-firebase-api-key>'
   HUGGINGFACE_API_KEY='<your-huggingface-token>'
   GOOGLE_API_KEY='<your-google-genai-key>'
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📝 Usage

### Anonymous Chat (Unsaved)
- Click "login/signup" button to navigate
- No authentication required
- Conversations are temporary

### Authenticated Chat (Saved)
- Sign up or log in with your credentials
- Conversations are saved to your personal SQLite database
- Create multiple chat threads
- Load previous conversations

## 🔧 Technologies Used

- **Frontend**: Streamlit
- **Backend**: LangGraph, LangChain
- **AI Models**: HuggingFace (DeepSeek), Google Gemini
- **Database**: SQLite for persistent storage
- **Authentication**: Firebase Admin SDK
- **Message Management**: LangChain Core

## 📦 Key Dependencies

- `streamlit` - Web UI framework
- `langgraph` - Graph-based agentic framework
- `langchain`, `langchain-core` - LLM integration
- `firebase-admin` - Firebase authentication
- `python-dotenv` - Environment variable management

## 🔐 Authentication Flow

1. Users can sign up/login using Firebase Authentication
2. Credentials stored securely in Firebase
3. Session tokens managed in Streamlit state
4. User ID used to create isolated SQLite databases

## 💾 Data Storage

- **Unsaved conversations**: Stored in memory (session state only)
- **Saved conversations**: SQLite database per user in `user_dbs/` directory

## 🐛 Troubleshooting

- **Firebase errors**: Verify credentials in `.env` file
- **API key issues**: Check HuggingFace and Google API keys are valid
- **Database errors**: Ensure `user_dbs/` directory has write permissions


## 👤 Author

SamaD3.O

---

## ✅ Future Enhancements

- [ ] Add more AI model integrations
- [ ] Implement conversation search/filtering
- [ ] Add file upload support
- [ ] Implement user settings/preferences
- [ ] Add rate limiting
