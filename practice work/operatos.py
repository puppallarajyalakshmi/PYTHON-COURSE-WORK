#1.arithmetic operators
a=10
b=20
print("addition(+):",a+b) #addition(+): 30
print("sub(-):",a-b) #sub(-): -10
print("mul(*):",a*b) #mul(*): 200
print("div(/):",a/b) #div(/): 0.5
print("flodiv(//):",a//b) #flodiv(//): 0
print("mod(%):",a%b)#mod(%): 10
print("exp(**):",a**b)#exp(**): 100000000000000000000


#2.comparison operators
c=10
d=40
print("equal to(==):",c==d)#equal to(==): False
print("notequal(!=):",c!=d)#notequal(!=): True
print("greater than(>):",c>d)#greater than(>): False
print("lessthan(<):",c<d)#lessthan(<): True
print("greaterthan or equal to(>=):",c>=d)#greaterthan or equal to(>=): False
print("lessthan or equal to(<=):",c<=d)#lessthan or equal to(<=): True



#3.assisgnment operator
'''var=var(op)(val)
e=e+10
var(op)=val
e+=10'''
e=20
e+=30#add & assign(+=): 50
print("add & assign(+=):",e)
e-=20#subtract & assign(-=): 30
print("subtract & assign(-=):",e)
e*=3#multiply & assign(*=): 90
print("multiply & assign(*=):",e)
e**=2#exponentiate & assign(**=): 8100
print("exponentiate & assign(**=):",e)
e/=9#divide & assign(/=): 900.0
print("divide & assign(/=):",e)
e//=10#floor divide & assign(//=): 90.0
print("floor divide & assign(//=):",e)
e%=10#modulus & assing(%=): 0.0
print("modulus & assing(%=):",e)



#5.membership operator
names=['raji','akhila','shmita','nikitha']
print('in result:','dharani' in names)#in result: False
print('not in result:','gayathri' in names)#not in result: False


#6.identity operator
l=[1,2,3,4]
b=[1,2,3,4]
print("l is b:",l is b)
a=b #assign b to a

print("l is b:",l is b)#l is b: False
print("a is b:",a is b)#l is b: False
print("id(l)",id(l))#id(l) 2391331651392
print("id(b)",id(b))#id(b) 2391331765824
print("id(a)",id(a))#id(a) 2391331765824



#7.bitwise operator
'''
3-011
5-101
---
3&5=001=1'''
print("3&5: ",3&5)#3&5:  1
''''4-100
5-101
---
4|5=101=5'''
print("4|5: ",4|5)#4|5:  5
'''5-101
6-100
---
5^6=011=3'''
print("5^6: ",5^6)#5^6:  3
'''1-001
---
~1=110'''
print("~1: ",~1)#~1:  -2
'''2<<1
2=010
4=100'''
print("2<<1: ",2<<1)#2<<1:  4
'''4>>1
4=100
2=010'''
print("4>>1: ",4>>1)#4>>1:  2





