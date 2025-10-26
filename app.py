from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# ✨ Beautiful interactive homepage with dynamic content
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🌸Flask API Dashboard 🌸</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    * {
      box-sizing: border-box;
    }

    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #ffdde1, #ee9ca7);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      overflow: hidden;
    }

    .container {
      background: rgba(255, 255, 255, 0.8);
      backdrop-filter: blur(10px);
      border-radius: 25px;
      padding: 40px 60px;
      text-align: center;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
      animation: fadeIn 1.2s ease-in-out;
      max-width: 500px;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    h1 {
      color: #ff1493;
      font-size: 2em;
      margin-bottom: 15px;
    }

    p {
      color: #555;
      font-size: 1.1em;
      margin-bottom: 25px;
    }

    button {
      background: #ff1493;
      color: white;
      border: none;
      padding: 12px 30px;
      font-size: 1em;
      border-radius: 30px;
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    button:hover {
      background: white;
      color: #ff1493;
      box-shadow: 0 6px 15px rgba(0,0,0,0.3);
    }

    .data-box {
      margin-top: 25px;
      background: #fff0f5;
      border: 2px solid #ff69b4;
      border-radius: 15px;
      padding: 15px;
      font-family: monospace;
      text-align: left;
      color: #333;
      display: none;
      animation: fadeIn 0.8s ease;
    }

    footer {
      margin-top: 25px;
      color: #666;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>✨ Welcome to My Flask API ✨</h1>
    <p>Explore student data through an elegant API experience 💕</p>
    <button onclick="fetchData()">View Student Info</button>

    <div id="dataBox" class="data-box"></div>

    <footer>Created with 💖 using Flask & JavaScript</footer>
  </div>

  <script>
    async function fetchData() {
      const box = document.getElementById('dataBox');
      box.style.display = 'block';
      box.innerHTML = 'Loading... ⏳';
      try {
        const res = await fetch('/student');
        const data = await res.json();
        box.innerHTML = JSON.stringify(data, null, 2);
      } catch (err) {
        box.innerHTML = 'Error fetching data ❌';
      }
    }
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Cutiee Joyiee 🌸",
        "grade": 10,
        "section": "Zechariah",
        "interests": ["Coding 💻", "Design 🎨", "Music 🎶"],
        "goal": "To build creative and inspiring tech projects ✨"
    })

if __name__ == '__main__':
    app.run(debug=True)
