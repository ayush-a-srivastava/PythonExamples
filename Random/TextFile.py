with open('text.txt','r') as file:
    data = file.read().replace("\n"," ")
    print(data)
