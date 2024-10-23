
r = input('輸入遊戲DB碼: ')
x = input('輸入修改db碼: ')
c = ''
a = 0

if len(r) >= len(x):
    a = len(x)
else:
    a = len(r)


for i in range(a):
    if r[i] != x[i]:
        c += '?'
    else:
        c += r[i]
print('修改後', c)