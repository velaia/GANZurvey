import pickle
import glob
from icecream import ic


sum_correct, sum_overall = 0, 0

for file in glob.glob('results/*.pkl'):
    result = pickle.load(open(file, 'rb'))
    for k, v in result.items():
        sum_overall += 1
        print(k + ": " + str(v))
        if v == 1:
            sum_correct += 1

ic(sum_correct)
ic(sum_overall)