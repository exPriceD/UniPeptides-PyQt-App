from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
from PyQt5.QtCore import QProcess
from setup import setupConfig
import sys


def screenSize():
    sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
    print("Screen size : " + str(sizeObject.width()) +
          "x" + str(sizeObject.height()))


class Ui_MainWindow(object):
    def __init__(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateTime)

    def timerEvent(self):
        global time
        time = time.addSecs(1)
        print(time.toString("hh:mm:ss"))

    def setupUi(self, MainWindow):
        if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
            QtWidgets.QApplication.setAttribute(
                QtCore.Qt.AA_EnableHighDpiScaling, True)
        if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(834, 899)

        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setBold(False)
        font.setWeight(50)

        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("background-color: rgb(240, 244, 255);")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")

        self.app_name = QtWidgets.QLabel(self.centralwidget)
        self.app_name.setGeometry(QtCore.QRect(210, 40, 691, 111))

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(65)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)

        self.app_name.setFont(font)
        self.app_name.setStyleSheet("color: rgb(21, 146, 255);")
        self.app_name.setObjectName("app_name")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 191, 191))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)

        self.logo.setFont(font)
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("static/images/Logo_blue.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.fake_search = QtWidgets.QLineEdit(self.centralwidget)
        self.fake_search.setGeometry(QtCore.QRect(20, 250, 791, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.fake_search.setFont(font)
        self.fake_search.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.fake_search.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "border: 2px solid #1592ff;\n"
            "border-radius: 20;\n"
            "color: black;\n"
            "")
        self.fake_search.setInputMask("")
        self.fake_search.setText("")
        self.fake_search.setFrame(False)
        self.fake_search.setEchoMode(QtWidgets.QLineEdit.NoEcho)
        self.fake_search.setObjectName("fake_search")

        self.main_text = QtWidgets.QLabel(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(130, 200, 581, 41))

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)

        self.main_text.setFont(font)
        self.main_text.setStyleSheet("color: rgb(21, 146, 255);")
        self.main_text.setObjectName("main_text")

        self.btn_enter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enter.setGeometry(QtCore.QRect(730, 255, 71, 71))

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)

        self.btn_enter.setFont(font)
        self.btn_enter.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_enter.setStyleSheet("QPushButton {\n"
                                     "    color: rgb(21, 146, 255);\n"
                                     "    background-color: #ffffff;\n"
                                     "    border-radius: 30;\n"
                                     "    border: 2px solid #ffffff;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    \n"
                                     "}")
        self.btn_enter.setText("")

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("static/images/export_blue.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)

        self.btn_enter.setIcon(icon)
        self.btn_enter.setIconSize(QtCore.QSize(60, 60))
        self.btn_enter.setObjectName("btn_enter")

        self.Filters_excel = QtWidgets.QLabel(self.centralwidget)
        self.Filters_excel.setGeometry(QtCore.QRect(20, 640, 231, 71))

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.Filters_excel.setFont(font)
        self.Filters_excel.setStyleSheet("color: rgb(21, 146, 255);")
        self.Filters_excel.setObjectName("Filters_excel")

        self.example = QtWidgets.QLabel(self.centralwidget)
        self.example.setGeometry(QtCore.QRect(40, 335, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.example.setFont(font)
        self.example.setStyleSheet("color: rgb(21, 146, 255);\n"
                                   "")
        self.example.setObjectName("example")

        self.entry_identifier = QtWidgets.QCheckBox(self.centralwidget)
        self.entry_identifier.setGeometry(QtCore.QRect(20, 710, 121, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)

        self.entry_identifier.setFont(font)
        self.entry_identifier.setStyleSheet("QCheckBox::indicator {\n"
                                            "     spacing: 50px;\n"
                                            "}")
        self.entry_identifier.setChecked(True)
        self.entry_identifier.setTristate(False)
        self.entry_identifier.setObjectName("entry_identifier")

        self.entry_name = QtWidgets.QCheckBox(self.centralwidget)
        self.entry_name.setGeometry(QtCore.QRect(20, 740, 101, 31))

        font = QtGui.QFont()
        font.setPointSize(11)

        self.entry_name.setFont(font)
        self.entry_name.setChecked(True)
        self.entry_name.setTristate(False)
        self.entry_name.setObjectName("entry_name")

        self.status = QtWidgets.QCheckBox(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(20, 770, 91, 31))

        font = QtGui.QFont()
        font.setPointSize(11)

        self.status.setFont(font)
        self.status.setChecked(True)
        self.status.setTristate(False)
        self.status.setObjectName("status")

        self.protein_name = QtWidgets.QCheckBox(self.centralwidget)
        self.protein_name.setGeometry(QtCore.QRect(20, 800, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.protein_name.setFont(font)
        self.protein_name.setChecked(True)
        self.protein_name.setTristate(False)
        self.protein_name.setObjectName("protein_name")

        self.protein_existence = QtWidgets.QCheckBox(self.centralwidget)
        self.protein_existence.setGeometry(QtCore.QRect(140, 800, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.protein_existence.setFont(font)
        self.protein_existence.setChecked(True)
        self.protein_existence.setTristate(False)
        self.protein_existence.setObjectName("protein_existence")

        self.org_s = QtWidgets.QCheckBox(self.centralwidget)
        self.org_s.setGeometry(QtCore.QRect(140, 710, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.org_s.setFont(font)
        self.org_s.setChecked(True)
        self.org_s.setTristate(False)
        self.org_s.setObjectName("org_s")

        self.gene = QtWidgets.QCheckBox(self.centralwidget)
        self.gene.setGeometry(QtCore.QRect(140, 770, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gene.setFont(font)
        self.gene.setChecked(True)
        self.gene.setTristate(False)
        self.gene.setObjectName("gene")

        self.org_c = QtWidgets.QCheckBox(self.centralwidget)
        self.org_c.setGeometry(QtCore.QRect(140, 740, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.org_c.setFont(font)
        self.org_c.setChecked(True)
        self.org_c.setTristate(False)
        self.org_c.setObjectName("org_c")

        self.id = QtWidgets.QCheckBox(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(345, 800, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.id.setFont(font)
        self.id.setChecked(True)
        self.id.setTristate(False)
        self.id.setObjectName("id")

        self.length = QtWidgets.QCheckBox(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(345, 710, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.length.setFont(font)
        self.length.setChecked(True)
        self.length.setTristate(False)
        self.length.setObjectName("length")

        self.category = QtWidgets.QCheckBox(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(345, 770, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.category.setFont(font)
        self.category.setChecked(True)
        self.category.setTristate(False)
        self.category.setObjectName("category")

        self.mass = QtWidgets.QCheckBox(self.centralwidget)
        self.mass.setGeometry(QtCore.QRect(345, 740, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mass.setFont(font)
        self.mass.setChecked(True)
        self.mass.setTristate(False)
        self.mass.setObjectName("mass")

        self.seq_length = QtWidgets.QCheckBox(self.centralwidget)
        self.seq_length.setGeometry(QtCore.QRect(450, 740, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.seq_length.setFont(font)
        self.seq_length.setChecked(True)
        self.seq_length.setTristate(False)
        self.seq_length.setObjectName("seq_length")

        self.occurrence = QtWidgets.QCheckBox(self.centralwidget)
        self.occurrence.setGeometry(QtCore.QRect(450, 770, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.occurrence.setFont(font)
        self.occurrence.setChecked(True)
        self.occurrence.setTristate(False)
        self.occurrence.setObjectName("occurrence")

        self.relative = QtWidgets.QCheckBox(self.centralwidget)
        self.relative.setGeometry(QtCore.QRect(590, 770, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.relative.setFont(font)
        self.relative.setChecked(True)
        self.relative.setTristate(False)
        self.relative.setObjectName("relative")

        self.sequence = QtWidgets.QCheckBox(self.centralwidget)
        self.sequence.setGeometry(QtCore.QRect(450, 710, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sequence.setFont(font)
        self.sequence.setChecked(True)
        self.sequence.setTristate(False)
        self.sequence.setObjectName("sequence")

        self.cter = QtWidgets.QCheckBox(self.centralwidget)
        self.cter.setGeometry(QtCore.QRect(590, 740, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cter.setFont(font)
        self.cter.setChecked(True)
        self.cter.setTristate(False)
        self.cter.setObjectName("cter")

        self.nter = QtWidgets.QCheckBox(self.centralwidget)
        self.nter.setGeometry(QtCore.QRect(590, 710, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nter.setFont(font)
        self.nter.setChecked(True)
        self.nter.setTristate(False)
        self.nter.setObjectName("nter")

        self.position = QtWidgets.QCheckBox(self.centralwidget)
        self.position.setGeometry(QtCore.QRect(450, 800, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.position.setFont(font)
        self.position.setChecked(True)
        self.position.setTristate(False)
        self.position.setObjectName("position")

        self.input_text = QtWidgets.QLabel(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(40, 370, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet("color: rgb(21, 146, 255);")
        self.input_text.setObjectName("input_text")

        self.searchbox = QtWidgets.QLineEdit(self.centralwidget)
        self.searchbox.setGeometry(QtCore.QRect(22, 255, 701, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(27)
        self.searchbox.setFont(font)
        self.searchbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "border: 2px solid #ffffff;\n"
                                     "border-radius: 20;\n"
                                     "color: balck;")
        self.searchbox.setObjectName("searchbox")

        self.Filters_peptides = QtWidgets.QLabel(self.centralwidget)
        self.Filters_peptides.setGeometry(QtCore.QRect(440, 600, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Filters_peptides.setFont(font)
        self.Filters_peptides.setStyleSheet("color: rgb(21, 146, 255);\n"
                                            "")
        self.Filters_peptides.setObjectName("Filters_peptides")
        self.btn_peptides_filter = QtWidgets.QToolButton(self.centralwidget)
        self.btn_peptides_filter.setGeometry(QtCore.QRect(670, 600, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_peptides_filter.setFont(font)
        self.btn_peptides_filter.setStyleSheet(
            "QToolButton {\n"
            "    color: black;\n"
            "    background-color:rgb(255, 255, 255);\n"
            "    border-radius: 7;\n"
            "    border: 2px solid #1592ff;\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "    background-color: #dfdfdf;\n"
            "}")
        self.btn_peptides_filter.setObjectName("btn_peptides_filter")
        self.btn_input_file_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_input_file_2.setGeometry(QtCore.QRect(250, 375, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_input_file_2.setFont(font)
        self.btn_input_file_2.setStyleSheet("QPushButton {\n"
                                            "    color: black;\n"
                                            "    background-color: #ffffff;\n"
                                            "    border-radius: 7;\n"
                                            "    border: 2px solid #1592ff;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #dfdfdf;\n"
                                            "}")
        self.btn_input_file_2.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                            QtWidgets.QSizePolicy.Expanding)

        self.btn_input_file_2.setObjectName("btn_input_file_2")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 860, 811, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setEnabled(False)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 430, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(21, 146, 255);")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 590, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(21, 146, 255);\n"
                                   "")
        self.label_3.setObjectName("label_3")

        self.btn_input_db = QtWidgets.QPushButton(self.centralwidget)
        self.btn_input_db.setGeometry(QtCore.QRect(280, 600, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_input_db.setFont(font)
        self.btn_input_db.setStyleSheet("QPushButton {\n"
                                        "    color: black;\n"
                                        "    background-color: #ffffff;\n"
                                        "    border-radius: 7;\n"
                                        "    border: 2px solid #1592ff;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #dfdfdf;\n"
                                        "}")
        self.btn_input_db.setObjectName("btn_input_db")

        self.example_2 = QtWidgets.QLabel(self.centralwidget)
        self.example_2.setGeometry(QtCore.QRect(40, 560, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.example_2.setFont(font)
        self.example_2.setStyleSheet("color: rgb(21, 146, 255);\n"
                                     "")
        self.example_2.setObjectName("example_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 470, 791, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(27)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border: 2px solid #1592ff;\n"
                                    "border-radius: 20;\n"
                                    "color: black;\n"
                                    "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_enter.clicked.connect(self.send_proteins)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UniPeptides"))
        self.app_name.setText(_translate("MainWindow", "UniPeptides"))
        self.main_text.setText(
            _translate(
                "MainWindow",
                "Enter one or more protein entry names"))
        self.Filters_excel.setText(_translate("MainWindow", "Excel filters"))
        self.example.setText(
            _translate(
                "MainWindow",
                "Example: P05067, A0A0C5B5G6, B7U540"))
        self.entry_identifier.setText(
            _translate("MainWindow", "Entry identifier"))
        self.entry_name.setText(_translate("MainWindow", "Entry name"))
        self.status.setText(_translate("MainWindow", "Status"))
        self.protein_name.setText(_translate("MainWindow", "Protein name"))
        self.protein_existence.setText(
            _translate("MainWindow", "Protein existence"))
        self.org_s.setText(
            _translate(
                "MainWindow",
                "Organism (scientific name)"))
        self.gene.setText(_translate("MainWindow", "Gene name"))
        self.org_c.setText(_translate("MainWindow", "Organism (common name)"))
        self.id.setText(_translate("MainWindow", "Peptide ID"))
        self.length.setText(_translate("MainWindow", "Length"))
        self.category.setText(_translate("MainWindow", "Category"))
        self.mass.setText(_translate("MainWindow", "Mass (Da)"))
        self.seq_length.setText(_translate("MainWindow", "Sequence length"))
        self.occurrence.setText(_translate("MainWindow", "Occurrence"))
        self.relative.setText(
            _translate(
                "MainWindow",
                "Relative (per 1000 amino acids)"))
        self.sequence.setText(_translate("MainWindow", "Sequence"))
        self.cter.setText(
            _translate(
                "MainWindow",
                "Amino acid from the C-terminus"))
        self.nter.setText(
            _translate(
                "MainWindow",
                "Amino acid from the N-terminus"))
        self.position.setText(_translate("MainWindow", "Position"))
        self.input_text.setText(_translate("MainWindow", "Or import txt file"))
        self.Filters_peptides.setText(
            _translate(
                "MainWindow",
                "Peptides database"))
        self.btn_peptides_filter.setText(_translate("MainWindow", "Create"))
        self.btn_input_file_2.setText(
            _translate("MainWindow", "Select a file"))
        # self.label.setText(_translate("MainWindow", "Selected: "))
        self.label_2.setText(_translate("MainWindow", "Enter peptides"))
        self.label_3.setText(_translate("MainWindow", "Or import database"))
        self.btn_input_db.setText(_translate("MainWindow", "Select a file"))
        self.example_2.setText(
            _translate(
                "MainWindow",
                "Example: VGLPNSR, MVGSAPGVL, HGPLGPL"))

        self.btn_input_db.clicked.connect(self.open_database)
        self.btn_input_file_2.clicked.connect(self.open_input)

    def send_proteins(self):
        self.prot_value = self.searchbox.text()
        self.peptides_value = self.lineEdit.text()
        self.searchbox.setText("")
        self.lineEdit.setText("")
        if len(self.peptides_value) > 1:
            try:
                fpeptides = open("cfg/Peptides.txt", "w")
                fpeptides.write(self.peptides_value)
                fpeptides.close()
            except BaseException:
                print('Saving proteins - error')
        try:
            save_path = QFileDialog.getExistingDirectory()
            line = self.get_line("User_config.txt")
            if "Save_Path:" not in line:
                config = open("cfg/User_config.txt", "w", encoding="utf-8")
                new_line = line + f"Save_Path:{save_path} @"
                config.write(new_line)
                config.close()
            else:
                config = open("cfg/User_config.txt", "w", encoding="utf-8")
                save_path_index = line.find("Save_Path:")
                if save_path != line[save_path_index + 10: save_path_index + 10 + line.find("@") - 1]:
                    new_line = line[0: line.find("Save_Path:")] + line[line.find("@") + 1: len(
                        line)] + f" Save_Path:{save_path} @"
                    config.write(new_line)
                    config.close()

            line = self.get_line("User_config.txt")
            filters = ''
            if self.entry_identifier.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.entry_name.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.status.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.protein_name.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.org_s.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.org_c.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.gene.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.protein_existence.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.length.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.mass.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.category.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.id.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.sequence.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.seq_length.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.occurrence.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.relative.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.position.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.nter.isChecked():
                filters += '1'
            else:
                filters += '0'
            if self.cter.isChecked():
                filters += '1'
            else:
                filters += '0'
            if "Excel filters:" not in line:
                config = open("cfg/User_config.txt", "w", encoding="utf-8")
                with config:
                    new_line = line + ' ' + f'Excel filters:{filters}'
                    config.write(new_line)
                    config.close()
            else:
                config = open("cfg/User_config.txt", "r", encoding="utf-8")
                cfg = config.readline()
                config.close()
                filters_index = cfg.find("Excel filters:")
                if filters != cfg[filters_index + 14: filters_index + 34]:
                    config = open("cfg/User_config.txt", "w", encoding="utf-8")
                    new_line = cfg[0: filters_index] + cfg[filters_index + 34: len(cfg)] + f" Excel filters:{filters}"
                    config.write(new_line)
                    config.close()

            if len(self.prot_value) > 1:
                try:
                    with open("cfg/Proteins.txt", "w", encoding="utf-8") as file_prot:
                        line = str(self.prot_value)
                        file_prot.write(line)
                        file_prot.close()
                    try:
                        self.btn_enter.setEnabled(False)
                        self.btn_input_file_2.setEnabled(False)
                        self.btn_peptides_filter.setEnabled(False)
                        self.progressBar.setEnabled(True)
                        self.backgroundStream = QProcess()
                        self.backgroundStream.finished.connect(self.finish)
                        self.backgroundStream.start('python', ["back.py"])
                        self.count_time = 0
                        self.timer.start(700)
                        while self.count_time < 19:
                            self.__DoNothing()
                            QApplication.processEvents()
                    except Exception as e:
                        print(e)
                except BaseException:
                    print('QProcess - error (1)')
                    self.proteinErrorMessage(line=line)

            else:
                try:
                    self.names = ''
                    line = self.get_line("User_proteins.txt")
                    for i in range(len(line)):
                        self.names += line[i].rstrip('\n') + ' '
                    prot = open("cfg/Proteins.txt", "w", encoding="utf-8")
                    line = str(self.names)
                    prot.write(line)
                    prot.close()
                    try:
                        self.btn_enter.setEnabled(False)
                        self.btn_input_file_2.setEnabled(False)
                        self.btn_peptides_filter.setEnabled(False)
                        self.progressBar.setEnabled(True)
                        self.backgroundStream = QProcess()
                        self.backgroundStream.finished.connect(self.finish)
                        self.backgroundStream.startDetached('python', ["back.py"])
                        self.count_time = 0
                        self.timer.start(700)
                        while self.count_time < 19:
                            self.__DoNothing()
                            QApplication.processEvents()
                    except BaseException:
                        print('QProcess - error (2)')
                except BaseException:
                    print("User file - error")
                    self.proteinErrorMessage(line=line)

        except BaseException:
            print('Input error')
            logs = open("cfg/Log error.txt")
            line = logs.readline()
            if len(line) > 2:
                self.proteinErrorMessage(line=line)

    def finish(self):
        self.backgroundStream = None
        self.btn_enter.setEnabled(True)
        self.btn_peptides_filter.setEnabled(True)
        self.btn_input_file_2.setEnabled(True)
        self.timer.stop()
        self.progressBar.setValue(100)
        self.progressBar.setEnabled(False)

        logs = open("cfg/Log error.txt")
        line = (logs.readline()).split()
        if len(line) > 0:
            self.proteinErrorMessage(line=line)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ready")
            msg.setText(
                "Ready! "
                "If you see the value None in the columns, try to run the program again."
                "If that doesn't help, maybe:"
                " 1)There is no information on Uniprot."
                " 2) Those problems with the Uniprot website."
                " 3)There was a software error with this protein")
            msg.setFixedSize(600, 600)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def readOut(self):
        out = self.backgroundStream.readAll()
        out = str(out).rstrip().replace("b", '')
        print(out[1:out.find('%') + 1])
        try:
            self.progressBar.setValue(int(out[1:out.find('%')]))
        except:
            pass

    def open_database(self):
        try:
            self.database_name = QFileDialog.getOpenFileName()[0]
            db = open("cfg/Database.txt", "w")
            db.write(self.database_name)
            data = self.database_name.split('/')
            self.database_name = data[-1]
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ready")
            msg.setText(f"Selected: {self.database_name}")
            msg.setFixedSize(600, 600)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.btn_input_db.setText(f"{self.database_name}")
            self.btn_input_db.adjustSize()
            self.btn_input_db.setGeometry(QtCore.QRect(280, 600, self.btn_input_db.width() + 5, 31))
        except BaseException:
            pass

    def open_input(self):
        try:
            self.fname = QFileDialog.getOpenFileName()[0]
            f = open(self.fname, 'r')
            with f:
                data = f.read()
                f.close()
            user_proteins = open(
                "cfg/User_proteins.txt", "w", encoding="utf-8")
            user_proteins.write(data)
            user_proteins.close()
            data = self.fname.split('/')
            self.filename = data[-1]
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ready")
            msg.setText(f"Selected: {self.filename}")
            msg.setFixedSize(600, 600)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.btn_input_file_2.setText(f"{self.filename}")
            self.btn_input_file_2.adjustSize()
            self.btn_input_file_2.setGeometry(QtCore.QRect(250, 375, self.btn_input_file_2.width() + 5, 31))
        except BaseException:
            print("Input userfile - error")

    def updateTime(self):
        self.count_time += 1
        if self.count_time == 20:
            self.timer.stop()
            return
        self.progressBar.setValue(self.count_time * 5)

    def __DoNothing(self):
        """print('Nothing')
        time.sleep(0.250)"""
        pass

    def proteinErrorMessage(self, line):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("Error")
        error_dialog.setInformativeText(f"Proteins: {','.join(line)}")
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()

    def get_line(self, filename):
        with open(f"cfg/{filename}", "r", encoding="utf-8") as file:
            line = file.readline()
            file.close()
            return line

if __name__ == "__main__":
    setupConfig()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())