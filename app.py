

from  flask import Flask,request,redirect,url_for,jsonify,render_template
from config import Config
from models import db,User
#
#
app=Flask(__name__)
app.config.from_object(Config) # loading all those configurations to the flask

db.init_app(app)# making connection between flask and the database
with app.app_context():
    db.create_all() # create the tables

@app.route("/")
def hello():
    return "Hello World"
    # return jsonify(message="Hello World") # converting it into dictionary.

@app.route("/html_template", methods=['GET'])
def html_temp():
    return render_template('demo.html')

@app.route("/html_content", methods=['GET'])
def html_cont_func():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>From Templates</h1>
</body>
</html>
    """

@app.route("/path_param/<int:id>", methods=['GET'])
def path_param_func(id):
    return {"message" : f"path param is {id}"}

@app.route("/query_param/", methods=['GET'])
def query_param_func():
    name=request.args.get('name')
    age=request.args.get('age')
    return {"message" : f"query params are {name}, {age}"}
    # data=request.args.to_dict() # when we don't know the parameters.
    # return {"message " : data}
    # data=request.args.getlist('name') #for same datatype
    # return {"message" : {'name' : data}}

@app.route("/form_data", methods=['POST'])
def post_form_data_func():
    name=request.form.get('name')
    age=request.form.get('age')
    return {"message" : f"query params are {name}, {age}"}

@app.route("/json_data",methods=['POST'])
def post_json_data():
    data=request.get_json()
    return data

@app.route("/string_length/<string(length=6):name>", methods=['GET'])
def str_len_func(name):
    return {"message" : f"string is {name}"}

@app.route("/redirect",methods=['GET'])
def redirect_func():
    return redirect(url_for("hello"))



if __name__ == "__main__":
    app.run(debug=True)
