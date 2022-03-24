#Quiz LOOPS CODE 

def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n))

# others code : **delete ''' for try the code what the output is 
# --- meaning other code
'''
for x in range(1,11):
    print(x**3)
  
---
for n in range(0,100):
    if (n%7==0):

        print(n)

---
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
      
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)

---
for x in range(10):
    for y in range(x):
        print(y)

'''

