import numpy as np
import time
import math
table={'2020':'Black','2010':'Black','2000':'Black','2100':'Black','2200':'Blue'
        ,'1120':'Orange','1220':'Orange','1210':'Orange','2120':'Orange','2121':'Orange','2220':'Orange'
        ,'2221':'Orange','2210':'Orange','2211':'Orange'
        ,'1021': 'Pink','1011':'Pink','1001':'Pink','1111':'Pink','1101':'Pink','1201':'Pink','2022':'Pink','2012':'Pink','2002':'Pink'
        ,'0000':'Purple','0001':'Purple','0002':'Purple','0100':'Purple','0101':'Purple','0102':'Purple','1002':'Purple','1102':'Purple','2102':'Purple','1020':'Red'
        , '1010': 'Red','1000':'Red','1110':'Red','1100':'Red','1200':'Red','2011':'Red','2001':'Red','2110':'Red','2111':'Red'
        , '2101': 'Red','2201':'Red','2021':'Red'
        , '0020': 'White','0021': 'White','0022': 'White','0011': 'White','0012': 'White','0110': 'White','0111': 'White','0112': 'White','0200': 'White','0201': 'White'
        , '0202': 'White','1022': 'White','1012': 'White','1112': 'White','1202': 'White','2112': 'White','2202': 'White','0010': 'White'
        , '0120': 'Yellow', '0121': 'Yellow', '0122': 'Yellow', '0221': 'Yellow', '0222': 'Yellow', '0210': 'Yellow', '0211': 'Yellow', '0212': 'Yellow', '1121': 'Yellow'
        , '1122': 'Yellow', '1221': 'Yellow', '1222': 'Yellow', '1211': 'Yellow', '1212': 'Yellow', '2122': 'Yellow', '2222': 'Yellow', '2212': 'Yellow', '0220': 'Yellow'}
def main():

 pl=list(table.keys())[list(table.values()).index('Pink')]
 pl=[k for k,v in table.items() if v=='Pink']
 result=hybrid('0100','0120')

 resultall1=bubble_sort(result)
 printlist(resultall1)

 input = [['2021', '0010', '0220'], [],[], [], [],[]]

 for i in range(len(input[0])):

     input[1].append(table[input[0][i]])
     input[2].append('')
     input[3].append( 1)
     input[4].append( 1)
     input[5].append( 1)


 blue=[[],[],[],[],[],[],[]]

 start = time.clock()
 target=['2200']
# target = ['0100']
 blueres=hybirdallnew2(input,6,blue,target,2,1,1.5,2)

 end = time.clock()
 print (end - start)
 blueres=sortbyrow(blueres,6)
 printflowerlist(blueres)

#



 #print(name)
hashset=set()
def hybirdallnew2(input,level,bluelist,target,MaxSelf,Para1,Para2,Para3):
    if(level==0 ):
        return
    level=level-1
    currall=[[],[],[],[],[],[],[],[]]
    for i in range(len(input[1])):
        for j in range(len(input[1])):
            #if input[0][i]=='1110' and input[0][j]=='1110':
               # print('hjhgj')
          if (input[0][i]+input[0][j])not in hashset and(input[0][j]+input[0][i])not in hashset:
            hashset.add(input[0][i]+input[0][j])
            hashset.add(input[0][j] + input[0][i])
            curr=hybrid(input[0][i],input[0][j])
            currall1=bubble_sort(curr)
            for k in range(len(currall1[0])):
                #if currall1[1][k]=='Blue':
                   # print('dfsf')

                currall[0].append(currall1[0][k])#number
                currall[1].append(currall1[1][k])#color
                currall[2].append(currall1[2][k])#得到概率
                currall[3].append(currall1[3][k])#本颜色概率
                if input[0][i] == input[0][j]:
                    currall[4].append('Level**' + str(6 - 1 - level) + currall1[1][k] + currall1[0][k] + 'selfprob1/' + str( currall1[3][k]) + 'from' + input[1][i] + input[0][i] + '+' + input[1][j] + input[0][ j] + 'tatalprob1/' + str(currall1[2][k]) + '||||(' + input[2][i] + ')||||')
                    currall[5].append(currall1[2][k] * input[3][i] )
                    currall[6].append(currall1[3][k] * input[5][i] )
                else:
                    currall[4].append('Level**'+str(6-1-level)+currall1[1][k]+currall1[0][k]+'selfColorP=1/'+str(currall1[3][k])+'from'+input[1][i]+input[0][i]+'+'+input[1][j]+input[0][j]+'CurP=1/'+str(currall1[2][k])+'||||('+input[2][i]+input[2][j]+')||||')
                    currall[5].append(currall1[2][k]*input[3][i] * input[3][j])
                    currall[6].append(currall1[3][k] * input[5][i] * input[5][j])


    for i in range(len(currall[0])):
        if ((currall[0][i] not in input[0]) and currall[3][i]<MaxSelf)and table[currall[0][i]]!='Blue' :
            input[0].append(currall[0][i])#number
            input[1].append(currall[1][i])#color
            input[2].append(currall[4][i])#path
            input[3].append(currall[5][i])#totalP
            input[4].append(currall[2][i])#curP
            input[5].append(currall[6][i])#totalselfcolorP
        if (currall[0][i] in input[0])and(currall[3][i] < MaxSelf) and table[currall[0][i]] != 'Blue':
           for ll in range(len(input[0])):
                if input[0][ll] == currall[0][i]:

                    idx = ll
                    if input[3][ll] >= currall[5][i] and input[5][ll] >= (currall[6][i]):
                        input[0][ll]=(currall[0][i])
                        input[1][ll]=(table[currall[0][i]])
                        input[2][ll]=(currall[4][i])
                        input[3][ll]=(currall[5][i])
                        input[4][ll] = (currall[2][i])
                        input[5][ll] = (currall[6][i])
        if  (currall[0][i]in target and currall[4][i]not in bluelist[2]):
            bluelist[0].append(currall[0][i])
            bluelist[1].append(table[currall[0][i]])
            bluelist[2].append(currall[4][i])
            bluelist[3].append(currall[5][i])
            bluelist[4].append(currall[2][i])
            bluelist[5].append(currall[6][i])
            bluelist[6].append(((math.log(currall[5][i]/currall[2][i]))**Para1)*(currall[2][i]**Para2)*(currall[6][i]**Para3))
    hybirdallnew2(input,level,bluelist,target,MaxSelf,Para1,Para2,Para3)
    return bluelist

