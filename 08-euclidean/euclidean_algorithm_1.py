print("a≧bとなる自然数を入力してください")
a = int(input("a="))
b = int(input("b="))

while True:
    r = a%b
    if r == 0:
        print("それらの数の最大公約数は", b)
        break
    a = b
    b = r
