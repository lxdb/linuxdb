#!/usr/bin/python3
#LinuxDBv2.0 QT
#Copyright (C) 2019  Denys Konovalov

#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
#of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/>.


#--------------------------------------------------------------------------------------------------------------------------------------------


#LinuxDBv2.0 QT
#Copyright (C) 2019 Denys Konovalov

#Dieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License,
#wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß
#Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.

#Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird,
#aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der
#VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.

#Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <http://www.gnu.org/licenses/>.


#---------------------------------------------------------------------------------------------------------------------------------------------


from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3
app = QApplication(sys.argv)
S_zahl=1



icon1 = QIcon('/opt/linuxdb/icons/folder.svg')
icon2 = QIcon('/opt/linuxdb/icons/exit.svg')
icon3 = QIcon('/opt/linuxdb/icons/database.svg')
icon4 = QIcon('/opt/linuxdb/icons/help.svg')
icon5 = QIcon('/opt/linuxdb/icons/next.svg')
icon6 = QIcon('/opt/linuxdb/icons/previous.svg')
icon7 = QIcon('/opt/linuxdb/icons/show.svg')
icon8 = QIcon('/opt/linuxdb/icons/send.svg')
icon9 = QIcon('/opt/linuxdb/icons/edit.svg')
icon10 = QIcon('/opt/linuxdb/icons/help-win.svg')
icon11 = QIcon('/opt/linuxdb/icons/license.svg')
icon12 = QIcon('/opt/linuxdb/icons/about.svg')

