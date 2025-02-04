a=[]

n=int(input("Enter the number of elements in the list:"))

for i in range(0,n):
    ele=int(input("Enter the element:"))
    a.append(ele)

print(a)
#code
b=[]
m=int(input('Enter a number:'))
for i in range(0,n):
    if(a[i]<m):
        b.append(a[i])
print(b)