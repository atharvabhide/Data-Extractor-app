# Data Extractor Application

This application takes in a PDF/PNG/JPEG/JPG file and extracts its data to create a csv file.
<br>
Currently works well for well formatted invoices, with proper segregation of data.


### Tech stack used:
#### Frontend: Streamlit
#### Backend: Django REST framework
#### Data extraction: Tessarect

#### How to Run: 

#### Clone the repository:
```
git clone https://github.com/atharvabhide/data-extractor-app.git
```
### Install requirements:
```
cd data-extractor-app
pip install requirements.txt
```

#### Run the streamlit frontend: 
```
cd frontend
streamlit run app.py
```

#### Run the DRF backend in a separate terminal window:
```
cd backend
python manage.py runserver
```

### Sample files:
```
cd files
```
<br>

![image](https://github.com/atharvabhide/data-extractor-app/assets/67187699/ec93cfbd-9f2a-45c8-a4a3-d07d7ca6d950)
