from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            ek = 20  # Startvärde
            question = int(request.form.get('question'))  # Hämta användarens input
            tion = 3 * question  # Multiplicera y med 3
            resultat = ek - tion if ek >= tion else tion - ek  # Se till att det inte blir negativt

            förklaring = f"Vi tar 20 - (3 * {question}), vilket ger {resultat}."  # Förklaring

            return render_template('index.html', question=question, resultat=resultat, förklaring=förklaring)
        except ValueError:
            return render_template('index.html', error="Skriv in ett giltigt nummer!")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)  # 🔥 Debug mode ON
