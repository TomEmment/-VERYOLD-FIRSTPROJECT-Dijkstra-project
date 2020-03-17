### set up ###
import pygame, math, sys, random 
import sqlite3 as lite
from pygame.locals import *
pygame.init()

### Data base ###
TAB = lite.connect("Maps.db")

with TAB:
    C = TAB.cursor()

    ### Maps ###
#    C.execute("""CREATE TABLE Map(
#                Map_Name text,
#                Start text,
#                End text,
#                TotalDistance integer
#                )""") 
#    ### Map_Draw ###
#    C.execute("""CREATE TABLE Maps_Draw(
#                Map_Name text,
#                Type integer,
#                PosX1 integer,
#                PosY1 integer,
#                PosX2 integer,
#                PosY2 integer,
#                Lable text
#                )""")
#
#    ### Map_Matrix ###
#    C.execute("""CREATE TABLE Map_Matrix(
#                Map_Name text,
#                Start text,
#                End text,
#                Distance integer
#                )""")
#C.execute("INSERT INTO Map VALUES ('Example','Example','Example','0')")
#C.execute("INSERT INTO Map VALUES ('Example1','Example1','Example1','0')")

TAB.commit()


### globals ###
global Current_Point
global Current_Line
global Map_Name_Current
global Start_Point
global End_Point
global Points
global Lines
global Font
global Letter_Start
global Letter_End
global Preload
global Line_Ready

### Map_Name ###
print ("Please choose a file to edit by typing its name from the list below or create a new one by typing in a new file name")
Maps = C.execute("SELECT Map_Name FROM Map").fetchall()
print(Maps)
Map_Name_Current = input("")
Step = 0
In = 0
for x in Maps:
    Current = Maps[Step][0]
    Step = Step + 1
    if Current == Map_Name_Current:
        print("Map loaded")
        In = 1
        Preload = True
if In == 0:
    print("Map Added")
    C.execute("INSERT INTO Map VALUES (?,?,?,?)",(Map_Name_Current,"-","-",0))
    Preload = False


### Images ###
Middle_Line = pygame.image.load("Middle_line.png")
Start_Point_Image = pygame.image.load("Start_Point.png")
End_Point_Image = pygame.image.load("End_Point.png")
White_Fill = pygame.image.load("Text_box_fill.png")
Distance_Calc = pygame.image.load("Calculate_Distance_Button.png")
Letter_A = pygame.image.load("Letter_A.png")
Letter_B = pygame.image.load("Letter_B.png")
Letter_C = pygame.image.load("Letter_C.png")
Letter_D = pygame.image.load("Letter_D.png")
Letter_E = pygame.image.load("Letter_E.png")
Letter_F = pygame.image.load("Letter_F.png")
Letter_G = pygame.image.load("Letter_G.png")
Letter_H = pygame.image.load("Letter_H.png")
Letter_I = pygame.image.load("Letter_I.png")
Letter_J = pygame.image.load("Letter_J.png")
Letter_K = pygame.image.load("Letter_K.png")
Letter_L = pygame.image.load("Letter_L.png")
Letter_M = pygame.image.load("Letter_M.png")
Letter_N = pygame.image.load("Letter_N.png")
Letter_O = pygame.image.load("Letter_O.png")
Letter_P = pygame.image.load("Letter_P.png")
Letter_Q = pygame.image.load("Letter_Q.png")
Letter_R = pygame.image.load("Letter_R.png")
Letter_S = pygame.image.load("Letter_S.png")
Letter_T = pygame.image.load("Letter_T.png")
Letter_U = pygame.image.load("Letter_U.png")
Letter_V = pygame.image.load("Letter_V.png")
Letter_W = pygame.image.load("Letter_W.png")
Letter_X = pygame.image.load("Letter_X.png")
Letter_Y = pygame.image.load("Letter_Y.png")
Letter_Z = pygame.image.load("Letter_Z.png")

