name={1:'raji',2:'akhila',3:'shimtha'}
for i in name.keys():
    print(f'{i}-{name[i].capitalize()}')
"""1-Raji
2-Akhila
3-Shimtha"""



a={1:1,2:2,3:3,4:4}
for i in a.keys():
    print(f'{i}-{a[i]**2}')
"""1-1
2-4
3-9
4-16"""



for i in range(1,21):
    print(f'17*{i}={17*i}')
"""17*1=17
17*2=34
17*3=51
17*4=68
17*5=85
17*6=102
17*7=119
17*8=136
17*9=153
17*10=170
17*11=187
17*12=204
17*13=221
17*14=238
17*15=255
17*16=272
17*17=289
17*18=306
17*19=323
17*20=340"""




email,pwd='abc@gmail.com','abc@123'
max_attempt=5
cur_attempt=1
while cur_attempt<=max_attempt:
    e=input("enter the email:")
    p=input("enter the pwd:")
    if e==email and p==pwd:
        print("login successful")
        break
    else:
        print("invalid email or pwd.try again")
else:
    print("maximum attempts are done.please try again after 5 mins")


"""enter the email:fghj
enter the pwd:jhgf
invalid email or pwd.try again
enter the email:sdfg
enter the pwd:kj
invalid email or pwd.try again
enter the email:tgh
enter the pwd:jh
invalid email or pwd.try again
enter the email:abc@gmail.com
enter the pwd:abc@123
login successful"""






































