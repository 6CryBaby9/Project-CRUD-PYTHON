from . import DataBase 
from time import time
from . Util import random_string
import time 
import os

def delete(no_buku):
    try:
        with open(DataBase.DB_NAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")
    
    os.rename("data_temp.txt",DataBase.DB_NAME)
                
def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = DataBase.TEMPLATE.copy()
    
    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + DataBase.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + DataBase.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f"{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n"
        
    panjang_data = len(data_str)
    
    try:
        with(open(DataBase.DB_NAME,'r+',enconding="utf-8")) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("error dalam update data")
def create(tahun,judul,penulis):
    data = DataBase.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + DataBase.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + DataBase.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f"{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n"
    try:
        with open(DataBase.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("data susah dtambhahkan boss")
    
    
def create_first_data():
    penulis = input('Penulis : ')
    judul = input('Judul: ')
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka bodohhhh, silahkan masukkan tahun lagi")                
        except:
            print("Tahun harus angka bodohhhh, silahkan masukkan tahun lagi")
    
    data = DataBase.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + DataBase.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + DataBase.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f"{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n"
    print(data_str)
    try:
        with open(DataBase.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udahlah boss")
        
def read(**kwargs):
    try:
        with open(DataBase.DB_NAME,'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("membaca database error")
        return False
            