### Lists and Dictionaries###
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Colour_Dictionary = {(255,0,0):"A",(254,0,0):"B",(253,0,0):"C",(252,0,0):"D",(251,0,0):"E",(250,0,0):"F",(249,0,0):"G",(248,0,0):"H",(247,0,0):"I",(246,0,0):"J",(245,0,0):"K",(244,0,0):"L",(243,0,0):"M",(242,0,0):"N",(241,0,0):"O",(240,0,0):"P",(239,0,0):"Q",(238,0,0):"R",(237,0,0):"S",(236,0,0):"T",(235,0,0):"U",(234,0,0):"V",(233,0,0):"W",(232,0,0):"X",(231,0,0):"Y",(230,0,0):"Z",}
Letter_Dictionary = {0:Letter_A,1:Letter_B,2:Letter_C,3:Letter_D,4:Letter_E,5:Letter_F,6:Letter_G,7:Letter_H,8:Letter_I,9:Letter_J,10:Letter_K,11:Letter_L,12:Letter_M,13:Letter_N,14:Letter_O,15:Letter_P,16:Letter_Q,17:Letter_R,18:Letter_S,19:Letter_T,20:Letter_U,21:Letter_V,22:Letter_W,23:Letter_X,24:Letter_Y,25:Letter_Z}
#Points ={"A":[],"B":{},"C":{},"D":{},"E":{},"F":{},"G":{},"H":{},"I":{},"J":{},"K":{},"L":{},"M":{},"N":{},"O":{},"P":{},"Q":{},"R":{},"S":{},"T":{},"U":{},"V":{},"W":{},"X":{},"Y":{},"Z":{},}
Lines = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[],16:[],17:[],18:[],19:[],20:[],21:[],22:[],23:[],24:[],25:[],26:[],27:[],28:[],29:[],30:[],31:[],32:[],33:[],34:[],35:[],36:[],37:[],38:[],39:[],40:[],41:[],42:[],43:[],44:[],45:[],46:[],47:[],48:[],49:[],50:[],51:[],52:[],53:[],54:[],55:[],56:[],57:[],58:[],59:[],60:[],61:[]}
Present = []

### Screen Set up###
Screen = pygame.display.set_mode((1200,900), 0, 32)
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
Screen.fill(WHITE)
Screen.blit(Middle_Line,(400,0))
Screen.blit(Start_Point_Image,(10,150))
Screen.blit(White_Fill,(100,130))
Screen.blit(End_Point_Image,(10,300))
Screen.blit(White_Fill,(100,280))
Screen.blit(Distance_Calc,(10,450))
Screen.blit(White_Fill,(100,600))

### Intials ###
Current_Point = 0
Current_Line = 0
Line_Ready = 0
font = pygame.font.SysFont('Calibri', 15, True, False)

def AddPoint(): # adds a point to the map 
    global Current_Point
    Point = Alphabet[Current_Point]
    C.execute("INSERT INTO Maps_Draw VALUES (?,?,?,?,?,?,?)",(Map_Name_Current, 0, X_Cordinate, Y_Cordinate, 0, 0, Point))
    TAB.commit()
    Current_Point = Current_Point + 1
    
def Start_Point_Sub(): # selects point to start at
    Done = 0
    global Chosen_Start
    global Start_Point
    global Letter_Start
    while Done == 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                whichKey = event.key
                pos = whichKey - 97
                if Current_Point >=pos:
                    Start_Point = chr(whichKey).upper()
                    C.execute("UPDATE Map SET Start=? WHERE Map_NAME=?",(Start_Point,Map_Name_Current))
                    TAB.commit()
                    Done = 1
                    Chosen_Start = 1
def End_Point_Sub(): # selects point to finish at
    Done = 0
    global Chosen_End
    global End_Point
    global Letter_End
    while Done == 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                whichKey = event.key
                pos = whichKey - 97
                if Current_Point >=pos:
                    End_Point = chr(whichKey).upper()
                    C.execute("UPDATE Map SET End=? WHERE Map_NAME=?",(End_Point,Map_Name_Current))
                    TAB.commit()
                    Done = 1
                    Chosen_End = 1
