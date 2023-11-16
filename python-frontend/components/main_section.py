import streamlit as st

def display_main_section():
    # Set the main title
    
    st.title("EduScan 📖")
    st.write("*Your classroom assistant for seamless student identification and academic information retrieval.*")

    # Project Summary
    text = """
    **Summary:**
    To create an elastic application that can automatically adjust its resources up and down as needed, all while keeping costs under control. We used a Platform as a Service (PaaS) cloud, specifically AWS Lambda and related AWS services.

    **Goal:**
    The project's main goal is to create a smart classroom assistant for educators. This assistant will take videos from a user's classroom, recognize students' faces in the videos, and provide academic information about each recognized student.
    """

    st.markdown(text)

    # Team Details
    st.write("**Team CloudPirates** - **Members**: Uttam Kumar, Jack Li, Sreeharsha Raveendra")
