'''
北京市 010
上海市 021
天津市 022
重庆市 023
香港 852
澳门 853
'''
with open('cmbc_raw','r') as file:
    for line in file.readlines():
        mylist = line.strip().split()
        if len(mylist) == 1:
            prov = mylist[0]
        else:
            print(mylist[1][1:]+','+prov+'-'+mylist[0])