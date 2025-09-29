import os
from flask import Flask

# Flask is the web framework we are using.
# __name__ tells Flask where to look for files and resources.
app = Flask(__name__)

# This is the main page (the '/' route).
@app.route("/")
def hello_world():
    # Cloud Run sets the PORT environment variable for us to use.
    port = os.environ.get("PORT", "8080")
    
    # This is the message that will display when someone visits your website.
    return f"Hello, Cloud Run is working on port {port}!"

# When running locally or on Cloud Run, we listen on the port Cloud Run gives us.
if __name__ == "__main__":
    # Get the port from the environment variable PORT, or default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Host on 0.0.0.0 so it is accessible from outside the container
    app.run(host="0.0.0.0", port=port)
