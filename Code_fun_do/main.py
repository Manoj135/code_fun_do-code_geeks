from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/port")
def port():
    return render_template('portfolio.html')

@app.route("/donation")
def donation():
    return render_template('donation.html')

@app.route("/volunteer")
def volunteer():
    return render_template('volunteer.html')

@app.route("/lost_found")
def lost_found():
    return render_template('lost_found.html')

@app.route("/status")
def status():
    return render_template('status.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/important")
def important():
    return render_template('important.html')
app.run(debug=True)