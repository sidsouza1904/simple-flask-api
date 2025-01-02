from flask import Flask
from data import students


app = Flask(__name__)


@app.route('/students', methods=['GET'])
def get():
    return students


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)