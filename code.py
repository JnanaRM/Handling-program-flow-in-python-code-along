# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data)
 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.

fir = data['innings'][0]['1st innings']['deliveries']
counterv = 0
for rec in fir:
    for key,val in rec.items():
        if val['batsman'] == 'SC Ganguly':
            counterv += 1
print(counterv)

#  Who was man of the match and how many runs did he scored ?
print(data['info']['player_of_match'][0])

runs_bb = 0

for rec in fir:  
    for key,val in rec.items():
        if val['batsman'] == 'BB McCullum':     
            runs_bb = val['runs']['batsman'] + runs_bb
print(runs_bb)

#  Which batsman played in the first inning?
bats = []
for rec in fir:
    for key,val in rec.items():
        bats.append(val['batsman'])
print(list(set(bats)))

# Which batsman had the most no. of sixes in first inning ?
six = {}
sixl = []
for rec in fir:
    for key,val in rec.items():
        if val['runs']['batsman'] == 6:
           # sixl.append(val['batsman'])
           #print(counter(sixl))
            if val['batsman'] in six:
                six[val['batsman']] += 1
            else:       
                six[val['batsman']] = 1
print(six)

# Find the names of all players that got bowled out in the second innings.
sec = data['innings'][1]['2nd innings']['deliveries']
bowled=[]
for rec in sec:
    for key,val in rec.items():
        if 'wicket' in val and val['wicket']['kind'] == 'bowled':
            bowled.append(val['batsman'])
print(bowled)

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
extras_sec = 0
extras_fir = 0
for rec in sec:
    for key,val in rec.items():
        if val.get('extras'):
            extras_sec += 1
for rec in fir:
    for key,val in rec.items():
        if val.get('extras'):
            extras_fir += 1
print(extras_sec)
print(extras_fir)
print(extras_sec - extras_fir)



# Code ends here


