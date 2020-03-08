import sys
from flask import Flask, render_template, request, send_file
import os
import zipfile

application = Flask(__name__)

@application.route('/') #creates the flask html route
def root():
    return render_template('main.html')

@application.route('/', methods=['POST']) #creates the flask html route
def post():
    text1 = request.form['user1'] #getting usernames

    args = "python3 multiThreadTask.py "+ str(text1)
    os.system(args)

    # zipFolder = zipfile.ZipFile('videos.zip','w', zipfile.ZIP_DEFLATED) 
    # for files in os.walk('videos/'):
    #     # for f in files:
    #     #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
    #     #     print(f)
    #     #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
    #     zipFolder.write('videos/' + str(files))
    #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
    #     print(files)
    #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # zipFolder.close()
    zipFolder = zipfile.ZipFile('videos.zip','w', zipfile.ZIP_DEFLATED) 
    for root, directs, files in os.walk('videos/'):
        for f in files:
            print(f)
            zipFolder.write('videos/' + str(f))
    zipFolder.close()    

    # os.system("rm videos/*")
    return send_file('videos.zip', mimetype ='zip', attachment_filename = 'videos.zip', as_attachment=True)

if __name__ == '__main__':
    # application.run(debug=True)
    application.run(host = '0.0.0.0', port = 5000)
    # application.run(debug=True, port=8000)