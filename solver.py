def check(sud,n,pos):
    #chech_row
    for i in range(0,9):
        if(sud[pos[0]][i]==n and sud[pos[0]][i]!=sud[pos[0]][pos[1]]):
            return False
    #check_column
    for i in range(0,9):
        if(sud[i][pos[1]]==n and sud[i][pos[1]]!=sud[pos[0]][pos[1]]):
            return False
    #check_box
    box_x=pos[0]//3
    box_y=pos[1]//3
    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if(sud[i][j]==n and sud[i][j]!=sud[pos[0]][pos[1]]):
                return False
    return True
def blank(sud):
    for i in range(0,9):
        for j in range (0,9):
            if(sud[i][j]==0):
                pos=(i,j)
                return pos
    return None

def solve(sud):
    empty=blank(sud)
    if not empty:
        return True
    else:
        row,col=empty
        for i in range(1,10):
            if(check(sud,i,empty)):
                sud[row][col]=i
                if(solve(sud)):
                    return True
                sud[row][col]=0
        return False
def display(sud):
    for i in range(0,9):
        if(i%3==0 and i!=0):
                print("--------------------")
        for j in range(0,9):
            if(j%3==0 and j!=0):
                print("|",end="")
            if(j==8):
                print(sud[i][j])
            else:
                print(str(sud[i][j])+" ",end='')