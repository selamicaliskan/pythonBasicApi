from flask import Flask
import secrets

app = Flask(__name__)

# Güvenlik başlıkları ekleyelim
@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.route('/')
def hello_world():
    secure_random = secrets.SystemRandom()
    secret_number = secure_random.randint(1, 100)
    return f'Hello, World! This is my secure API. Secret number: {secret_number}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
