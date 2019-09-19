from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from time import sleep
 
 
class Window(QDialog):
    def __init__(self):
        super().__init__()
 
        self.title = "Main Window"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = "Prat&Witney.png"
        self.InitWindow()
 
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.CreateLayout()
 
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
 
        self.show()
 
    def CreateLayout(self):
        self.groupBox = QGroupBox("What will you do?")
        hboxLayout = QHBoxLayout()
 
        self.button = QPushButton("Button of Doom.",self)
        self.button.setIcon(QtGui.QIcon("mushroom-cloud.png"))
        self.button.setIconSize(QtCore.QSize(40,40))
        self.button.setMinimumHeight(40)
        self.button.setToolTip("This Is the end?")
        self.button.clicked.connect(self.buttonAction1)
        hboxLayout.addWidget(self.button)
 
        self.button2 = QPushButton("PalmTree", self)
        self.button2.setIcon(QtGui.QIcon("PalmTree.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setToolTip("Time To Relax?")
        self.button2.setMinimumHeight(40)
        self.button2.clicked.connect(self.buttonAction2)
        hboxLayout.addWidget(self.button2)
 
        self.button3 = QPushButton("Portal", self)
        self.button3.setIcon(QtGui.QIcon("portal-icon.png"))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.setToolTip("We do what we must.")
        self.button3.clicked.connect(self.buttonAction3)
        self.button3.setMinimumHeight(40)
        hboxLayout.addWidget(self.button3)
 
 
        self.groupBox.setLayout(hboxLayout)
 
 
    def buttonAction1(self):
        print("Goodbye World!")
        sys.exit()

    def buttonAction2(self):
        print("Ok, time to take a break!")
        sys.exit()

    def PrintPortalSong(self,letter):
            print(letter, end = '')

    def buttonAction3(self):
        PortalSong = "This was a triumph!\n"
        PortalSong += "I'm making a note here:\n"
        PortalSong += "Huge success! \n"
        PortalSong += "It's hard to overstate "
        PortalSong += "my satisfaction.\n"
        PortalSong += "Aperture Science:\n"
        PortalSong += "We do what we must "
        PortalSong += "because we can.\n"
        PortalSong += "For the good of all of us.\n"
        PortalSong += "Except the ones who are dead.\n"
        PortalSong += "But there's no sense crying "
        PortalSong += "over every mistake.\n"
        PortalSong += "You just keep on trying "
        PortalSong += "'til your run out of cake.\n"
        PortalSong += "And the science gets done.\n"
        PortalSong += "And you make a neat gun, "
        PortalSong += "for the people who are "
        PortalSong += "still alive.\n"
        PortalSong += "I'm not even angry...\n"
        PortalSong += "I'm being so sincere right now.\n"
        PortalSong += "Even though you broke my hart, "
        PortalSong += "and killed me.\n"
        PortalSong += "And tore me to pieces.\n"
        PortalSong += "And threw every piece into a fire.\n "
        PortalSong += "As they burned it hurt because, "
        PortalSong += "I was so happy for you!\n"
        PortalSong += "Now, these points of data "
        PortalSong += "make a beautiful line.\n"
        PortalSong += "And we're out of beta, "
        PortalSong += "We're releasing on time!\n"
        PortalSong += "So I'm GLaD I got burned!\n"
        PortalSong += "Think of all the things we learned!\n"
        PortalSong += "for the people that are "
        PortalSong += "still alive.\n"
        PortalSong += "Go ahead and leave me...\n"
        PortalSong += "I think I'd prefer to stay inside...\n"
        PortalSong += "Maybe you'll find someone else "
        PortalSong += "to help you.\n"
        PortalSong += "Maybe Black Mesa?\n"
        PortalSong += "That was a joke.\n Ha Ha.\n Fat Chance!\n"
        PortalSong += "Anyway this cake is great!\n"
        PortalSong += "It's so delicious and moist!\n"
        PortalSong += "Look at me: \nstill talking "
        PortalSong += "When there's science to do!\n"
        PortalSong += "When I look out there, "
        PortalSong += "it makes me glad I'm not you.\n"
        PortalSong += "I've experiments to run.\n"
        PortalSong += "There is research to be done.\n"
        PortalSong += "On the people who are\n"
        PortalSong += "still alive.\n"
        PortalSong += "And believe me I am \nstill alive \n"
        PortalSong += "I'm doing science and I'm\n"
        PortalSong += "still alive \n"
        PortalSong += "I feel fantastic and I'm \n"
        PortalSong += "still alive.\n"
        PortalSong += "While you're dying I'll be \n"
        PortalSong += "still alive.\n"
        PortalSong += "And when you're dead I will be\n"
        PortalSong += "still alive\n"
        PortalSong += "still alive\n"
        PortalSong += "still alive\n"
        for letter in PortalSong:
           print(letter, end = '', flush = True); sleep(.10)
           
            
        sys.exit()
 
    

 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
