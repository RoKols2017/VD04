from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ultra-secret-mode'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def get_template_path(page):
    ui = session.get('ui', 'vanilla')
    return f'{ui}/{page}.html'

@app.route('/')
def index():
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render_template(get_template_path('index'), current_time=now)

@app.route('/blog')
def blog():
    return render_template(get_template_path('blog'))

@app.route('/contacts')
def contacts():
    return render_template(get_template_path('contacts'))

@app.route('/switch-ui')
def switch_ui():
    session['ui'] = 'bootstrap' if session.get('ui', 'vanilla') == 'vanilla' else 'vanilla'
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)