num_list = [int(number) for number in input("データを入力してください(スペース区切り) >").split()]


# 合計
def total(num_list):
    total = 0
    for num in num_list:
        total += int(num)

    return total


def max(num_list):
    max = num_list[0]
    for i in num_list:
        if i > max:
            max = i
    return max


def min(num_list):
    min = num_list[0]
    for i in num_list:
        if i < min:
            min = i
    return min


def ave(num_list):
    total = 0
    for num in num_list:
        total += num
    return total // len(num_list)


print(f"合計値: {total(num_list)}")
print(f"合計値: {max(num_list)}")
print(f"合計値: {min(num_list)}")
print(f"合計値: {ave(num_list)}")
