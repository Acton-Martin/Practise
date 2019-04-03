def fab(max):
   n, a, b = 0, 0, 1
   while n < max:
       print(b)
       a, b = b, a + b
       n = n + 1
a = fab(100)
print(fab(100))