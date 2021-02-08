Predict profit on the basis of RND and MKTProfit??
---------------------------------------------------------------------------------------

ML-Model-Flask-Deployment

Prerequisites
----------------------------------------------------------------------------------------
You must have AWS account, Pandas and Flask installed.
----------------------------------------------------------------------------------------


1. Create the machine learning model by running below command -

app.py(Contains application flow)
model.py(Contains ML model)
model.pkl(generated when you train the model)
index.html(contains html code for form)

2. Run app.py using below command to start Flask AP

3. Create a server(ec2-13-56-188-130.us-west-1.compute.amazonaws.com)(13.56.188.130)

4. Install python as well as other modules on this server.
Login: using ssh

init_script.sh
------------------
sudo apt-get update,
sudo apt-get -y install python3.6,
sudo apt-get -y install python3-pip,
sudo apt-get -y install nginx,
sudo apt-get -y install gunicorn3,
pip3 install flask,
pip3 install pandas,
pip3 install sklearn,
-------------------
source 'init_script.sh'

5. Create local project folder and put your files locally on that folder
(https://www.w3schools.com/html/html_forms.asp) for creating forms
index.html
model.py
app.py

6. Migrate that folder to cloud machine using WinSCP/FileZilla

7. Write server script, restart nginx service

8. Run the app using guinicorn
