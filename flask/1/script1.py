#This imports the class flask from Flask
from flask import Flask, render_template
#This instantiates the app using the flask class
app=Flask(__name__)

#This defines the Home page of the Website - app.route - is the URL
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

#This confirms that is the script is run normally, if the script is imported it will fail.
if __name__=="__main__":
    app.run(debug=True)
