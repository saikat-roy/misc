import numpy as np
import math

'''
Approximate Angle between 2 vectors using LSH. Done as part of the 
Data Science and Big Data lecture at University of Bonn (SS2018)
'''

def generate_unit_vector(d):
	'''
	Generate a unit vector with dimensions d
	'''
	n = np.random.randn(d)
	return n/np.sqrt(np.sum(n**2))

def hash_vec(u,n):
	'''
	Hash Vector u with unit vector n into 2 buckets
	'''
	if np.dot(u,n)>=0:
		return 1
	else: return 0
	
d=5									# dimension of data
u1 = np.random.randn(d)				# point 1
u2 = np.random.randn(d)				# point 2

# Calculate True Angle between vectors
ang_true = np.dot(u1,u2)/(np.sqrt(np.dot(u1,u1))*np.sqrt(np.dot(u2,u2)))
ang_true = math.degrees(math.acos(ang_true))

print "\n Vector 1"
print u1
print "\n Vector 2"
print u2

print "\nData Dimension = "+str(d)+"\n"
h_list = [10,50,100,200,300,400,500,600,700,800,900,1000,5000,10000]
for h_count in h_list:				# iterate over no. of hash functions
	c = 0
	for i in range(h_count):		# generate new unit vector n and  
		n = generate_unit_vector(d)	# count similarity between h_n(u1)
		b1 = hash_vec(u1,n)			# and h_n(u2)
		b2 = hash_vec(u2,n)
		if b1==b2:
			c+=1.0

	ang_approx = (1-(c/h_count))*180 # Calculate approx angle

	print "Number of hash functions = "+str(h_count)
	print "True Angle between vectors = "+str(ang_true)
	print "Approx Angle between vectors = "+str(ang_approx)
