from flask import Flask, render_template, request, redirect
# import pyodbc

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for handling form submission
@app.route('/login', methods=['POST'])
def submit():
    validation = False
    logged = False
    username = request.form['username']
    password = request.form['password']
    if password == "Sangavi":
        validation = True
    
    ## Connect to the database
    # conn = pyodbc.connect('DRIVER={SQL Server};SERVER=your_server_name;DATABASE=your_database_name;Trusted_Connection=yes;')

    # Create a cursor object
    # cursor = conn.cursor()

    # Execute an SQL statement to insert the username and password into the table
    # cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

    # Commit the changes
    # conn.commit()

    # Close the connection
    # conn.close()
    
    if validation:
        logged = True
        return f"Submitted username: {username} logged in successfully"
    else:
        #return redirect('/')
        return "Incorrect username or password! Please try again"

@app.route('/loggedin')
def loggedin():
    if logged:
        return f"Hi {username}, Welcome to our site"
    else:
        return redirect('/')
