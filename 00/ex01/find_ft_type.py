import time 
import datetime 

epoch = time.time()
x = datetime.datetime.now()

print(f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e} in scientific notation")
print (x.strftime("%b %d %Y"))