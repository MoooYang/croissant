with open('icbc_raw', 'r') as file:
    for line in file.readlines():
        line = line.strip().split()
        with open('icbc_parsed.txt', 'a') as file:
            if line:
                try:
                    file.write(",".join((line[2], line[0] + '-' + line[1] + '\n')))
                except:
                    print(line)
