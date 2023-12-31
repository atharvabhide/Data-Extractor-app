import streamlit as st 
import requests
import time
import csv
import base64

def extract_data(applicant_token, response):
    headers = {"Authorization": f"Token {applicant_token}"}
    data = {"uuid": response.json()["uuid"]}
    response = requests.post(
        "http://127.0.0.1:8000/api/extract/",
        headers=headers,
        json=data
    )
    if response.status_code == 200:
        st.success("Data extracted successfully!")
        data = response.content
        # Generate a downloadable link for the content
        download_link = get_download_link(data, "extracted_content.txt")
        st.markdown(download_link, unsafe_allow_html=True)
    else:
        st.error("Data extraction failed.")

def get_download_link(file_content, file_name):
    encoded_content = base64.b64encode(file_content).decode()
    href = f'<a href="data:text/plain;base64,{encoded_content}" download="{file_name}">Download Content</a>'
    return href


def upload_file(applicant_token):
    if applicant_token:
        with st.form("my_form"):
            st.write("Upload your file here")
            file = st.file_uploader("Choose a file")
            submit_res = st.form_submit_button(label='Upload File')
            if submit_res:
                if file is not None:
                    file_content = file.read()
                    file_name = file.name
                    file_type = file.type
                    data = {
                        "file": (file_name, file_content, file_type)
                    }
                    headers = {"Authorization": f"Token {applicant_token}"}
                    response = requests.post("http://127.0.0.1:8000/api/files/", 
                                             headers=headers,
                                             files=data)

                    if response.status_code == 201:
                        st.success("File uploaded successfully!")
                        extract_data(applicant_token=applicant_token, response=response)
                    else:
                        st.error("File upload failed.")
                else:
                    st.write("Please upload a file!")
    else:
        with st.form("my_form"):
            st.write("Please login first!")
            submit_res = st.form_submit_button(label='Login here')
            if submit_res:
                login_page(applicant_token=applicant_token)


def login_page(applicant_token):
    if(applicant_token):
        upload_file(applicant_token=applicant_token)
    else:
        with st.form("my_form"):            
            email = st.text_input(label='Email')
            password = st.text_input(label='Password', type="password")
            submit_res = st.form_submit_button(label='Login')
            if submit_res:
                st.write("login clicked!")
                headers = {"Content-Type": "application/json; charset=utf-8"}
                response = requests.post('http://127.0.0.1:8000/api/auth/',
                  headers=headers, json={"email":email,"password":password})
                response_json = response.json()
                if response.status_code == 200:
                    applicant_token = response_json["token"]
                    if applicant_token:
                       st.session_state.key = 'applicant-token'
                       st.session_state['applicant-token'] = applicant_token
                       st.experimental_rerun()


def register(applicant_token):
    if applicant_token:
        with st.form("my_form"):
                    st.write("You need to first logout before registering!")
                    submit_res = st.form_submit_button(label='Logout here') 
                    if submit_res:
                        st.write("You are now logged out!")
                        del st.session_state['applicant-token']
                        time.sleep(3)
                        st.experimental_rerun()
    else:
        with st.form("my_form"):   
            email = st.text_input(label ='Email')
            username = st.text_input(label='Username')
            password = st.text_input(label='Password', type="password")
            submit_res = st.form_submit_button(label='Register')
            if submit_res:
                st.write("registered clicked!")
                headers = {"Content-Type": "application/json; charset=utf-8"}
                response = requests.post('http://127.0.0.1:8000/api/register/',
                headers=headers, json={"email":email, "username": username,"password":password})
                if response.status_code == 200:
                    st.success("You have successfully registered!")
                    st.experimental_rerun()
                else:
                    st.error("Registration failed.")
                    st.experimental_rerun()


def log_out(applicant_token):
    if applicant_token:
             with st.form("my_form"):
                st.write("Do you want to log out?")
                submit_res = st.form_submit_button(label='Logout here') 
                if submit_res:
                    if 'applicant-token' in st.session_state:
                        del st.session_state['applicant-token']
                    st.write("You are now logged out!")        


def load_view():

    st.set_page_config(
     page_title="Data Extractor App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
    )

    st.header(":100: PDF/PNG/JPEG/JPG Data Extractor :hourglass_flowing_sand:")

    add_selectbox = st.sidebar.selectbox(
    "Please select an option:",
    ("Login", "Register","Log out")
    )

    applicant_token =''
    if 'applicant-token' in st.session_state:
        applicant_token = st.session_state['applicant-token']
    if add_selectbox == 'Login':
        login_page(applicant_token=applicant_token) 
    elif add_selectbox == 'Register':
        register(applicant_token=applicant_token)
    elif add_selectbox == 'Log out':
        log_out(applicant_token=applicant_token)


if __name__ == '__main__':
    load_view()