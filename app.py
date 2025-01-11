import streamlit as st

# App Title
st.title('Python Code Executor')

# Instructions
st.write("Paste your Python code in the text box below, and it will be executed.")

# Text Area for input
code_input = st.text_area("Enter Python code", height=200)

# Button to run the code
if st.button("Run Code"):
    try:
        # Execute the user-inputted code
        exec(code_input)
    except Exception as e:
        # Show error message if code execution fails
        st.error(f"Error: {e}")
