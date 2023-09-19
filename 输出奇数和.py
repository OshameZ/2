count=0
for number in range(100):
    if number%2==0:
        continue
    count +=number
print(count)