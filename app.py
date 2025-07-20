from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html')
@app.route('/todo')
def todo():
    return render_template('todo.html')
@app.route('/progress')
def progress():
    return render_template('progress.html')
if __name__ == '__main__':
    app.run(debug=True)
