from flask import Flask, render_template, request, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/identify_ip", methods=["POST"])
def identify_ip():
    url = request.form.get("url")
    # Extract IP addresses from the provided URL
    ip_addresses = get_ip_addresses(url)
    return jsonify({"ip_addresses": ip_addresses})

def get_ip_addresses(url):
    try:
        ip_addresses = [socket.gethostbyname(url)]
    except socket.gaierror:
        ip_addresses = ["Unable to resolve IP address"]
    return ip_addresses

if __name__ == "__main__":
    app.run(debug=True)