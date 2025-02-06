import streamlit as st
import pickle
import os

data_file = "chat_history.pkl"

def load_chat_history():
    if os.path.exists(data_file):
        with open(data_file, "rb") as f:
            return pickle.load(f)
    return []

def delete_chat_history():
    if os.path.exists(data_file):
        os.remove(data_file)
    st.session_state["messages"] = []

def save_chat_history(messages):
    with open(data_file, "wb") as f:
        pickle.dump(messages, f)

def reload_chat():
    st.session_state["messages"] = load_chat_history()
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
  
    st.rerun()

def main():
    st.title("Simple Chat 😎")
    if st.button("Reload"):
        reload_chat()
    if st.button("Delete Chat History"):
        delete_chat_history()
        st.rerun()  
        
    if "messages" not in st.session_state:
        st.session_state["messages"] = load_chat_history()
    
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
  
    user_input = st.chat_input("Type your message...")
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        save_chat_history(st.session_state["messages"])
        
        with st.chat_message("user"):
            st.markdown(user_input)
        
        save_chat_history(st.session_state["messages"])
        reload_chat()
        
if __name__ == "__main__":
    main()
