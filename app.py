from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# تخزين مؤقت في الذاكرة بدل قاعدة بيانات
registered_users = []  # كل عنصر هيكون dict فيه name و email

@app.route('/')
def home():
    return render_template('index.html', error=None)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # تحقق لو الاسم أو الإيميل موجودين قبل كده
    for user in registered_users:
        if user['name'] == username or user['email'] == email:
            return render_template('index.html', error="الاسم أو الإيميل ده متسجل بالفعل!")

    # لو جديد، خزّنه وودّيه لجوجل
    registered_users.append({'name': username, 'email': email, 'password': password})
    return redirect("https://google.com")

if __name__ == '__main__':
    app.run(debug=True)
