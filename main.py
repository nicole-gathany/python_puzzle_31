def ping(
      i): #1
  if i > 0:  
    return pong(i - 1) #pong(0)
  return "0"

def pong(
      i): #0
  if i > 0:
    return ping(i - 1) #ping(-1)
  return "1"

print(ping(29))

#"0"

#############################
## id 351
## Puzzle Elo 1346
## Correctly solved 52 %
#############################

print(range(5, 10)[-1]) #prints: 9
print(range(0, 10, 3)[2]) #[0, 3, 6, 9] prints: 6
print(range(-10, -100, -30)[1]) # [-10, -40, -70] prints -40

#############################
## id 112
## Puzzle Elo 1353
## Correctly solved 41 %
#############################

def matrix_find(
      matrix, value):
  if not matrix or not matrix[0]:
    return False
          
  j = len(matrix) - 1
  for row in matrix:
    while row[j] > value: 
      j=j-1
      if j == -1:
        return False
    if row[j] == value:
      return True
  return False


matrix = [[3, 4, 4, 6],
          [6, 8, 11, 12],
          [6, 8, 11, 15],
          [9, 11, 12, 17]]
    
print(matrix_find(matrix=matrix, value=11))
 

