#coding=utf-8
# import re
# test=input('please enter:')
# mail=re.compile(r'[0-9a-zA-Z._]*@\w+.com')
# m=mail.match(test)
# if m:
# 	print("mail_address")
# else:
# 	print("wrong")
#

import re
Email=input('please enter the Email:')
re_mode=re.compile(r'<([a-zA-Z]* [a-zA-Z]*)> [\w.]*@\w+.[a-z]*')
we=re_mode.match(Email)
if we:
    print(we.groups())
else:
    print('failed!')

#<Tom Paris> tom@voyager.org