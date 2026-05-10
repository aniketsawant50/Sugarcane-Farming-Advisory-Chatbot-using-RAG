import streamlit as st
from app.rag_chain import generate_answer

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Sugarcane Farming Advisory Chatbot",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>

.main {
    background-color: #f7fff7;
}

.stChatMessage {
    border-radius: 10px;
    padding: 10px;
}

h1 {
    color: #2E7D32;
    text-align: center;
}

.example-box {
    background-color: #e8f5e9;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2909/2909768.png",
        width=120
    )

    st.title("🌱 About")

    st.markdown("""
This AI chatbot helps farmers by answering
questions related to:

- Sugarcane cultivation
- Irrigation
- Fertilizers
- Pest control
- Yield improvement

Powered using:
- RAG
- Groq LLM
- Streamlit
""")

    st.markdown("---")

    st.subheader("📌 Tips")

    st.info("""
Ask clear farming questions for better answers.
""")

# -----------------------------------
# MAIN TITLE
# -----------------------------------
st.title("🌱 Sugarcane Farming Advisory Chatbot")

st.markdown("""
<center>
AI-powered farming assistant using RAG technology
</center>
""", unsafe_allow_html=True)

# -----------------------------------
# EXAMPLE QUESTIONS
# -----------------------------------
with st.expander("🌾 Example Questions"):

    st.markdown("""
- What is the best method to cultivate sugarcane?
- Best way for water management in sugarcane?
- Which fertilizer is best for sugarcane?
- How to increase sugarcane yield?
- How to control pests in sugarcane?
""")

# -----------------------------------
# CHAT HISTORY
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chats
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------------
# USER INPUT
# -----------------------------------
query = st.chat_input(
    "Ask your sugarcane farming question..."
)

# -----------------------------------
# HANDLE USER QUERY
# -----------------------------------
if query:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(query)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("🌱 Generating farming advice..."):

            try:
                answer = generate_answer(query)

                st.markdown(answer)

                # Store assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                error_message = f"❌ Error: {str(e)}"

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")

st.caption(
    "🌱 Sugarcane Farming Advisory Chatbot | Built with Streamlit + RAG + Groq"
)