import os
from flask import Flask
from flask_cors import CORS
from routes.birthdays import birthday_bp

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Register blueprint
app.register_blueprint(birthday_bp, url_prefix='/api')

@app.route("/")
def home():
    return {"message": "Birthday Reminder Backend Running"}

if __name__ == "__main__":
    # Bind to 0.0.0.0 and use Render-assigned port
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
