import random

# This is main function that is connected to the Test button. You don't need to touch it.
def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)

# This is main function that is connected to the Test button. You don't need to touch it.
def mod_exp(x, y, N): 
	if y == 0:
		return 1
	z = mod_exp(x, y//2, N)
	if y % 2 == 0:
		return (z*z) % N
	else:
		return (x*z*z) % N
	
# You will need to implement this function and change the return value.   
def fprobability(k):
    return 1 - (1 / (2**k))

# You will need to implement this function and change the return value.   
def mprobability(k):
    return 0.0

# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
# hi, inclusive.
def fermat(N,k):
	is_prime = True
	for i in range(k):
		a = random.randint(2,N-1)
		if mod_exp(a,N-1,N) != 1:
			is_prime = False

	if is_prime:
		return 'prime'
	else:
		return 'composite'

# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
#  hi, inclusive.
def miller_rabin(N,k):
	return 'composite'