def printlist(result):
    for all in range(len(result[0])):
        print(result[0][all], result[1][all], '1/', result[2][all],'1/', result[3][all])
def sortbyrow(list2,num):
    list1=list2
    list=list1[num]
    length = len(list)
    # 第一级遍历
    for index in range(length):
        # 第二级遍历
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                # 交换两者数据，这里没用temp是因为python 特性元组。
                for k in range(len(list1)):
                 list1[k][j - 1], list1[k][j] = list1[k][j], list1[k][j - 1]

    return list1
def printflowerlist(list):
    for i in range(len(list[0])):
        print('score'+str(int(list[6][i]))+'totalP',list[3][i]/16384,'currentP',list[4][i],'selfcolor',list[5][i],'Blue',list[2][i])
    return
def bubble_sort(list2):
    list1=list2
    list=list1[1]
    length = len(list)
    # 第一级遍历
    for index in range(length):
        # 第二级遍历
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                # 交换两者数据，这里没用temp是因为python 特性元组。
                list1[0][j - 1], list1[0][j] = list1[0][j], list1[0][j - 1]
                list1[1][j - 1], list1[1][j] = list1[1][j], list1[1][j - 1]
                list1[2][j - 1], list1[2][j] = list1[2][j], list1[2][j - 1]
                list1[3][j - 1], list1[3][j] = list1[3][j], list1[3][j - 1]
    i=0
    k=0
    while i < len(list1[1]):
       if k < len(list1[1])-1:
        if((list1[1][i]==list1[1][k+1])and k < len(list1[1])-1):

                k=k+1
        else:
            sum=0
            for m in range(i,k+1):
                sum=sum+1/list1[2][m]
            for n in range(i,k+1):
                list1[3][n]=sum/(1/list1[2][n])
            i=k+1
            k=i
       else:
           sum = 0
           for m in range(i, k + 1):
               sum = sum + 1 / list1[2][m]
           for n in range(i, k + 1):
               list1[3][n] = sum / (1 / list1[2][n])
           i = k + 1
           k = i



    return list1
def bubble_sort_flag(list):
    length = len(list)
    for index in range(length):
        # 标志位
        flag = True
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
            # 没有发生交换，直接返回list
            return list
    return list
def hybrid(a1,b1):
    a=[]
    for c in a1:
        a.append(c)
    b = []
    for c in b1:
        b.append(c)


    aa = hybridsingle(a[0],b[0])
    bb = hybridsingle(a[1], b[1])
    cc = hybridsingle(a[2], b[2])
    dd = hybridsingle(a[3], b[3])
    m=0
    result=[]
    result2=[]
    for i in aa[0]:
        for j in bb[0]:
            for k in cc[0]:
                for l in dd[0]:

                   result.append(i+j+k+l)
                   m=m+1
    m=0
    for i in aa[1]:
        for j in bb[1]:
            for k in cc[1]:
                for l in dd[1]:

                   result2.append(i*j*k*l)
                   m=m+1
    result = [result, result2]
    resultall=[[],[],[],[]]
    for all in range(len(result[0])):
         resultall[0].append(result[0][all])
         resultall[1].append(table[result[0][all]])
         resultall[2].append(result[1][all])
         resultall[3].append(1/result[1][all])
    return  resultall
def hybridsingle(a,b):
    if (a=='1' and b=='2') or (a=='2' and b=='1')or (a=='0' and b=='1')or(a=='1' and b=='0'):
        return [[a,b],[2,2]]
    if (a=='2' and b=='2') or (a=='0' and b=='0'):
        return [[a],[1]]
    if ((a=='2' and b=='0')or(a=='0' and b=='2') ):
        return [['1'],[1]]
    if (a=='1' and b=='1') :
        return [['0','1','2'],[4,2,4]]

main()
