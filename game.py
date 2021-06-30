#2048 game design


import random
class Board:
    def __init__(self):
        self.n=4
        self.gridCell=[[0]*4 for i in range(4)] # has the tile values 
        self.gridVar=[[[]]*4 for i in range(4)] # has the tile names
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0
    
    def showGrid(self):
        print("_ _ _ _ _ _ _ _")
        for i in range(4):
            for j in range(4): 
                print(self.gridCell[i][j],end=' | ')
            print()
            print("_ _ _ _ _ _ _ _")
            print()
    
    
    
    
    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                self.gridVar[ind][i],self.gridVar[ind][j]=self.gridVar[ind][j],self.gridVar[ind][i]
                i+=1
                j-=1
                
    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]
        self.gridVar=[list(t)for t in zip(*self.gridVar)]
        
    def compressGrid(self):
        self.compress=False
        temp=[[0] *4 for i in range(4)]
        tempVar=[[[]]*4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.gridCell=temp
        for i in range(4):
            cnt=0
            for j in range(4):
                if len(self.gridVar[i][j])!=0: # its not empty
                    tempVar[i][cnt]=self.gridVar[i][j]
                    cnt+=1
        self.gridVar=tempVar
        
        
    def mergeGrid(self,option):
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    if option=="ADD":
                        self.gridCell[i][j]=self.gridCell[i][j]+self.gridCell[i][j]
                        self.gridVar[i][j]=self.gridVar[i][j]+self.gridVar[i][j+1] # merges the names of the variable
                    elif option=="MULTIPLY":
                        self.gridCell[i][j]=self.gridCell[i][j]*self.gridCell[i][j]
                        self.gridVar[i][j]=self.gridVar[i][j]+self.gridVar[i][j+1] # merges the names of the variable
                    elif option=="DIVIDE":
                        self.gridCell[i][j]=int(self.gridCell[i][j]/self.gridCell[i][j])
                        self.gridVar[i][j]=self.gridVar[i][j]+self.gridVar[i][j+1] # merges the names of the variable
                    elif option=="SUBTRACT":
                        self.gridCell[i][j]=self.gridCell[i][j]-self.gridCell[i][j]
                        self.gridVar[i][j]=[] # drops the names of the variable
                    
                    self.gridVar[i][j+1]=[]
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True
                    
    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]=2
    
    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True
        
        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False
    
                    
    def nameAssign(self,name,x,y):
        for i in range(4): # to check distinct name exists
            for j in range(4):
                for a in self.gridVar[i][j]:
                    if a==name:
                        return -1
        
        
        
        
        
        if self.gridCell[x][y]!=0:
            self.gridVar[x][y]=self.gridVar[x][y]+[name] #assign name to a tile
            return 1;
        elif self.gridCell[x][y]==0:
            return 0;
        
            
        
        
        
    def valueIn(self,x,y):
        print(self.gridCell[x][y])
        
    def valueAssign(self,val,x,y):
        self.gridCell[x][y]=val #assign value to a tile
        if val==0:
            self.gridVar[x][y]=[] #dropping the name of varianle if its tile value is made 0
        self.showGrid()
        
         
                    
                    
class Game:
    def __init__(self,gamepanel):
        self.gamepanel=gamepanel
        self.end=False
        self.won=False
        
    def showGrid(self):
        for i in range(4):
            for j in range(4): 
                print(self.gamepanel.gridCell[i][j],end=' | ')
            print()
            print("_ _ _ _ _ _ _ _")
            print()
    
    def start(self):
        self.gamepanel.random_cell()
        self.gamepanel.random_cell()
        print("Game started... This is the initial state.")
        self.showGrid()
        
    

      
    
            
    
    def link_keys(self,option,x): # to perform commands
        if self.end or self.won:
            return
        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False
        presed_key=x
        if presed_key=='UP':
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid(option)
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()
        elif presed_key=='DOWN':
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid(option)
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()
        elif presed_key=='LEFT':
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid(option)
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
        elif presed_key=='RIGHT':
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid(option)
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
        else:
            pass
        flag=0
        for i in range(4):
            for j in range(4):
                if(self.gamepanel.gridCell[i][j]==2048):
                    flag=1
                    break
        if(flag==1): #found 2048
            self.won=True
            print("won")
            return
        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j]==0:
                    flag=1
                    break
        if not (flag or self.gamepanel.can_merge()):
            self.end=True
            print("Over")
        if self.gamepanel.moved:
            self.gamepanel.random_cell()
        self.showGrid()
