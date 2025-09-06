-Library System Project
A Django-based library management system designed for managing books, checkouts, and user accounts. This system provides both a REST API for programmatic access and a clean web interface for administrators and users.
The system enforces secure admin-controlled user creation, robust password policies, and dynamic book inventory management.
  
  Key Features
User Management
•    Admin-controlled user registration via a secret code.
•    Password policy enforcement:
o    Minimum 8 characters
o    Must include at least one special character
•    Prevents duplicate usernames.
•    User login and logout functionality.
•    Clear, contextual feedback for success and error messages.
Checkout Management
•    Add, edit, delete, and return book checkouts.
•    Automatic stock adjustment when books are checked out or returned.
•    REST API endpoints powered by Django REST Framework.
Frontend
•    Clean and modern HTML templates:
o    Signup and login pages
o    Users list
o    Checkouts list
•    Consistent UI styling with message notifications for success and errors.
•    Responsive table layouts for easy data viewing.

Installation Instructions
Prerequisites
•    Python 3.9+
•    Django 4.2+
•    Django REST Framework
Setup Steps
1.    Clone the repository
-    git clone <https://github.com/leulMas/library_system_project>
-    cd library_system_project
2.    Create and activate a virtual environment
-    python -m venv venv
-    source venv/bin/activate  # 
3.    Install dependencies
-    pip install -r requirements.txt
4.    Apply database migrations
-    python manage.py makemigrations
-    python manage.py migrate
5.    Create a superuser (optional)
-    python manage.py createsuperuser
6.    Run the development server
-    python manage.py runserver
7.    Access the application
•    Home: http://127.0.0.1:8000/
•    Admin signup: http://127.0.0.1:8000/users/signup/
•    Login: http://127.0.0.1:8000/users/login/

Admin User Signup & Password Policy
•    Admin Secret Code: Required to register new users. Configure in users/forms.py:
ADMIN_SECRET_CODE = "Password"  # Replace with your secret
•    Password Policy: Enforced via AdminUserCreationForm:
o    Minimum length: 8 characters
o    At least one special symbol: !@#$%^&*(),.?":{}|<>
•    Error messages are displayed on the signup page:
o    Weak password
o    Incorrect secret code
o    Duplicate username

Customizable Features
•    Admin Secret Code: Changeable in forms.py.
•    Password Validation: Easily adjustable in AdminUserCreationForm.
•    Frontend Templates: HTML templates can be customized to match your branding.
Future Enhancements
•    Add password reset functionality.
•    Implement searchable book catalog with categories.
•    Introduce user role management (e.g., librarian vs. standard user).
•    Enhance UI with Bootstrap or Tailwind CSS.
•    Expand REST API coverage for checkouts and users.

