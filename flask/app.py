from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', name=name, lst_1=lst_1)

@app.route('/input/<inp1>')
def output_text(inp1):
    return escape(inp1)


if __name__ == '__main__':
    app.run()

name = "ccewo"
lst_1 = [
    {'name': '张三', 'age': 20},
    {'name': '李四', 'age': 21},
    {'name': '王五', 'age': 22}
]

