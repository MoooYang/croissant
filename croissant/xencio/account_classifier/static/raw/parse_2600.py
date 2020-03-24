with open('gb2600', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split()
        if line[0][2:]=='0000':
            province = line[1]
        elif line[0][4:]=='00':
            print(line[0][:4]+','+province+'-'+line[1])
