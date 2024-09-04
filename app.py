from flask import Flask 

app = Flask('counter')
counter = 0

@app.route('/counter')
def count():
    counter +=1
    return counter

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5000, debug=True)