from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QStatusBar, QAction, QMenu, QMenuBar, \
    QPushButton, QTextBrowser, QFrame, QLabel, QLineEdit, QDialog, QGraphicsView


class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QWidget(MainWindow)
        self.intro = QTextBrowser(self.centralwidget)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.exp = QWidget()
        self.expBrowser = QTextBrowser(self.exp)
        self.mach = QWidget()
        self.machBrowser = QTextBrowser(self.mach)
        self.gands = QWidget()
        self.geoBrowser = QTextBrowser(self.gands)
        self.recc = QTextBrowser(self.centralwidget)
        self.prevBtn = QPushButton(self.centralwidget)
        self.currentBtn = QPushButton(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menuInput = QMenu(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.actionInput = QAction(MainWindow)
        self.actionExit = QAction(MainWindow)

        self.Dialog = QDialog()
        self.pushButton = QPushButton(self.Dialog)
        self.pushButton_2 = QPushButton(self.Dialog)
        self.label = QLabel(self.Dialog)
        self.lineEdit = QLineEdit(self.Dialog)
        self.label_2 = QLabel(self.Dialog)
        self.lineEdit_2 = QLineEdit(self.Dialog)
        self.label_3 = QLabel(self.Dialog)
        self.lineEdit_3 = QLineEdit(self.Dialog)
        self.label_4 = QLabel(self.Dialog)
        self.lineEdit_4 = QLineEdit(self.Dialog)
        self.label_5 = QLabel(self.Dialog)
        self.lineEdit_5 = QLineEdit(self.Dialog)
        self.label_6 = QLabel(self.Dialog)
        self.lineEdit_6 = QLineEdit(self.Dialog)
        self.lineEdit_7 = QLineEdit(self.Dialog)
        self.label_7 = QLabel(self.Dialog)

        self.info = None
        self.db = connect("data/DBs/mining.db")
        self.prevDb = connect("data/Dbs/prev.db")

        try:
            self.prevDb.execute("create table previous (html text);")
            self.prevDb.commit()
            self.prevDb.execute("create table current (html text);")
            self.prevDb.commit()
        except OperationalError:
            pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 590)
        self.centralwidget.setObjectName("centralwidget")
        self.intro.setGeometry(QRect(10, 0, 381, 491))
        self.intro.setFrameShape(QFrame.StyledPanel)
        self.intro.setObjectName("intro")
        self.tabWidget.setGeometry(QRect(400, 50, 391, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.exp.setObjectName("exp")
        self.expBrowser.setGeometry(QRect(0, 0, 391, 481))
        self.expBrowser.setObjectName("expBrowser")
        self.tabWidget.addTab(self.exp, "")
        self.mach.setObjectName("mach")
        self.machBrowser.setGeometry(QRect(0, 0, 391, 481))
        self.machBrowser.setObjectName("machBrowser")
        self.tabWidget.addTab(self.mach, "")
        self.gands.setObjectName("gands")
        self.geoBrowser.setGeometry(QRect(0, 0, 391, 471))
        self.geoBrowser.setObjectName("geoBrowser")
        self.tabWidget.addTab(self.gands, "")
        self.recc.setGeometry(QRect(400, 0, 391, 41))
        self.recc.setObjectName("recc")
        self.prevBtn.setGeometry(QRect(50, 510, 101, 31))
        self.prevBtn.setCheckable(True)
        self.prevBtn.setChecked(True)
        self.prevBtn.setObjectName("prevBtn")
        self.currentBtn.setGeometry(QRect(264, 510, 101, 31))
        self.currentBtn.setCheckable(True)
        self.currentBtn.setEnabled(False)
        self.currentBtn.setObjectName("currentBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        self.menuInput.setObjectName("menuInput")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInput.setObjectName("actionInput")
        self.actionExit.setObjectName("actionExit")
        self.menuInput.addAction(self.actionInput)
        self.menuInput.addAction(self.actionExit)
        self.menubar.addAction(self.menuInput.menuAction())

        self.Dialog.setModal(True)
        self.pushButton.setGeometry(QRect(50, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2.setGeometry(QRect(270, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label.setGeometry(QRect(10, 10, 41, 21))
        self.label.setObjectName("label")
        self.lineEdit.setGeometry(QRect(60, 10, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2.setGeometry(QRect(190, 10, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2.setGeometry(QRect(280, 10, 111, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3.setGeometry(QRect(10, 40, 101, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3.setGeometry(QRect(110, 40, 281, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4.setGeometry(QRect(10, 70, 141, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4.setGeometry(QRect(160, 70, 51, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5.setGeometry(QRect(230, 70, 101, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5.setGeometry(QRect(340, 70, 51, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6.setGeometry(QRect(10, 100, 131, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6.setGeometry(QRect(150, 100, 51, 20))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7.setGeometry(QRect(350, 100, 41, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7.setGeometry(QRect(210, 100, 131, 21))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mine-Falcon"))
        self.Dialog.setWindowTitle(_translate('Dialog', 'Enter blast parameters'))
        self.intro.setHtml(_translate("MainWindow",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                      "<p align=\"center\" style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"data/images/logo.jpg\" width=\"350\" height=\"250\" /></p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\';\"><br /></p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:8pt;\"><br /></p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:8pt;\"><br /></p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:8pt;\"><br /></p>\n"
                                      "<p align=\"center\" style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\">MINE-FALCON IS AN APPLICATION USED</span></p>\n"
                                      "<p align=\"center\" style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:12pt;\"> TO MONITOR AND ASSIST MINE FLOW <br />PRODUCTIVITY</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exp), _translate("MainWindow", "Explosive"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mach), _translate("MainWindow", "Machinery"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gands),
                                  _translate("MainWindow", "Geology and Survey results"))
        self.prev()
        self.recc.setHtml(_translate("MainWindow",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                     "<p align=\"center\" style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">RECOMMENDATION</span></p></body></html>"))
        self.prevBtn.setText(_translate("MainWindow", "PREVIOUS BLAST"))
        self.prevBtn.clicked.connect(self.prev)
        self.currentBtn.setText(_translate("MainWindow", "CURRENT BLAST"))
        self.currentBtn.clicked.connect(self.current)
        self.menuInput.setTitle(_translate("MainWindow", "Actions"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionInput.triggered.connect(self.Dialog.show)
        self.actionExit.setText(_translate("MainWindow", "Save and Exit"))
        self.actionExit.triggered.connect(self.exit)

        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton.clicked.connect(self.enter)
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_2.clicked.connect(self.Dialog.close)
        self.label.setText(_translate("MainWindow", "Section"))
        self.label_2.setText(_translate("MainWindow", "Section ore grade"))
        self.label_3.setText(_translate("MainWindow", "Geometrical position"))
        self.label_4.setText(_translate("MainWindow", "Average ucs of exposed ore"))
        self.label_5.setText(_translate("MainWindow", "RMR of exposed ore"))
        self.label_6.setText(_translate("MainWindow", "Nature of joints"))
        self.label_7.setText(_translate("MainWindow", "Average dip angle of joints"))

    def enter(self):
        trans = QCoreApplication.translate
        ucs = self.lineEdit_4.text()
        rmr = self.lineEdit_5.text()
        nature = self.lineEdit_6.text()
        pos = self.lineEdit_3.text()
        try:
            ucs = int(ucs)
            if ucs > 30:
                data = self.db.execute(
                    'select * from machinery where "favourable conditions"="very hard rock ore";').fetchall()
                name = data[0][0]
                rate = data[0][2]
                eff = data[0][4]
                img = "3.jpg"
            elif 30 >= ucs >= 25:
                data = self.db.execute(
                    'select * from machinery where "favourable conditions"="fairly hard rock";').fetchall()
                name = data[0][0]
                rate = data[0][2]
                eff = data[0][4]
                img = "4.jpg"
            else:
                data = self.db.execute(
                    'select * from machinery where "favourable conditions"="fairly soft rock";').fetchall()
                name = data[0][0]
                rate = data[0][2]
                eff = data[0][4]
                img = "5.png"
            self.machBrowser.setText(trans("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           f"<p align=\"center\" style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"data/images/{img}\" width=\"300\" height=\"250\"/></p>\n"
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                           f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Name:            {name}</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                           f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Working rate:        {rate}</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                           f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Efficiency update:        {eff}%</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))

            if rmr == "weak":
                data = self.db.execute('select * from explosives where expname="ANFO";').fetchall()
                name = data[0][0]
                amount = data[0][1]
                usable = 50
                img = "7.jpg"
            elif rmr == "strong":
                data = self.db.execute('select * from explosives where expname="BOOSTERS";').fetchall()
                name = data[0][0]
                amount = data[0][1]
                usable = 50
                img = "6.jpg"
            self.expBrowser.setHtml(trans("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                          f"<p align=\"center\" style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"data/images/{img}\" width=\"300\" height=\"250\"/></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Name:             {name}</span></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Amount in magazine:        {amount}tonnes</span></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Current blast-usable amount:    {usable}kg</span></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
            self.geoBrowser.setHtml(trans("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">RMR:        {rmr}</span></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">UCS:        {ucs}MPa</span></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Nature of joints:    {nature}</span></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                          f"<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Location of joints:    {pos}</span></p></body></html>"))
            exp = self.expBrowser.toHtml()
            mach = self.machBrowser.toHtml()
            geo = self.geoBrowser.toHtml()
            self.info = [exp, mach, geo]
            for text in self.info:
                self.prevDb.execute("insert into current values (?);", (text,))
                self.prevDb.commit()
            self.currentBtn.setEnabled(True)
            self.currentBtn.click()
        except (OperationalError, ValueError):
            pass
        finally:
            self.Dialog.close()

    def prev(self):
        _translate = QCoreApplication.translate
        try:
            results = self.prevDb.execute("select html from previous;").fetchall()
            self.expBrowser.setHtml(_translate("MainWindow", results[0][0]))
            self.machBrowser.setHtml(_translate("MainWindow", results[1][0]))
            self.geoBrowser.setHtml(_translate("MainWindow", results[2][0]))
        except (OperationalError, IndexError):
            self.expBrowser.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Name:             </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Amount in magazine:        </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Current blast-usable amount:    </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
            self.machBrowser.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Name:            </span></p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Working rate:        </span></p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                                "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Efficiency update:        </span></p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
            self.geoBrowser.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">RMR:        </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">UCS:        </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Nature of joints:    </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                               "<p style=\" margin:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Location of joints:    </span></p></body></html>"))
        self.prevBtn.setChecked(True)
        self.currentBtn.setChecked(False)

    def current(self):
        _translate = QCoreApplication.translate
        try:
            results = self.prevDb.execute("select html from current;").fetchall()
            self.expBrowser.setHtml(_translate("MainWindow", results[0][0]))
            self.machBrowser.setHtml(_translate("MainWindow", results[1][0]))
            self.geoBrowser.setHtml(_translate("MainWindow", results[2][0]))
        except OperationalError:
            pass
        self.currentBtn.setChecked(True)
        self.prevBtn.setChecked(False)

    def exit(self):
        if self.info is not None:
            self.prevDb.execute("Delete from previous;")
            self.prevDb.commit()
            self.prevDb.execute("Delete from current;")
            self.prevDb.commit()
            self.prevDb.execute("vacuum;")
            self.prevDb.commit()
            for text in self.info:
                self.prevDb.execute("insert into previous values (?);", (text,))
                self.prevDb.commit()
        sys.exit()


class Ui_Entry():
    """Setup of cover displayed when program starts."""

    def setupUi(self, Form):
        """Arrange the cover page."""
        Form.setObjectName("Entry")
        Form.resize(801, 590)
        flag = Qt.WindowFlags(Qt.FramelessWindowHint)
        Form.setWindowFlags(flag)

        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setGeometry(QRect(0, 0, 801, 590))
        self.graphicsView.setStyleSheet(
            '''background: url("data/images/splash.png") no-repeat;'''
        )
        self.graphicsView.setObjectName("graphicsView")
        app.processEvents()

        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        QMetaObject.connectSlotsByName(Form)


if __name__ == "__main__":
    import sys
    from time import sleep
    from sqlite3 import connect, OperationalError

    app = QApplication(sys.argv)
    MainWindow,  Splash = QMainWindow(), QWidget()
    ui, splash = Ui_MainWindow(), Ui_Entry()
    ui.setupUi(MainWindow)
    splash.setupUi(Splash)
    Splash.show()
    app.processEvents()
    sleep(7)
    Splash.close()
    sleep(2)
    MainWindow.show()
    sys.exit(app.exec_())
