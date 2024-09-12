print("1개의 숫자를 입력하세요")
num = int(input())
#if num%2==0 :
#    print("짝수이다 - True")
#else:
#    print("짝수이다 - False")

result = (num % 2) == 0
print(f"짝수이다 - {result}")