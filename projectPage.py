import pandas as pd
import zipfile
import streamlit as st
import os
def unzip_and_list_contents(zip_file):
    try:
        # Check if the folder already exists in 'extracted_contents'
        extract_dir = 'extracted_contents'
        os.makedirs(extract_dir, exist_ok=True)

        # Check if the folder with the same name already exists
        folder_name = os.path.splitext(zip_file.name)[0]
        folder_path = os.path.join(extract_dir, folder_name)

        if os.path.exists(folder_path):
            return f"'{folder_name}' already exists"

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(folder_path)
            return os.listdir(folder_path)
    except Exception as e:
        return f"An error occurred: {str(e)}"




def get_project_info(project_dir):
    project_info = []
    for project_name in os.listdir(project_dir):
        project_path = os.path.join(project_dir, project_name)
        if os.path.isdir(project_path):
            num_files = len(os.listdir(project_path))
            description_file = os.path.join(project_path, 'description.txt')
            if os.path.exists(description_file):
                with open(description_file, 'r') as desc_file:
                    description = desc_file.read()
            else:
                description = "No description available"
            project_info.append((project_name, num_files, description))
    return project_info


def list_projects():
    project_dir = 'extracted_contents'
    if not os.path.exists(project_dir):
        st.warning("No projects found.")
        return

    projects = get_project_info(project_dir)

    if not projects:
        st.warning("No projects found.")
    else:


        # Create a DataFrame from project_info
        df = pd.DataFrame(projects, columns=[" 📂 Project Name", "Number of Files", "Description"])

        # Display the DataFrame
        st.dataframe(df)
def project_page():
    st.title("Report Page")

    st.subheader("Upload a new project please !")

    uploaded_file = st.file_uploader("Upload a ZIP folder", type=["zip"])

    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        file_name = uploaded_file.name

        result = unzip_and_list_contents(uploaded_file)

        if isinstance(result, list):
            st.success(f"Uploaded and extracted '{file_name}'")


    st.subheader("List of Projects")
    list_projects()







