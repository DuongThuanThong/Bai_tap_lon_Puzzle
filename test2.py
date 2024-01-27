import pygame #Khởi tạo thư viện game
import sys #Khởi tạo để dừng chương trình Python
import random #Tạo giá trị random
from setting import*
pygame.init()
#Kiểu chữ
FONT=pygame.font.Font(None,30)
FONTBUTTON=pygame.font.SysFont('Comic Sans MS',17)
FONTBUTTONLEVEL=pygame.font.SysFont('Comic Sans MS',35)
#Cài chiều cao và chiều rộng cho màn hình hiển thị game
DISPLAY = pygame. display.set_mode((WINDOW_W, WINDOW_H))
autoRect = None
autoRun = None
buttonLevel = None
global arr
arr=[]
#Tạo nút chế độ
def makeButtonLevel(text, color, bgcolor, top , left):
     buttonSurf = FONTBUTTONLEVEL.render(text, True, color, bgcolor)
     buttonRect = buttonSurf.get_rect()
     buttonRect.topleft = (top,left)
     DISPLAY.blit(buttonSurf,buttonRect)
     return (buttonRect)
def main_menu():
    arr.clear()
    while True:
        DISPLAY.fill((0,0,0))
        global BOARD_H , BOARD_W
        # Khởi tạo phông chữ
        font = pygame.font.SysFont("Comic Sans MS", 90)
        text = "Game Puzzle"
        textSurf = font.render(text, True, (255,255,255))
        DISPLAY.blit(textSurf, (80, 20))
        font = pygame.font.SysFont("arial.ttf", 50)
        text = "SELECT LEVEL GAME:"
        textSurf = font.render(text, True, (255,255,255))
        DISPLAY.blit(textSurf, (140, 170))
        easyButton= makeButtonLevel(" 3X3(Easy) ", (0, 0, 0), (255, 255, 255), WINDOW_W  -425 , WINDOW_H -260)    
        mediumButton= makeButtonLevel(" 4x4(Medium) ", (0, 0, 0), (255, 255, 255), WINDOW_W  -449.5 , WINDOW_H -190)
        hardButton= makeButtonLevel(" 5X5(Hard) ", (0, 0, 0), (255, 255, 255), WINDOW_W  -425.5, WINDOW_H -120)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if easyButton.collidepoint(event.pos):
                    BOARD_H=3
                    BOARD_W= 3  
                    main()
                elif mediumButton.collidepoint(event.pos):
                    BOARD_H=4
                    BOARD_W=4   
                    main()
                elif hardButton.collidepoint(event.pos):
                    BOARD_H=5
                    BOARD_W=5
                    main()
def main():
#----------Bắt đầu hàm main-----------------------------------------
    board = frameBoard() 
    #Đặt tên cho game
    DISPLAY.fill((0,0,0))
    fontFun = pygame.font.SysFont("Comic Sans MS", 20)
    textFun = "Thay cho tui em qua mon di :) "
    textSurf = fontFun.render(textFun, True, (255,255,255))
    global autoRect,autoRun,buttonLevel 
    DISPLAY.blit(textSurf, (180 ,450))
    fontFunN = pygame.font.SysFont("Comic Sans MS", 30)
    textFunN = "Happy New Year 2024"
    textSurfN = fontFunN.render(textFunN, True, (255,255,255))
    global autoRect,autoRun,buttonLevel 
    DISPLAY.blit(textSurfN, (170 ,20))      
    pygame.display.set_caption('Game Puzzle')
    DefRandomMove(board)  
     
    while True:
        #Tắt trò chơi
        drawBoard(board)
        offGameandMove(board)     
        #Tạo điều khiên cho trò chơi
        pygame.display.update()

