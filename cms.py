
#

# l =['abc','add','dfdf',55222,20.2]
#
#
# for v in l:
#     print(v,type(v))
l =[]
class Customer:
    def __init__(self):
        self.name = ''
        self.password =''
        self.mobile =''
        self.email = ''

    def addCustomer(self):
        l.append(self)


while(True):
    c =Customer()
    c.name =input("enter name:")
    c.password =input("enter password:")
    c.mobile =input("enter mobile:")
    c.email =input("enter email:")

    c.addCustomer()
    print("Customer added Successfully")
    ch =int(input("Press 0 for Exit Enter Chice="))
    if ch==0:
        break

for v in l:
    print(v, type(v))


