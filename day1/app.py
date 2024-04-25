from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # 템플릿에 전달할 데이터
    data = {
        "title": "Flask Jinja Template",
        "user": "Inseop",
        "is_admin": True,
        # "items": ["Item 1", "Item 2", "Item 3"], # 얘는 왜 안될까?
        "myitems": ["Item 1", "Item 2", "Item 3"],
    }

    # render_template을 사용하여 템플릿 파일을 렌더링
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
