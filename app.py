from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Temporary in-memory student list (no database needed)
students = [
    {"id": 1, "name": "Cutiee Joyiee ", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Aira ", "grade": 9, "section": "Judah"}
]

# 🌸 Home Page with full CRUD UI
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🌸 Student Management - Flask API 🌸</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    * { box-sizing: border-box; }
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(120deg, #ffb6c1, #ffc0cb, #ff69b4);
      background-size: 300% 300%;
      animation: gradientShift 10s ease infinite;
      display: flex; justify-content: center; align-items: center;
      height: 100vh; margin: 0;
    }
    @keyframes gradientShift {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    .container {
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(12px);
      border-radius: 25px;
      padding: 40px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
      width: 600px;
      text-align: center;
    }
    h1 { color: #ff1493; margin-bottom: 10px; }
    h2 { color: #444; margin-top: 30px; }
    button {
      background: #ff1493; color: white; border: none;
      padding: 10px 20px; border-radius: 30px;
      cursor: pointer; margin: 5px;
      transition: 0.3s; font-weight: 600;
    }
    button:hover { background: white; color: #ff1493; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
    input {
      padding: 8px 12px; border-radius: 10px; border: 1px solid #ff69b4;
      margin: 5px; outline: none; width: 30%;
    }
    table {
      width: 100%; margin-top: 15px; border-collapse: collapse;
      border: 2px solid #ff69b4; border-radius: 15px; overflow: hidden;
    }
    th, td {
      padding: 10px; border-bottom: 1px solid #ffb6c1; color: #333;
    }
    th { background: #ffb6c1; color: white; }
    tr:hover { background-color: #fff0f5; }
    footer { margin-top: 20px; color: #666; font-size: 0.9em; }
  </style>
</head>
<body>
  <div class="container">
    <h1>🎓 Student Management API 💕</h1>
    <p>Add, Edit, or Delete Students dynamically!</p>

    <div>
      <input type="text" id="name" placeholder="Student Name">
      <input type="number" id="grade" placeholder="Grade">
      <input type="text" id="section" placeholder="Section">
      <button onclick="addStudent()">➕ Add</button>
    </div>

    <h2>📋 Student List</h2>
    <table id="studentTable">
      <thead>
        <tr>
          <th>ID</th><th>Name</th><th>Grade</th><th>Section</th><th>Action</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>

    <footer>Created with 💖 Flask & Python 3.12</footer>
  </div>

  <script>
    async function loadStudents() {
      const res = await fetch('/students');
      const data = await res.json();
      const tbody = document.querySelector("#studentTable tbody");
      tbody.innerHTML = "";
      data.forEach(s => {
        tbody.innerHTML += `
          <tr>
            <td>${s.id}</td>
            <td>${s.name}</td>
            <td>${s.grade}</td>
            <td>${s.section}</td>
            <td>
              <button onclick="editStudent(${s.id})">✏️ Edit</button>
              <button onclick="deleteStudent(${s.id})">🗑️ Delete</button>
            </td>
          </tr>`;
      });
    }

    async function addStudent() {
      const name = document.getElementById("name").value;
      const grade = document.getElementById("grade").value;
      const section = document.getElementById("section").value;
      if (!name || !grade || !section) return alert("Please fill all fields!");
      await fetch('/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, grade, section })
      });
      loadStudents();
      document.getElementById("name").value = '';
      document.getElementById("grade").value = '';
      document.getElementById("section").value = '';
    }

    async function editStudent(id) {
      const newName = prompt("Enter new name:");
      const newGrade = prompt("Enter new grade:");
      const newSection = prompt("Enter new section:");
      if (!newName || !newGrade || !newSection) return;
      await fetch('/students/' + id, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newName, grade: newGrade, section: newSection })
      });
      loadStudents();
    }

    async function deleteStudent(id) {
      if (!confirm("Are you sure you want to delete this student?")) return;
      await fetch('/students/' + id, { method: 'DELETE' });
      loadStudents();
    }

    loadStudents();
  </script>
</body>
</html>
"""

# === Flask Routes ===
@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_id = max([s["id"] for s in students]) + 1 if students else 1
    new_student = {
        "id": new_id,
        "name": data.get("name"),
        "grade": data.get("grade"),
        "section": data.get("section")
    }
    students.append(new_student)
    return jsonify({"message": "Student added!", "student": new_student})

@app.route('/students/<int:student_id>', methods=['PUT'])
def edit_student(student_id):
    data = request.get_json()
    for s in students:
        if s["id"] == student_id:
            s["name"] = data.get("name", s["name"])
            s["grade"] = data.get("grade", s["grade"])
            s["section"] = data.get("section", s["section"])
            return jsonify({"message": "Student updated!", "student": s})
    return jsonify({"error": "Student not found"}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Student deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
