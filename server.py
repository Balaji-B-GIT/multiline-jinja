from flask import Flask,render_template
import requests
app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

response = requests.get(blog_url)
data = response.json()
@app.route('/')
def func():
    return render_template("index.html",blogs = data)

if __name__ == "__main__":
    app.run(debug=True)