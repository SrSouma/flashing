from flask import Flask, flash, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/flashing')
def flashing():
  flash('sucesso', 'success')
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)