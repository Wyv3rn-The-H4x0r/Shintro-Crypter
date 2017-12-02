import zipfile
import commands
import os
import shutil
import Zeichen

begrenzer = "=========================================================================================================="
writtenbegremzer = "\r\n==========================================================================================================\r\n"
class ziper:
    def __init__(self):
        self.Zeichen = Zeichen.coder()

    def open(self,name,encode):#name. . . ordner , encode name of encode
        self.make_new(name,encode)
        if ".zip" not in encode:
            encode += ".zip"
        old = zipfile.ZipFile("./old.zip",mode="r")
        f = zipfile.ZipFile(encode,mode = "w")
        key_file = open("key_file.txt","w+")
        for file in old.namelist():
            if "." in file:
                self.krypt_file(file,f,key_file,old,name)
        f.close()
        key_file.close()
        old.close()
        os.remove("./old.zip")


    def krypt_file(self,file,f,key_file,old,path):

        massage = old.read(file).decode(encoding='UTF-8')
        key, encode, check = commands.encode(massage)
        f.writestr(file, encode)
        key_file.write(file + "] " + key + "\n" + begrenzer + "\n")



    def read(self,bytes):
        m = ''
        for x in bytes:
            m += self.Zeichen.int_str(x,True)
        return m


    def make_new(self,name,path):
        shutil.make_archive(path, 'zip', name)
        shutil.make_archive("./old", 'zip', name)
    def find(self,tofind,string,place = 0):
        count = 0
        for x in string:
            if x == tofind[0]:
                if string[count:count+len(tofind)] == tofind:
                    if place == 0:
                        return count
                    else:
                        place -= 1
            count += 1

    def decode_zip(self,path,new):
        decode_zip = zipfile.ZipFile(new, mode="w")
        key_file = open("./key_file.txt")
        key_f = key_file.read()
        zip_file = zipfile.ZipFile(path, mode="r")
        count = 0
        for x in zip_file.namelist():
            header = self.find(x,key_f)
            beg = self.find(begrenzer,key_f,count)
            key = key_f[header + len(x) + 2:beg - 1]

            encode = zip_file.open(x).read().decode("utf-8")
            massage = commands.Krypto_3.decode(key, encode,check=False)
            decode_zip.writestr(x, massage)
            count += 1

        key_file.close()
        decode_zip.close()
        zip_file.close()
        os.remove("./key_file.txt")
        os.remove(path)
