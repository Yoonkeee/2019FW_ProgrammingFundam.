def smallerOdd(x,y):
    if(x == None) :
        if(y%2 == 1) : return y
        elif(y%2 != 1) : return None
    if(x%2 == 1) :
        if(y%2 == 1) :
            if(x < y) : return x
            else : return y
        else : return x
    elif(y%2 ==1) : return y
    else : return None


def smallestOdd(x,y,z) :
    return smallerOdd(smallerOdd(x,y),z)


print(smallestOdd(3,2,2)) # returns 3 
print(smallestOdd(3,5,7)) # returns 3 
print(smallestOdd(3,5,1)) # returns 1 
print(smallestOdd(8,3,4)) # returns 3
print(smallestOdd(8,3,5)) # returns 3
print(smallestOdd(8,5,3)) # returns 3
print(smallestOdd(2,8,3)) # returns 3
print(smallestOdd(2,8,4)) # returns None
