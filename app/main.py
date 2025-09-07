from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def users():
    return jsonify({"users": ["Ahmed", "Amr", "Sara"]})

@app.route('/posts')
def posts():
    return jsonify({"posts": ["Hello DevOps!", "Learning K8s", "CI/CD Rocks"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
