from flask import Flask

# Instantiating the flask app
app = Flask(__name__)

# Bounding url to the function by using decorator
@app.route("/")
def hello_world():
	return "welcome to CDAC (240940128026)"

# Running the flask app if the current script is main program
if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 5000)

