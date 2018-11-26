
Data extractor for PDF invoices

extracts text from PDF files using different techniques, like pdftotext, pdfminer or OCR – tesseract, tesseract4 or gvision (Google Cloud Vision).
searches for regex in the result using a YAML-based template system
saves results as CSV, JSON or XML or renames PDF files to match the content.

INSTALLATION OF VIRTUAL ENVIRONMENT AND FLASK:

commands to install virtual environment:

sudo apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install Flask
pip install pymongo
pip install invoice2data


AFTER INSTALLATION GO TO PROJECT DIRECTORY:

eg:-
(venv) taher@ubuntu:~/projects/invoice_reader_ai$


RUN THE FOLLOWING COMMAND FROM PROJECT DIRECTORY:
export FLASK_APP=pdfinvoice2data.py
flask run

GO TO YOUR BROWSER RUN THE PROJECT:
http://127.0.0.1:5000/


Go from PDF files to this:

{'date': (2014, 5, 7), 'invoice_number': '30064443', 'amount': 34.73, 'desc': 'Invoice 30064443 from QualityHosting', 'lines': [{'price': 42.0, 'desc': u'Small Business StandardExchange 2010\nGrundgeb\xfchr pro Einheit\nDienst: OUDJQ_office\n01.05.14-31.05.14\n', 'pos': u'7', 'qty': 1.0}]}
{'date': (2014, 6, 4), 'invoice_number': 'EUVINS1-OF5-DE-120725895', 'amount': 35.24, 'desc': 'Invoice EUVINS1-OF5-DE-120725895 from Amazon EU'}
{'date': (2014, 8, 3), 'invoice_number': '42183017', 'amount': 4.11, 'desc': 'Invoice 42183017 from Amazon Web Services'}
{'date': (2015, 1, 28), 'invoice_number': '12429647', 'amount': 101.0, 'desc': 'Invoice 12429647 from Envato'}
