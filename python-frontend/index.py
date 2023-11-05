import streamlit as st

from components.main_section import display_main_section
from components.workload_test import workload_test
from components.upload_file import upload_file
from components.display_results import display_file_upload_results, display_workload_results
from components.download_results import download_csv

# Set the page title and icon
st.set_page_config(page_title="EduScan", page_icon="📖")

# global variables
is_file_uploaded = False
is_workload_test_completed = False

# Sidebar
with st.sidebar:
    # Workload Test section
    is_workload_test_completed = workload_test()

    # Horizontal line spacer
    st.markdown("---")

    # Upload section
    is_file_uploaded, object_key = upload_file()

# Main Page
with st.container():
    # Display the main section
    display_main_section()

    # Horizontal line spacer
    st.markdown("---")

    # Display the results
    st.subheader('Results')

    if is_file_uploaded or is_workload_test_completed:
        if is_file_uploaded and not is_workload_test_completed:
            # get file upload results
            st.info('📊 File Upload Results')
            # Display file upload results
            result_data = display_file_upload_results(object_key)
        else:
            st.info('📊 Workload Test Results')
            # Display workload test results
            result_data = display_workload_results()
        
        # Display Download link
        st.markdown(download_csv(result_data), unsafe_allow_html=True)

    else:
        st.info('👈 Upload an mp4 file or run workload generator to get started')