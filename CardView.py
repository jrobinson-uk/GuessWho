import sys
from PyQt4 import QtGui #imports




class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        WINDOW_WIDTH=1024
        WINDOW_HEIGHT=768
        SPACING = 10
        COLS = 8
        ROWS = 3
        grid = QtGui.QGridLayout()
        grid.setSpacing(SPACING)
        cards = []
        for x in range(3):
            for y in range(8):
                pic = QtGui.QPixmap("pic.jpeg")
                pic.scaledToWidth(10)
                card = QtGui.QLabel(self)
                #card.setFrameShape(QtGui.QFrame.StyledPanel)
                card.setPixmap(pic.scaledToHeight((WINDOW_HEIGHT-((ROWS+1)*SPACING))/ROWS).scaledToWidth((WINDOW_WIDTH-((COLS+1)*SPACING))/COLS))
                grid.addWidget(card,x,y,1,2)
            
        self.setLayout(grid)
        self.setGeometry(100,100,WINDOW_WIDTH,WINDOW_HEIGHT)
        self.setWindowTitle('Pi Guess  Who')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()

def main():
    
    app = QtGui.QApplication(sys.argv) # define app using system arguments

    ex = Example()
    sys.exit(app.exec())    #enter main loop for the app

if __name__ == '__main__':
    main()



##
##pixmap = QtGui.QPixmap("wires.png")
##        lbl = QtGui.QLabel(self)
##        lbl.setPixmap(pixmap)
##
##        title = QtGui.QLabel('Title')
##        grid.addWidget(title,4,3,4,4)
##        grid.addWidget(lbl,15,15,16,16)
