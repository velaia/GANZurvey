import json
import glob
import pickle
from icecream import ic

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

    images = glob.glob("." + config["IMG_PATH"] + '/A/*.png')

    image_dict = {}
    for num, i in enumerate(range(len(images))):
        image_dict[num] = images[i].split('/')[-1]

    pickle.dump(image_dict, open('image_dict.pkl', 'wb'))

    ic(len(image_dict))
