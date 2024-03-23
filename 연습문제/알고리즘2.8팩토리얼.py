def factorial(n):
    result =1
    for k in range(n,0,-1):
        result = result*k
    return result

a= int(input("팩도리얼을 구할 숫자를 입력하시오: "))
print(factorial(a))