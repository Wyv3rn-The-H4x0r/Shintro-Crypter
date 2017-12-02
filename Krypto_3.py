import Zeichen
import random

c = Zeichen.coder()


def generate_int(x,zip=False):
    m = c.generate_int(x,zip)
    return m

def lengh_finder(x):
    count = 0
    for y in x:
        count += 1
    return count

def creat_random_pattern(lengh,max,min):
    #print("creat random",min,max)
    g = []
    for x in range(0,lengh):
        g += [random.randint(min,max)]
    return g

def encode(massage,max = 233,min = 0,zip = False):
    mass_org = generate_int(massage,zip)
    random_pat = creat_random_pattern(len(mass_org),max,min)

    count = 0

    encode = ""
    key = ""
    for x in mass_org:
        encode += c.int_str(random_pat[count],zip)

        g = x - random_pat[count]
        if g < min:
            if g > 0:
                g = max - (g)
            else:
                g = max -(g*-1)
        key += c.int_str(g,zip)
        count += 1
    #print("encode", min, max, zip, massage,key,encode)

    return encode,key

def decode(key,massage,max = 233,min = 0,zip = False,check = True):

    if len(key) != len(massage):
        if check == True:
            print("ERROR key",lengh_finder(key),"massage",lengh_finder(massage));return
        else:
            KeyError

    massage = generate_int(massage,zip)
    key = generate_int(key,zip)

    decode = ""

    count = 0

    for x in massage:
        g = key[count] + x
        if g >= max:
            g = min + (g - max)
        decode += c.int_str(g,zip)
        count += 1

    return decode