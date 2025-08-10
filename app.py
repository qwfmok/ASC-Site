from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/sns')
def sns():
    return render_template('sns.html')

# 게시판
posts = []  # 임시 데이터

@app.route("/board", methods=["GET", "POST"])
def board():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        posts.append({"title": title, "content": content})
        return redirect("/board")
    return render_template("board.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)