class ldb_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()
    
    def initMe(self):
        
        self.striche1 = QLabel('---------------',self)
        self.striche2 = QLabel('---------------',self)
        self.striche3 = QLabel('---------------',self)
        self.striche1.setFixedHeight(20)
        
        self.dbanlU=QLabel('Datenbank anlegen',self)
        self.dbanlL=QLabel('Datenbankname',self)
        self.dbanlE=QLineEdit(self)
        self.dbanlB=QPushButton('Datenbank anlegen',self)
        self.dbanlB.setIcon(icon3)
        self.dbselanl= QPushButton('',self)
        self.dbselanl.setIcon(icon1)
        self.dbselanl.clicked.connect(self.fdcre)
        self.dbanlB.clicked.connect(self.db_anlegen)
        self.dbanlB.setStatusTip('Eine Datenbank anlegen')

        readdb = QAction(QIcon(icon7),'&Datenbank auslesen',self)
        readdb.triggered.connect(self.fdget)
        readdb.setStatusTip('Daten aus einer Datenbank auslesen')
        
        credb = QAction(QIcon(icon3),'&Neue Datenbank',self)
        credb.triggered.connect(self.fdcre)
        credb.setStatusTip('Eine neue Datenbank anlegen')
        
        schrdb = QAction(QIcon(icon9),'&In die Datenbank schreiben',self)
        schrdb.triggered.connect(self.fdwrite)
        schrdb.setToolTip('Daten in eine Datenbank eingeben')
        
        helpact = QAction(QIcon(icon4),'&Help',self)
        helpact.triggered.connect(self.help2)
        helpact.setToolTip('Hilfe aufrufen')

        liact = QAction(QIcon(icon12),'&Lizenz',self)
        liact.triggered.connect(self.licacti)
        liact.setStatusTip('Lizenz anzeigen')
        
        
        self.menubar = QMenuBar()
        
        file = self.menubar.addMenu('&File')
        help = self.menubar.addMenu('&Hilfe')
        license = self.menubar.addMenu('&Lizenz')
        
        file.addAction(credb)
        file.addAction(schrdb)
        file.addAction(readdb)
        help.addAction(helpact)
        license.addAction(liact)
        self.menubar.setFixedHeight(30)

        self.dbschrU = QLabel('In die Datenbank schreiben',self)
        self.dbschrU.setFixedHeight(25)

        self.dbschrDbU = QLabel('Datenbank',self)
        self.dbschrDbU.setFixedHeight(25)
        self.dbschrIdU = QLabel('Id',self)
        self.dbschrDiU = QLabel('Distribution',self)
        self.dbschrVerU = QLabel('Version',self)
        self.dbschrKerU = QLabel('Kernel',self)
        self.dbschrsel = QPushButton(self)
        self.dbschrsel.setIcon(icon1)
        self.dbschrsel.clicked.connect(self.fdwrite)
        
        
        self.dbschrDb = QLineEdit(self)
        self.dbschrId = QLineEdit(self)
        self.dbschrDi = QLineEdit(self)
        self.dbschrKer = QLineEdit(self)
        self.dbschrVer = QLineEdit(self)

        self.dbschrB = QPushButton('Senden',self)
        self.dbschrB.clicked.connect(self.db_schreiben)
        self.dbschrB.setIcon(icon8)
        Seite_E2=str(S_zahl)
        self.Seite_E = QLineEdit(self)
        self.Seite_E.setText(Seite_E2)
        self.nach_button = QPushButton('zurück',self)
        self.nach_button.clicked.connect(self.nach)        
        self.nach_button.setIcon(icon6)
        
        self.vor_button = QPushButton('vor',self)
        self.vor_button.setIcon(icon5)
        self.vor_button.clicked.connect(self.vor)
        self.dbanU = QLabel('Die Datenbank auslesen',self)
        self.dbanDbU = QLabel('Datenbank',self)
        self.dbanDb = QLineEdit(self)
        self.dbanB = QPushButton('Daten anzeigen')
        self.tabL1 = QLabel('Id',self)
        self.tabL2 = QLabel('Distribution',self)
        self.tabL3 = QLabel('Version',self)
        self.tabL4 = QLabel('Kernel',self)
        self.dbanB.clicked.connect(self.daten_abrufen)

        self.dbanB.setIcon(icon7)
        
        self.dbansel = QPushButton(self)
        self.dbansel.setIcon(icon1)
        self.dbansel.clicked.connect(self.fdget)
        self.E_0_0 = QLineEdit(self)
        self.E_0_1 = QLineEdit(self)
        self.E_0_2 = QLineEdit(self)
        self.E_0_3 = QLineEdit(self)

        self.E_1_0 = QLineEdit(self)
        self.E_1_1 = QLineEdit(self)
        self.E_1_2 = QLineEdit(self)
        self.E_1_3 = QLineEdit(self)

        self.E_2_0 = QLineEdit(self)
        self.E_2_1 = QLineEdit(self)
        self.E_2_2 = QLineEdit(self)
        self.E_2_3 = QLineEdit(self)

        self.E_3_0 = QLineEdit(self)
        self.E_3_1 = QLineEdit(self)
        self.E_3_2 = QLineEdit(self)
        self.E_3_3 = QLineEdit(self)

        self.E_4_0 = QLineEdit(self)
        self.E_4_1 = QLineEdit(self)
        self.E_4_2 = QLineEdit(self)
        self.E_4_3 = QLineEdit(self)

        self.E_5_0 = QLineEdit(self)
        self.E_5_1 = QLineEdit(self)
        self.E_5_2 = QLineEdit(self)
        self.E_5_3 = QLineEdit(self)

        self.E_6_0 = QLineEdit(self)
        self.E_6_1 = QLineEdit(self)
        self.E_6_2 = QLineEdit(self)
        self.E_6_3 = QLineEdit(self)

        self.E_7_0 = QLineEdit(self)
        self.E_7_1 = QLineEdit(self)
        self.E_7_2 = QLineEdit(self)
        self.E_7_3 = QLineEdit(self)

        self.E_8_0 = QLineEdit(self)
        self.E_8_1 = QLineEdit(self)
        self.E_8_2 = QLineEdit(self)
        self.E_8_3 = QLineEdit(self)

        self.E_9_0 = QLineEdit(self)
        self.E_9_1 = QLineEdit(self)
        self.E_9_2 = QLineEdit(self)
        self.E_9_3 = QLineEdit(self)

        self.copyright = QLabel('Copyright (C) 2019 Denys Konovalov (lxdb)',self)
        



        grid = QGridLayout()
        #grid.setSpacing(10)
        grid.addWidget(self.menubar,0,0)
        grid.addWidget(self.dbanlL,3,0)
        grid.addWidget(self.dbanlE,4,0)
        grid.addWidget(self.dbanlB,5,0)
        grid.addWidget(self.dbanlU,1,0)        
        grid.addWidget(self.striche1,2,0)
        grid.addWidget(self.dbselanl,4,1)
        grid.addWidget(self.dbschrU,1,2)

        grid.addWidget(self.striche2,2,2)

        grid.addWidget(self.dbschrDbU,3,2)
        grid.addWidget(self.dbschrDb,4,2)
        grid.addWidget(self.dbschrsel,4,3)
        grid.addWidget(self.dbschrIdU,5,2)
        grid.addWidget(self.dbschrId,6,2)
        grid.addWidget(self.dbschrDiU,7,2)
        grid.addWidget(self.dbschrDi,8,2)
        grid.addWidget(self.dbschrVerU,9,2)
        grid.addWidget(self.dbschrVer,10,2)
        grid.addWidget(self.dbschrKerU,11,2)
        grid.addWidget(self.dbschrKer,12,2)
        grid.addWidget(self.dbschrB,13,2)
        
        grid.addWidget(self.dbanU,1,4)

        grid.addWidget(self.striche3,2,4)

        grid.addWidget(self.dbanDbU,3,4)
        grid.addWidget(self.dbanDb,4,4)
        grid.addWidget(self.dbanB,5,4)
        grid.addWidget(self.dbansel,4,5)
        
        
        grid.addWidget(self.tabL1,6,4)
        grid.addWidget(self.tabL2,6,5)
        grid.addWidget(self.tabL3,6,6)
        grid.addWidget(self.tabL4,6,7)
        grid.addWidget(self.nach_button,17,4)
        grid.addWidget(self.vor_button,17,6)
        grid.addWidget(self.Seite_E,17,5)
        grid.addWidget(self.E_0_0,7,4)
        grid.addWidget(self.E_0_1,7,5)
        grid.addWidget(self.E_0_2,7,6)
        grid.addWidget(self.E_0_3,7,7)

        grid.addWidget(self.E_1_0,8,4)
        grid.addWidget(self.E_1_1,8,5)
        grid.addWidget(self.E_1_2,8,6)
        grid.addWidget(self.E_1_3,8,7)

        grid.addWidget(self.E_2_0,9,4)
        grid.addWidget(self.E_2_1,9,5)
        grid.addWidget(self.E_2_2,9,6)
        grid.addWidget(self.E_2_3,9,7)

        grid.addWidget(self.E_3_0,10,4)
        grid.addWidget(self.E_3_1,10,5)
        grid.addWidget(self.E_3_2,10,6)
        grid.addWidget(self.E_3_3,10,7)

        grid.addWidget(self.E_4_0,11,4)
        grid.addWidget(self.E_4_1,11,5)
        grid.addWidget(self.E_4_2,11,6)
        grid.addWidget(self.E_4_3,11,7)

        grid.addWidget(self.E_5_0,12,4)
        grid.addWidget(self.E_5_1,12,5)
        grid.addWidget(self.E_5_2,12,6)
        grid.addWidget(self.E_5_3,12,7)

        grid.addWidget(self.E_6_0,13,4)
        grid.addWidget(self.E_6_1,13,5)
        grid.addWidget(self.E_6_2,13,6)
        grid.addWidget(self.E_6_3,13,7)
        
        grid.addWidget(self.E_7_0,14,4)
        grid.addWidget(self.E_7_1,14,5)
        grid.addWidget(self.E_7_2,14,6)
        grid.addWidget(self.E_7_3,14,7)
        
        grid.addWidget(self.E_8_0,15,4)
        grid.addWidget(self.E_8_1,15,5)
        grid.addWidget(self.E_8_2,15,6)
        grid.addWidget(self.E_8_3,15,7)
    
        grid.addWidget(self.E_9_0,16,4)
        grid.addWidget(self.E_9_1,16,5)
        grid.addWidget(self.E_9_2,16,6)
        grid.addWidget(self.E_9_3,16,7)
        grid.addWidget(self.copyright,18,4)               

        self.setLayout(grid)
        self.setGeometry(50,50,1920,1080)
        self.setWindowTitle("LinuxDB v2.0")
        self.setWindowIcon(QIcon("/opt/linuxdb/LinuxDB.png"))
        self.show()
        helpw.close()
    def db_anlegen(self):
        print("Datenbank wurde angelegt")
        db_name=self.dbanlE.text()
        connection = sqlite3.connect(db_name)
        cursor= connection.cursor()
        cursor.execute('''
        CREATE TABLE LinuxVersionen(id INTEGER PRIMARY KEY, Distribution TEXT, Version TEXT, Kernel TEXT )
        ''')
    
    
        connection.close()
    def db_schreiben(self):
        print("Daten werden eingetragen ...")
        db_name2=self.dbschrDb.text()
        connection = sqlite3.connect(db_name2)
        cursor= connection.cursor()
        Distribution=self.dbschrDi.text()
        Version=self.dbschrVer.text()
        Kernel=self.dbschrKer.text()
    

        #cursor.execute("INSERT INTO LinuxVersionen VALUES (8,'2018', '12', '11', '11','58','33','hallo')")
        #cursor.execute("INSERT INTO LinuxVersionen VALUES (9,'2018', '12', '11', '11','58','33','hallo')")

        id_text=self.dbschrId.text()
        sql_text=""
        sql_text += "INSERT INTO LinuxVersionen VALUES ("
        sql_text +=id_text+","
        sql_text +=" '"+Distribution+"',"
        sql_text +=" '"+Version+"',"
        sql_text +=" '"+Kernel+"')"
    
    
        print("sql_text ", sql_text)
        cursor.execute(sql_text)
    
        connection.commit()
        connection.close()
    def nach(self):
        global S_zahl
        S_zahl=int(self.Seite_E.text())
        if (S_zahl>2):
            S_zahl=S_zahl-1
            print('Seite: ',S_zahl)

        else:
            S_zahl=1
        
        S_zahl1=str(S_zahl)
        self.Seite_E.clear()
        self.Seite_E.setText(S_zahl1)
        self.daten_abrufen()
    def help2(self):
        helpw.show()

    def daten_abrufen(self):
        print("--------------------------")
        global S_zahl
        print("S_zahl ", S_zahl)

        db_name2=self.dbanDb.text()
        connection = sqlite3.connect(db_name2)
        cursor= connection.cursor()

        sql = "SELECT * FROM LinuxVersionen"
        cursor.execute(sql)
        #laenge=cursor.len()
        #print("laenge ",laenge)
        text=""
        spalte=[]
        reihe=[]
    
        i=0
        for row in cursor:
        
            #print ("Id ", row[0])
            #print ("Vorname ", row[1])
            #print ("Nachname ", row[2])
            #print ("Anrede ", row[3])
            #print ("Adresse ", row[4], "\n")

            r0=str(row[0])
            r1=str(row[1])
            r2=str(row[2])
            r3=str(row[3])
        
        
            spalte = [(r0, r1, r2, r3)]
            reihe.extend(spalte)
        

    
        connection.commit()
        connection.close()
        print("len(spalte)", len(spalte))
        print("len(reihe)", len(reihe))
        x=len(reihe)

        #Reihe 0
        i=0
        self.E_0_0.clear()    
        k=0+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_0_0.setText(x)
        except:
            self.E_0_0.setText("")


        i=1
        self.E_0_1.clear()    
        k=0+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_0_1.setText(x)
        except:
            self.E_0_1.setText("")
        

        i=2
        self.E_0_2.clear()    
        k=0+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_0_2.setText(x)
        except:
            self.E_0_2.setText("")
        

        i=3
        self.E_0_3.clear()    
        k=0+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_0_3.setText(x)
        except:
            self.E_0_3.setText("")
        

    
    

        #Reihe1
        i=0
        self.E_1_0.clear()    
        k=1+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_1_0.setText(x)
        except:
            self.E_1_0.setText("")


        i=1
        self.E_1_1.clear()    
        k=1+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_1_1.setText(x)
        except:
            self.E_1_1.setText("")
        

        i=2
        self.E_1_2.clear()    
        k=1+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_1_2.setText(x)
        except:
            self.E_1_2.setText("")
        

        i=3
        self.E_1_3.clear()    
        k=1+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_1_3.setText(x)
        except:
            self.E_1_3.setText("")
        

   

        #Reihe2
        i=0
        self.E_2_0.clear()    
        k=2+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_2_0.setText(x)
        except:
            self.E_2_0.setText("")


        i=1
        self.E_2_1.clear()    
        k=2+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_2_1.setText(x)
        except:
            self.E_2_1.insert("")
        

        i=2
        self.E_2_2.clear()    
        k=2+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_2_2.setText(x)
        except:
            self.E_2_2.setText("")
        

        i=3
        self.E_2_3.clear()    
        k=2+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_2_3.setText(x)
        except:
            self.E_2_3.setText("")
        

    


        #Reihe3
        i=0
        self.E_3_0.clear()    
        k=3+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_3_0.setText(x)
        except:
            self.E_3_0.setText("")


        i=1
        self.E_3_1.clear()    
        k=3+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_3_1.setText(x)
        except:
            self.E_3_1.setText("")
        

        i=2
        self.E_3_2.clear()    
        k=3+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_3_2.setText(x)
        except:
            self.E_3_2.setText("")
        

        i=3
        self.E_3_3.clear()    
        k=3+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_3_3.setText(x)
        except:
            self.E_3_3.setText("")
        

    

        #Reihe4
        i=0
        self.E_4_0.clear()    
        k=4+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_4_0.setText(x)
        except:
            self.E_4_0.setText("")


        i=1
        self.E_4_1.clear()    
        k=4+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_4_1.setText(x)
        except:
            self.E_4_1.setText("")
        

        i=2
        self.E_4_2.clear()    
        k=4+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_4_2.setText(x)
        except:
            self.E_4_2.setText("")
        

        i=3
        self.E_4_3.clear()    
        k=4+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_4_3.setText(x)
        except:
            self.E_4_3.setText("")
        

    
        #Reihe5
        i=0
        self.E_5_0.clear()    
        k=5+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_5_0.setText(x)
        except:
            self.E_5_0.setText("")


        i=1
        self.E_5_1.clear()   
        k=5+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_5_1.setText(x)
        except:
            self.E_5_1.setText("")
        

        i=2
        self.E_5_2.clear()    
        k=5+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_5_2.setText(x)
        except:
            self.E_5_2.setText("")
        

        i=3
        self.E_5_3.clear()   
        k=5+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_5_3.setText(x)
        except:
            self.E_5_3.setText("")
        

   


        #Reihe6
        i=0
        self.E_6_0.clear()  
        k=6+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_6_0.setText(x)
        except:
            self.E_6_0.setText("")


        i=1
        self.E_6_1.clear() 
        k=6+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_6_1.setText(x)
        except:
            self.E_6_1.setText("")
        

        i=2
        self.E_6_2.clear()    
        k=6+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_6_2.setText(x)
        except:
            self.E_6_2.setText("")
        

        i=3
        self.E_6_3.clear()    
        k=6+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_6_3.setText(x)
        except:
            self.E_6_3.setText("")
        

   
        #Reihe7
        i=0
        self.E_7_0.clear()   
        k=7+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_7_0.setText(x)
        except:
            self.E_7_0.setText("")


        i=1
        self.E_7_1.clear()    
        k=7+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_7_1.setText(x)
        except:
            self.E_7_1.setText("")
        

        i=2
        self.E_7_2.clear()    
        k=7+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_7_2.setText(x)
        except:
            self.E_7_2.setText("")
        

        i=3
        self.E_7_3.clear()    
        k=7+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_7_3.setText(x)
        except:
            self.E_7_3.setText("")
        

   

        #Reihe8
        i=0
        self.E_8_0.clear()    
        k=8+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_8_0.setText(x)
        except:
            self.E_8_0.setText("")


        i=1
        self.E_8_1.clear()    
        k=8+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_8_1.setText(x)
        except:
            self.E_8_1.setText("")
        

        i=2
        self.E_8_2.clear()    
        k=8+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_8_2.setText(x)
        except:
            self.E_8_2.setText("")
        

        i=3
        self.E_8_3.clear()    
        k=8+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_8_3.setText(x)
        except:
            self.E_8_3.setText("")
        

    

        #Reihe9
        i=0
        self.E_9_0.clear()    
        k=9+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_9_0.setText(x)
        except:
            self.E_9_0.setText("")


        i=1
        self.E_9_1.clear()   
        k=9+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            print("x ",x)
            self.E_9_1.setText(x)
        except:
            self.E_9_1.setText("")
        

        i=2
        self.E_9_2.clear()   
        k=9+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_9_2.setText(x)
        except:
            self.E_9_2.setText("")
        

        i=3
        self.E_9_3.clear()    
        k=9+(S_zahl-1)*10
        x=""
        try:
            x=str(reihe[k][i])
            self.E_9_3.setText(x)
        except:
            self.E_9_3.setText("")

        
    def fdcre(self):
        filedia = QFileDialog()
        fdiasave= filedia.getSaveFileName(self, 'Datenbank anlegen', 'Databases/Database.db', 'SQLite Datenbank (*.db)')
        self.dbanlE.setText(fdiasave[0])
    
    def fdget(self):
        filedia = QFileDialog()
        fdiaget= filedia.getOpenFileName(self, 'Datenbank auswählen', 'Databases', 'SQLite Datenbank (*.db)')
        self.dbanDb.setText(fdiaget[0])
        self.daten_abrufen()
    def fdwrite(self):
        filedia = QFileDialog()
        fdiaget= filedia.getOpenFileName(self, 'Datenbank auswählen', 'Databases', 'SQLite Datenbank (*.db)')
        self.dbschrDb.setText(fdiaget[0])
    
    def vor(self):
        print("vor")
        global S_zahl
        S_zahl=int(self.Seite_E.text())
    
        S_zahl=S_zahl+1


        S_zahl5 = str(S_zahl)
        self.Seite_E.clear()
        self.Seite_E.setText(S_zahl5)
        self.daten_abrufen()

    def licacti(self):
        liw.show()

        
