import os

print("請輸入一個偶數：")

x = int(input())

for i in range(1, x):
    print(' ' * (x-1-i) + '*' * (2*i-1))

print(f'{" "*(x-4)}CPTTM')

for i in reversed(range(1, x-1)):
    print(' ' * (x-1-i) + '*' * (2*i-1))

# os.system("pause")