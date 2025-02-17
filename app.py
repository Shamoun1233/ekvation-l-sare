from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    ek = 20  
    question = 3  
    tion = 3 * question  
    svar = ek - tion  

    return render_template("index.html", question=question, svar=svar)

if __name__ == "__main__":
    app.run(debug=True)
