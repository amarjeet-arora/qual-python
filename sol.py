
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} {% endblock %}</title>
</head>
<body>
    <h1>Amarjeets Website</h1>
    {% block content %}
     {% endblock %}
</body>
</html>






{% extends "base.html"%}

{% block title %} ABC Page {% endblock %}


{% block content %} <h2>Welcome App</h2>{% endblock %}
