import commands
import ziper



class command:
    def __init__(self):
        self.max = 500
        self.min = 0
        self.running = True
        #self.log = logger("encode.txt")
        self.zip = ziper.ziper()
    def eingabe(self):
        print("[STOP only meanes that you only have to copy to this point (or the massage ends there)")
        while self.running == True:
            command = input(">>>")
            if command == "encode":
                massage = input("massage >>>")
                key,encode,check = commands.encode(massage)
                print("!!!",len(key),len(encode))
                print("=======================key===================")
                print(key,"[STOP")
                print("=====================encode==================")
                print(encode,"[STOP")
                print("=============================================")
                print(check)
                #self.log.add(key,encode)
            elif command == "decode":
                key = input("key >>>")
                encode = input("encode >>>")
                massage = commands.Krypto_3.decode(key,encode)
                print("====================Massage========================")
                print(massage)
                print("===================================================")

            elif command == "encode_f":
                path = input("path >>>")
                option = input("option >>>")
                f = open(path)
                massage = f.read()
                f.close()
                key, encode, check = commands.encode(massage)
                if option == "print":
                    print("!!!", len(key), len(encode))
                    print("=======================key===================")
                    print(key, "[STOP")
                    print("=====================encode==================")
                    print(encode, "[STOP")
                    print("=============================================")
                    print(check)
                elif option == "same" or option == "other":
                    if option == "other":
                        path = input("new path >>>")
                    d = open(path,"w+")
                    en = list(encode)
                    for x in en:
                        try:
                            d.write(x)
                        except:
                            print(x)
                    d.close()
            elif command =="encode_zip":
                print("Ordner den man verschlüsseln will")
                file = input("path >>>")
                print("Name der verschlüsselten zip Datei .zip wird weggelassen")
                name = input("path >>>")
                self.zip.open(file,name)
            elif command == "decode_zip":
                print("Name der verschlüsselten zip datei")
                path1 = input(">>>")
                print("Name der entschlüsselten Datei .zip nicht vergessen")
                path2 = input(">>>")
                self.zip.decode_zip(path1,path2)



class logger:
    def __init__(self,path):
        self.path = path

    def add(self,key,encode,clear = True):
        if clear == True:
            d = open(self.path,"w+")
        else:
            d = open(self.path,"a+")

        d.write(key+"\n"+encode)
        d.close()

command().eingabe()