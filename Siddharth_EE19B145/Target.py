import numpy as np
#Question 2: Find pair from array that sums to a target value.
#Class for the computation
class PairFind(object):
	def __init__(self,Arr,target):
		self.pairs={}; #The dictionary of the solutions
		self.size=len(Arr); #Size of input array
		self.arr=Arr;
		self.tar=target;
		
	def Find(self):
		D={};
		Arr=self.arr;
		for i in range(self.size):
			if(D.get(Arr[i],False)):
				D[Arr[i]]+=[i];
			else:
				D.update({Arr[i]:[i]});
		
		Tar=self.tar;
		revOut={};
		Pairs=self.pairs;
		count=1;
		for i in D:
			diff=Tar-i;
			for j in D[i]:
				if D.get(diff,False):
					for k in D[diff]:
						if(revOut.get((k,j),False))==False:						
							revOut.update({(j,k):count});
							Pairs.update({count:(j,k)});
							count+=1;			
		self.pairs=Pairs;
		
	def display(self):  #Function to print the indices of the pairs that add up to target
		print("The pairs of values from the input array that add up to the target of "+str(self.tar)+" are: ");
		print(self.pairs,'\n');			
								

#Test case:
A=np.array([10,20,30,10,40,30,1,49,44,6,3.7,46.3]);
target=50.0;
X=PairFind(A,target);
X.Find();
print("Question 2: ");
X.display();
