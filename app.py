from flask import Flask, render_template


# Create a Flask application instance
app=Flask(__name__)

#Home route
@app.route('/')
def home():
    return render_template('index.html', title='Home Page')


if __name__ == '__main__':
    app.run(debug=True)