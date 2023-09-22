# 今日講IT第三輯(第17集) 範例檔案

大家可以複製以下程式碼 又或者直接下載 HelloWorld.py 檔案

``` python
import os

print("請輸入一個偶數：")

x = int(input())

for i in range(1, x):
    print(' ' * (x-1-i) + '*' * (2*i-1))

print(f'{" "*(x-4)}CPTTM')

for i in reversed(range(1, x-1)):
    print(' ' * (x-1-i) + '*' * (2*i-1))

# os.system("pause")
```
