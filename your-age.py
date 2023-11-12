from datetime import datetime
nowdate=datetime.today().strftime('%Y-%m-%d').split('-')
inputdate=input().split('/')
yy=int(inputdate[0])-int(nowdate[0])
if int(inputdate[1])<=12 and int(inputdate[2]) <= 31 :
    print(abs(yy))
else:
    print('WRONG')





