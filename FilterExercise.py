"""
Use Filter/lambda to find a list of words including substring ‘cat’

Example a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]

Result = ['cat', 'wildcat', 'thundercat']

Hint use: re.compile(pattern, flags=0) , you need to import re
"""
import re
a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
#compile the RE
#a = filter( lambda a:re.match()a
#b = list(filter(lambda a:re.search("cat")))
#print(b)