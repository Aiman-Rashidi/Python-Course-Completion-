total = 0
while (number := input("Enter number (or 'done'): ").strip().lower()) != "done":
    try:
        total += int(number)
    except ValueError:
        print("Enter a valid number or 'done' to finish.")

print(f"Total sum: {total}")



# total = 0
# while (number := input("enter: ").strip().lower()) != "done":
#     try:
#         total += int(number)
#     except Exception as e:
#         print(e)
# print(f"Total sum: {total}")