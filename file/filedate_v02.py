#coding=utf-8
import os,time,pprint
import csv

def get_information(directory):
    total = [x[0] for x in os.walk(directory)]
    file_list = None
    final=[]
    a=0
    for i in total:

        file_list=[]
        path = i
        name=[x.strip('') for x in i.split("/")][-1]

        ctime=os.stat(path)
        shortpath=path.replace(directory,'')
        if i.endswith('/'):
            name = 'test_a'
            shortpath='/'
        # print(i)
        # print(name)
        # print(shortpath)
        file_list.append([name,i,shortpath,time.ctime(ctime.st_ctime)]) #[file,most_recent_access,created]
        a+=1
        final.append(file_list)
    return final
a_path='/Users/jianxuan/Desktop/test_a/'
b_path='/Users/jianxuan/Desktop/test_b/'
ta=(get_information(a_path))
tb=(get_information(b_path))


# print(tb)
# print(len(tb))
# print(ta)
# print(len(ta))
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
try:
    dpa=os.path.join('/Users/jianxuan/Desktop/dict_a_v02.csv')
    dpb=os.path.join('/Users/jianxuan/Desktop/dict_b_v02.csv')
    dpc=os.path.join('/Users/jianxuan/Desktop/dict_c_v02.csv')
    os.remove(dpa)
    os.remove(dpb)
    os.remove(dpc)
except:
    pass

with open('/Users/jianxuan/Desktop/dict_a_v02.csv', 'w') as csvfile:
    fieldnames = ['file_name', 'path','shortpath','create_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in ta:
        print(i)
        for k,p,sp,t in i:
            writer.writerow({'file_name': k, 'path': p,'shortpath':sp,"create_time":t})

with open('/Users/jianxuan/Desktop/dict_a_v02.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict_a={rows[2]:rows[3] for rows in reader}
        # mydict_a = {rows[0]:{"path":rows[1],"time":rows[2]} for rows in reader}
#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
with open('/Users/jianxuan/Desktop/dict_b_v02.csv', 'w') as csvfile:
    fieldnames = ['file_name', 'path','shortpath','create_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in tb:
        for k,p,sp,t in i:
            writer.writerow({'file_name': k, 'path': p,'shortpath':sp,"create_time":t})

with open('/Users/jianxuan/Desktop/dict_b_v02.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict_b = {rows[2]:rows[3] for rows in reader}

# print(mydict_b)
# print(mydict_a)
# print((mydict_a))
# print(len(mydict_b))
tc=[]
# print(mydict_b)
for i in mydict_b.keys():
    # print(i)
    tc_e=[]
    if i =='shortpath':
        pass
    else:
        try:
            if mydict_a[i]:
                # print("y")
                if mydict_a[i]>mydict_b[i]:
                    # print("yyyyyyyyyyy",mydict_b[i],mydict_a[i])
                    tc_e.append(i)
                    full_path=a_path+i
                    # print(full_path)
                    tc_e.append(full_path)
                    tc_e.append(mydict_a[i])
                    mydict_a.pop(i)
                    # print(tc_e)
                else:
                    tc_e.append(i)
                    full_path=b_path+i
                    tc_e.append(full_path)
                    tc_e.append(mydict_b[i])
                    mydict_a.pop(i)
                    # print(tc_e)
                # tc.append(tc_e)
        except:
            # print("noooooooo")
            tc_e.append(i)
            full_path = b_path + i
            tc_e.append(full_path)
            tc_e.append(mydict_b[i])
            # print(tc_e)
        tc.append(tc_e)
tc_e=[]
for k,v in mydict_a.items():
    # print(k)
    if k=='shortpath':
        pass
    else:
        tc_e = []
        tc_e.append(k)
        full_path = a_path + k
        tc_e.append(full_path)
        tc_e.append(v)
        tc.append(tc_e)
    # print(tc_e)

# pprint.pprint(tc)
# print(len(tc))
print(tc)
print(len(tc))

######cccccccccccccccccccc
with open('/Users/jianxuan/Desktop/dict_c_v02.csv', 'w') as csvfile:
    fieldnames = ['shortPath', 'path','create_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in tc:
        k,p,t=i
        writer.writerow({'shortPath': k, 'path': p,"create_time":t})