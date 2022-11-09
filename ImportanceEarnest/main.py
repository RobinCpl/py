import re
file = open(".\\importance_earnest_act_1.txt")
lines = file.readlines()
max_sentence_length = 0
sentence_length = 0
for line in lines:
    line = re.sub("\[*\]", "", line)
    sentence_length = len(line)
    print(line)