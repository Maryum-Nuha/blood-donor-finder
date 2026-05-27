from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "blood123"

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect("donors.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        blood_group TEXT,
        city TEXT,
        phone TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            session["user"] = "admin"
            return redirect("/")
        return "Invalid login"
    return render_template("login.html")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# ---------- HOME ----------
@app.route("/", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect("/login")

    msg = ""

    if request.method == "POST":
        name = request.form["name"]
        blood_group = request.form["blood_group"]
        city = request.form["city"]
        phone = request.form["phone"]

        conn = sqlite3.connect("donors.db")
        c = conn.cursor()
        c.execute("INSERT INTO donors VALUES (NULL,?,?,?,?)",
                  (name, blood_group, city, phone))
        conn.commit()
        conn.close()

        msg = "✔ Donor Added Successfully!"

    return render_template("index.html", msg=msg)

# ---------- SEARCH ----------
@app.route("/search", methods=["GET", "POST"])
def search():
    if "user" not in session:
        return redirect("/login")

    data = []

    if request.method == "POST":
        bg = request.form["blood_group"]

        conn = sqlite3.connect("donors.db")
        c = conn.cursor()
        c.execute("SELECT * FROM donors WHERE blood_group=?", (bg,))
        data = c.fetchall()
        conn.close()

    return render_template("search.html", data=data)

# ---------- ALL DONORS ----------
@app.route("/donors")
def donors():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("donors.db")
    c = conn.cursor()
    c.execute("SELECT * FROM donors")
    data = c.fetchall()
    conn.close()

    return render_template("donors.html", data=data)

# ---------- DELETE ----------
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("donors.db")
    c = conn.cursor()
    c.execute("DELETE FROM donors WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/donors")

# ---------- EDIT ----------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = sqlite3.connect("donors.db")
    c = conn.cursor()

    if request.method == "POST":
        c.execute("""UPDATE donors SET name=?, blood_group=?, city=?, phone=? WHERE id=?""",
                  (request.form["name"], request.form["blood_group"],
                   request.form["city"], request.form["phone"], id))
        conn.commit()
        conn.close()
        return redirect("/donors")

    c.execute("SELECT * FROM donors WHERE id=?", (id,))
    donor = c.fetchone()
    conn.close()

    return render_template("edit.html", donor=donor)

if __name__ == "__main__":
    app.run(debug=True)