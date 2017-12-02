import Krypto_3


def encode(massage,max = 233 ,min = 0,zip = False):
    lengh = len(massage)
    runds = int(lengh/10)
    extra = lengh - runds*10
    data = []
    encode1 = ""
    key = ""
    #print(lengh,runds,extra)
    count = 0
    for x in range(0,runds):
        data += [[massage[count:count+10]]]
        count += 10
    if len(massage[runds*10:]) >= 1:
        data += [[massage[runds*10:]]]
    for x in data:
        x = x[0]
        en,key1 = Krypto_3.encode(x,max=max,min=min,zip=zip)
        ret = Krypto_3.decode(key1,en,max=max,min=min,zip=zip)

        if check_korreckt(key1,en,x,ret) == 1:
            while check_korreckt(key1,en,x,ret) == 1:
                #print("new_little zirkel",x,en,key1)
                en, key1 = Krypto_3.encode(x, max=max, min=min, zip=zip)
                ret = Krypto_3.decode(key1, en, max=max, min=min, zip=zip)
                #print("little Sirckel",ret,x)
        encode1 += en
        key += key1
    check = Krypto_3.decode(key,encode1,max=max,min=min,zip=zip)
    if check_korreckt(key,encode1,massage,check) == 1:
        print("big")
        encode1, key,check = Krypto_3.encode(massage, max=max, min=min, zip=zip)
    return key,encode1,check





def check_korreckt(key1,encode1,org,ret):
    error = 0
    if "\n" in encode1 or "\n" in key1:
        #print("zeilenumbruch")
        error = 1
    if ret != org:
        print("falsche verschlüsselung",ret,org)
        error = 1
    if len(key1) != len(encode1):
        #print("verschiedene länge,key,encode1")
        error = 1
    if len(org) != len(key1):
        #print("verschiedene länge,ord,key")
        error = 1
    if len(org) != len(encode1):
        #print("verschiedene länge,org,en")
        error = 1
    if len(org) != len(ret):
        #print("verschiedene länge,org,ret")
        error = 1
    return error






