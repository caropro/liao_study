#coding=utf-8
import os,time,pprint

def get_information(directory):
    total=[]
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        file_list.append([i,time.ctime(a.st_atime),time.ctime(a.st_ctime)]) #[file,most_recent_access,created]
        total.append(file_list)
    return total

pprint.pprint (sorted(get_information("/"),key=lambda x:x[1]))
listtotal=sorted(get_information("/"),key=lambda x:x[1])[0]
names=[x[0] for x in listtotal]
for n in names:
    path=os.path.join('/',n)
    print(path)



