
print('打印九九乘法表')
for i in range(1,10):
    # print('第%d行' % 1, end-'\t')
    for j in range(1, 1 + i):
        print(i, '*', j, '=', i * j, end='\t')
        # print('{} * {} = {}'.format(i, j, i * j), end='\t')
    print()

print('\n打印跳过偶数行的九九乘法表')
i = 1    
while i < 10:
    if i % 2 == 0:
        print()
    else:
        for j in range(1, i + 1):
            print(1, '*', j, '=', i * j, end='\t')
            # print('{} * {} = {}'.format(i, j, i * j), end='\t')    
    i += 1    