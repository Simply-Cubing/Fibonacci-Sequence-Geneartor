n = int(input("How many terms do you want to see: "))
term1, term2 = 0, 1
showed = 0

if n <= 0:
  print("Please enter a POSITIVE integer")
  retry = int(input("""
How many terms do you want to see: """))  
  if retry <=0:
    print("... listen to instructions next time")
    print('good night')
  
  
while showed < n:
  print(""" 
""",term1)
  nthterm = term1+term2
  term1 = term2
  term2 = nthterm
  showed += 1
