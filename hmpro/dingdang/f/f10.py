f=open('a.txt','r')
data=f.read(6)
data2=f.readline()
data3=f.readline()
f.close()
print(data)
print(data2)
print(data3)