array_num= [4, 10, 6, 14, 18, 19, 20]
Target=20

serial_no=1
n=len(array_num)
print("Output:{",end ='')
for i in range(n):
  for j in range(n):
      if(array_num[i]+array_num[j]==Target):
          print(serial_no,":[",i,",",j,"],",end='')
          serial_no+=1
print("}")