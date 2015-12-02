from graphics import *
win = GraphWin("TIC TAC TOE", 500,200)

"""Starting Box without anything"""

def EmptyBox():
    line1 = Line(Point(60,0),Point(60,200))
    line1.setOutline("red")
    line1.draw(win)
    line2 = Line(Point(0,67), Point(200,67))
    line2.setOutline("red")
    line2.draw(win)
    line3 = Line(Point(0,134), Point(200,134))
    line3.setOutline("red")
    line3.draw(win)
    line4 = Line(Point(140, 0), Point(140, 200))
    line4.setOutline("red")
    line4.draw(win)
    a = Text(Point(53,60), "1")
    a.setSize(7)
    a.setOutline("blue")
    a.draw(win)
    b = Text(Point(133,60), "2")
    b.setSize(7)
    b.setOutline("blue")
    b.draw(win)
    c = Text(Point(193,60), "3")
    c.setSize(7)
    c.setOutline("blue")
    c.draw(win)
    d = Text(Point(54,127), "4")
    d.setSize(7)
    d.setOutline("blue")
    d.draw(win)
    e = Text(Point(133,127), "5")
    e.setSize(7)
    e.setOutline("blue")
    e.draw(win)
    f = Text(Point(193,127), "6")
    f.setSize(7)
    f.setOutline("blue")
    f.draw(win)
    g = Text(Point(54,197), "7")
    g.setSize(7)
    g.setOutline("blue")
    g.draw(win)
    h = Text(Point(133,197), "8")
    h.setSize(7)
    h.setOutline("blue")
    h.draw(win)
    i = Text(Point(193,197), "9")
    i.setSize(7)
    i.setOutline("blue")
    i.draw(win)

""" O's and X's """

"""First row"""
def BoxAx():
    line1 = Line(Point(5,5), Point(50,50))
    line1.draw(win)
    line2 = Line(Point(50,5), Point(5, 50))
    line2.draw(win)
def BoxAo():
    circle = Circle(Point(32,30),20)
    circle.draw(win)
def BoxBx():
    line1 = Line(Point(65,5), Point(135,50))
    line1.draw(win)
    line2 = Line(Point(135,5), Point(65, 50))
    line2.draw(win)
def BoxBo():
    circle = Circle(Point(100,30),20)
    circle.draw(win)
def BoxCx():
    line1 = Line(Point(145,5), Point(195,65))
    line1.draw(win)
    line2 = Line(Point(195,5), Point(145, 65))
    line2.draw(win)
def BoxCo():
    circle = Circle(Point(170,35),23)
    circle.draw(win)

"""Second Row"""
def BoxDx():
    line1 = Line(Point(5,70), Point(50,130))
    line1.draw(win)
    line2 = Line(Point(50,70), Point(5, 130))
    line2.draw(win)
def BoxDo():
    circle = Circle(Point(32,100),23)
    circle.draw(win)
def BoxEx():
    line1 = Line(Point(65,70), Point(135,130))
    line1.draw(win)
    line2 = Line(Point(135,70), Point(65, 130))
    line2.draw(win)
def BoxEo():
    circle = Circle(Point(100, 100), 25)
    circle.draw(win)
def BoxFx():
    line1 = Line(Point(145,70), Point(195,130))
    line1.draw(win)
    line2 = Line(Point(195,70), Point(145, 130))
    line2.draw(win)
def BoxFo():
    circle = Circle(Point(170,100),23)
    circle.draw(win)

"""Third Row"""
def BoxGx():
    line1 = Line(Point(5,140), Point(50,190))
    line1.draw(win)
    line2 = Line(Point(50,140), Point(5, 190))
    line2.draw(win)
def BoxGo():
    circle = Circle(Point(32,165),23)
    circle.draw(win)
def BoxHx():
    line1 = Line(Point(65,140), Point(135,190))
    line1.draw(win)
    line2 = Line(Point(135,140), Point(65, 190))
    line2.draw(win)
def BoxHo():
    circle = Circle(Point(100, 165), 25)
    circle.draw(win)
def BoxIx():
    line1 = Line(Point(145,140), Point(195,190))
    line1.draw(win)
    line2 = Line(Point(195,140), Point(145, 190))
    line2.draw(win)
