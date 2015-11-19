from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def about():
	# return "Qdiary Project Started on 2015.11.17"
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)