class Hello: 

     

    def func (self): 

         

        n=int(input())  #getting number of elements in array 

        num=[]  #defining a list 

         

        for k in range (0,n):  #getting array elements  

            a=int(input()) 

            num.append(a)  #adding elements to list 

             

        count=0 

        m=int(input()) #getting target from user 

        eq_Sum ={}  #defining a dictionary  

         

        for i in range (0,n): 

            for j in range (0,n): 

                if(i!=j): 

                    if(num[i] + num[j] == m):  #checking condition 

                        count = count+1 

                        eq_Sum[count]=[i,j]  #entering values to dictionary  

        print(eq_Sum) 

         

H=Hello() 

H.func() 