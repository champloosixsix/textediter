# PROGRAM TO: Find and Replace X with Y

open("tobedited.txt", mode='r')

#create variable and store text you want to find
search_text = "X"

#create variable and store text you want to replace with

replace_text = "Y"

#open text file in read only mode using open() function
with open("tobedited.txt", mode='r') as file:

    #reading the content of the file using the read()
    #function and storing them in a new var
    data = file.read()

    #searching and replacing
    data = data.replace(search_text, replace_text)

#open our text file in write only to write replaced

with open("edited.txt", mode='w') as file:

    #writing the replaced data
    file.write(data)

print("Text Replaced")

# PROGRAM TO: Find X in each line and append Y after the found X

with open("tobedited", 'r') as istr:
    with open('edited.txt', 'w') as ostr:
        for line in istr:
            #>>>append each line with A
            #line = line.rstrip('\n') + 'A'
            #>>>find first instance of A in each line and replace with B
            #line = line.rstrip('\n')
            #line = line.replace('A', 'B', 1)
            print(line, file=ostr)
