from flask import Flask
app = Flask(__name__)

@app.route("/")
def about():
	return "Qdiary Project Started on 2015.11.17"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)
