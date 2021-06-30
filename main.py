
import sys 
from game import *
from lexer import *
from parser import *

# to print to stderr
def print_to_stderr(*a):
    print(*a, file = sys.stderr)
    return


#returns string to be printed in stderr
def combine(Value,Names):
    s = ""
    for i in range(4):
        for j in range(4):
            s+=str(Value[i][j])
            s+=" "
            
    for i in range(4):
        for j in range(4):
            if len(Names[i][j]) != 0:
                s+=str(i+1)
                s+=","
                s+=str(j+1)
                a=0
                for name in Names[i][j]: 
                    if(a==0):
                        s+=name
                    else:
                        s+=','
                        s+=name
                    a=a+1
                s+=" "
    return s
 
if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    print("Hi, I am the 2048-game Engine.")
    print_to_stderr(combine(gamepanel.gridCell, gamepanel.gridVar))
    won = 0
    while (won!=1): 
        print('Please type a command.')
        text = input()
        if text=="EXIT" or text=="exit": # Type EXIT or exit to stop running in between
            print("EXITING")
            break
        
        try:
            won = parser.parse(lexer.tokenize(text))
        except:
            print("Sorry I don't understand that.")
            print_to_stderr("-1")
            continue
            
        if(won==1):
            print_to_stderr(combine(gamepanel.gridCell, gamepanel.gridVar))
            print("Game Won.... EXITING")
        if(won==-1):
            print_to_stderr("-1")
        if(won==0):
            print_to_stderr(combine(gamepanel.gridCell, gamepanel.gridVar))
