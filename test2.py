for x in range (5):
   if (x==0 or x==2):
      print("xxxxx")
   else:
    print("xx")

numbers=[5, 2, 5, 2, 2]
#numbers1=[0,1,2,3,4,5]
for i in numbers :
   print(f'x' * i)

numbers=[5, 2, 5, 2, 2]
for i in numbers :
   output = ''
   for j in range(i):
      output += '*'
   print(output)
