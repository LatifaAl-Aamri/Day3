"""
f = lambda a,n : a * n
result = f(3,11)
print(result)

def oddEven(n):
    if n%2 == 0:
        return 'Even'
    else:
        return 'odd'
print(oddEven(14))
print(oddEven(15))

oddEven1 = lambda n:(n % 2 and 'odd' or 'even')
print(oddEven1(14))
print(oddEven1(15))
"""

add = lambda *arg : sum(arg)
print(add(20,3,40,5))








