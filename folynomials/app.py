import os
import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import math

# Configure application
app = Flask(__name__, static_url_path='/static')

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def convert_to_int_or_float(n):
    if is_number(n):
        if n.isdigit():
            n = int(n)
        else:
            n = float(n)
    else:
        n = 0
    
    
    return n

def solve_quadratic(a, b, c):
    
    if a == 0:
        return False
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is negative, zero, or positive
    if discriminant < 0:
        # No real roots
        return "The equation has no real roots"
    elif discriminant == 0:
        # One real root
        x = -b / (2*a)
        return (x,)
    else:
        # Two real roots
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return (x1, x2)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphing')
def graphing():
    return render_template('graphing.html')

@app.route('/factorizing')
def factorizing():
    return render_template('factorizing.html')

@app.route('/completing_the_square')
def completing_the_square():
    return render_template('completing_the_square.html')

@app.route('/quadratic_formula')
def quadratic_formula():
    return render_template('quadratic_formula.html')


@app.route('/calculator', methods=["GET", "POST"])
def calculator():
    
    if request.method != 'POST':
        return render_template('calculator.html')
    
    
    a = str(request.form.get('a')) 
    b = str(request.form.get('b')) 
    c = str(request.form.get('c')) 
    

    if not a:
        a = '0'
    if not b:
        b = '0'
    if not c:
        c = '0'

    if any(not is_number(val) for val in [a, b, c]):
        return apology('Please enter a valid integer or rational number')

    a = convert_to_int_or_float(a)
    b = convert_to_int_or_float(b)
    c = convert_to_int_or_float(c)

    two_a = 2 * a
    discriminant = b**2 - (4 * a * c)
    
    if b < 0:
        neg_b = -b
    else:
        neg_b = b
        
    roots = solve_quadratic(a, b, c)
    
    if not roots:
        return apology("Please enter a non zero number for 'a'")
    
    if isinstance(roots, str):
        nature = roots
        root1 = None
        root2 = None
    else:
        nature = None
        root1, root2 = roots if len(roots) == 2 else (roots[0], None)

    return render_template("calculator.html", display=True, a=a, b=b, c=c, two_a=two_a, discriminant=discriminant, neg_b=neg_b, nature=nature, root1=root1, root2=root2) 


if __name__ == '__main__':
    app.run(debug=True)