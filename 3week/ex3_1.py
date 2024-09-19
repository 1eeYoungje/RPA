num = int(input("수를 입력하세요: "))

if num>0 and num < 10:
    for i in range(1, 10):
        print(f"{num} X {i} = {num*i}")
else:
    print("수를 다시 입력하세요")