
      ################################
      #      Goldbach Conjecture     #
      ################################
      
import matplotlib.pyplot as plt

def prime(n):
    if n==3: return True
    for i in range(3,int(n**0.5)+1,2):  
        if n%i==0:
            return False    
    return True


count = 0
plt.plot(4, 1,'ro', markersize=0.5)
for i in range(6,10000,2):
    for j in range(3,(i//2)+1,2):
        if prime(j) and prime(i-j):
            count = count + 1

    plt.plot(i, count,'ro', markersize=0.5)
    count = 0

plt.show()
