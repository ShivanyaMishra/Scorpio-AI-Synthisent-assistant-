from flask import Flask, render_template

app = Flask(__name__, template_folder="SCORPIO_FRONTEND/templates", static_folder="SCORPIO_FRONTEND/static")  # Explicitly set template folder


@app.route('/')
def home():
    return render_template("index.html")        

@app.route('/features')
def features():
    return render_template("features.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)