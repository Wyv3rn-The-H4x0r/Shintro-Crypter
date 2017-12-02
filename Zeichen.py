

class coder:
    def __init__(self):
        self.zeichen = []
        self.list = []
        self.find_zeichen()
        self.all_list()

    def find_zeichen(self):
        for x in range(0,1000):
            try:
                d = open("test.txt","w+")
                d.write(chr(x))
                d.close()
                self.zeichen += [chr(x)]
            except:pass



    def all_list(self):
        for x in range(0,20000):
            self.list += [chr(x)]


    def generate_int(self,x,off = False):
        if off == False:
            list_key = list(x)
            #print("ggg",list_key)
            m = []
            for x in list_key:
                if type(x) is str:
                    m += [self.str_int(x,off = off)]
            return m

        elif off == True:
            m = []
            for y in list(x):
                #if y == '"':print("FUCK ME UP",y,ord(y))
                m += [self.str_int(y,off = True)]
            return m

    def str_int(self,x,off = False):
        if off == False:
            count = 0
            for y in self.zeichen:
                #print(y,x)
                if x == y:
                    #print(x,y,"here")
                    return count
                count += 1
        elif off == True:
            count = 0

            for y in self.list:
                if x == y:
                    if count == 8240: print("here",x,y)
                    return count

                count += 1






    def int_str(self,x,off = False):
        #print(x,off,chr(x))
        if off == False:
            if type(x) is str:return x
            try:
                y = self.zeichen[x]
                #print(x,y)
                return y
            except:print("geht nicht",x,self.zeichen[x-1])
        elif off == True:
            #print("FUCKK",x,chr(x))
           # print(x)
            return self.list[x]