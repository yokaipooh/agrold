from flask import Flask, render_template, json, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__, template_folder='templates')
#SET SECRETKEY ---------------------------------------------------------------------------------
class Config_SK(object):
    app.config['SECRET_KEY'] = '6efc92e4fdea016b2111bd8a6432f19b'

#DATABASE---------------------------------------------------------------------------------------
class Config_DB(object):
    POSTGRES = {
        'user': 'postgres',
        'pw': '12345',
        'db': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }

    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

app.config.from_object(Config_DB)
db = SQLAlchemy(app)


#HEX USERPASSWORD-------------------------------------------------------------------------------
bcrypt = Bcrypt(app)


#-----------------------------------------------------------------------------------------------


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title = 'Basic search')

#@app.route('/search_results/<query>')
#def search_results(query):
#    if query == 'krp1':
#        results = krp1.query.all()
#    elif query == 'tcp2':
#        results = tcp2.query.all()
#    return render_template('search_results.html', query=query, results=results, title ='Search Results')

#form = SearchForm()
#   if request.method == 'POST' and form.validate_on_submit():
#        query=form.search.data
#        return redirect(url_for('search_results', query = query))
@app.route('/about')
def about():
    return render_template('about.html', title =' About')

@app.route('/search_advance')
def search_advance():
    return render_template('search_adv.html', title =' Search Advance')





if __name__ == '__main__':
    app.run(Debug = True)
