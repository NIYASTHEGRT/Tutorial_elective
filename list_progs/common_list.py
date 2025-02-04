a=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("Enter the element:"))
    a.append(ele)
print(a,"\n")
#list 2
b=[]
n=int(input("Enter the number of elements in the seccond list:"))

for i in range(0,n):
    ele=int(input("Enter the element:"))
    b.append(ele)
print(b,"\n")
#intersection
common = list(filter(lambda x: x in b, a))

print("The common list is ",common)

