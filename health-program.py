voroodia=int(input())
sen_A=input()
ghad_A=input()
vazn_A=input()

sena=0
ghada=0
vazna=0




for i in ghad_A.split():
    ghada+=int(i)
for i in sen_A.split():
    sena+=int(i)
for i in vazn_A.split():
    vazna+=int(i)
########
voroodib=int(input())
sen_B=input()
ghad_B=input()
vazn_B=input()

senb=0
ghadb=0
vaznb=0
for i in ghad_B.split():
    ghadb+=int(i)
for i in sen_B.split():
    senb+=int(i)
for i in vazn_B.split():
    vaznb+=int(i)







class kind:

    def __init__(self,tedad,sen,ghad,vazn):
        self.tedad=tedad 
        self.ghad=ghad 
        self.sen=sen
        self.vazn=vazn   

    def mean_sen(self):
        return float(self.sen/self.tedad)     
      
    def mean_ghad(self):
        return float(self.ghad/self.tedad)
  
    def mean_vazn(self):
        return float(self.vazn/self.tedad)
    



aval=kind(voroodia,sena,ghada,vazna)
dovom=kind(voroodib,senb,ghadb,vaznb)

print(aval.mean_sen())
print(aval.mean_ghad())
print(aval.mean_vazn())
print(dovom.mean_sen())
print(dovom.mean_ghad())
print(dovom.mean_vazn())
#print(ghad_bishtar)

if aval.mean_ghad() > dovom.mean_ghad():
    print('A')
if  dovom.mean_ghad()> aval.mean_ghad():
    print("B")
if aval.mean_ghad() == dovom.mean_ghad() and aval.mean_vazn() <dovom.mean_vazn():
    print('A')
if aval.mean_ghad() == dovom.mean_ghad() and aval.mean_vazn() > dovom.mean_vazn():
    print('B')
if aval.mean_ghad() == dovom.mean_ghad() and aval.mean_vazn() == dovom.mean_vazn():  
    print('Same')  
