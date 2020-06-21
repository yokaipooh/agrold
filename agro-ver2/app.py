from flask import Flask, render_template, url_for, request, jsonify


app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title ='About')

@app.route('/search_adv')
def search_adv():
    return render_template('search_adv.html', title ='Search Advanced')

if __name__ == '__main__':
    app.run(debug=True)
