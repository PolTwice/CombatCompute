from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define a "route" (the URL path a user visits)
@app.route("/")
def home():
    # Returning a dictionary automatically converts it to JSON data
    return {"message": "Welcome to the Illithid Fight Club"}

# This ensures the server only runs if we execute this file directly
if __name__ == "__main__":
    app.run(debug=True)
    
# The <username> syntax tells Flask to capture whatever text is typed there
@app.route("/user/<username>")
def show_user_profile(username):
    # The variable is automatically passed into your function
    return {"message": f"Hello, {username}! Fetching your combat data..."}

@app.route("/logs")
def get_logs():
    # request.args.get('key', 'default_value') reads the URL parameters safely
    level = request.args.get("level", "info") 
    limit = request.args.get("limit", 10)
    
    return {
        "status": "success",
        "filters_applied": {
            "severity_level": level,
            "max_records": limit
        }
    }