def dbschr_help():
    helptext.clear()
    helptext.setText("2) Daten in eine Datenbank eingeben.\n Als erstes trägt man die Daten in die Textfelder\n ein (ID, Distribution, Version und Kernel).\n Anschließend gibt man den Datenbanknamen/Pfad inm\n Datenbank-Textfeld an oder wählt diese aus(Ordner-Symbol). Jetzt drückt man noch\n die Senden-Taste und die Daten werden\n hineingeschrieben.\n\n")
def dban_help():
    helptext.clear()
    helptext.setText("1) Eine Datenbank anlegen\n Als erstes gibt man im Eingabefeld den Pfad ein oder wählt diese aus(Ordner-Symbol).\n Wenn man nur einen Datenbanknamen eingibt wird\n die Datenbank im Heimverzeichniss (/home/USER)\n erstellt. Der Datenbankname muss die Endung .db\n haben.\n\n")

def dbles_help():
    helptext.clear()
    helptext.setText("3) Daten aus einer Datenbank auslesen\n Als erstes gibt man den Datenbanknamen/Pfad im\n Textfeld ein. Anschließend drückt man auf den\n Lese-Knopf. In der Tabelle unten erscheinen dann\n die Daten.")

box = QVBoxLayout()
helpU = QLabel('Hilfe zu LinuxDB v2.0 Qt')
helpB1 = QPushButton('1. Eine Datenbank Anlegen')
helpB2 = QPushButton('2.Daten in eine Datenbank einschreiben')
helpB3 = QPushButton('3. Daten aus einer Datenbank auslesen')
helpB1.clicked.connect(dban_help)
helpB2.clicked.connect(dbschr_help)
helpB3.clicked.connect(dbles_help)