def Draw_Line(): # makes a connection between two points
    global Colour1
    global Colour2
    global BLACK_LINE
    global Current_Line
    global Line_Ready
    global X_Cordinate2
    global Y_Cordinate2
    global Present
    Done = 0
    while Done == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                MousePos2 = pygame.mouse.get_pos()
                X_Cordinate2 = MousePos2[0]
                Y_Cordinate2 = MousePos2[1]
                Colour2 = Screen.get_at((MousePos2[0], MousePos2[1]))
                Colour2 = Colour2[:-1]
                if Screen.get_at((MousePos2[0], MousePos2[1])) == WHITE:
                    Done = 1
                if Done == 0:
                    if Colour2[0] >= 220:
                        Check1 = Colour_Dictionary[Colour1]
                        Check2 = Colour_Dictionary[Colour2]
                        maps = C.execute("SELECT Distance FROM Map_Matrix WHERE Map_Name=? AND Start=? AND End=?",(Map_Name_Current, Check1, Check2)).fetchall()
                        Done = 1
                        if maps  == []:
                            maps = C.execute("SELECT Distance FROM Map_Matrix WHERE Map_Name=? AND Start=? AND End=?",(Map_Name_Current, Check2, Check1)).fetchall()
                            if maps  == []:
                                Done = 0
                        if Done == 0:
                            if Colour2[1] == 0:
                                if Colour1[0] != Colour2[0]:
                                    PointAdder()
                                    C.execute("INSERT INTO Maps_Draw VALUES (?,?,?,?,?,?,?)",(Map_Name_Current, 1, X_Cordinate, Y_Cordinate, X_Cordinate2, Y_Cordinate2, Colour1))
                                    C.execute("INSERT INTO Maps_Draw VALUES (?,?,?,?,?,?,?)",(Map_Name_Current, 1, X_Cordinate, Y_Cordinate, X_Cordinate2, Y_Cordinate2, Colour2))
                                    Present.append(X_Cordinate2)
                                    Present.append(Y_Cordinate2)
                                    C.execute("INSERT INTO Map_Matrix VALUES (?,?,?,?)",(Map_Name_Current, Colour1, Colour2, 0))
                                    TAB.commit()
                                    Line_Ready = 1
                                    Done = 1
                                    Current_Line = Current_Line +1
                                if Colour1[0] == Colour2[0]:
                                    Done = 1

def PointAdder(): # adds the points to list
    global Colour1
    global Colour2
    global Current_Line
    global Lines
    Colour1 = Colour_Dictionary[Colour1]
    Colour2 = Colour_Dictionary[Colour2]

    Lines[Current_Line] =[(Colour1),(Colour2),0]

def Distance(): # adds distance to conncections
    global Line_Ready
    global Lines
    Line = Colour1[0] -1
    print(Line)
    Number = []
    Done = 0
    while Done == 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                whichKey = event.key
                if whichKey == 13:
                    Done = 1
                else:
                    Distance = whichKey - 48
                    Number.append(Distance)
    Number = map(str,Number)
    Number = "".join(Number)
    Number = int(Number)
    Point1 = Lines[Line][0]
    Point2 = Lines[Line][1]
    C.execute("UPDATE Map_Matrix SET Distance=? WHERE Map_NAME=? AND Start=? AND End=?",(Number,Map_Name_Current,Point1,Point2))
    TAB.commit()
    for x in Lines:
        if Lines[x] != []:
            if Lines[x][0]== Point1:
                if Lines[x][1]== Point2:
                    Lines[x] = [(Point1),(Point2),(Number)]
            if Lines[x][0]== Point2:
                if Lines[x][1]== Point1:
                    Lines[x] = [(Point2),(Point1),(Number)]  
    Line_Ready = 1

def RemovePoint(): # remove a point and connected lines
    global X_Cordinate
    global Y_Cordinate
    global Current_Point
    global Lines
    Letter= Screen.get_at((X_Cordinate, Y_Cordinate))
    Letter = Letter[:-1]
    Letter = Colour_Dictionary[Letter]               
    Letter = ord(Letter)-65
    Current_Point = Current_Point - 1
    if Letter == Current_Point:
        for x in Lines:
            if Lines[x] != []:
                if Lines[x][0]== Letter:
                    Lines[x] = []
                if Lines[x][1]== Letter:
                    Lines[x] = [] 
        Point = Alphabet[Current_Point]
        C.execute("DELETE FROM Maps_Draw WHERE Map_Name=? AND Lable=?", (Map_Name_Current,Point))
        TAB.commit()
        Point = Point.upper()
        C.execute("DELETE FROM Map_Matrix WHERE Map_Name=? AND Start=?", (Map_Name_Current,Point))
        TAB.commit()
        C.execute("DELETE FROM Map_Matrix WHERE Map_Name=? AND End=?", (Map_Name_Current,Point))
        TAB.commit()   
    else:
        Current_Point = Current_Point + 1
        print("Can only delete most recent point")

