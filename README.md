# ✨ Flask To-Do List App

A full-featured task management application built with Python and Flask. This project allows users to create accounts, manage their personal tasks, set priorities, and track progress through a clean, responsive interface.

## 🚀 Features

* **User Authentication**: Secure Login and Registration system using `Flask-Login`.
* **Task Management**: Create, Read, Update, and Delete (CRUD) tasks.
* **Status Tracking**: Toggle tasks between **Pending**, **Working**, and **Done** states.
* **Prioritization**: Categorize tasks by **Low**, **Medium**, or **High** priority.
* **Sorting**: Sort your dashboard by Priority or Due Date.
* **Responsive Design**: Mobile-friendly interface with custom CSS.
* **Data Persistence**: Uses SQLite with SQLAlchemy for reliable data storage.

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Database**: SQLite, SQLAlchemy
* **Authentication**: Flask-Login, Werkzeug Security
* **Frontend**: HTML5, CSS3, Jinja2 Templates

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
2. Create a Virtual Environment (Recommended)
Bash

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install flask flask-login flask-sqlalchemy
4. Run the Application
Bash

python run.py
Open your browser and navigate to: http://127.0.0.1:5000

📂 Project Structure
├── app/
│   ├── routes/         # Blueprints for Auth and Task logic
│   ├── static/         # CSS and JavaScript files
│   ├── templates/      # HTML templates (Jinja2)
│   ├── __init__.py     # App factory and DB initialization
│   └── models.py       # Database models (User, Task)
├── run.py              # Entry point for the application
├── todo.db             # SQLite Database (Auto-generated)
└── README.md
📸 Screenshots
(You can upload screenshots of your Login page and Dashboard here later)

🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request
