import streamlit as st
import io
import sys
import contextlib

# Function to run Python code with input
def run_python_code(code, inputs):
    # Capture the standard output
    stdout = sys.stdout
    sys.stdout = io.StringIO()

    # Prepare input for code execution
    input_buffer = io.StringIO(inputs)
    sys.stdin = input_buffer

    try:
        # Execute the provided code
        exec(code)
        result = sys.stdout.getvalue()
    except Exception as e:
        result = f"Error: {str(e)}"

    # Reset the standard input and output
    sys.stdout = stdout
    sys.stdin = sys.__stdin__

    return result

# Streamlit user interface
st.title("Python Code Runner IDE")

# Text area for users to paste Python code
code_input = st.text_area("Enter your Python code here:", height=300)

# If the code asks for input, let the user provide it
input_prompt = st.text_area("Enter input (if your code asks for input):", height=150)

# Button to run the code
if st.button("Run Code"):
    if code_input:
        # Run the user code with input
        output = run_python_code(code_input, input_prompt)
        
        # Display the output
        st.subheader("Output:")
        st.text(output)
    else:
        st.error("Please enter some Python code.")
