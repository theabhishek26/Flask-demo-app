# Flask-demo-app

A simple **Flask-based web application** that displays a styled page.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [How This Project Was Made](#how-this-project-was-made)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)

---

## Overview

This project demonstrates:
- Basics of Flask routing
- HTML templating
- CSS styling

---

## Features

- Flask backend serving HTML templates
- Static CSS for design
- Responsive layout

---

## Project Structure

```
Flask-demo-app/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── static/              # Static files (CSS, images, JS)
│   └── style.css
├── templates/           # HTML templates
│   └── index.html
```

---

## How This Project Was Made

1. **Initialize Project Folder**
   - Created a folder named `Flask-demo-app`.

2. **Set Up Flask Application**
   - Created `app.py` as the main entry point.
   - Imported Flask and set up a basic application instance:
     ```python
     from flask import Flask, render_template
     app = Flask(__name__)
     ```

3. **Define Routing**
   - Added a home route (`/`) in `app.py` that renders an HTML template:
     ```python
     @app.route('/')
     def home():
         return render_template('index.html', title='Home Page')
     ```

4. **Create HTML Template**
   - Made a `templates` folder.
   - Added `index.html` for the homepage layout.
   - Used Jinja templating to display the title and structure the page.

5. **Add CSS Styling**
   - Created a `static` folder.
   - Added `style.css` for custom styles.
   - Linked the CSS file in `index.html` to style the page.

6. **List Dependencies**
   - Created `requirements.txt` with Flask as a dependency:
     ```
     Flask
     ```

7. **Run the Application**
   - Used the following command to start the server:
     ```
     python app.py
     ```
   - Accessed the app in the browser at `http://127.0.0.1:5000/`.

---

## Setup Instructions

1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/`.

---

## Usage

- The homepage displays a styled page using HTML and CSS.
- You can modify `index.html` and `style.css` to change the content and appearance.

---