def BoxIo():
    circle = Circle(Point(170,165),23)
    circle.draw(win)


"""Entry Point"""
def EntryPoint():
    text = Text(Point(400,10), "Enter box letter")
    text.setFill("Blue")
    text.draw(win)
    entry = Entry(Point(480,10),5)
    entry.draw(win)
    win.getMouse()
    return entry.getText()

"""To determine whether the user has entered a legal choice or not"""
def LegalChoice(guessed_box, legal_letters, guessed_letters):
    if guessed_box in legal_letters and guessed_box not in guessed_letters:
        return True
    return False

"""To call the functions easily and reduce the code, to learn more about this, google "Calling functions in for loop" """
BoxX = [BoxAx,BoxBx,BoxCx,BoxDx,BoxEx,BoxFx,BoxGx,BoxHx,BoxIx]
BoxO = [BoxAo,BoxBo,BoxCo,BoxDo,BoxEo,BoxFo,BoxGo,BoxHo,BoxIo]

emptybox = ["1", "2", "3","4", "5", "6","7", "8", "9"]

"""To check if the user has won the game"""
def GameWin():
    if emptybox[0] == emptybox[1] and emptybox[1] == emptybox[2]:
        line = Line(Point(5,35), Point(200,35))
        line.setFill("Blue")
        line.draw(win)
        return True
    if emptybox[3] == emptybox[4] and emptybox[4] == emptybox[5]:
        line = Line(Point(5,100), Point(200,100))
        line.setFill("Blue")
        line.draw(win)
        return True
    if emptybox[6] == emptybox[7] and emptybox[7] == emptybox[8]:
        line = Line(Point(5,165), Point(200,165))
        line.setFill("Blue")
        line.draw(win)
        return True
    if emptybox[0] == emptybox[3] and emptybox[3] == emptybox[6]:
        line = Line(Point(27,5), Point(27,200))
        line.setFill("Blue")
        line.draw(win)
        return True
    if emptybox[1] == emptybox[4] and emptybox[4] == emptybox[7]:
        line = Line(Point(100,5), Point(100,200))
        line.setFill("Blue")
        line.draw(win)
        return True
    if emptybox[2] == emptybox[5] and emptybox[5] == emptybox[8]:
        line = Line(Point(170,5), Point(170,200))
        line.setFill("Blue")
        line.draw(win)
        return True
    if emptybox[0] == emptybox[4] and emptybox[4] == emptybox[8]:
        line = Line(Point(5,5), Point(200,200))
        line.setFill("Blue")
        line.draw(win)
        return True
    if emptybox[2] == emptybox[4] and emptybox[4] == emptybox[6]:
        line = Line(Point(200,15), Point(0,180))
        line.setFill("Blue")
        line.draw(win)
        return True
    return False

"""Main Function"""
def Play():
    legal_letters = ['1','2','3','4','5','6','7','8','9']
    guessed_letters = []
    i = 1
    while i < 10 and not GameWin():
        submit = Rectangle(Point(400,30), Point(460,50))
        submit.setOutline("Red")
        submit.setFill("Yellow")
        submit.draw(win)
        submitext = Text(Point(428,40), "Submit")
        submitext.setFill("Blue")
        submitext.draw(win)
        if i % 2 == 0:
            text = Text(Point(425,190),"X's TURN!!!")
        else:
            text = Text(Point(425,190), "O's TURN!!!")
        text.setSize(20)
        text.setFill("Blue")
        text.draw(win)
        guessed_box = EntryPoint()
        print(guessed_box)
        if LegalChoice(guessed_box, legal_letters, guessed_letters):
            guessed_letters.append(guessed_box)
            if i % 2 == 0:
                
                emptybox[int(guessed_box) - 1] = "X"
                BoxX[int(guessed_box) - 1]()
            else:
                
                emptybox[int(guessed_box) - 1] = "O"
                BoxO[int(guessed_box) - 1]()
            i += 1
        else:
            print("False")
        text.undraw()
        submit.undraw()
    if GameWin():
        if i % 2 == 0:
            text = Text(Point(400,100),"O wins the game")
        else:
            text = Text(Point(400,100),"X wins the game")
        text.draw(win)
    else:
        text = Text(Point(400,100),"Game ends in a draw")
        text.draw(win)
    
EmptyBox()
Play()
