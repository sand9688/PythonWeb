x = [1,9,8,7,6,5,4,3,2,1]
y = x
for i in x:
    a = 0
    for j in range(len(x)):
        if int(i) > x[j]:
            a += 1
    y[a] = x
print(x)