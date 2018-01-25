import math
# Program to generate prime numbers
# use the method that if a number is not divided by any other prime numbers that less than that, it is a prime number.
# Another method that used to decrease calcualtion is not chech any prime that larger than sqrt of the current number.
def generator():
    i=0
    a=3
    Prime_list =[2]
    file = open("Primelist.txt","w")
    
    while i <20000:
        s = math.sqrt(a)
        for j in range(len(Prime_list)):
            if Prime_list[j] > s:
                Prime_list.append(a)
                file.write("%d\n" % a)
                i += 1
                break
            if a % Prime_list[j] == 0:
                break
        a += 1
    file.close()
    #print Prime_list
        
generator()