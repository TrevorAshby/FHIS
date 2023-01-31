from flask import Flask, render_template, request, jsonify
import json

app=Flask(__name__, template_folder='./GUI/template', static_folder='./GUI/static') #instantiating flask object

@app.route('/')
def index():
    return render_template('gui.html')


if __name__=='__main__': #calling  main 
    app.debug=True #setting the debugging option for the application instance
    app.run(host="0.0.0.0", port="3000") #launching the flask's integrated development webserver