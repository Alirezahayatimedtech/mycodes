from random import randint

import secrets

list1=['A','A','A','A','A','A',"A","A","A","A",'A','B','B','B','B','B','B','B',"B","B","B","B"]
class human:
    def __init__(self,name):
        self.name=name
class football(human):
    def __init__(self, name,team):
        self.team=team
        self.name=name
    
    def choose(self):
        me=randint(0,(len(list1)-1))
        self.team=list1[me]
        

        del list1[me]

a=football("حسین",'A')
b=football("مازیار",'A')
c=football("اکبر",'B')
d=football("سهیل",'B')
e=football("نیما",'B')
f=football("فرهاد",'B')
a1=football("محمد",'A')
b1=football("مهدی",'A')
c1=football("خشایار",'B')
d1=football("میلاد",'B')
e1=football("سامان",'B')
f1=football("مصطفی",'B')
a2=football("امین",'A')
b2=football("سعید",'A')
c2=football("پویا",'B')
d2=football("پوریا",'A')
e2=football("رضا",'B')
f2=football("بهزاد",'B')
g=football("محسن",'B')
h=football("بهروز",'B')
l=football("شهروز",'B')
k=football("علی",'B')

a.choose()
b.choose()
c.choose()
d.choose()
e.choose()
f.choose()

a1.choose()
b1.choose()
c1.choose()
d1.choose()
e1.choose()
f1.choose()

a2.choose()
b2.choose()
c2.choose()
d2.choose()
e2.choose()
f2.choose()

g.choose()
h.choose()
l.choose()
k.choose()
dict1={a.name:a.team,a1.name:a1.team,a2.name:a2.team,b.name:b.team,b1.name:b1.team,b2.name:b2.team,c.name:c.team,c1.name:c1.team,c2.name:c2.team,d.name:d.team,d1.name:d1.team,d2.name:d2.team,e.name:e.team,e1.name:e1.team,e2.name:e2.team,f.name:f.team,f1.name:f1.team,f2.name:f2.team,g.name:g.team,h.name:h.team,k.name:k.team,l.name:l.team}
for i in dict1.keys():
    
    print(i,dict1[i])




    
    



#

    
        


