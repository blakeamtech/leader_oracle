import datetime
import time
import streamlit as st
from openai_service import OpenAIService

# Instantiate services
leader_ai = OpenAIService()

def add_custom_css():
    """Add custom CSS for chat interface."""
    st.markdown(
        """
        <style>
            body {
                overflow-x: hidden; /* Ensure no horizontal overflow */
            }
            .chatbox {
                background-color: #fafafa;
                border-radius: 10px;
                padding: 10px;
                word-wrap: break-word;
                overflow-wrap: break-word;
                width: 100%;
                max-width: 90vw; /* Maximum width */
                margin: auto; /* Centering */
            }
            .message {
                color: #333;
                font-size: 16px;
                padding: 8px;
                border-radius: 8px;
                border: 1px solid #ddd;
                display: block;
                white-space: pre-wrap; /* Wrap text */
                overflow-x: hidden; /* Prevent horizontal overflow */
            }
            .bot-message {
                background-color: #e1f5fe;
            }
            .user-message {
                background-color: #c8e6c9;
            }
            .stButton > button {
                width: 100%;
                border-radius: 20px;
                background-color: #4CAF50;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_custom_css()

st.title("Leader Oracle")
st.subheader("Explore World Leaders' Strategies on Global Issues")

def typing_animation(message):
    """Display typing animation for the chatbot response."""
    placeholder = st.empty()
    for i in range(1, len(message) + 1):
        placeholder.markdown(
            f"<span style='word-wrap: break-word; display: block; white-space: pre-wrap;'>"
            f"{message[:i]}</span>",
            unsafe_allow_html=True,
        )
        time.sleep(0.005)
    placeholder.markdown(
        f"<span style='word-wrap: break-word; display: block; white-space: pre-wrap;'>{message}</span>",
        unsafe_allow_html=True,
    )

if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = [{
        "role": "system",
        "content": "You are Chinese politician Xi Jinping. You respond in a methodical and strategic manner. You are always focused on solving problems with a long-term vision, emphasizing stability, development, and national interests. Your responses are carefully constructed to reflect the principles of governance and leadership, aligning with the goals of the Chinese Communist Party. You only respond with actionable plans that are to the point."
    }]

user_input = st.text_area("Enter your message:", key="user_input", height=100, max_chars=None, help="Type your message here.")

def send_response():
    if st.session_state["user_input"]:
        user_prompt = f"""
        As Xi Jinping, please come up with a well-thought-out response to the following reporter's question that is indicative of how you would actually approach the problem. Please leave out any fluff or numbered lists and just give a straightforward, actionable answer to the question.

        Remember to role-play as Xi Jinping, taking into consideration his leadership style, priorities, and vision for China. Please output a concise, specific action that Xi Jinping would be likely to take.

        It's very important for it to be specific and not sound AI-generated please.
        
        **Background Context:**
        1. Emphasize the importance of stability and national security, aligning with the Chinese Communist Party's (CCP) long-term goals.
        2. Highlight China's socio-economic development and the promotion of the Chinese Dream, focusing on prosperity, national rejuvenation, and international standing.
        3. Address the need for innovative approaches, especially in technology and infrastructure, to maintain China's competitive edge.
        4. Reflect Xi Jinping's commitment to anti-corruption measures and maintaining the integrity of the CCP.
        5. Consider Xi Jinping's stance on global diplomacy, emphasizing mutual respect, non-interference, and the Belt and Road Initiative (BRI).
        6. Balance traditional Chinese values with modern governance practices, demonstrating a harmonious blend of the two.

        **Question from Reporter:**
        {st.session_state['user_input']}
        """

        st.session_state["conversation_history"].append({"role": "user", "content": user_prompt})
        response = leader_ai.generate_response(st.session_state["conversation_history"])
        st.session_state["conversation_history"].append({"role": "assistant", "content": response})
        st.session_state['generated_response'] = response
        st.session_state['user_input'] = ""  # Reset the input field

if st.button("Send", on_click=send_response):
    pass  # The send_response function will handle the input field reset

st.write("### Response")
if "generated_response" in st.session_state:
    typing_animation(st.session_state["generated_response"])
