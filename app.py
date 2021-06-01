import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)


# local imports
from s3_handler import upload_file_handler, list_files_handler,get_file_handler,delete_file_handler

app.config["UPLOAD_FOLDER"] = "static/"

# page to upload
@app.route('/upload')
def upload_file():
    return render_template('index.html')
	
# api to handle uploaded file
@app.route('/api/upload', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']

        f.save(secure_filename(f.filename))

        res = upload_file_handler(f"{f.filename}", f.filename)

        return {"result" : res}

		
# api to get all file names
@app.route('/api/list/files', methods = ['GET'])
def list_all_files():

    all_files = list_files_handler()

    return {
        "files": all_files
    }


@app.route('/api/get/file', methods = ['GET'])
def get_all_files():

    result = get_file_handler()

    result.save(secure_filename(result))

    return {
        "result": result
    }

@app.route('/api/delete/file', methods = ['POST'])
def delete_files():
    
    file_name = request.form['file_name']

    result = delete_file_handler(file_name)

    return {
        "result": result
    }




# @app.route('/get-info', methods = ['GET', 'POST'])
# def get_info():
#     if request.method == 'POST':

#         f = request.files['file']
        
#         f.save(secure_filename(f.filename))
        
#         file = open(f.filename,"r")
#         line_count = 0
#         word_count = 0

#         content = file.read()
#         line_list = content.split("\n")
        
#         for line in line_list:
#             word_list = line.split(" ")
#             word_count += len(word_list)
            
#         for i in line_list:
#             if i:
#                 line_count += 1
		
#         print(word_count-1, len(line_list)-1)

#         print("This is the number of lines in the file")
#         print(line_count)

#         print("This is the number of words in the file")
#         print(word_count)

#         return {
#             'line count': line_count,
#             'word count': word_count
#         }

	
# @app.route('/image', methods = ['GET', 'POST'])
# def display_image():
#     if request.method == 'POST':
#         f = request.files['file']

#         filename = secure_filename(f.filename)
#         print('hhshh---------',  app.config['UPLOAD_FOLDER'] + filename)
#         f.save(app.config['UPLOAD_FOLDER'] + filename)

#         return render_template('image-display.html', filename = f.filename )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)