def RemoveLine(): # removes lines
    global X_Cordinate
    global Y_Cordinate
    global Current_Line
    global Present
    Num = len(Present)-1
    X_Cord2 = Present[Num-1]
    Y_Cord2 = Present[Num]
    Letter= Screen.get_at((X_Cordinate, Y_Cordinate))
    Letter = Letter[0]
    Point = Letter
    if Current_Line == 1:
        Letter = Letter-1
    if Letter == Current_Line:
        Maps = C.execute("SELECT Lable FROM Maps_draw WHERE Map_Name=? AND PosX2=? AND PosY2=? ", (Map_Name_Current,X_Cord2,Y_Cord2)).fetchall()
        Present.pop()
        Present.pop()
        C.execute("DELETE FROM Map_Matrix WHERE Map_Name=? AND Start=? AND End=?", (Map_Name_Current,Maps[0][0],Maps[1][0]))
        TAB.commit()
        C.execute("DELETE FROM Map_Matrix WHERE Map_Name=? AND Start=? AND End=?", (Map_Name_Current,Maps[1][0],Maps[0][0]))
        TAB.commit()
        C.execute("DELETE FROM Maps_Draw WHERE Map_Name=? AND PosX2=? AND PosY2=? ", (Map_Name_Current,X_Cordinate2,Y_Cordinate2))
        TAB.commit()
    else:
        Current_Line = Current_Line+1
        print("Can only delete most recent Line")
    Current_Line = Current_Line-1

def Dijkstra(Start,End):
    global Lines
    Connections = []
    print(Start)
    print(End)
    Shortest_Distance = 99999999999999999999999999999999999999999999
    for x in Lines:
        if Lines[x] != []:
            if Lines[x][0]==Start:
                if Lines[x][1]==End:
                    Shortest_Distance = Lines[x][2]
            if Lines[x][0]==End:
                if Lines[x][1] == Start:
                    Shortest_Distance = Lines[x][2]
    
    print(Shortest_Distance)
    
def Check(): # check if all points are conncted and start and stop point and selcted
    global Checker
    global Map_Name_Current
    global Current_Point
    Checker = False
    Done = 0
    if Done == 0: # Start point selected
        Maps = C.execute("SELECT Start FROM Map WHERE Map_Name=?",(Map_Name_Current,)).fetchall()
        if Maps[0][0] == "-":
            Done = 1
    if Done == 0: # End point selected
        Maps = C.execute("SELECT End FROM Map WHERE Map_Name=?",(Map_Name_Current,)).fetchall()
        if Maps[0][0] == "-":
            Done = 1               
    if Done == 0: # each point is connected
        Number = Current_Point
        while Number >0:
            Number = Number -1
            Letter_Check = Number +65
            Letter_Check = chr(Letter_Check)
            Maps = C.execute("SELECT Start FROM Map_Matrix WHERE MAP_Name=? AND End=?",(Map_Name_Current,Letter_Check)).fetchall()
            if Maps == []:
                Maps = C.execute("SELECT End FROM Map_Matrix WHERE MAP_Name=? AND Start=?",(Map_Name_Current,Letter_Check)).fetchall()
                if Maps == []:
                    Done = 1
    if Done == 0: # each line has a distance
        Maps = C.execute("SELECT Distance FROM Map_Matrix WHERE MAP_Name=? AND Distance=?",(Map_Name_Current,0)).fetchall()
        if len(Maps) > 0:
            Done = 1
    if Done == 0:
        Checker = True

def Calc_Distance():
    Start = C.execute("SELECT Start FROM Map WHERE Map_Name=?",(Map_Name_Current,)).fetchall()
    Start = Start[0][0]
    End = C.execute("SELECT End FROM Map WHERE Map_Name=?",(Map_Name_Current,)).fetchall()
    End = End[0][0]
    Dijkstra(Start,End)
    
