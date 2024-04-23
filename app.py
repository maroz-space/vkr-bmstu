from flask import Flask, render_template, request, json
from markupsafe import Markup
from config import config_app
import pandas as pd
import pickle

app = Flask(__name__)
struct = config_app()

@app.route('/')
def main():
    return render_template(
        'index.html',
        struct=Markup(json.dumps(struct))
    )

@app.route('/ajax', methods=['post'])
def ajax():
    res = {}
    if request.method == 'POST':
        data = request.form
        form = False
        input = {}

        # ~~~~~~~~~~~~~~~~~~~~~~~~
        for i in data:
            if i == 'form':
                form = data[i]
                continue
            try:
                input[i] = [float(data[i])]
                if input[i] == '':
                    return json.dumps({'error': i})
            except:
                return json.dumps({'error': i})

        # ~~~~~~~~~~~~~~~~~~~~~~~~
        if form == False: return ''

        # ~~~~~~~~~~~~~~~~~~~~~~~~
        models = struct['form'][int(form)]['model']
        answer = struct['form'][int(form)]['answer']

        # ~~~~~~~~~~~~~~~~~~~~~~~~
        for i in range(len(models)):
            file = open('project/model/' + models[i] + '.pkl', 'rb')
            model = pickle.load(file)
            file.close()

            pr = list(answer.keys())[i]
            res[pr] = model.predict(pd.DataFrame(input))
            while len(res[pr].shape): res[pr] = res[pr][0]
            res[pr] = str(res[pr])

    return json.dumps(res)

#app.run()