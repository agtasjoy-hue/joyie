from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Beautiful home page template
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🌸 Welcome to My Flask API 🌸</title>
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ff69b4);
      color: #333;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }
    h1 {
      background: white;
      padding: 20px 40px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
      font-size: 2em;
      color: #ff1493;
      text-align: center;
    }
    p {
      font-size: 1.2em;
      margin-top: 15px;
      color: #444;
    }
    a {
      margin-top: 25px;
      display: inline-block;
      background: #ff1493;
      color: white;
      text-decoration: none;
      padding: 10px 25px;
      border-radius: 30px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
      transition: all 0.3s ease;
    }
    a:hover {
      background: white;
      color: #ff1493;
      box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }
    footer {
      position: absolute;
      bottom: 20px;
      font-size: 0.9em;
      color: #555;
    }
  </style>
</head>
<body>
  <h1>✨ Welcome to My Flask API ✨</h1>
  <p>Use the endpoint below to view student details:</p>
  <a href="/student">➡️ View Student JSON</a>
  <footer>Created with 💖 using Flask</footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

if __name__ == '__main__':
    app.run(debug=True)
