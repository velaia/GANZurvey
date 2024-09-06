import pickle
import random
from datetime import date, datetime

import numpy as np
from flask import Flask, render_template, flash, redirect, url_for, session
from flask_session import Session
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, FieldList
from wtforms.validators import Optional

POST, GET = 'POST', 'GET'
app = Flask(__name__)
app.config.from_json('config.json')
Session(app)

cat_to_num = {'A': 1, 'B': 2}
images = pickle.load(open('./image_dict.pkl', 'rb'))
NUM_IMAGES = len(images)

@app.route('/', methods=[GET, POST])
def display_survey():
    form = OneQuestionForm()
    print('here')
    if form.validate_on_submit():
        flash(f'Survey has been submitted.')
        save_result(form.questions.data)
        return redirect(url_for('thank_you'))
    session['permutations'] = form.imgs
    return render_template('display_survey.html', img_path=app.config['IMG_PATH'], form=form, images=images)


@app.route('/gt', methods=[GET, POST])
def display_survey_gt():
    form = OneQuestionForm()
    print('here')
    if form.validate_on_submit():
        flash(f'Survey has been submitted.')
        save_result(form.questions.data)
        return redirect(url_for('thank_you'))
    session['permutations'] = form.imgs
    return render_template('display_survey_gt.html', img_path=app.config['IMG_PATH'], form=form, images=images)


@app.route('/thank_you', methods=[GET])
def thank_you():
    return render_template('thank_you.html')


class OneQuestionForm(FlaskForm):
    radios = [(x, RadioField(label='Your choice', choices=[('1', '1'), ('2', '2')]))
              for x in range(app.config['NUM_QUESTIONS'])]
    submit = SubmitField('Submit')
    rands = ''
    questions = FieldList(RadioField('Your choice', choices=[('1', '1'), ('2', '2')]),
                          min_entries=app.config['NUM_QUESTIONS'], validators=[Optional()])
    imgs = ''

    def __init__(self):
        self.rands = random.sample(range(0, NUM_IMAGES), app.config['NUM_QUESTIONS'])
        self.imgs = [[rand, np.random.permutation(['A', 'B']), x, images[rand]] for x, rand in enumerate(self.rands, 1)]
        # session['permutations'] = self.imgs
        super(OneQuestionForm, self).__init__()


def save_result(data: list, ground_truth: bool = False):
    perms = session['permutations']
    persist = {}
    for i in range(len(data)):
        if data[i] in ('1', '2'):
            res = 0
            print(f'data[i]: {data[i]}, perms[i][1][0]: {perms[i][1][0]}, file: {perms[i][3]}')
            if ((data[i] == '1' and perms[i][1][0] == 'A') or (data[i] == '2' and perms[i][1][0] == 'B')):
                res = 1
            persist[perms[i][3]] = res
    print(persist)
    filename = f'results/result-{date.today()}-{datetime.now().time()}.pkl' if not ground_truth else f'results_gt/result-{date.today()}-{datetime.now().time()}.pkl'
    with  open(filename.replace(':', '_'), 'wb') as file:
        pickle.dump(persist, file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
