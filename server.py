from flask import Flask,render_template,send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('portfolio.html')

@app.route('/personal_data/<path:path>')
def personal_data(path):
   return send_from_directory("personal_data",path)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)