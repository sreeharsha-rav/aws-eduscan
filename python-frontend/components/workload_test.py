import streamlit as st
import time

from aws.workload import run_workload

def workload_test():
    st.sidebar.title("Workload Test 🖥️")
    
    # Create an empty placeholder for the button and status message
    button_placeholder = st.sidebar.empty()
    status_placeholder = st.sidebar.empty()

    # Initialize the button text and status message
    button_text = "Run Workload Generator"
    
    # Create the button
    if button_placeholder.button(button_text):
        status_placeholder.info('🚀 Running Workload Generator')
        
        # Simulate your workload test or any other task here
        run_workload()
        #time.sleep(5)

        # Change the button text and update the status message
        button_text = "Workload Completed"
        button_placeholder.button(button_text)

        status_placeholder.info('✅ Workload Generation Completed. Click to reset.')
        return True
    
    else:
        status_placeholder.info('☝️ Click to run workload generator')
        return False