Bookmark Manager – CRUD Application

This is a simple Bookmark Manager project built using Django, Python, MySQL, HTML, and CSS.
The application performs basic CRUD operations: create, read, update, and delete bookmarks.
Each bookmark contains a Title and a URL.

Features

1.Add a new bookmark
2.View all bookmarks
3.Update an existing bookmark
4.Delete a bookmark
5.Simple and clean user interface
6.Uses Django ModelForm for input
7.MySQL database integration

Technologies Used

Python
Django
MySQL
HTML

How to Run the Project

1.Open terminal or command prompt inside the project folder.
2.Create and activate a virtual environment.
    python -m venv venv
    venv\Scripts\activate

3.Configure MySQL database in settings.py
    python manage.py makemigrations
    python manage.py migrate
    
4.Start the Django development server
    python manage.py runserver
