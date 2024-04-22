from flask import Flask, render_template, request, json
from markupsafe import Markup
from config import config_app

app = Flask(__name__)

@app.route('/')
def main():
    return render_template(
        'index.html',
        struct=Markup(json.dumps(config_app()))
    )

@app.route('/ajax', methods=['post'])
def ajax():
    if request.method == 'POST':
        data = request.form
        print(data)

        # try:
        #     z = float(z)
        # except:

    return json.dumps({
        'Модуль упругости при растяжении, ГПа': '1234',
        'Прочность при растяжении, МПа': '4321'
    })

# app.run()