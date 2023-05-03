from flask import Flask, render_template, request
from recommender import nmf

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/results')
def recommender():
    user_query = request.args.to_dict()
    user_query = {key:int(value) for key,value in user_query.items()}

    suggestions = nmf(user_query)
    return render_template('results.html', movies = suggestions)

if __name__ == '__main__':
    app.run(port=5000, debug=True)