#nested loop within another loop (outer, inner)
#           outer loop:
#                 inner loop:
rows = int(input("Enter the # of rows: "))
columns= int(input("Enter the # of columns: "))
symbol = input("Enter a Symbol to use: ")

for x in range(rows): #repeats the code 3 times or x amount of times
  for y in range (columns):
     print(symbol , end="")#this code keeps the numbers on the same line
  print()
