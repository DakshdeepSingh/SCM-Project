# Cafeteria Management System
li=[]
print("The Menu is \n 1 Samosa Rs.15 \n 1 Tea Rs.10 \n 1 Spring Roll Rs.99 \n 1 Pav Bhaji Rs.109 \n 1 Oreo Shake Rs.50")
def price(it,qty):
    if it=="s":
        return qty*15
    elif it=="t":
        return qty*10
    elif it=="sr":
        return qty*99
    elif it=="p":
        return qty*109
    elif it=="o":
        return qty*50
def order():
    for k in range(1):
        it=input("Type 's' for samosa, 't' for tea, 'sr' for spring roll, 'p' for pav bhaji, 'o' for oreo shake: \n")
        qty=int(input("Enter the quantity of the order: "))
        p=price(it,qty)
        if it=="s":
            it="Samosa"
        elif it=="t":
            it="Tea"
        elif it=="sr":
            it="Spring Roll"
        elif it=="p":
            it="Pav Bhaji"
        elif it=="o":
            it="Oreo Shake"
        li.append([it,qty,p])
        while True:
            t=int(input("Type \n '1' for ordering anything else \n '2' for starting over \n '3' for removing a item \n '4' for billing \n '5' for reviewing the order list: \n"))
            if t==1:
                it=input("Type 's' for samosa, 't' for tea, 'sr' for spring roll, 'p' for pav bhaji, 'o' for oreo shake: \n")
                qty=int(input("Enter the quantity of the order: "))
                p=price(it,qty)
                if it=="s":
                    it="Samosa"
                elif it=="t":
                    it="Tea"
                elif it=="sr":
                    it="Spring Roll"
                elif it=="p":
                    it="Pav Bhaji"
                elif it=="o":
                    it="Oreo Shake"
                li.append([it,qty,p])
            if t==2:
                li.clear()
                order()
                break
            if t==3:
                r=input("Type 's' for samosa, 't' for tea, 'sr' for spring roll, 'p' for pav bhaji, 'o' for oreo shake: \n")
                if r=="s":
                    r="Samosa"
                elif r=="t":
                    r="Tea"
                elif r=="sr":
                    r="Spring Roll"
                elif r=="p":
                    r="Pav Bhaji"
                elif r=="o":
                    r="Oreo Shake"
                flag= False
                for i in range(len(li)):
                    for j in range(2):
                        if r==li[i][j]:
                            li.remove(li[i])
                            flag= True
                            break
                    if flag is True:
                        break
            if t==4:
                break
            if t==5:
                print("Your Bill is:\n[Order Name, Quantity, Total Price]")
                for i in range(len(li)):
                    print(li[i])

order()

print("Your Bill is:\n[Order Name, Quantity, Total Price]")

for i in range(len(li)):
    print(li[i])

sum=0
for i in range(len(li)):
    sum+=li[i][2]
print("Total Rs.{}".format(sum))
