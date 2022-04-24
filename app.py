import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# import psycopg2

UPLOAD_FOLDER = '/home/max/Загрузки'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# conn = psycopg2.connect(database="postgres", user="postgres", password='postgres', host="localhost", port="5432")
#
# cursor = conn.cursor()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form.get("YoutubeGet"):
            youtube = request.form.get("youtube")
            return render_template('error.html', src=f'{youtube}')
        elif request.form.get("FileGet"):
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('error.html', src=f'{file}')

            # cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s",
            # (str(username.title()), str(password)))
            # records = list(cursor.fetchall())
            # elif len(records) != 0:
            #    return render_template('account.html', full_name=records[0][1], login=records[0][2],
            #    password=records[0][3])
            # elif len(records) == 0:
            #    print(records)
            #    return render_template('error.html', text='You are not in data base, but you can create a new account')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
