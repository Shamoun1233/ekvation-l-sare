from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        if request.method == 'POST':
            ek = 20  
            question = int(request.form.get('question'))  
            tion = 3 * question  
            resultat = ek - tion if ek >= tion else tion - ek  
            förklaring = f"Vi tar 20 - (3 * {question}), vilket ger {resultat}."  

            return render_template('index.html', question=question, resultat=resultat, förklaring=förklaring)
        return render_template('index.html')
    except Exception as e:
        return f"Error: {e}", 500  # Shows error message

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
