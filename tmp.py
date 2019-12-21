import pandas as pd
import numpy as np

train_data = pd.read_csv('data/train.csv', index_col=False)
tmp_list = []
for i in train_data['CTR_CATEGO_X']:
    if i not in tmp_list:
        print(i)
        tmp_list.append(i)

print(tmp_list)

dc = {}

for name in tmp_list:
    dc[name] = []

for i in train_data['CTR_CATEGO_X']:
    for j in dc:
        if i == j:
            dc[j].append(1)
        else:
            dc[j].append(0)

new_list = []
for i in dc:
    new_list.append(dc[i])

for i in range(len(tmp_list)):
    tmp_list[i] = 'CTR_CATEGO_X' + tmp_list[i]
    print(tmp_list[i])

#print(new_list)

df = pd.DataFrame(np.array(new_list).T.tolist(), columns=tmp_list)

num = train_data.columns.get_loc("CTR_CATEGO_X")
train_data = train_data.drop('CTR_CATEGO_X', axis=1)

for i in df:
    train_data.insert(num, i, df[i].values)