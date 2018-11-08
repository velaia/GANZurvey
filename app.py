import random, pickle, numpy as np

from flask import Flask, render_template, flash, redirect, url_for, session
from flask_session import Session
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, FieldList
from datetime import date, datetime



POST, GET = 'POST', 'GET'
app = Flask(__name__)
app.config.from_json('config.json')
Session(app)

cat_to_num = {'A': 1, 'B': 2}
images = {0: 'Rhinoceros_Auklet_0003_797535_s-1.png', 1: 'Marsh_Wren_0099_188579_s-1.png',
          2: 'Great_Crested_Flycatcher_0058_29523_s-1.png', 3: 'Sayornis_0114_98976_s-1.png',
          4: 'American_Crow_0117_25090_s-1.png', 5: 'Acadian_Flycatcher_0013_29232_s-1.png',
          6: 'Cedar_Waxwing_0041_179183_s-1.png', 7: 'Black_Billed_Cuckoo_0042_795308_s-1.png',
          8: 'Hooded_Oriole_0075_90788_s-1.png', 9: 'Great_Grey_Shrike_0064_106778_s-1.png',
          10: 'Wilson_Warbler_0080_175770_s-1.png', 11: 'Northern_Flicker_0104_28371_s-1.png',
          12: 'Mockingbird_0098_81117_s-1.png', 13: 'Black_Throated_Sparrow_0044_107270_s-1.png',
          14: 'Horned_Grebe_0055_35104_s-1.png', 15: 'White_Eyed_Vireo_0110_158947_s-1.png',
          16: 'Sayornis_0037_98949_s-1.png', 17: 'Wilson_Warbler_0040_175347_s-1.png',
          18: 'Bank_Swallow_0046_129742_s-1.png', 19: 'Northern_Flicker_0079_28630_s-1.png',
          20: 'Western_Wood_Pewee_0057_795040_s-1.png', 21: 'Groove_Billed_Ani_0004_1528_s-1.png',
          22: 'Brewer_Blackbird_0090_2658_s-1.png', 23: 'Western_Grebe_0105_36542_s-1.png',
          24: 'Sayornis_0039_98420_s-1.png', 25: 'Horned_Grebe_0019_34811_s-1.png',
          26: 'Field_Sparrow_0099_113872_s-1.png', 27: 'Belted_Kingfisher_0032_70573_s-1.png',
          28: 'Scott_Oriole_0023_795835_s-1.png', 29: 'Western_Grebe_0037_36469_s-1.png',
          30: 'Marsh_Wren_0118_188512_s-1.png', 31: 'Black_Footed_Albatross_0076_417_s-1.png',
          32: 'Northern_Waterthrush_0087_177148_s-1.png', 33: 'Cedar_Waxwing_0100_178643_s-1.png',
          34: 'Golden_Winged_Warbler_0051_794805_s-1.png', 35: 'White_Pelican_0025_97604_s-1.png',
          36: 'Black_Footed_Albatross_0056_796078_s-1.png', 37: 'Field_Sparrow_0042_113815_s-1.png',
          38: 'Indigo_Bunting_0054_12213_s-1.png', 39: 'Boat_Tailed_Grackle_0049_33422_s-1.png',
          40: 'Bank_Swallow_0040_129674_s-1.png', 41: 'Golden_Winged_Warbler_0078_794827_s-1.png',
          42: 'Golden_Winged_Warbler_0068_794825_s-1.png', 43: 'Baltimore_Oriole_0018_87782_s-1.png',
          44: 'White_Pelican_0083_95840_s-1.png', 45: 'Mockingbird_0097_79951_s-1.png',
          46: 'Baltimore_Oriole_0021_87089_s-1.png', 47: 'Acadian_Flycatcher_0044_795624_s-1.png',
          48: 'Pacific_Loon_0019_75422_s-1.png', 49: 'White_Eyed_Vireo_0102_159420_s-1.png',
          50: 'Wilson_Warbler_0073_175876_s-1.png', 51: 'Mockingbird_0096_79878_s-1.png',
          52: 'Baltimore_Oriole_0064_89554_s-1.png', 53: 'Mockingbird_0085_81417_s-1.png',
          54: 'Yellow_Billed_Cuckoo_0028_26446_s-1.png', 55: 'Red_Legged_Kittiwake_0020_795439_s-1.png',
          56: 'Rhinoceros_Auklet_0008_797531_s-1.png', 57: 'Brandt_Cormorant_0044_22884_s-1.png',
          58: 'Pacific_Loon_0045_75589_s-1.png', 59: 'Great_Crested_Flycatcher_0073_29330_s-1.png',
          60: 'Horned_Grebe_0071_35078_s-1.png', 61: 'Hooded_Oriole_0044_90082_s-1.png',
          62: 'Yellow_Bellied_Flycatcher_0052_42621_s-1.png', 63: 'Great_Grey_Shrike_0070_106547_s-1.png',
          64: 'Great_Grey_Shrike_0089_797036_s-1.png', 65: 'Purple_Finch_0076_27441_s-1.png',
          66: 'Hooded_Oriole_0055_90850_s-1.png', 67: 'Golden_Winged_Warbler_0049_164509_s-1.png',
          68: 'Marsh_Wren_0103_188483_s-1.png', 69: 'Indigo_Bunting_0003_13049_s-1.png',
          70: 'Bohemian_Waxwing_0102_796692_s-1.png', 71: 'Black_Billed_Cuckoo_0092_795313_s-1.png',
          72: 'White_Eyed_Vireo_0111_158864_s-1.png', 73: 'Brewer_Blackbird_0116_2327_s-1.png',
          74: 'Rhinoceros_Auklet_0038_797544_s-1.png', 75: 'Gray_Crowned_Rosy_Finch_0007_797278_s-1.png',
          76: 'Pacific_Loon_0069_75446_s-1.png', 77: 'Grasshopper_Sparrow_0073_115996_s-1.png',
          78: 'Groove_Billed_Ani_0010_1704_s-1.png', 79: 'Yellow_Billed_Cuckoo_0002_26715_s-1.png',
          80: 'Cedar_Waxwing_0019_178654_s-1.png', 81: 'Great_Grey_Shrike_0039_797015_s-1.png',
          82: 'Hooded_Oriole_0029_90485_s-1.png', 83: 'Brewer_Blackbird_0045_2303_s-1.png',
          84: 'Bank_Swallow_0036_129567_s-1.png', 85: 'Field_Sparrow_0130_113846_s-1.png',
          86: 'White_Breasted_Kingfisher_0101_73261_s-1.png', 87: 'Field_Sparrow_0108_114154_s-1.png',
          88: 'Brandt_Cormorant_0039_22945_s-1.png', 89: 'Western_Gull_0066_54105_s-1.png',
          90: 'Least_Auklet_0039_795081_s-1.png', 91: 'Black_Throated_Sparrow_0019_107192_s-1.png',
          92: 'Great_Grey_Shrike_0044_106851_s-1.png', 93: 'Bohemian_Waxwing_0057_177784_s-1.png',
          94: 'American_Crow_0119_25610_s-1.png', 95: 'Western_Grebe_0061_36181_s-1.png',
          96: 'Brewer_Blackbird_0097_2322_s-1.png', 97: 'Great_Grey_Shrike_0023_106670_s-1.png',
          98: 'Black_Footed_Albatross_0080_796096_s-1.png', 99: 'Acadian_Flycatcher_0056_29086_s-1.png'}


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


