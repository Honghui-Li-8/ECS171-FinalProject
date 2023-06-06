### ECS171-FinalProject - Team 14
Letter recognition

### Demo Instruction
#### Frontend Webpage
Located under "Demo" folder, should be ready to open with any browser but need to run the backend server to be able to utilize our model and recived prediction.

#### Backend Server
Located under "Demo" folder
- `backend.py` file hosts the server, install all needed library below and use command "python backend.py" in Demo folder to run
- `routes_predicts.py` file contains the prediction routes/functions for the server to handel the request of using one version of our model.
- 
- Libary needed
  - `flask` & `flask-cors` for hosting server using python, intall with "pip intsall flask" & "pip intsall flask-cors"
  - `PIL` for image processing and save local copy of collected image, intall with "pip intsall pillow"
  - `numpy` and `tensorflow` for data processing and model calling
