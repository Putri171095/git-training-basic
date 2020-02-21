#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problems 46


# In[2]:


n = 5
f = 1
primes = set()
 
while True:
    if all(n % p for p in primes):
        primes.add(n)
    else:
        if not any((n-2*i*i) in primes for i in range(1, n)):
            break
    n += 3-f
    f = -f

print ("Project Euler 46 Solution =", n)

