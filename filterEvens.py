def is_even(L):
    evenList = []
    for num in L:
        if num%2 == 0:  #Even
            evenList.append(num)
        return evenList
numbers = [10, 2, 3, 1, 17, 9, 19, 18, 22, 26]
evens = is_even(numbers)
print("Numbers: ",numbers)
print("Even Numbers: ", evens)
#using filter


#map---> use more than list
d1 = [1,2,3]
d2 = [3,5,7]
result = list(map(lambda x,y: x+y, d1 ,d2))
print(result)


from functools import reduce



