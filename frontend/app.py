import streamlit as st
import requests


st.header(":100: PDF/PNG/JPEG/JPG Data Extractor :hourglass_flowing_sand:")

st.markdown("<br><br>", unsafe_allow_html=True)
file = st.file_uploader("Upload file", type=["pdf", "png", "jpeg", "jpg"])
st.markdown("<br>", unsafe_allow_html=True)
submit = st.button("Submit")
list = st.button("List all files")

if list:
    response = requests.get("http://127.0.0.1:8000/api/files/")
    if response.status_code == 200:
        files = []
        for file in response.json():
            files.append(file["file"])
        st.write(files)
    else:
        st.error("Something went wrong.")

if submit and file is not None:
    file_content = file.read()
    file_name = file.name
    file_type = file.type

    # Prepare the request data
    data = {
        "file": (file_name, file_content, file_type)
    }

    # Make a POST request to the DRF backend
    response = requests.post("http://127.0.0.1:8000/api/files/", files=data)

    if response.status_code == 201:
        st.success("File uploaded successfully!")
    else:
        st.error("File upload failed.")