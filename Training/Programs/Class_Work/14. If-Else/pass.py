# if statements cannot be empty, but if you for 
# some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error. 
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")