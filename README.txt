
INSTALLATION OF VIRTUAL ENVIRONMENT AND FLASK:

commands to install virtual environment:

sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install Flask

AFTER INSTALLATION GO TO PROJECT DIRECTORY:

eg:-
(venv) taher@ubuntu:~/projects/invoice_reader_ai$


RUN THE FOLLOWING COMMAND FROM PROJECT DIRECTORY:
export FLASK_APP=pdfinvoice2data.py
flask run

GO TO YOUR BROWSER RUN THE PROJECT:
http://127.0.0.1:5000/


