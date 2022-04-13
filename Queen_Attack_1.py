from pickle import FALSE, TRUE
   
# This function returns the possible numbers of attacks by Queen. 
# Number of 'obstacles' is there in Queen's possible attack. If so, break from that point.

# n : Size of chess board
# k : Number of obstacles
# r_q : Location of Queen in row
# c_q : Location of Queen in column
# obstacles : list of obstacle locations 
def queensAttack(n, k, r_q, c_q, obstacles):

    # Checks for valid Queen Location. If so, goes for inner loop. Else returns "Invalid Queen Location"
    if r_q <= n and c_q <= n: 
        
        # Initialize 'count' value as zero
        count = 0

        # left
        # This while loop checks whether there is a possible to move left. If so, increments 'count' value by 1
        # Else if obstacles found, removes that value from obstacles and breaks from that point.
        # This removal of value from obstacle, controls the excess time consumed by the program for the calculation occurs in rest of the sides. 
        new_limit = c_q - 1
        while TRUE:
            if new_limit > 0: 
                val = [r_q, new_limit]
                
                if val in obstacles:
                    obstacles.remove(val)
                    break
                else:
                    new_limit -= 1
                    count += 1

            else:
                break
            
        # right of the queen
        # This while loop checks whether there is a possible to move right. If so, increments 'count' value by 1
        # Else if obstacles found, removes that value from obstacles and breaks from that point.
        # This removal of value from obstacle, controls the excess time consumed by the program for the calculation occurs in rest of the sides.
        new_limit = c_q + 1
        while TRUE:
            if new_limit <= n:
                val = [r_q, new_limit]
                
                if val in obstacles:
                    obstacles.remove(val)
                    break
                else:
                    new_limit += 1
                    count += 1
            
            else:
                break
           
        
        # top of queen
        # This while loop checks whether there is a possible to move top. If so, increments 'count' value by 1
        # Else if obstacles found, removes that value from obstacles and breaks from that point.
        # This removal of value from obstacle, controls the excess time consumed by the program for the calculation occurs in rest of the sides.
        new_limit = r_q - 1
        while TRUE:
            if new_limit > 0: 
                val = [new_limit, c_q]
                
                if val in obstacles:
                    obstacles.remove(val)
                    break
                else:
                    new_limit -= 1
                    count += 1

            else:
                break
            

        # down of queen
        # This while loop checks whether there is a possible to move down. If so, increments 'count' value by 1
        # Else if obstacles found, removes that value from obstacles and breaks from that point.
        # This removal of value from obstacle, controls the excess time consumed by the program for the calculation occurs in rest of the sides.
        new_limit = r_q + 1
        while TRUE:
            if new_limit <= n: 
                val = [new_limit, c_q]
                
                if val in obstacles:
                    obstacles.remove(val)
                    break
                else:
                    new_limit += 1
                    count += 1

            else:
                break
             
        # top left diagonal(primary diagonal - top)
        # This while loop checks whether there is a possible to top-left diagonal. If so, increments 'count' value by 1
        # Else if obstacles found, removes that value from obstacles and breaks from that point.
        # This removal of value from obstacle, controls the excess time consumed by the program for the calculation occurs in rest of the sides.
        new_limit_row = r_q - 1
        new_limit_column = c_q - 1
        while TRUE:
            if (new_limit_row > 0 and new_limit_column > 0):
                val = [new_limit_row, new_limit_column]
                if val in obstacles:
                    obstacles.remove(val)
                    break
                else:
                    new_limit_row -= 1
                    new_limit_column -= 1
                    count += 1
            else:
                break

        
        # bottom right diagonal(primary diagonal - bottom)
        # This while loop checks whether there is a possible to move bottom-right diagonal. If so, increments 'count' value by 1
        # Else if obstacles found, removes that value from obstacles and breaks from that point.
        # This removal of value from obstacle, controls the excess time consumed by the program for the calculation occurs in rest of the sides.
        new_limit_row = r_q + 1
        new_limit_column = c_q + 1
        while TRUE:
            if (new_limit_row <= n and new_limit_column <= n):
                val = [new_limit_row, new_limit_column]
                if val in obstacles:
                    obstacles.remove(val)
                    break
                else:
                    new_limit_row += 1
                    new_limit_column += 1
                    count += 1
            else:
                break
          
        # top right(secondary diagonal - top)
        # This while loop checks whether there is a possible to move top-right diagonal. If so, increments 'count' value by 1
        # Else if obstacles found, removes that value from obstacles and breaks from that point.
        # This removal of value from obstacle, controls the excess time consumed by the program for the calculation occurs in rest of the sides.
        new_limit_row = r_q - 1
        new_limit_column = c_q + 1
        while TRUE:
            if (new_limit_row > 0 and new_limit_column <= n):
                val = [new_limit_row, new_limit_column]
                if val in obstacles:
                    obstacles.remove(val)
                    break
                else:
                    new_limit_row -= 1
                    new_limit_column += 1
                    count += 1
            else:
                break

         
        # bottom left(secondary diagonal - bottom)
        # This while loop checks whether there is a possible to move bottom-left diagonal. If so, increments 'count' value by 1
        # Else if obstacles found, removes that value from obstacles and breaks from that point.
        # This removal of value from obstacle, controls the excess time consumed by the program for the calculation occurs in rest of the sides.
        new_limit_row = r_q + 1
        new_limit_column = c_q - 1
        while TRUE:
            if (new_limit_row <= n and new_limit_column > 0 ):
                val = [new_limit_row, new_limit_column]
                if val in obstacles:
                    obstacles.remove(val)
                    break
                else:
                    new_limit_row += 1
                    new_limit_column -= 1
                    count += 1
            else:
                break
         
    else:
        print("Invalid Queen Location")

    print(count)
if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()
    # n - no of rows and columns in the chess board
    
    n = int(first_multiple_input[0])

    # k = number of obstacles
    k = int(first_multiple_input[1])

    # To get location of Queen in chess board
    second_multiple_input = input().rstrip().split()

    # Row position of Queen
    r_q = int(second_multiple_input[0])

    # column position of Queen
    c_q = int(second_multiple_input[1])

    
    obstacles = []
    # gets 'k' number of obstacle locations in the chess board and stored in the list 'obstacles'
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    # Just cal the function 'queenAttack' and pass the required arguments
    result = queensAttack(n, k, r_q, c_q, obstacles)

    
