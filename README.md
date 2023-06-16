# Data Extractor Application: Deeplogic AI assessment

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

![image](https://github.com/atharvabhide/data-extractor-app/assets/67187699/5585aa92-ac06-4d3b-a9d4-aaac6f299d7c)

