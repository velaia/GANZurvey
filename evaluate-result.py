import pickle
import glob


sum_correct = 0
sum_overall = 0
for file in glob.glob('results/*.pkl'):
    result = pickle.load(open(file, 'rb'))
    for k, v in result.items():
        sum_overall += 1
        print(k + ": " + str(v))
        if v == 1:
            sum_correct += 1

print("Sum correct: " + str(sum_correct) + " of " + str(sum_overall))