from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message" : "Hello world" })

@app.route('/login/', methods=["GET","POST"])
def login_page():
    error = ''
    try:
        if request.method == "POST":
            content = request.json
            attempted_username = content['username']
            attempted_password = content['password']
            if attempted_username == "admin" and attempted_password == "password":
                return jsonify({"status": "logged in"})
            else:
                error = "Invalid credentials. Try Again."

        return jsonify({"error": error})

    except Exception as e:
        print(e)
        return jsonify({"error": "some error occurred"})  
		
if __name__ == "__main__":
    app.run(debug=True)

