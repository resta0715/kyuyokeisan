number=123.65

a=int(number)
b=number-int(number)

if b<=0.5:
    b=0
if 0.5<b:
    b=1

print(b)

number=a+b
print(number)




