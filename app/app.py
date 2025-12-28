from flask import Flask, render_template

app = Flask(__name__)

def get_data_from_file():
    try:
        with open('storage/data.txt', 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return ["File not found!"]

@app.route('/')
def home():
    title = "Hello, World!"
    data = get_data_from_file()

    return render_template('index.html', title=title, data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