@app.route('/thank_you', methods=[GET])
def thank_you():
    return render_template('thank_you.html')


class OneQuestionForm(FlaskForm):
    radios = [(x, RadioField(label='Your choice', choices=[('1', '1'), ('2', '2')]))
              for x in range(app.config['NUM_QUESTIONS'])]
    submit = SubmitField('Submit')
    rands = ''
    questions = FieldList(RadioField('Your choice', choices=[('1', '1'), ('2', '2')]),
                          min_entries=app.config['NUM_QUESTIONS'])
    imgs = ''

    def __init__(self):
        self.rands = random.sample(range(0, app.config['NUM_IMAGES']), app.config['NUM_QUESTIONS'])
        self.imgs = [[rand, np.random.permutation(['A', 'B']), x, images[rand]] for x, rand in enumerate(self.rands, 1)]
        # session['permutations'] = self.imgs
        super(OneQuestionForm, self).__init__()

def save_result(data: list):
    perms = session['permutations']
    persist = {}
    for i in range(len(data)):
        res = 0
        print(f'data[i]: {data[i]}, perms[i][1][0]: {perms[i][1][0]}, file: {perms[i][3]}')
        if((data[i] == '1' and perms[i][1][0] == 'A') or (data[i] == '2' and perms[i][1][0] == 'B')):
            res = 1
        persist[perms[i][3]] = res
    print(persist)
    with  open(f'results/result-{date.today()}-{datetime.now().time()}.pkl'.replace(':', '_'), 'wb') as file:
        pickle.dump(persist, file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
