"""
- 과제 안내
    
    이 웹 애플리케이션은 사전 정의된 사용자 목록을 웹 페이지에 표시해야 합니다.
    
    **요구 사항**
    
    - **Flask 애플리케이션 설정**: Flask 애플리케이션 (**`app.py`**)을 설정하고, 루트 URL (**`'/'`**)에 접속했을 때 사용자 목록을 보여주는 뷰 함수를 만드세요.
    - **Jinja 템플릿 작성**: **`templates`** 폴더 안에 **`index.html`** 파일을 만들고, Jinja 템플릿을 사용하여 사용자 목록을 HTML로 렌더링하세요.
    - **웹 페이지 디자인**: **`index.html`**에서 각 사용자의 이름(**`name`**)과 사용자 이름(**`username`**)을 목록 형태로 표시하세요.
    - **애플리케이션 실행 및 테스트**: Flask 애플리케이션을 실행하고, 브라우저에서 **`http://localhost:5000/`** 주소로 접속하여 결과를 확인하세요.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    Jinja Template renderer
    """
    users = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"},
    ]
    return render_template("index.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
