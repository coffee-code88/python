broad_size = int(raw_input("Enter broad size: "))

def print_item():
    print("x " * broad_size)

# Function will print board like an actual board
def print_board():
  for row in range(broad_size):
    print_item()
    
print_board()
