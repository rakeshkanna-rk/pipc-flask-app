# PIP CREATOR | FLASK

## Overview
This PIP CREATOR Plugin automates the creation of all necessary files and folders to set up a Flask application. You can choose between three types of Flask apps: **Basic**, **Advanced**, and **With Framework**. The plugin also supports additional features like virtual environment creation, git initialization, and CDN framework integration for front-end development.

## Features
1. **App Types**:
    - **Basic**: Simple Flask structure with static files, templates, and virtual environment.
    - **Advanced**: More structured Flask project with Blueprints, models, forms, and configuration files.
    - **With Framework**: Flask integrated with front-end frameworks like React, Next.js, or Vite. Custom frameworks are also supported.

2. **Virtual Environment**: Automatically creates a Python virtual environment (`venv`) for safe package management.

3. **Git Initialization**: Optionally initialize a git repository with `.gitignore` and create a proper project structure.

4. **Test Folder**: Creates a test folder if required by the user.

5. **CDN Frameworks**: Easy integration with popular CSS frameworks via CDN:
    - Bootstrap (v5.3.2)
    - Foundation (v6.6.3)
    - Materialize (v1.0.0)
    - Bulma (v0.9.4)
    - Semantic UI (v2.4.2)
    - UIkit (v3.16.23)
    - Tailwind (v3.3.3)
    - Pure CSS (v2.1.0)
    - Spectre.css (v0.5.9)
    - Skeleton (v2.0.4)

    [CDN Frameworks](https://github.com/rakeshkanna-rk/pipc-flask-app/blob/master/docs/CDN%20FRAMEWORKS.MD)

---

## App Structures

### 1. **Basic Flask App**
```
{project_name}/
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── images/
├── templates/
│   ├── layout.html
│   └── home.html
├── test/ (optional)
│   ├── test_basic.py
│   └── conftest.py
├── venv/
├── README.md
├── run.py
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── .gitignore
```

### 2. **Advanced Flask App**
```
{project_name}/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── layout.html
│       └── home.html
│
├── tests/ (optional)
│   ├── test_basic.py
│   └── conftest.py
├── config.py
├── README.md
├── run.py
├── requirements.txt
├── pyproject.toml
├── LICENSE
├── venv/
├── instance/
│   └── config.py
├── migrations/
└── .env or .flaskenv
```

### 3. **Flask App With Front-End Framework**
```
{project_name}/
│
├── client/
│   └── <framework>/
│ 
├── server/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── layout.html
│       └── home.html
│
├── tests/ (optional)
│   ├── test_basic.py
│   └── conftest.py
├── venv/
├── config.py
├── README.md
├── run.py
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── .gitignore
```
Framework options: **React**, **Next.js**, **Vite**. Custom frameworks can be installed with commands like `npx create-next-app`.

---

## Installation

1. Install the plugin: `pip install pipc-flask` else `pipc install pipc.flask-app --plugin` if you have pipCreator installed.
2. Run the script to create the Flask app:
   ```bash
   pipc-flask create <project_name>
   ```
