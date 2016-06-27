from random import randint
from time import sleep

broad_size = int(raw_input("Enter broad size: "))
# init board
db_list=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# print board with item in list
def print_board():
    for row in db_list:
        row = [str(i) for i in row]
        print " ".join(row)    

print db_list
print_board()

username = raw_input("Enter your name: ")
computername = "Lena Comp"
print "You will fight a computer"
is_over = False


def user_move(value):
    x = int(raw_input("Enter your x move: "))
    y = int(raw_input("Enter your y move: "))
    db_list[x][y]=value

def computer_move(value):
    x = randint(0,2)
    y = randint(0,2)
    if db_list[x][y] == 0:
        db_list[x][y] = value
    else:
        print "Computer is thinking..."
        sleep(2)
        computer_move(value)

def is_not_full_board():
    for row in db_list:
        if 0 in row:
            return True
    return False

def who_is_won():
    if db_list[0][0] + db_list[0][1] + db_list[0][2] == 3 or db_list[0][0] + db_list[1][0] + db_list[2][0] == 3 or db_list[0][0] + db_list[1][1] + db_list[1][2] == 3 or db_list[0][1] + db_list[1][1] + db_list[2][1] == 3 or db_list[0][2] + db_list[1][2] + db_list[2][2] == 3 or db_list[0][2] + db_list[1][1] + db_list[2][0] == 3 or db_list[1][0] + db_list[1][1] + db_list[1][2] == 3 or db_list[2][0] + db_list[2][1] + db_list[2][2] == 3:
        is_over = True
        return username + " is WON"
    elif db_list[0][0] + db_list[0][1] + db_list[0][2] == -3 or db_list[0][0] + db_list[1][0] + db_list[2][0] == -3 or db_list[0][0] + db_list[1][1] + db_list[1][2] == -3 or db_list[0][1] + db_list[1][1] + db_list[2][1] == -3 or db_list[0][2] + db_list[1][2] + db_list[2][2] == -3 or db_list[0][2] + db_list[1][1] + db_list[2][0] == -3 or db_list[1][0] + db_list[1][1] + db_list[1][2] == -3 or db_list[2][0] + db_list[2][1] + db_list[2][2] == -3:
        is_over = True
        return computername + " is WON"
        
    else:
        if is_not_full_board():
            return "CONTINUE"
        else:
            return "DRAW"
            is_over = True

while not is_over:
    print_board()
    print "you can think"
    sleep(2)
    user_move(1)
    print who_is_won()
    computer_move(-1)
    print who_is_won()



