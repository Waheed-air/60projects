# Python Projects 1 to 60

import math
import random
import string

# 1. Hello World Program
def hello_world():
    print("Hello, World!")

# 2. Simple Calculator
def simple_calculator():
    print("Enter two numbers:")
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "Undefined (division by zero)")

# 3. Odd or Even
def odd_or_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# 4. Area of a Circle
def area_of_circle():
    radius = float(input("Enter the radius: "))
    area = math.pi * radius**2
    print("Area of the circle:", area)

# 5. Temperature Converter
def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

# 6. Factorial Calculator
def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}.")

# 7. Palindrome Checker
def palindrome_checker():
    word = input("Enter a word: ")
    if word == word[::-1]:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")

# 8. Fibonacci Sequence
def fibonacci_sequence():
    n = int(input("Enter the number of terms: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# 9. Random Number Guessing Game
def guessing_game():
    number = random.randint(1, 100)
    guess = None
    while guess != number:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("Congratulations! You guessed the number.")

# 10. Prime Number Checker
def prime_checker():
    num = int(input("Enter a number: "))
    if num < 2:
        print(f"{num} is not a prime number.")
        return
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return
    print(f"{num} is a prime number.")

# 11. To-Do List
def to_do_list():
    todos = []
    while True:
        task = input("Enter a task (or 'quit' to stop): ")
        if task.lower() == 'quit':
            break
        todos.append(task)
    print("Your To-Do List:", todos)

# 12. Countdown Timer
def countdown_timer():
    seconds = int(input("Enter time in seconds: "))
    while seconds:
        print(seconds)
        seconds -= 1
    print("Time's up!")

# 13. Simple Interest Calculator
def simple_interest_calculator():
    p = float(input("Principal: "))
    r = float(input("Rate of Interest: "))
    t = float(input("Time (years): "))
    si = (p * r * t) / 100
    print("Simple Interest:", si)

# 14. Compound Interest Calculator
def compound_interest_calculator():
    p = float(input("Principal: "))
    r = float(input("Rate of Interest: "))
    t = float(input("Time (years): "))
    n = int(input("Compounds per year: "))
    ci = p * (1 + r / (100 * n)) ** (n * t)
    print("Compound Interest:", ci)

# 15. Number Reversal
def number_reversal():
    num = input("Enter a number: ")
    print("Reversed number:", num[::-1])

# 16. Rock, Paper, Scissors Game
def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

# 17. Password Generator
def password_generator():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", password)

# 18. BMI Calculator
def bmi_calculator():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi = weight / height**2
    print("Your BMI is:", bmi)

# 19. Quadratic Equation Solver
def quadratic_solver():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two real roots:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("One real root:", root)
    else:
        print("No real roots.")

# 20. Multiplication Table
def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# --- For brevity, projects 21 to 60 continue similarly, defining each function ---

# Example usage:
if __name__ == "__main__":
    hello_world()   # Run each function as needed for testing
    # Uncomment any function to test

# 21. Prime Numbers in Range
def prime_numbers_in_range():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    print("Prime numbers in range:", primes)

# 22. Count Vowels in a String
def count_vowels():
    text = input("Enter a string: ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    print("Number of vowels:", count)

# 23. Check Armstrong Number
def is_armstrong():
    num = int(input("Enter a number: "))
    order = len(str(num))
    sum_val = sum(int(digit)**order for digit in str(num))
    if num == sum_val:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

# 24. Generate Random Password
def generate_password():
    length = int(input("Enter the desired password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", password)

# 25. Decimal to Binary Converter
def decimal_to_binary():
    num = int(input("Enter a decimal number: "))
    binary = bin(num).replace("0b", "")
    print("Binary representation:", binary)

# 26. Remove Duplicates from List
def remove_duplicates():
    elements = input("Enter elements separated by space: ").split()
    unique_elements = list(set(elements))
    print("List without duplicates:", unique_elements)

# 27. Celsius to Fahrenheit Converter
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit}")

# 28. Max and Min of List
def max_min_of_list():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

# 29. Sort Words in Alphabetical Order
def sort_words():
    words = input("Enter words separated by space: ").split()
    words.sort()
    print("Sorted words:", words)

# 30. Linear Search
def linear_search():
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter the target value: "))
    for i, num in enumerate(arr):
        if num == target:
            print("Target found at index:", i)
            return
    print("Target not found.")

# 31. Binary Search
def binary_search():
    arr = sorted(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter the target value: "))
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print("Target found at index:", mid)
            return
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Target not found.")

# 32. Generate Multiplication Table
def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# 33. Find GCD of Two Numbers
def gcd():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    while b:
        a, b = b, a % b
    print("GCD is:", a)

# 34. Convert Binary to Decimal
def binary_to_decimal():
    binary = input("Enter a binary number: ")
    decimal = int(binary, 2)
    print("Decimal representation:", decimal)

# 35. Calculate Factorial Recursively
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_recursive_call():
    n = int(input("Enter a number: "))
    print("Factorial:", factorial_recursive(n))

# 36. Generate Fibonacci Sequence Recursively
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_recursive_call():
    n = int(input("Enter the number of terms: "))
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")
    print()

# 37. Sum of Elements in List
def sum_of_list():
    elements = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Sum of elements:", sum(elements))

# 38. Convert List of Strings to Integers
def convert_to_integers():
    strings = input("Enter numbers separated by space: ").split()
    integers = list(map(int, strings))
    print("Converted list:", integers)

# 39. Calculator with Functions
def calculator_with_functions():
    def add(x, y): return x + y
    def subtract(x, y): return x - y
    def multiply(x, y): return x * y
    def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"
    
    a, b = map(int, input("Enter two numbers: ").split())
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))

# 40. Sort List of Integers
def sort_list():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    numbers.sort()
    print("Sorted list:", numbers)

# --- More projects continue similarly ---

# The example usage is omitted for brevity.

if __name__ == "__main__":
    # Uncomment the functions to run each project
    hello_world()
    # simple_calculator()
    # linear_search()
    # ... continue with more tests as needed




# 41. Convert Decimal to Hexadecimal
def decimal_to_hexadecimal():
    num = int(input("Enter a decimal number: "))
    hexadecimal = hex(num).replace("0x", "")
    print("Hexadecimal representation:", hexadecimal)

# 42. Merge Two Lists
def merge_lists():
    list1 = input("Enter elements of list 1 separated by space: ").split()
    list2 = input("Enter elements of list 2 separated by space: ").split()
    merged_list = list1 + list2
    print("Merged list:", merged_list)

# 43. Check Leap Year
def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# 44. Sum of Digits
def sum_of_digits():
    num = int(input("Enter a number: "))
    sum_digits = sum(int(digit) for digit in str(num))
    print("Sum of digits:", sum_digits)

# 45. Count Occurrences of a Character in a String
def count_character_occurrences():
    text = input("Enter a string: ")
    char = input("Enter the character to count: ")
    count = text.count(char)
    print(f"'{char}' appears {count} times in the text.")

# 46. Generate a List of Even Numbers
def generate_even_numbers():
    n = int(input("Enter the number of even numbers to generate: "))
    evens = [i for i in range(2, 2 * n + 1, 2)]
    print("Even numbers:", evens)

# 47. Reverse a String
def reverse_string():
    text = input("Enter a string: ")
    reversed_text = text[::-1]
    print("Reversed string:", reversed_text)

# 48. Count Words in a Sentence
def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("Number of words:", len(words))

# 49. Calculate Sum of Squares
def sum_of_squares():
    n = int(input("Enter a number: "))
    sum_squares = sum(i ** 2 for i in range(1, n + 1))
    print("Sum of squares:", sum_squares)

# 50. Convert Celsius to Kelvin
def celsius_to_kelvin():
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)

# 51. Capitalize Each Word in a Sentence
def capitalize_words():
    sentence = input("Enter a sentence: ")
    capitalized = sentence.title()
    print("Capitalized sentence:", capitalized)

# 52. Check Perfect Number
def is_perfect_number():
    num = int(input("Enter a number: "))
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")

# 53. Sum of Cubes
def sum_of_cubes():
    n = int(input("Enter a number: "))
    sum_cubes = sum(i ** 3 for i in range(1, n + 1))
    print("Sum of cubes:", sum_cubes)

# 54. Count Upper and Lower Case Characters
def count_case():
    text = input("Enter a string: ")
    upper_case = sum(1 for char in text if char.isupper())
    lower_case = sum(1 for char in text if char.islower())
    print(f"Uppercase letters: {upper_case}, Lowercase letters: {lower_case}")

# 55. Convert Kilometers to Miles
def kilometers_to_miles():
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print("Distance in miles:", miles)

# 56. Check Armstrong Numbers in a Range
def armstrong_numbers_in_range():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    armstrong_numbers = []
    for num in range(start, end + 1):
        order = len(str(num))
        sum_val = sum(int(digit) ** order for digit in str(num))
        if num == sum_val:
            armstrong_numbers.append(num)
    print("Armstrong numbers in range:", armstrong_numbers)

# 57. Calculate LCM of Two Numbers
def lcm():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            print("LCM is:", greater)
            break
        greater += 1

# 58. Check Palindrome for Sentences
def sentence_palindrome():
    sentence = input("Enter a sentence: ").replace(" ", "").lower()
    if sentence == sentence[::-1]:
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")

# 59. Generate Random Name
def generate_random_name():
    first_names = ["John", "Jane", "Alex", "Alice", "Chris"]
    last_names = ["Doe", "Smith", "Johnson", "Brown", "Wilson"]
    print("Random name:", random.choice(first_names) + " " + random.choice(last_names))

# 60. Simple Mad Libs Game
def mad_libs_game():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    print(f"The {adjective} {noun} decided to {verb} today!")
    
# --- Usage Example ---
if __name__ == "__main__":
    decimal_to_hexadecimal()
    # Uncomment more function calls to test each project
