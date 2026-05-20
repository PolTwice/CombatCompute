from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define a "route" (the URL path a user visits)
@app.route("/")
def home():
    # Returning a dictionary automatically converts it to JSON data
    return {"message": "Welcome to the CombatCompute API!"}

# This ensures the server only runs if we execute this file directly
if __name__ == "__main__":
    app.run(debug=True)