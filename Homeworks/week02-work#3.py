def smallest(x,y,z):
    if(x < y) :
        if(x < z) : return x
        else : return z

    elif(y < z) : return y
    else : return z


print(smallest(3,5,9)) # returns 3
print(smallest(5,3,9)) # returns 3
print(smallest(5,9,3)) # returns 3
print(smallest(3,9,5)) # returns 3
print(smallest(9,3,5)) # returns 3
print(smallest(9,5,3)) # returns 3
print(smallest(3,3,5)) # returns 3
print(smallest(5,3,3)) # returns 3
print(smallest(3,5,3)) # returns 3
print(smallest(3,3,3)) # returns 3
