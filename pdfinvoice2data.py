from flask import Flask, render_template, request
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import yaml
import glob
import errno
import os
import pymongo
#import PyPDF2

app = Flask(__name__)

read_template = read_templates(folder="invoice_templates")

pdfFiles = []
pdfFiles1 = []
pdfFiles2 = []
filenames=[]
path_filename=[]

#path = "/home/taher/Desktop/iconnect-opensource-invoice_reader_ai-b82f8f46c28c/static/pdf_files"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pdfinvdata"]
mycol = mydb["invoicedata"]


for filename in os.listdir('/home/taher/Desktop/iconnect-opensource-invoice_reader_ai-b82f8f46c28c/static/pdf_files/'):
    if filename.endswith(".pdf"):
        filenames.append(filename)
        pathname = '/home/taher/Desktop/iconnect-opensource-invoice_reader_ai-b82f8f46c28c/static/pdf_files/'+str(filename)
        path_filename.append(pathname)
        result = extract_data('/home/taher/Desktop/iconnect-opensource-invoice_reader_ai-b82f8f46c28c/static/pdf_files/'+filename, read_template)
        pdfFiles1.append(result)
        #print(type(result))
        #print("----------------------")
        if (result==False):
            pdfFiles.append(filename)
        else:
            pdfFiles.append(result)


#pdfFiles.sort()
#print(pdfFiles)
#print(filenames)
#print(path_filename)


i = 0
amount_total = 0.00

for k in pdfFiles1:
    if (k!=False):
        #print(k)
        amount_total = amount_total + k['amount']

amount_total = format(amount_total, '.2f')
print(amount_total)


files_count = len(filenames)
#print(files_count)

count_data_extracted = 0

for count1 in pdfFiles1:
    #print(count1)
    if(count1!=False):
        count_data_extracted = count_data_extracted+1

for count1 in pdfFiles1:
    #print(count1)
    if(count1!=False):
        pdfFiles2.append(count1)

#print(count_data_extracted)
print(pdfFiles2)

#print(pdfFiles[0]['amount'])

count_values={"Data_Extracted":count_data_extracted, "Number_of_Files":files_count, "Amount_Total":amount_total}






'''
posts1 = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

'''

@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
def home():
    return render_template('BS3/invoice_data_extraction.html', posts=pdfFiles, posts1=filenames, posts3=count_values)


@app.route("/verify_invoices")
def about():
    return render_template('BS3/verify_invoices.html', title='About', posts=pdfFiles, posts1=filenames, posts3=count_values, posts4=pdfFiles2)

@app.route("/home1", methods = ['GET', 'POST'])
def home1():
    if request.method == 'POST':
        result12 = request.form.to_dict()
        print(result12)
        mycol.insert_one(result12)
    return render_template('home1.html', result13=result12)




if __name__ == '__main__':
    app.run(debug=True)
