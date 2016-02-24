import json
import csv

# I convert the csv file to the json file
op = open('price_list.csv', 'r')
reader = csv.reader(op)
js = open("jfile.json", 'w')
w_json = json.dumps([row for row in reader])
js.write(w_json)
print(w_json)
op.close()
js.close()

# Need to do my logic
js = open("jfile.json", 'r')
j_reader = json.loads(w_json)
# for i in j_reader:
#     sh = int(i[1])
#     pr = int(i[2])
#     if sh >= 1:
#         print('Shtuki')
#     elif pr >= 1:
#         print('Pary')
#     else:
#         pass
js.seek(0)
count_sh = sum(1 for i in j_reader if int(i[1]) >= 1)
count_pr = sum(1 for i in j_reader if int(i[2]) >= 1)
print(count_sh)
print(count_pr)
js.close()
# I am writing the results into the separate json file
js = open('jresults.json', 'w')
j_res = "Shtuki: " + str(count_sh) + "    " + "Pary: " + str(count_pr)
j_write = json.dumps(j_res)
js.write(j_write)
js.close()
# Checking what I wrote
jsr = open('jresults.json', 'r')
j_r = json.loads(j_write)
print("Good Job ", j_r)
# in the json dict the third corresponds to the shtuki for 5th
# and the 4th corresponds to the shtuki for the 6th
# the first corr to the par for the 5th
# the second corresp to the par for the 6th
