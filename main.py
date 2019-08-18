# coding:utf:8
from flask import Flask, render_response 
app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
	#return "Hello World!"
    #return "<html><head><title>Hi there!</title></head><body>Hello World!</body></html>", 200
    return render_template("index.html")

if __name__ == "__main__":
	app.run()	