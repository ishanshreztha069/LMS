# Library Management System (LMS)

A Django-based web application for managing a library's books, authors, categories, and user borrowing records, developed for the BCA 4th Semester lab report.

## 👥 Team Members
* [Ishan Shrestha](https://github.com/ishanshreztha069)
* [ronin-x3](https://github.com/ronin-x3)

## 🛠 Technical Specifications
* **Architecture:** Django MVT (Model-View-Template)
* **Database:** MySQL (Relational Schema)
* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Python 3.x

## 🚀 Features
- User registration and authentication
- Book catalog with search functionality
- Borrowing and returning books
- User profiles with borrowed book history
- Admin dashboard for managing library data
- Responsive design

## 💻 Setup Instructions

1. Clone the repository or navigate to the LMS directory:
```bash
git clone [https://github.com/ishanshreztha069/LMS.git](https://github.com/ishanshreztha069/LMS.git)

```
 2. Install dependencies:
```bash
pip install -r requirements.txt

```
 3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate

```
 4. Create a superuser:
```bash
python manage.py createsuperuser

```
 5. Run the development server:
```bash
python manage.py runserver

```
 6. Access the application at http://127.0.0.1:8000/
## 📖 Usage
 * Register a new account or login with existing credentials.
 * Browse and search for books in the catalog.
 * Borrow available books and view them in your profile.
 * Return books from your profile.
 * Admin users can access the admin dashboard to manage books, authors, categories, and borrow records.
## 📂 Project Structure
 * LMS/: Main Django project directory
 * main/: Main app containing models, views, templates, and static files
 * db.sqlite3: SQLite database file
 * manage.py: Django management script
```

```
