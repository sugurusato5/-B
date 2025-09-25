row = int(input("行数を入力してください: "))
col = int(input("列数を入力してください: "))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        print(f"{i} x {j} ={i * j:>3}", end=" |")
                # 1 x 1 =  1 |
    print()
