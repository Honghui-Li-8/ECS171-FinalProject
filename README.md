## ECS171-FinalProject - Team 14
Topic: Letter recognition</br>
PRoject Report: [report]()

## Demo Instruction
#### Frontend Webpage
Located under `Demo` folder
- `DemoLocal.html` should be ready to open with any browser but need to run the backend server to be able to utilize our model and recived prediction.
- `DemoInternet.html` is under Demo/templates, is same website but hosted by server 
  - (still only work for local unless you set up the router fowrding, behaves the same)

#### Backend Server
Located under "Demo" folder
- `backend.py` file hosts the server, install all needed library below and use command "python backend.py" in Demo folder to run
- `routes_predicts.py` file contains the prediction routes/functions for the server to handel the request of using one version of our model.
- Libary needed
  - `flask` & `flask-cors` for hosting server using python, intall with "pip intsall flask" & "pip intsall flask-cors"
  - `PIL` for image processing and save local copy of collected image, intall with "pip intsall pillow"
  - `numpy` and `tensorflow` for data processing and model calling

Also, change line 257 of DemoLocal.html `const IP_address = "http://127.0.0.1:5000"` to the correct address that server is running at.
Example terminal output when run server:
PS ........ECS171-FinalProject\demo> python .\backend.py

 \* Serving Flask app 'backend'<\br>
 
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

 \* Running on all addresses (0.0.0.0)
 
 \* Running on http://127.0.0.1:5000
 


## Model Instruction
All model training code locates under `ModelTraining` folder
- `Final Data Preprocessing.ipynb` collects all the preprocessing functions we created.
- `Final Model.ipynb` contains the training process and the performance analysis graphs.
- `CNN_ver8_grid_search.ipynb` contains the grid search histroy for the last hyper parameter tunning step, and it generated the structure of our final model.
- The rest notbook files which named with version number are the cleaned-up version of recorded attemps on data-processing / hyper parameter tuning with some analysis.
