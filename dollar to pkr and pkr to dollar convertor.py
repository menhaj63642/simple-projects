import time


# welcoming and guiding

time.sleep(0.5)
print("hello dear ! welcome to money convertor\n\n")
time.sleep(1)
print("the price of dollar is as according to todays date \n you can change dollar price here\n\n\n")

#dollar price as 26 05 2022

dollartoday = 202
time.sleep(1)

#asking if he/she wants to chage dollar price
tdollar = input("do you want to change dollar price(y-yes n_no) :")
time.sleep(0.5)
if tdollar.lower()== "y":
    askdollar = int(input("whats the dollar price :"))
    dollartoday = askdollar

else:
    pass

#asking if dollar to pkr or pkr to dollar
print("         choose one      \n1-dollar to pkr\n2-pkr to dollar")
time.sleep(1)
opt=int(input(' :'))

#making function for calculation

def doll_pkr():
    ans= dollar * dollartoday
    time.sleep(1)
    print(f"usd {dollar} is equal to pkr {ans}")
    time.sleep(5)
def pkr_doll():
    ans=pkr/dollartoday
    time.sleep(1)
    print(f"pkr {pkr} is {ans} in dollar")
    time.sleep(5)

# checking what he/she choose in opt and using the function
if opt == 1:
    dollar =int(input('how much dollar :'))
    doll_pkr()
if opt == 2:
    pkr = int(input("how much pkr :"))
    pkr_doll()






