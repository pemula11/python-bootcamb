# num = [1,2,3,4,5,6,7,8,9,10]
# jumlah = len(num)
# for i in range(0,jumlah):
#     print(num[i])


# num = ["satu", "dua", "tiga"]
# for i in num:
#     print(i)


# def halo(a, b):
#    hasil = a+b
#    print(hasil)
# halo(20, 39)


## Lambda 

# hitung = lambda nilai: nilai * 0.2
# print(hitung(80))


### Class

class Myclass():
    nama = "andri"
    hp = 50
    speed = 30

p1 = Myclass()
print(p1.hp)


class player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("halo, namaku " + self.name)

p2 = player("andri", 23)

print(p2.name)
p2.myfunc()