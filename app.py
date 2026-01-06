from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
    <h1>Hello from Flask - Gabriella är klar med labben!</h1>
    <p>Version: {os.getenv("APP_VERSION")}</p>
    """

