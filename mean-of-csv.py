import csv
from statistics import mean
from collections import OrderedDict

def calculate_averages(input_file_name,output_file_name):
    a=OrderedDict()
    with open(input_file_name) as fin:
        lines= csv.reader(fin,delimiter=',')
        for row in lines:
            b=[]
            name=row[0]
            for i in range(1, len(row)):
                b.append(float(row[i]))
            miangin=mean(b)
            a[name]=miangin
            
    with open(output_file_name,'w') as out:
        count = 0
        for one in a:
            count += 1
            if count == 1:
                out.write(one + "," + str(a[one]))
            else:
                out.write("\n" + one + ","+ str(a[one]))
            




def calculate_sorted_averages(input_file_name,output_file_name):
    a=OrderedDict()
    with open(input_file_name) as fin:
        lines= csv.reader(fin,delimiter=',')
        for row in lines:
            
            b=[]
            name=row[0]
            for i in range(1, len(row)):
                b.append(float(row[i]))
            miangin=mean(b)
            a[name]=miangin
    asort=sorted(a.items() , key=lambda x:(x[1], x[0]))
    with open(output_file_name,'w') as out:
        count = 0
        for one in asort:
            count += 1
            if count == 1:
                out.write(str(one[0]) + "," + str(one[1]))
            else:
                out.write("\n" + str(one[0]) + ","+ str(one[1]))
            





def calculate_three_best(input_file_name,output_file_name):
    a=OrderedDict()
    with open(input_file_name) as fin:
        lines= csv.reader(fin,delimiter=',')
        for row in lines:
            b=[]
            name=row[0]
            for i in range(1, len(row)):
                b.append(float(row[i]))
            miangin=mean(b)
            a[name]=miangin
    asort=sorted(a.items() , key=lambda x:(-x[1], x[0]))
    with open(output_file_name,'w') as out:
        best=[]
        for i in range (3):
            bestmean=asort.pop(False)
            best.append(bestmean)

        out.write(best[0][0] + "," + str(best[0][1]) + "\n")
        out.write(best[1][0] + "," + str(best[1][1]) + "\n")
        out.write(best[2][0] + "," + str(best[2][1]))



def calculate_three_worst(input_file_name,output_file_name):
    a=OrderedDict()
    with open(input_file_name) as fin:
        lines= csv.reader(fin,delimiter=',')
        for row in lines:
            name=row[0]
            b=[]
            for i in range(1, len(row)):
                b.append(float(row[i]))
            miangin=mean(b)
            a[name]=miangin
    asort=sorted(a.items() , key=lambda x:(x[1], x[0]))
    with open(output_file_name,'w') as out:
        worst=[]
        for i in range (3):
            worstmean=asort.pop(False)
            worst.append(worstmean)
        out.write(str(worst[0][1]) + "\n")
        out.write(str(worst[1][1]) + "\n")
        out.write(str(worst[2][1]))
    

def calculate_average_of_averages(input_file_name, output_file_name):
    a=OrderedDict()
    with open(input_file_name) as fin:
        lines= csv.reader(fin,delimiter=',')
        for row in lines:
            name=row[0]
            b=[]
            for i in range(1, len(row)):
                b.append(float(row[i]))
            miangin=mean(b)
            a[name]=miangin
    asort=sorted(a.items() , key=lambda x:(x[1], x[0]))    
    SUM = 0
    count = 0
    for a in asort:
        count += 1
        SUM += float(a[1])

    meanmean= SUM/count
    with open (output_file_name,'w') as out:
        out.write(str(meanmean))

 