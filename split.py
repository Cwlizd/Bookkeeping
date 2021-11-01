#檢查檔案在不在
import os #operating system

products = []
if os.path.isfile('products.csv'):
    print('yes')
    with open('products.csv','r') as f:
        for line in f:
            if '品項,價格' in line:
                continue#繼續(一樣在回圈內，進到下一回)
            name, price = line.strip().split(',')
            products.append([name,price])
    print(products)
#split 後為清單
    
else: 
    print('uh...I can not find it')



#讓使用者輸入
while True:
    name = input('商品品項:')
    if name == 'q':
        break
    price = input('商品價格:')
    products.append([name,price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0],'價格為:',p[1])

#寫入檔案
with open('products.csv','w') as f:
    f.write('品項,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')