#----------Kết thúc hàm main-----------------------------------------
def offGameandMove(board):
    global BOARD_W,BOARD_H
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                #TẠI SAO PHẢI ĐỂ MOVEITEMS NÀY GAME VÌ GIÚP Cải thiện code vì nếu tách 2 phần ra riêng sẽ có 2 cái for event in pygame.event.get bị trễ
                #vì phải dò cái đầu tiên coi có phải đang nhấn x hay không
            elif event.type == pygame.MOUSEBUTTONUP:
                #Xác định vị trí click của con trỏ tại các ô khác trừ ô đen
                pointX=None
                pointY=None
                for tileX in range (BOARD_W):
                    for tileY in range(BOARD_H):
                        left,top = XYTile(tileX,tileY)
                        tileRect = pygame.Rect(left,top,TILESIZE,TILESIZE)
                        if tileRect.collidepoint(event.pos[0],event.pos[1]):
                            pointX=tileX
                            pointY=tileY
                            

                #Tìm vị trí của ô đen
                tilexNone, tileyNone = findBlackTile(board)
                #Cho các ô di chuyển khi bấm
                if pointX==tilexNone-1 and pointY==tileyNone:#right
                    arr.append("right")
                    print ("chuyen right")
                    board[tilexNone][tileyNone], board[pointX][pointY] = board[pointX][pointY], board[tilexNone][tileyNone]
                    drawBoard(board)
                elif pointX==tilexNone+1 and pointY==tileyNone:#left
                    arr.append("left")
                    print ("chuyen left")
                    board[tilexNone][tileyNone], board[pointX][pointY] = board[pointX][pointY], board[tilexNone][tileyNone]
                    drawBoard(board)
                elif pointX==tilexNone and pointY==tileyNone+1:#up
                    arr.append("up")
                    print ("chuyen up")
                    board[tilexNone][tileyNone], board[pointX][pointY] = board[pointX][pointY], board[tilexNone][tileyNone]
                    drawBoard(board)
                elif pointX==tilexNone and pointY==tileyNone-1:#down
                    arr.append ("down")
                    print ("chuyen down")
                    board[tilexNone][tileyNone], board[pointX][pointY] = board[pointX][pointY], board[tilexNone][tileyNone]
                    drawBoard(board)
                
                elif autoRect.collidepoint(event.pos):  # Nhấn vào nút Auto Random
                    DefRandomMove(board)
                elif autoRun.collidepoint(event.pos):
                    arr.reverse()
                    for move in arr:
                        if move == "down":
                             move = "up"
                        elif move == "up":
                             move = "down"
                        elif move == "left":
                             move = "right"
                        elif move == "right":
                             move = "left"
                        moveTilex(move, board)
                    arr.clear()
                elif buttonLevel.collidepoint(event.pos):
                    main_menu()
    
#Tạo khung và gán các giá trị tương ứng vào các ô.   
def frameBoard():
    number=1
    board = []
    for column in range (BOARD_W):
        columns=[]
        for row in range (BOARD_H):
            columns.append(number)
            number += BOARD_H
        board.append (columns)
        number-= ((BOARD_W) * (BOARD_H-1) + (BOARD_W) -1)#Công thức lụm nhặt tính gán giá trị number vào danh sách.
    board[BOARD_W-1][BOARD_H-1] = None
    return board 
#Xác định vị trí x và y của các ô nhỏ
def XYTile(tileX, tileY):
    left = ((WINDOW_W - (TILESIZE*BOARD_W+(BOARD_W-1)))/2)+ (tileX*TILESIZE) +  (tileX-1)
    top = ((WINDOW_H - (TILESIZE*BOARD_H+(BOARD_H-1)))/2) + (tileY*TILESIZE) + (tileY-1)
    return (left,top)
#Vẽ từng ô nhỏ
def drawTile(tileX, tileY, number, X=0 , Y=0 ):
    left, top = XYTile(tileX,tileY)
    pygame.draw.rect(DISPLAY,TILECOLOR,((left+ X),(top+Y),TILESIZE,TILESIZE) )
    textSurf= FONT.render(str(number),True,TEXTCOLOR)
    text=textSurf.get_rect()
    text.center = left + int(TILESIZE/2) + X, top + int (TILESIZE/2)+Y
    DISPLAY.blit(textSurf,text)
# Tìm kiếm ô đen 
def findBlackTile(board):
    for tileX in range (BOARD_W):
        for tileY in range(BOARD_H):
            if board [tileX][tileY] == None:
                tileXNone= tileX
                tileYNone= tileY
    return tileXNone, tileYNone
