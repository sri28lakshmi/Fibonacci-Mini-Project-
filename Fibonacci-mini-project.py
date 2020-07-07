def fibonacci_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

def main():
    while 1:
        print("~WELCOME TO FIBONACCI!~\nPress 1: Start\nPress 2: Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            num = int(input("Enter Number: "))
            print(f"The {num}th number in the Fibonacci sequence is:", fibonacci_recur(num))
        elif choice == 2:
            exit()
        else:
            print("Please enter a valid choice!")

main()