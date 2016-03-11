from flask import Flask, url_for, redirect, session, flash
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import  Moment
from datetime import datetime
import wtf as wtf
# from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string' #设置密钥保护所有表单免受跨站请求伪造
bootstrap = Bootstrap(app)
moment = Moment(app)

# @app.route('/')
# def root_page():
#     return '<h1>ssss</h1>'

@app.route('/user/<name>')
def show_name(name):
    comments=['k', 'l', 1, 'rr', 6]
    return render_template('user.html', name=name, comments=comments)

@app.route('/templates/base')
def show_icon():
    return  render_template('base.html',current_time=datetime.utcnow())

@app.route('/', methods=['GET', 'POST'])
def index():
   # name = None
    form = wtf.NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('New User Ha')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('form.html', form=form, name=session.get('name'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_error(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    app.run(debug='true')

