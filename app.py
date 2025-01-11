import streamlit as st
import concurrent.futures
import time

# App Title
st.title('Python Code Executor')

# Instructions
st.write("Paste your Python code in the text box below, and it will be executed.")

# Text Area for input
code_input = st.text_area("Enter Python code", height=200)

# Function to run the code with a timeout
def run_code_with_timeout(code, timeout=5):
    try:
        # Execute the code within a future to allow timeout
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(exec, code)
            result = future.result(timeout=timeout)
        return result
    except concurrent.futures.TimeoutError:
        return "Error: Code execution exceeded the timeout limit."
    except Exception as e:
        return f"Error: {e}"

# Button to run the code
if st.button("Run Code"):
    if code_input:
        # Limit the execution time to 5 seconds
        output = run_code_with_timeout(code_input, timeout=5)
        st.code(output)
    else:
        st.warning("Please enter some Python code.")
