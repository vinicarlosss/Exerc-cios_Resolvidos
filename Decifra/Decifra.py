seq = list(map(str,input().split()))
frase = list(map(str,input().split()))
for e in range(len(frase)):
    if frase[e] == "a":
        frase[e] = seq[0]
    elif frase[e] == "b":
        frase[e] = seq[1]
    elif frase[e] == "c":
        frase[e] = seq[2]
    elif frase[e] == "d":
        frase[e] = seq[3]
    elif frase[e] == "e":
        frase[e] = seq[4]
    elif frase[e] == "f":
        frase[e] = seq[5]
    elif frase[e] == "g":
        frase[e] = seq[6]
    elif frase[e] == "h":
        frase[e] = seq[7]
    elif frase[e] == "i":
        frase[e] = seq[8]
    elif frase[e] == "j":
        frase[e] = seq[9]
    elif frase[e] == "k":
        frase[e] = seq[10]
    elif frase[e] == "l":
        frase[e] = seq[11]
    elif frase[e] == "m":
        frase[e] = seq[12]
    elif frase[e] == "n":
        frase[e] = seq[13]
    elif frase[e] == "o":
        frase[e] = seq[14]
    elif frase[e] == "p":
        frase[e] = seq[15]
    elif frase[e] == "q":
        frase[e] = seq[16]
    elif frase[e] == "r":
        frase[e] = seq[17]
    elif frase[e] == "s":
        frase[e] = seq[18]
    elif frase[e] == "t":
        frase[e] = seq[19]
    elif frase[e] == "u":
        frase[e] = seq[20]
    elif frase[e] == "v":
        frase[e] = seq[21]
    elif frase[e] == "w":
        frase[e] = seq[22]

    elif frase[e] == "x":
        frase[e] = seq[23]
    elif frase[e] == "y":
        frase[e] = seq[24]
    else:
        frase[e] = seq[25]
print("".join(frase))