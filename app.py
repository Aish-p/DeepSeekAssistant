import re
import base64
import streamlit as st
from ollama import chat

# Set Streamlit page configuration
st.set_page_config(page_title="Mini ChatGPT with DeepSeek Intelligence", layout="centered")


def format_reasoning_response(content):
    """Remove <think> tags from assistant content."""
    return re.sub(r"<think>|</think>", "", content)


def display_message(message):
    """Display a single message in the chat interface."""
    role = "user" if message["role"] == "user" else "assistant"
    with st.chat_message(role):
        if role == "assistant":
            display_assistant_message(message["content"])
        else:
            st.markdown(message["content"])


def display_assistant_message(content):
    """Display assistant message with thinking content if present."""
    match = re.search(r"<think>(.*?)</think>", content, re.DOTALL)
    if match:
        think_content = format_reasoning_response(match.group(0))
        response_content = content.replace(match.group(0), "")
        with st.expander("Thinking complete!"):
            st.markdown(think_content)
        st.markdown(response_content)
    else:
        st.markdown(content)


def display_chat_history():
    """Display all previous messages in the active chat history."""
    st.session_state["messages"] = st.session_state["conversations"][st.session_state["active_chat"]]
    
    for msg in st.session_state["messages"]:
        if msg["role"] != "system":
            display_message(msg)


def process_thinking_phase(stream):
    """Process the thinking phase of the assistant's response."""
    thinking_content = ""
    with st.status("Thinking...", expanded=True) as status:
        think_placeholder = st.empty()
        
        for chunk in stream:
            content = chunk["message"]["content"] or ""
            thinking_content += content
            
            if "<think>" in content:
                continue
            if "</think>" in content:
                content = content.replace("</think>", "")
                status.update(label="Thinking complete!", state="complete", expanded=False)
                break
            think_placeholder.markdown(format_reasoning_response(thinking_content))
    
    return thinking_content


def process_response_phase(stream):
    """Process the response phase of the assistant's response."""
    response_placeholder = st.empty()
    response_content = ""
    for chunk in stream:
        content = chunk["message"]["content"] or ""
        response_content += content
        response_placeholder.markdown(response_content)
    return response_content


@st.cache_resource
def get_chat_model():
    """Get a cached instance of the chat model."""
    return lambda msgs: chat(
        model="deepseek-r1",
        messages=msgs,
        stream=True
    )


def handle_user_input():
    """Handle new user input and generate assistant response."""
    if user_input := st.chat_input("Type your message here..."):
        st.session_state["messages"].append({"role": "user", "content": user_input})
        
        with st.chat_message("user"):
            st.markdown(user_input)
        
        with st.chat_message("assistant"):
            chat_model = get_chat_model()
            stream = chat_model(st.session_state["messages"])
            
            thinking_content = process_thinking_phase(stream)
            response_content = process_response_phase(stream)
            
            # Save the complete response
            st.session_state["messages"].append(
                {"role": "assistant", "content": thinking_content + response_content}
            )


def initialize_session():
    """Initialize session state variables."""
    if "conversations" not in st.session_state:
        st.session_state["conversations"] = {
            "Chat 1": [{"role": "system", "content": "You are a helpful assistant."}]
        }
    if "active_chat" not in st.session_state:
        st.session_state["active_chat"] = "Chat 1"

    st.session_state["messages"] = st.session_state["conversations"][st.session_state["active_chat"]]


def new_chat():
    """Create a new chat tab without deleting previous chats."""
    chat_count = len(st.session_state["conversations"]) + 1
    new_chat_name = f"Chat {chat_count}"
    st.session_state["conversations"][new_chat_name] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    st.session_state["active_chat"] = new_chat_name
    st.rerun()


def main():
    """Main function to handle the chat interface."""
    initialize_session()
    
    logo_path = "assets/deep-seek.png"
    with open(logo_path, "rb") as img_file:
        encoded_logo = base64.b64encode(img_file.read()).decode()
    
    # Sidebar for chat selection
    st.sidebar.title("Chats")
    if st.sidebar.button("➕ New Chat", use_container_width=True):
        new_chat()
    
    chat_selection = st.sidebar.radio(
        "Select a conversation:",
        list(st.session_state["conversations"].keys()),
        index=list(st.session_state["conversations"].keys()).index(st.session_state["active_chat"])
    )
    
    # Update active chat
    if chat_selection != st.session_state["active_chat"]:
        st.session_state["active_chat"] = chat_selection
        st.session_state["messages"] = st.session_state["conversations"][chat_selection]
        st.rerun()

    # Display UI
    st.markdown(f"""
        <div style="text-align: center;">
            <h3>Mini ChatGPT, Driven by <img src="data:image/png;base64,{encoded_logo}" width="170"><br> Intelligence</h3> 
            <h4>How can I help you today?</h4>
        </div>
    """, unsafe_allow_html=True)
    
    display_chat_history()
    handle_user_input()


if __name__ == "__main__":
    main()
