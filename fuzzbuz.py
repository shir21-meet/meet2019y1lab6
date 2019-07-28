result=[]
n=200
for count in range (1,n):
    if count % 3 == 0:
        result.append("fizz")
    elif count % 5 == 0:
        result.append("fizz")
    else:
        result.append(count)
print(result) 
