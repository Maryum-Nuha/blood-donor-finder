# 🩸 Blood Donor Finder System

A lightweight and user-friendly web application built using **Flask** and **SQLite3** to manage blood donor records efficiently. The system helps users quickly search donors based on blood groups while securely maintaining donor information.

---

# 🚀 Features

✅ Secure Admin Login System  
✅ Add New Donors  
✅ Search Donors by Blood Group  
✅ View Complete Donor History  
✅ Edit Donor Information  
✅ Delete Donor Records  
✅ Automatic Date & Time Tracking  
✅ Phone Number Validation  
✅ Professional Red & White UI Design  
✅ SQLite Local Database Support  

---

# 🛠️ Technologies Used

- Python
- Flask
- SQLite3
- HTML5
- CSS3

---

# 📁 Project Structure

```text
blood-donor-finder/
│
├── app.py
├── donors.db
├── requirements.txt
│
├── static/
│   └── style.css
│
└── templates/
    ├── login.html
    ├── index.html
    ├── search.html
    ├── donors.html
    └── edit.html
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/blood-donor-finder.git
```

---

## 2️⃣ Open Project Folder

```bash
cd blood-donor-finder
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

---

# 🌐 Open In Browser

```text
http://127.0.0.1:5000/login
```

---

# 🔐 Default Login Credentials

```text
Username: admin
Password: admin123
```

---

# 📊 Main Modules

## 🏠 Home Page
- Add donor details
- Stores donor with current date & time

## 🔍 Search Donor
- Search donor by blood group
- Displays “No Donors Found” if unavailable

## 🩸 Donor History
- Displays all donors
- Latest donors shown first

## ✏️ Edit Donor
- Update donor details anytime

## ❌ Delete Donor
- Remove donor records permanently

---

# 🗄️ Database

The project uses a lightweight local SQLite database:

```text
donors.db
```

Database is automatically created when the app runs.

---

# 🎯 Future Improvements

- Dashboard Analytics
- Blood Group Statistics Charts
- Mobile Responsive Design
- Online Deployment
- Email Notifications
- Hospital Integration

---

# 👨‍💻 Developed Using Flask

A beginner-friendly mini project suitable for:
- College Projects
- Flask Learning
- Database Management Practice
- Web Development Practice

---