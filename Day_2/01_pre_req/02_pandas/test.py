import sys
max_length = 100
square_list = [x**2 for x in range(max_length)]
print("list size: ",sys.getsizeof(square_list))
print("Sum of list: ",sum(square_list))

print("="*50)
square_generatore = (x**2 for x in range(max_length))
print("Generator size: ",sys.getsizeof(square_generatore))
print("Sum of generator: ",sum(square_generatore))