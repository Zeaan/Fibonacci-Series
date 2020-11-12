def Fibonacci(end_num):
    print("0")
    print("1")
    a = 0
    b = 1
    for i in range(end_num-2):
        c = a + b
        print(c)
        a = b
        b = c
        i+=1
end_num = int(input(print("Enter the number of fibnonacci numbers you want")))
Fibonacci(end_num)
