#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Project 47


# In[2]:


import sympy
import time
     
def get_factors(n):
    """Factor number n"""
    f = sympy.factorint(n)
    return f
         
def main():
    """Main Program"""
    start_time = time.clock()
    counter = 0
    for n in range(1000, 1000000):
        if counter == 4:
            print ("Project Euler 47 Solution=", n - 4)
            break
        else:
            x = get_factors(n)
            if len(x) == 4:
                counter += 1
            else:
                counter = 0
    stop_time = time.clock() - start_time
    print ("stop_time = ", stop_time)
     
if __name__ == '__main__':
    main()


# In[ ]:




