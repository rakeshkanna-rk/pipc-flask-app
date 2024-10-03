# PipCreator - pipc-flask-app - CND Frameworks

### 1. **Folder Structure**

Flask uses a specific folder structure for static files (CSS, JS, images) and HTML templates. Here’s the recommended structure:

```txt
/your_flask_app
   /static
       /css
       /js
   /templates
       layout.html
       your_page.html
   app.py
```

### 2. **Step-by-Step Guide**

#### a. **Place CSS and JS Files in Static Folder (Optional)**
If you want to serve the CSS and JS files locally instead of via CDN, download the files and place them in the `/static/css` and `/static/js` directories. However, using the CDN is simpler for external frameworks.

#### b. **Add CDN Links in Base Template (layout.html)**
Create a `layout.html` file in the `/templates` folder, which will act as the base template for all other pages.

Here’s an example of how to add the frameworks to your `layout.html` using the CDN links:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    
    <!-- Add your framework's CSS here -->
    {{ bootstrap_css|safe }}
    {{ foundation_css|safe }}
    {{ bulma_css|safe }}
    <!-- Add more frameworks as needed -->
</head>
<body>
    <!-- Add your page content here -->
    {% block content %}
    {% endblock %}

    <!-- Add your framework's JS here (optional) -->
    {{ bootstrap_js|safe }}
    {{ foundation_js|safe }}
    <!-- Add more frameworks' JS as needed -->
</body>
</html>
```

#### c. **Inject Variables into Templates (app.py)**

In your `app.py` (the main Flask file), you can define the framework variables and pass them into the templates like this:

```python
from flask import Flask, render_template
from pipc_flask_app.framework import bootstrap_css, bootstrap_js, foundation_css, foundation_js, bulma_css 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('your_page.html', 
                           bootstrap_css=bootstrap_css, 
                           bootstrap_js=bootstrap_js,
                           foundation_css=foundation_css,
                           foundation_js=foundation_js,
                           bulma_css=bulma_css)

if __name__ == '__main__':
    app.run(debug=True)
```

#### d. **Create Content Page (your_page.html)**

In your `your_page.html` (or other template files), inherit from the `layout.html` like this:

```html
{% extends "layout.html" %}

{% block content %}
<div class="container">
    <h1>Welcome to My Flask App</h1>
    <p>This page is styled using Bootstrap and other frameworks.</p>
</div>
{% endblock %}
```

### 3. **Run the Flask App**
After setting everything up, run your Flask app using:

```bash
flask run
```

This will start the development server, and you should see your app styled with the frameworks' CSS.

This setup allows you to easily switch between frameworks or add more as needed. Just pass additional CDN links in `app.py` and include them in the templates!