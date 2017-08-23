#coding=utf-8
import os,time,pprint
import json
import xml
import dicttoxml

def get_information(directory):
    total=[]
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        # print(a)
        file_list.append([i,time.ctime(a.st_ctime)]) #[file,most_recent_access,created]
        total.append(file_list)
    return total
a_path='/Users/jianxuan/Desktop/test_a/'
b_path='/Users/jianxuan/Desktop/test_b/'
# pprint.pprint (sorted(get_information(a_path),key=lambda x:x[1]))
org_a=(sorted(get_information(a_path),key=lambda x:x[1]))[0]
norg_a=[]
for i in org_a:
    path=os.path.join(a_path, i[0])
    i.insert(1,path)
    norg_a.append(i)
    print(i)

print(norg_a)
listtotal_a=sorted(get_information(a_path),key=lambda x:x[1])[0]
name_a=[x[0] for x in listtotal_a]

pprint.pprint (sorted(get_information(b_path),key=lambda x:x[1]))
listtotal_b=sorted(get_information(b_path),key=lambda x:x[1])[0]
name_b=[x[0] for x in listtotal_b]
na={}
nb={}

for n in name_a:
    path=os.path.join(a_path,n)
    na[n]=path
for n in name_b:
    path=os.path.join(b_path,n)
    nb[n]=path

with open('/Users/jianxuan/Desktop/test_list.json',"w") as f:
    json.dump(na,f,indent=4)

import csv
# with open('/Users/jianxuan/Desktop/dict.csv', 'w',newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     for key, value in na.items():
#        writer.writerow([key] value])
#
# import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# with open('/Users/jianxuan/Desktop/dict_v02.csv', 'w') as csvfile:
#     fieldnames = ['file_name', 'path','create_time']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for k,p,t in norg_a:
#         writer.writerow({'file_name': k, 'path': p,"create_time":t})