def Start():
    global Checker
    global X_Cordinate
    global Y_Cordinate
    global Chosen_Start
    global Chosen_End
    global Colour1
    global Preload
    Chosen_Start = 0
    Chosen_End = 0

    while 1 == 1:
        if Preload == True:
            Screen_Wrtie_Saved()
            Preload = False
        MousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (MousePos[0] in range (100,250)) and (MousePos[1] in range (130,230)):
                    Start_Point_Sub()
                    Screen_Write()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (MousePos[0] in range (100,250)) and (MousePos[1] in range (280,380)):
                    End_Point_Sub()
                    Screen_Write()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (MousePos[0] in range (10,250)) and (MousePos[1] in range (450,550)):
                    Check()
                    if Checker == True:
                        Calc_Distance()
                        Screen_Write()
                    if Checker == False:
                        print("Not all points are connected, not all points have distances or start and end points are not selected could not find da wae")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (MousePos[0] in range (400,1200)) and (MousePos[1] in range (0,900)):
                    X_Cordinate = MousePos[0]
                    Y_Cordinate = MousePos[1]
                    Colour1 = Screen.get_at((MousePos[0], MousePos[1]))
                    Colour1 = Colour1[:-1]
                    if Colour1[0] <=219:
                        if Colour1[0] != 0:
                            if event.button == 1:
                                Distance()
                                Screen_Write()
                            if event.button == 3:
                                RemoveLine()
                                Screen_Write()
                    if Colour1[0] >= 220:
                        if Colour1[1] == 0:
                            if event.button == 1:
                                Draw_Line()
                            if event.button == 3:
                                RemovePoint()
                            Screen_Write()
                    if Screen.get_at((MousePos[0], MousePos[1])) == WHITE:
                        if event.button == 1:
                            AddPoint()
                        Screen_Write()
        pygame.display.update()

