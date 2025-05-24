# #Print All Pythagorean Triplets with Values ≤ n
# # Ask the user to enter n. Find and print all *Pythagorean triplets* (a, b, c) such that a² + b² = c² and a, b, c ≤ n.
# n = int(input("enter a number: "))
# for a in range(1,n):
#  for b in range(1,n):
#      for c in range(1,n):
#          if (a*a)+(b*b) == (c*c) and c<=n:
#             print(a,b,c)

# # Write a Python program using nested loops to print the multiplication tables from 1 to 10.
# for i in range(1,11):
#    for j in range(1,11):
#       print(f"{i} X {j} = {i*j}")

# # Using nested loops, count how many prime numbers exist between 1 and 100.

# # > 💡 *Hint*: A number is prime if it’s only divisible by 1 and itself.
# count = 0
# for i in range(2,101):
#    is_prime = True
#    for j in range(2,(j**0.5)+1):
#       if j%2==0:
#          is_prime = True
#          break
#    if is_prime:
#         count+=1

# print("the numbe of prime numbers bewteen 1 to 100 is",count)      

# # . Print All Pairs of Numbers (1 to n) Where Sum is Even*
# # Ask the user to enter a number n. Using nested loops, print all pairs (i, j) from 1 to n where the sum i + j is even.
# n = int(input("enter a number"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         a = i+j
#         if a%2 ==0:
#             print(i,j)

# #  Count Total Factors of All Numbers from 1 to n*
# # Ask the user to enter a number n. Use nested loops to find how many total factors (divisors) exist for all numbers from 1 to n
# z = int(input("enter a number: "))
# count_fac = 0
# for i in range(1,z+1):
#    for j in range(1,i+1):
#         if i%j ==0:
#           count_fac += 1
# print("total factors of all numbers from 1 to",z ,"is",count_fac)

# 1 to N multiplication table using while loop
# y = int(input("enter a number: "))
# i=1
# while i<=y:
#    j=1
#    while j<11:
#     print(f"{i} X {j} = {i*j}")
#     j+=1
#    i+=1

#print the pattern using while loop 11122222333444445556666677788888......
x = int(input("enter a number: "))
i=1
while i<=x:
    if i%2==0:
        j=1
        while j<=5:
            print(i)
            j+=1
    else:
        n=1
        while n<=3:
            print(i)
            n+=1
    i+=1