helptext = QTextEdit()
box.addWidget(helpU)
box.addWidget(helpB1)
box.addWidget(helpB2)
box.addWidget(helpB3)
box.addWidget(helptext)


helpw = QWidget()
helpw.setLayout(box)
helpw.setGeometry(550,200,500,500)

helpw.setWindowTitle("LinuxDB v2.0 Help")
helpw.setWindowIcon(QIcon(icon10))

box1 = QVBoxLayout()
liL = QLabel('Lizenz')
def litextset():
    litext.clear()
    litext.setText("LinuxDBv2.0 QT\n Copyright (C) 2019  Denys Konovalov\nThis program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warrantyof MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/>.\n--------------------------------------------------------------------------------------------------------------------------------------------\nLinuxDBv2.0 QT\nCopyright (C) 2019 Denys Konovalov \nDieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License,wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird,aber OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. Falls nicht, siehe <http://www.gnu.org/licenses/>.---------------------------------------------------------------------------------------------------------------------------------------------")


litext = QTextEdit()
box1.addWidget(liL)
box1.addWidget(litext)
liw = QWidget()
liw.setLayout(box1)

litextset()
liw.setWindowTitle("LinuxDB v2.0 license")
liw.setWindowIcon(QIcon(icon11))
   






window=ldb_window()
grid1 = QGridLayout()
grid1.setSpacing(10)
sys.exit(app.exec_())
