with open("C:\VSCode\Python File Editor\\nades.txt", 'r') as istr:
    with open('NEWnades.txt', 'w') as ostr:
        for line in istr:
            #line = line.rstrip('\n') + ',   -1'
            line = line.rstrip('\n')
            line = line.replace(',', ',1,-1,0,', 1)
            print(line, file=ostr)
