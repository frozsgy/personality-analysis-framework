data = eval(open("vectors_all", "r").read())

for i in "aceno":
    r = ""
    #resultvector-75-25-7-E
    f = open("resultvector-38-25-7-" + i.upper() + ".csv","w+")

    for key,value in data.items():
        personality = value['personality']
        vectors = value['twitter']
        vj = ','.join(map(str, vectors))
        p = personality[i]
        r += str(int(p)) + "," + vj + "\n"
    
    f.write(r)
    f.close()