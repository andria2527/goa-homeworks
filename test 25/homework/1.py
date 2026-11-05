# 2) კომენტარებით ახსენით თუ რა არის custom ფუნქციები, რისთვის გამოვიყენებთ და რა დანიშნულება გააჩნიათ, ასევე ახსენით მისი შექმნის გზები ეტაპობრივად და ახსენეთ თუ რაა პარამეტრები და არგუმენტები.

# 3) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვი. თქვენი დავალებაა დააბრუნოთ ამ ორი რიცხვის ჯამი.

# 4) შექმენით ფუნქცია, რომელსაც გადაეცემა 1 რიცხვი. თქვენი დავალებაა შეამოწმოთ ამ რიცხვის ლუწობა. თუ იგი ლუწია, დაბეჭდეთ "რიცხვი ლუწია" სხვა შემთხვევაში "რიცხვი კენტია"

# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა 1 რიცხვი. თქვენი დავალებაა დააბრუნოთ ამ რიცხვის კვადრატული მნიშნელობა.

# 6) შექმენით ფუნქცია, რომელიც გადაცემულ ტექსტს აბრუნებს დიდი ასოებით.

# 7) შექმენით ფუნქცია, რომელსაც პარამეტრებად გადაეცემა სახელი და გვარი, თქვენი დავალებაა გამოიტანოთ მნიშვნელობები ერთი წინადადების სახით.
#cumstom functionebi aris anu shentvitonve shegidzlia sheqmna funqciis
def greet(num1,num2):
    return num1 + num2
print(greet(67,69))


def greet(num1):
    if num1 == 2:
        return"ricxvi luwia"
    else:
        return"ricxvi kentia"
print(greet(2))


def greet():
    return"batoni davit shavidze aris chadi".upper()
print(greet())


def greet(name,lastname):
    return f"hello its me its {name} i know {lastname}"
print(greet("andria","machavariani"))


def greet(num1):
    return(num1 ** 2)
print(greet(5)) 