#Vẽ cái bảng 
def drawBoard (board):
    for tileX in range(len(board)):#Đếm số hàng của bảng đó
        for tileY in range(len(board[0])):#Đếm số ô của hàng đó
            if board[tileX][tileY]:
                drawTile(tileX,tileY, board[tileX][tileY])
            else :
                left, top = XYTile(tileX,tileY)
                pygame.draw.rect(DISPLAY,(0,0,0),((left),(top),TILESIZE,TILESIZE))
    top,left= XYTile(0,0)
    width = BOARD_W * TILESIZE
    heigh =BOARD_H * TILESIZE
    pygame.draw.rect(DISPLAY, BODERCOLOR, (left+80, top-80, width +6, heigh +6),5)
    makeButtonAutoRandom(TOPAUTOBUTTON+25, LEFTAUTOBUTTON)
    makeButtonAutoRun(TOPAUTOBUTTON+20,LEFTAUTOBUTTON+40)
    makeButtonSelectLevel(TOPAUTOBUTTON+10, LEFTAUTOBUTTON+80)
# Vẽ nút chọn cấp độ
def makeButtonSelectLevel( top, left ):
    global buttonLevel
    autoSurfLevel=FONTBUTTON.render(TEXTLEVEL,True,TEXTCOLORBUTTON,BGCOLORBUTTON)
    buttonLevel = autoSurfLevel.get_rect(topleft=(top, left))
    DISPLAY.blit(autoSurfLevel, buttonLevel)
# Vẽ nút autoRun
def makeButtonAutoRun ( top, left ):
    global autoRun
    autoSurfRun=FONTBUTTON.render(TEXTAUTORUN,True,TEXTCOLORBUTTON,BGCOLORBUTTON)
    autoRun = autoSurfRun.get_rect(topleft=(top, left))
    DISPLAY.blit(autoSurfRun, autoRun)
# Vẽ nút random
def makeButtonAutoRandom ( top, left ):
    global autoRect
    autoSurf=FONTBUTTON.render(TEXTAUTO,True,TEXTCOLORBUTTON,BGCOLORBUTTON)
    autoRect = autoSurf.get_rect(topleft=(top, left))
    DISPLAY.blit(autoSurf, autoRect)
# Tạo chế độ autoradom để xáo trộn
def DefRandomMove(board):
    direction = ['left','down','right','up']
    arrMove = []
     
    for i in range (150):#Cho vòng lặp chạy từ random từ 0 đến 100 
        tilexNone, tileyNone=findBlackTile(board)
        directionMove=(random.choice(direction))
        if ( directionMove == 'left' and tilexNone != BOARD_W-1):
            arr.append(directionMove)
            board[tilexNone][tileyNone], board[tilexNone+1][tileyNone] = board[tilexNone+1][tileyNone], board[tilexNone][tileyNone]
        elif (directionMove == 'right' and tilexNone !=0):
            arr.append(directionMove)
            board[tilexNone][tileyNone], board[tilexNone-1][tileyNone] = board[tilexNone-1][tileyNone], board[tilexNone][tileyNone]
        elif (directionMove == 'down' and tileyNone !=0):
            arr.append(directionMove)
            board[tilexNone][tileyNone], board[tilexNone][tileyNone-1] = board[tilexNone][tileyNone-1], board[tilexNone][tileyNone]
        elif (directionMove == 'up' and tileyNone != BOARD_W-1 ):
            arr.append(directionMove)
            board[tilexNone][tileyNone], board[tilexNone][tileyNone+1] = board[tilexNone][tileyNone+1], board[tilexNone][tileyNone]
        drawBoard(board)
        pygame.time.wait(50)
        pygame.display.update()
def moveTilex (directionMove, board):
    tilexNone, tileyNone=findBlackTile(board) #Hàm này có tác dụng mỗi lần lặp sẽ tìm vị trí ô đen trong bảng
    if ( directionMove == 'left' and tilexNone != BOARD_W-1):
            board[tilexNone][tileyNone], board[tilexNone+1][tileyNone] = board[tilexNone+1][tileyNone], board[tilexNone][tileyNone]
    elif (directionMove == 'right' and  tilexNone !=0):
            board[tilexNone][tileyNone], board[tilexNone-1][tileyNone] = board[tilexNone-1][tileyNone], board[tilexNone][tileyNone]
    elif (directionMove == 'down' and  tileyNone !=0 ):
            board[tilexNone][tileyNone], board[tilexNone][tileyNone-1] = board[tilexNone][tileyNone-1], board[tilexNone][tileyNone]      
    elif (directionMove == 'up' and tileyNone != BOARD_W-1):
            board[tilexNone][tileyNone], board[tilexNone][tileyNone+1] = board[tilexNone][tileyNone+1], board[tilexNone][tileyNone]
    drawBoard(board)
    pygame.time.wait(50)
    pygame.display.update()
    
if __name__ == '__main__':
    main_menu()