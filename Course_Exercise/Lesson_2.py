
"""
Exercise from class:
1. Write a python program to print the square of all numbers from 0 to 10
2. Write a python program to find the sum of all even numbers from 0 to 10
3. Write a python program to read three numbers (a,b,c) and check how many
numbers between ‘a’ and ‘b’ are divisible by ‘c’
4. Write a python program to get the following output
1-----99
2-----98
3-----97
. .
. .
98-----2
99-----1

5. Write a python program to read four numbers (representing the four octets of an IP)
and print the next five IP address
Eg:
Input:
192.168.255.252
----------Output---------
192.168.255.253
192.168 255.254
192.168 255.255
192.169.0.0
192.169.0.1
6. Write a python program to print the factorial of a given number

7. Write a python program to print the first 10 numbers Fibonacci series
8. Write a python program to read a number and print a right triangle using "*"
Eg :
Input : 5
----------Output---------
*
* *
* * *
* * * *
* * * * *
9. Write a python program to check given number is prime or not
10. Write a python program to print all prime numbers between 0 to 100 , and print
how many prime numbers are there.
(you can find the solutions in the gist, or solve it by yourselves :))

-----
"""
import math

def ex_1():
    #1. Write a python program to print the square of all numbers from 0 to 10

    for i in range(0,11):
        print(f"square of {i} is: {math.sqrt(i)} ")


def ex_2():
    #2. Write a python program to find the sum of all even numbers from 0 to 10
    total = sum(range(0,11,2))
    print(f"sum of all even numbers from 0 to 10 is: {total}")

def ex_3():
  #3. Write a python program to read three numbers (a,b,c) and check how many
  #   numbers between ‘a’ and ‘b’ are divisible by ‘c’

  user_input = input("please enter 3 numbers with coma between them:\n")
  user_range = []

  for i in user_input.split(", "):
    print(f"Got this numbers: {i}")
    user_range.append(int(i))

  print (f"Will check how many number from {user_range[0]} to {user_range[1]} can be divided with {user_range[2]}")
  for t in range(user_range[0], user_range[1]+1):
      if t % user_range[2] == 0:
          print(f"The number {t} divided with {user_range[2]} and {t} / {user_range[2]} = {t/user_range[2]}")
      else:
          print(f"The number {t} does NOT divided with {user_range[2]} ")

def ex_4():
    """
        Write a python program to get the following output
        1-----99
        2-----98
        3-----97
        . .
        . .
        98-----2
        99-----1
    """
    start = 1
    end = 100

    for i in range(start, end):
      print(f"{i} --- {end - i}")

def check_ip_range(ip):
    ip[3] += 1
    if ip[3] == 256:
        ip[3] = 0
        ip[2] += 1
    if ip[2] == 256:
      ip[2] = 0
      ip[1] += 1
    if ip[1] == 256:
        ip[1] = 0
        ip[0] += 1
    if ip[0] == 256:
        ip[0] = 1
    return(ip)

def ex_5():
    print("Write a python program to read four numbers (representing the four octets of an IP and print the next five IP address")
    user_ip = input("enter IP address \n")

    _ip = []
    for i in user_ip.split("."):
        _ip.append(int(i))
    if any(item >= 256 for item in _ip):
        print("The IP address is not valid")
        exit()

    print(f"got the following IP address {_ip[0]}.{_ip[1]}.{_ip[2]}.{_ip[3]}")
    print("The next 5 IP address should be:")
    for i in range(1, 6):
        calc_ip = check_ip_range(_ip)
        new_ip = ".".join(str(e) for e in calc_ip)
        print(f"{new_ip}")

def generic_error():
    print("Not a good selection, please enter a valid option! Try again.")
    return


def validate_input():
    while True:
        try:
            user_input = int(input("please enter your choice: \n"))
            if (user_input <= 0):
                generic_error()
                continue
            else:
                print(f"User choose option number {user_input}")
        except ValueError:
            generic_error()
            continue
        else:
            return user_input
            break

def ex_6():
    print("print the factorial of a given number")
    user_input = int(input("please provide a number:"))
    if user_input < 0:
        print(" Factorial does not exist for negative numbers")
    elif user_input == 0:
        print("The factorial of 0 is 1")
    else:
        facto = 1
        print(f"{user_input}! = ", end ='')
        for i in range(1,user_input+1):
            facto = facto * i
            if i < user_input:
                print(f"{i}x", end = '')
            else:
                print(f"{i}", end='')
        print(f" = {facto}")


def ex_7():
    print("Printing the first 10 Fibonacci numbers:")
    print("0, 1 ", end ='' )
    for i in range(3,11):
        print(f", {i-1 + i-2}", end ='')


def ex_8():
    print("enter a number to create triangle shape \n")
    user_choice = validate_input()

    for i in range(1,(user_choice+1)):
        print("*"*i)

def is_prime(n):
    for i in range(2, int(n)):
        if (n % i) == 0:
            return False
    return True

def ex_9():
    print("Enter a number to check if it is prime or not.")
    user_input = int(validate_input())
    result = is_prime(user_input)

    if result:
        print("The number you enter is prime...")
    else:
        print("The number you enter is not prime...")


def ex_10():
    print("printing all the prime numbers from 0 to 100...")
    print("0 1 2 ", end='')
    count = 3
    for i in range(3,101):
        result = is_prime(i)
        if result:
            count +=1
            print(f"{i} ", end='')
    print(f"\nThere are {count} prime numbers between 0 to 100")

#ex_2()
#ex_3()
#ex_4()
#ex_5()
#ex_6()
#ex_7()
#ex_8()
#ex_9()
ex_10()