num_list = input("データを入力してください(スペース区切り) >").split(" ")
total = 0
for num in num_list:
    total += int(num)

print(f"合計値: {total}")

max = num_list[0]
for i in range(1, len(num_list)):
    if num_list[i] > max:
        max = num_list[i]

print(f"最大値: {max}")

min = num_list[0]
for i in range(1, len(num_list)):
    if num_list[i] < min:
        min = num_list[i]
print(f"最小値: {min}")

print(f"平均値: {total // len(num_list)}")
