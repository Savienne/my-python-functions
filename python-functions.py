#Question1

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

#Question2
  
#largest([1,2,3,4,0])
#largest([10,4,2,231,91,54])

def largest(list):
  largest_num = max(list)
  print(largest_num)

#Question3

#occurrences('fleep floop', 'e')
#occurrences('fleep floop', 'p')
#occurrences('fleep floop', 'ee')
#occurrences('fleep floop', 'fe')

def occurrences(string1, string2):
  return string1.count(string2)

  #Question4

#product(-1, 4)
#product(2, 5, 5)
#product(4, 0.5, 5)  

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product
