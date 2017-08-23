#coding=utf-8
import os
import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

#coding=utf-8
import os,time,pprint
import json
import xml
import dicttoxml
import pprint
#
# def get_information(directory):
# 	total=[x[0] for x in os.walk(directory)]
# 	return total
#
# a_path='/Users/jianxuan/Desktop/test_a/'
# b_path='/Users/jianxuan/Desktop/test_b/'
# lis=get_information(a_path)
# pprint.pprint(lis)

# a=[1,2,3,5,6,7,8,9]
# b=[[1,2],42,5,6,8,10]
# for i in a:
# 	if i in b:
# 		print(i,b.index(i))
# with open('/Users/jianxuan/Desktop/dict_v02.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('coors_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         mydict = {rows[0]:{"path":rows[1],"time":rows[2]} for rows in reader}
#
# print(mydict)

# a={'a':1,'b':2,'c':3,'d':4}
# b={'c':1,'d':2,'f':5,'e':4}
# c={}
#
#
# for i in b.keys():
# 	try:
# 		if a[i]:
# 			if a[i]>b[i]:
# 				b[i]=a[i]
# 				a.pop(i)
# 			else:
# 				a.pop(i)
#
# 	except:
# 		continue
#
# b.update(a)
# print(b)