def Screen_Wrtie_Saved():
    global Chosen_Start
    global Chosen_End
    global Line_Ready
    global Current_Line
    global Current_Point
    Screen.fill(WHITE)
    Screen.blit(Middle_Line,(400,0))
    Screen.blit(Start_Point_Image,(10,150))
    Screen.blit(White_Fill,(100,130))
    Screen.blit(End_Point_Image,(10,300))
    Screen.blit(White_Fill,(100,280))
    Screen.blit(Distance_Calc,(10,450))
    Screen.blit(White_Fill,(100,600))
    
    Maps = C.execute("SELECT Start FROM Map WHERE Map_Name=?",(Map_Name_Current,)).fetchall()

    Maps = Maps[0][0]
    if Maps != "-":
        Chosen_Start = 1
        Maps = ord(Maps)-65
        Letter_Start = Letter_Dictionary[Maps]
        Screen.blit(Letter_Start,(100,130))#Start Point

    Maps = C.execute("SELECT End FROM Map WHERE Map_Name=?",(Map_Name_Current,)).fetchall()
    Maps = Maps[0][0]
    if Maps != "-":
        Chosen_End = 1
        Maps = ord(Maps)-65
        Letter_End = Letter_Dictionary[Maps]
        Screen.blit(Letter_End,(100,280))#End point    
    
    Maps = C.execute("SELECT PosX1 FROM Maps_Draw WHERE MAP_Name=? AND Type=?",(Map_Name_Current,0)).fetchall()
    Amount = len(Maps)-1
    Current_Point = Amount + 1
    while Amount >= 0: #show points
        Point = C.execute("SELECT Lable FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,0)).fetchall()
        Point = Point[Amount][0]
        Point = ord(Point)-97
        CordX = C.execute("SELECT PosX1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,0)).fetchall()
        CordX = CordX[Amount][0]
        CordY = C.execute("SELECT PosY1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,0)).fetchall()
        CordY = CordY[Amount][0]
        Screen.blit(Letter_Dictionary[Point],(CordX-20,CordY-20))
        RED1 = (255-Amount,0,0)
        pygame.draw.circle(Screen,RED1,(CordX,CordY),10)
        pygame.display.update()
        Amount = Amount -1
        
    Maps = C.execute("SELECT PosX1 FROM Maps_Draw WHERE MAP_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
    Amount = len(Maps)-1
    Current_Line_Colour = Amount-1
    Current_Line_Colour//2#show lines
    while Amount >= 0:
        CordX1 = C.execute("SELECT PosX1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
        CordX1 = CordX1[Amount][0]
        CordY1 = C.execute("SELECT PosY1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
        CordY1 = CordY1[Amount][0]
        CordX2 = C.execute("SELECT PosX2 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
        CordX2 = CordX2[Amount][0]
        CordY2 = C.execute("SELECT PosY2 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
        CordY2 = CordY2[Amount][0]
        Amount = Amount -2
        BLACK_LINE = (1+Current_Line_Colour,0,0)
        pygame.draw.line(Screen,BLACK_LINE,(CordX1,CordY1), (CordX2,CordY2), 5)
        Current_Line_Colour = Current_Line_Colour-1

        
    Maps = C.execute("SELECT Start FROM Map_Matrix WHERE MAP_Name=?",(Map_Name_Current,)).fetchall()
    Amount = len(Maps)-1
    Turner = 0
    Adder = 0
    Line_Holder = 0
    while Amount >= 0:#show distances
        Line_Ready= 1
        Point1 = C.execute("SELECT Start FROM Map_Matrix WHERE MAP_Name=?",(Map_Name_Current,)).fetchall()
        Point1 = Point1[Amount][0]
        Point2 = C.execute("SELECT End FROM Map_Matrix WHERE MAP_Name=?",(Map_Name_Current,)).fetchall()
        Point2 = Point2[Amount][0]
        CordX1 = C.execute("SELECT PosX1 FROM Maps_Draw WHERE Map_Name=? AND TYPE=?",(Map_Name_Current,1)).fetchall()
        CordX1 = CordX1[Turner+Adder][0]
        CordY1 = C.execute("SELECT PosY1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1,)).fetchall()
        CordY1 = CordY1[Turner+Adder][0]
        CordX2 = C.execute("SELECT PosX2 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1,)).fetchall()
        CordX2 = CordX2[Turner+Adder][0]
        CordY2 = C.execute("SELECT PosY2 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1,)).fetchall()
        CordY2 = CordY2[Turner+Adder][0]
        MidX = (CordX1+CordX2)//2
        MidY = (CordY1+CordY2)//2
        Number = C.execute("SELECT Distance FROM Map_Matrix WHERE MAP_Name=?",(Map_Name_Current,)).fetchall()
        Number = Number[Turner][0]
        Number = str(Number)
        text = font.render(Number, True, BLACK)
        Screen.blit(text,(MidX-20,MidY-20))
        Amount = Amount - 1
        Turner = Turner + 1
        Adder =Adder + 1
        Lines[Line_Holder] = [(Point1),(Point2),(Number)]
        Line_Holder = Line_Holder+1
        Current_Line= Current_Line +1
    pygame.display.update()
    
def Screen_Write():
    global Current_Point
    global Current_Line
    global Line_Ready
    global Chosen_Start
    global Chosen_End
    Screen.fill(WHITE)
    Screen.blit(Middle_Line,(400,0))
    Screen.blit(Start_Point_Image,(10,150))
    Screen.blit(White_Fill,(100,130))
    Screen.blit(End_Point_Image,(10,300))
    Screen.blit(White_Fill,(100,280))
    Screen.blit(Distance_Calc,(10,450))
    Screen.blit(White_Fill,(100,600))
    
    if Chosen_Start == 1:
        Maps = C.execute("SELECT Start FROM Map WHERE Map_Name=?",(Map_Name_Current,)).fetchall()
        Maps = Maps[0][0]
        Maps = ord(Maps)-65
        Letter_Start = Letter_Dictionary[Maps]
        Screen.blit(Letter_Start,(100,130))#Start Point
        
    if Chosen_End == 1:
        Maps = C.execute("SELECT End FROM Map WHERE Map_Name=?",(Map_Name_Current,)).fetchall()
        Maps = Maps[0][0]
        Maps = ord(Maps)-65
        Letter_End = Letter_Dictionary[Maps]
        Screen.blit(Letter_End,(100,280))#End point

    if Current_Point > 0:
        Maps = C.execute("SELECT PosX1 FROM Maps_Draw WHERE MAP_Name=? AND Type=?",(Map_Name_Current,0)).fetchall()
        Amount = len(Maps)-1
        while Amount >= 0: # show points
            Point = C.execute("SELECT Lable FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,0)).fetchall()
            Point = Point[Amount][0]
            Point = ord(Point)-97
            CordX = C.execute("SELECT PosX1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,0)).fetchall()
            CordX = CordX[Amount][0]
            CordY = C.execute("SELECT PosY1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,0)).fetchall()
            CordY = CordY[Amount][0]
            Screen.blit(Letter_Dictionary[Point],(CordX-20,CordY-20))
            RED1 = (255-Amount,0,0)
            pygame.draw.circle(Screen,RED1,(CordX,CordY),10)
            Amount = Amount -1
            
    if Current_Line > 0:
        Maps = C.execute("SELECT PosX1 FROM Maps_Draw WHERE MAP_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
        Amount = len(Maps)-1
        Current_Line_Colour = 1
        if Amount > 1: # show lines
            Current_Line_Colour = Amount-1
            Current_Line_Colour = Current_Line_Colour//2
        while Amount >= 0:
            CordX1 = C.execute("SELECT PosX1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
            CordX1 = CordX1[Amount][0]
            CordY1 = C.execute("SELECT PosY1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
            CordY1 = CordY1[Amount][0]
            CordX2 = C.execute("SELECT PosX2 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
            CordX2 = CordX2[Amount][0]
            CordY2 = C.execute("SELECT PosY2 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1)).fetchall()
            CordY2 = CordY2[Amount][0]
            Amount = Amount -2
            Colour1 = Screen.get_at((CordX1, CordY1))
            Colour2 = Screen.get_at((CordX2, CordY2))
            if Colour1[0] >= 220:
                if Colour1[1] == 0:
                    if Colour2[0] >= 220:
                        if Colour2[1] == 0:
                            BLACK_LINE = (1+Current_Line_Colour,0,0)
                            pygame.draw.line(Screen,BLACK_LINE,(CordX1,CordY1), (CordX2,CordY2), 5)
                            Current_Line_Colour = Current_Line_Colour-1

            
    if Line_Ready == 1:
        Maps = C.execute("SELECT Start FROM Map_Matrix WHERE MAP_Name=?",(Map_Name_Current,)).fetchall()
        Amount = len(Maps)-1
        Turner = 0
        Adder = 0
        while Amount >= 0:# show distances
            Point1 = C.execute("SELECT Start FROM Map_Matrix WHERE MAP_Name=?",(Map_Name_Current,)).fetchall()
            Point1 = Point1[Amount][0]
            Point2 = C.execute("SELECT End FROM Map_Matrix WHERE MAP_Name=?",(Map_Name_Current,)).fetchall()
            Point2 = Point2[Amount][0]
            CordX1 = C.execute("SELECT PosX1 FROM Maps_Draw WHERE Map_Name=? AND TYPE=?",(Map_Name_Current,1)).fetchall()
            CordX1 = CordX1[Turner+Adder][0]
            CordY1 = C.execute("SELECT PosY1 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1,)).fetchall()
            CordY1 = CordY1[Turner+Adder][0]
            CordX2 = C.execute("SELECT PosX2 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1,)).fetchall()
            CordX2 = CordX2[Turner+Adder][0]
            CordY2 = C.execute("SELECT PosY2 FROM Maps_Draw WHERE Map_Name=? AND Type=?",(Map_Name_Current,1,)).fetchall()
            CordY2 = CordY2[Turner+Adder][0]
            MidX = (CordX1+CordX2)//2
            MidY = (CordY1+CordY2)//2
            Number = C.execute("SELECT Distance FROM Map_Matrix WHERE MAP_Name=?",(Map_Name_Current,)).fetchall()
            Number = Number[Turner][0]
            Number = str(Number)
            text = font.render(Number, True, BLACK)
            Screen.blit(text,(MidX-20,MidY-20))
            Amount = Amount - 1
            Turner = Turner + 1
            Adder =Adder + 1
    pygame.display.update()          
            


if __name__ == "__main__": # start code
    Start() 



