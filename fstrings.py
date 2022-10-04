for _ in range (0,2):

    GST = 0.05

    amount = float(input("Enter the pre-tax total of your order: "))
    total = amount * (1 + GST)

    print("With 2 strings, 8.2f...")
    print("Before tax: $", f'{amount:8.2f}')
    print("Total:      $", f'{total:8.2f}')
    print("\n")
    
    print("With one string, 8.2f...")
    print(f"Before tax: ${amount:8.2f}")
    print(f"Total:      ${total:8.2f}")
    print("\n")

    print("With one string, 9.2f...")
    print(f"Before tax: ${amount:9.2f}")
    print(f"Total:      ${total:9.2f}")
    print("\n")

    print("With one string, 8.2f, and '>'...")
    print(f"Before tax: ${amount:>9.2f}")
    print(f"Total:      ${total:^9.2f}")
    print("\n")
