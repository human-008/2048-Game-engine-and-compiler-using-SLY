from sly import Parser
from game import *
from lexer import *

#making game objects
gamepanel = Board()
game2048 = Game(gamepanel)
game2048.start()


class BasicParser(Parser):

   
    
        tokens = BasicLexer.tokens
        
        def error(self, token):
            '''
            Default error handling function.  This may be subclassed.
            Over ride the sly error handler.
            '''
            
            raise Exception #raising an exception to be caught by the error handler... It detects all commnads not in grammer

        def __init__(self):
            self.env = { }
            
        @_('')
        def statement(self, p):
            pass

        
        
  

        @_('OPERATION DIRECTION') # without fullstop
        def statement(self, p):
            print("You need to end a command with a full-stop.")
            return -1

        @_('OPERATION DIRECTION "."') # correct command
        def statement(self, p):
            print("Thanks,move done,random tile added.")
            game2048.link_keys(p[0], p[1])
            return 0


        @_('OPERATION_ERR DIRECTION_ERR "."')
        def statement(self, p):
            print("Syntax Error")
            return -1

        @_('OPERATION_ERR DIRECTION "."')
        def statement(self, p):
            print("Syntax Error")
            return -1

        @_('OPERATION DIRECTION_ERR "."')
        def statement(self, p):
            print("Syntax Error")
            return -1

        @_('ASSIGN NUMBER TO NUMBER "," NUMBER') # without fullstop
        def statement(self, p):
            print("You need to end a command with a full-stop.")
            return -1



        @_('ASSIGN NUMBER TO NUMBER "," NUMBER "."') # correct command
        def statement(self, p):
            if(int(p[3])>=1 and int(p[3])<=4 and int(p[5])>=1 and int(p[5])<=4):
                print("Thanks, assignment done.")
                gamepanel.valueAssign(int(p[1]), int(p[3])-1, int(p[5])-1)

                if(int(p[1])==2048):
                    return 1
                else:
                    return 0
            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1



        @_('ASSIGN NUMBER TO_ERR NUMBER "," NUMBER "."')
        def statement(self, p):
            print("Syntax Error")
            return -1

        @_('ASSIGN_ERR NUMBER TO NUMBER "," NUMBER "."')
        def statement(self, p):
            print("Syntax Error")
            return -1
        
        @_('ASSIGN_ERR NUMBER TO_ERR NUMBER "," NUMBER "."')
        def statement(self, p):
            print("Syntax Error")
            return -1


        @_('NUMBER "," NUMBER IS VAR') # without fullstop
        def statement(self, p):
            print("You need to end a command with a full-stop.")
            return -1

        @_('NUMBER "," NUMBER IS OPERATION "."')
        def statement(self, p):
            print("NO, a keyword cannot be a variable name")
            return -1


        @_('NUMBER "," NUMBER IS DIRECTION "."')
        def statement(self, p):
            print("NO, a keyword cannot be a variable name")
            return -1


        @_('NUMBER "," NUMBER IS ASSIGN "."')
        def statement(self, p):
            print("NO, a keyword cannot be a variable name")
            return -1


        @_('NUMBER "," NUMBER IS TO "."')
        def statement(self, p):
            print("NO, a keyword cannot be a variable name")
            return -1


        @_('NUMBER "," NUMBER IS IS "."')
        def statement(self, p):
            print("NO, a keyword cannot be a variable name")
            return -1



        @_('NUMBER "," NUMBER IS VALUE "."')
        def statement(self, p):
            print("NO, a keyword cannot be a variable name")
            return -1

        @_('NUMBER "," NUMBER IS IN "."')
        def statement(self, p):
            print("NO, a keyword cannot be a variable name")
            return -1

        @_('NUMBER "," NUMBER IS OPERATION_ERR "."') # correct command
        def statement(self, p):
            if(int(p[0])>=1 and int(p[0])<=4 and int(p[2])>=1 and int(p[2])<=4):

                    flag=gamepanel.nameAssign(p[4],int(p[0])-1,int(p[2])-1)
                    if flag==1:

                        print("Thanks, naming done.")

                        return 0
                    elif flag==0:
                        print("Sorry the tile mentioned is empty and cannot be named")
                        return -1
                    elif flag==-1:
                        print("Sorry the name mentioned already exists")
                        return -1


            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1




        @_('NUMBER "," NUMBER IS DIRECTION_ERR "."') # correct command
        def statement(self, p):
            if(int(p[0])>=1 and int(p[0])<=4 and int(p[2])>=1 and int(p[2])<=4):

                    flag=gamepanel.nameAssign(p[4],int(p[0])-1,int(p[2])-1)
                    if flag==1:

                        print("Thanks, naming done.")

                        return 0
                    elif flag==0:
                        print("Sorry the tile mentioned is empty and cannot be named")
                        return -1
                    elif flag==-1:
                        print("Sorry the name mentioned already exists")
                        return -1


            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1


        @_('NUMBER "," NUMBER IS ASSIGN_ERR "."')# correct command
        def statement(self, p):
            if(int(p[0])>=1 and int(p[0])<=4 and int(p[2])>=1 and int(p[2])<=4):

                    flag=gamepanel.nameAssign(p[4],int(p[0])-1,int(p[2])-1)
                    if flag==1:

                        print("Thanks, naming done.")

                        return 0
                    elif flag==0:
                        print("Sorry the tile mentioned is empty and cannot be named")
                        return -1
                    elif flag==-1:
                        print("Sorry the name mentioned already exists")
                        return -1


            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1



        @_('NUMBER "," NUMBER IS TO_ERR "."')# correct command
        def statement(self, p):
            if(int(p[0])>=1 and int(p[0])<=4 and int(p[2])>=1 and int(p[2])<=4):

                    flag=gamepanel.nameAssign(p[4],int(p[0])-1,int(p[2])-1)
                    if flag==1:

                        print("Thanks, naming done.")

                        return 0
                    elif flag==0:
                        print("Sorry the tile mentioned is empty and cannot be named")
                        return -1
                    elif flag==-1:
                        print("Sorry the name mentioned already exists")
                        return -1


            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1



        @_('NUMBER "," NUMBER IS IS_ERR "."')# correct command
        def statement(self, p):
            if(int(p[0])>=1 and int(p[0])<=4 and int(p[2])>=1 and int(p[2])<=4):

                    flag=gamepanel.nameAssign(p[4],int(p[0])-1,int(p[2])-1)
                    if flag==1:

                        print("Thanks, naming done.")

                        return 0
                    elif flag==0:
                        print("Sorry the tile mentioned is empty and cannot be named")
                        return -1
                    elif flag==-1:
                        print("Sorry the name mentioned already exists")
                        return -1


            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1



        @_('NUMBER "," NUMBER IS VALUE_ERR "."')# correct command
        def statement(self, p):
            if(int(p[0])>=1 and int(p[0])<=4 and int(p[2])>=1 and int(p[2])<=4):

                    flag=gamepanel.nameAssign(p[4],int(p[0])-1,int(p[2])-1)
                    if flag==1:

                        print("Thanks, naming done.")

                        return 0
                    elif flag==0:
                        print("Sorry the tile mentioned is empty and cannot be named")
                        return -1
                    elif flag==-1:
                        print("Sorry the name mentioned already exists")
                        return -1


            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1



        @_('NUMBER "," NUMBER IS IN_ERR "."')# correct command
        def statement(self, p):
            if(int(p[0])>=1 and int(p[0])<=4 and int(p[2])>=1 and int(p[2])<=4):

                    flag=gamepanel.nameAssign(p[4],int(p[0])-1,int(p[2])-1)
                    if flag==1:

                        print("Thanks, naming done.")

                        return 0
                    elif flag==0:
                        print("Sorry the tile mentioned is empty and cannot be named")
                        return -1
                    elif flag==-1:
                        print("Sorry the name mentioned already exists")
                        return -1


            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1



        @_('NUMBER "," NUMBER IS VAR "."')# correct command
        def statement(self, p):
            if(int(p[0])>=1 and int(p[0])<=4 and int(p[2])>=1 and int(p[2])<=4):
                if p[4]=="VAR": # check for "VAR" keyword
                    print("NO, a keyword cannot be a variable name")
                    return -1 
                else:

                    flag=gamepanel.nameAssign(p[4],int(p[0])-1,int(p[2])-1)
                    if flag==1:

                        print("Thanks, naming done.")

                        return 0
                    elif flag==0:
                        print("Sorry the tile mentioned is empty and cannot be named")
                        return -1
                    elif flag==-1:
                        print("Sorry the name mentioned already exists")
                        return -1


            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1

        @_('NUMBER "," NUMBER IS_ERR VAR "."')
        def statement(self, p):
            print("Syntax Error")
            return -1



        @_('VALUE IN NUMBER "," NUMBER') # without fullstop
        def statement(self, p):
            print("You need to end a command with a full-stop.")
            return -1






        @_('VALUE IN NUMBER "," NUMBER "."') # correct command
        def statement(self, p):
            if(int(p[2])>=1 and int(p[2])<=4 and int(p[4])>=1 and int(p[4])<=4):
                print("Value is:", end=' ')
                gamepanel.valueIn(int(p[2])-1,int(p[4])-1)
                return 0
            else:
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                return -1

        @_('VALUE_ERR IN_ERR NUMBER "," NUMBER "."')
        def statement(self, p):
            print("Syntax Error")
            return -1

        @_('VALUE_ERR IN NUMBER "," NUMBER "."')
        def statement(self, p):
            print("Syntax Error")
            return -1

        @_('VALUE IN_ERR NUMBER "," NUMBER "."')
        def statement(self, p):
            print("Syntax Error")
            return -1
    
        
        
    

    
    