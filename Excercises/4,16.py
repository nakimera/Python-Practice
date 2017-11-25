v1,v2,v3,v4,v5=eval(input('Please enter 5 integers:'))

biggest = 0
if v1>biggest:
    biggest = v1
if v2>biggest:
    biggest = v2
if v3>biggest:
    biggest = v3
if v4>biggest:
    biggest = v4
if v5>biggest:
    biggest = v5

print(biggest, 'is the maximum number,', end=' ')

minimum = v1
if v1<minimum:
    minimum = v1
if v2<minimum:
    minimum = v2
if v3<minimum:
    minimum = v3
if v4<minimum:
    minimum = v4
if v5<minimum:
    minimumbiggest = v5
print(minimum, 'is the minimum number')
    
