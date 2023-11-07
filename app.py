from flask import Flask,url_for,render_template,request,flash,redirect


app = Flask(__name__)


@app.route('/')
def connexion():
    return render_template('connexion.html')

@app.route('/acceuil/')
def acceuil():
    return render_template('acceuil.html')


if __name__ == "__main__":
    app.run(debug=True)