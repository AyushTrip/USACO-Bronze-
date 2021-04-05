#Ayush Tripathi
#February Problem 3 - Clockwise Fence

sequences = []

#Read the input
n = int(input())
for i in range(n):
  sequences.append(str(input()))

#Find all the corners
def find_corners(sequence):
  corners = []
  for i in range(len(sequence)-1):
    if sequence[i] != sequence[i+1]:
      corners.append(sequence[i] + sequence[i+1])
  return corners

#Create corner key
corner_key = {
  'NE' : 'C',
  'NW' : 'A',
  'SE' : 'A',
  'SW' : 'C',
  'WN' : 'C',
  'WS' : 'A',
  'EN' : 'A',
  'ES' : 'C'
}

#Create a function to determine the greater amount
def find_direction(sequence):
  global corner_key
  anticlockwise, clockwise = 0,0
  corners = find_corners(sequence)

  for corner in corners:
    if corner_key.get(corner) == 'A':
      anticlockwise += 1
    if corner_key.get(corner) == 'C':
      clockwise += 1
    
  if anticlockwise > clockwise:
    return 'CCW'

  else:
    return 'CW'


for sequence in sequences:
  print(find_direction(sequence))
