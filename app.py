import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QProcess
from setup import setupConfig, saveFilters, creatingLogs
import sys
import json
import re


def screenSize():
    sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
    print("Screen size : " + str(sizeObject.width()) +
          "x" + str(sizeObject.height()))


class Ui_MainWindow(object):
    def setupFilters(self):
        import os.path
        if os.path.exists("config.json"):
            with open("config.json", "r") as cfg:
                config_data = json.load(cfg)
                self.entry_identifier.setChecked(config_data["excelFilters"]["entryIdentifier"])
                self.entry_name.setChecked( config_data["excelFilters"]["entryName"])
                self.status.setChecked(config_data["excelFilters"]["entryType"])
                self.protein_name.setChecked(config_data["excelFilters"]["fullName"])
                self.org_s.setChecked(config_data["excelFilters"]["scientificName"])
                self.org_c.setChecked(config_data["excelFilters"]["commonName"])
                self.gene.setChecked(config_data["excelFilters"]["genes"])
                self.protein_existence.setChecked(config_data["excelFilters"]["proteinExistence"])
                self.length.setChecked(config_data["excelFilters"]["length"])
                self.mass.setChecked(config_data["excelFilters"]["massDa"])
                self.category.setChecked(config_data["excelFilters"]["category"])
                self.id.setChecked(config_data["excelFilters"]["id"])
                self.sequence.setChecked(config_data["excelFilters"]["sequence"])
                self.seq_length.setChecked(config_data["excelFilters"]["sequence_length"])
                self.occurrence.setChecked(config_data["excelFilters"]["occurrence"])
                self.relative.setChecked(config_data["excelFilters"]["relative"])
                self.position.setChecked(config_data["excelFilters"]["position"])
                self.nter.setChecked(config_data["excelFilters"]["nter"])
                self.cter.setChecked(config_data["excelFilters"]["cter"])
                saveFilters()
        else:
            setupConfig()

    def setupUi(self, MainWindow):
        if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
            QtWidgets.QApplication.setAttribute(
                QtCore.Qt.AA_EnableHighDpiScaling, True)
        if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1260, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.app_name = QtWidgets.QLabel(self.centralwidget)
        self.app_name.setGeometry(QtCore.QRect(150, 20, 931, 111))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(55)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet("color: rgb(21, 146, 255);\n"
"\n"
"")
        self.app_name.setObjectName("app_name")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 10, 131, 131))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.logo.setFont(font)
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setPixmap(QtGui.QPixmap("static/images/Logo_blue.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setOpenExternalLinks(False)
        self.logo.setObjectName("logo")
        self.btn_theme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_theme.setGeometry(QtCore.QRect(1094, 60, 43, 43))
        self.btn_theme.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #1592FF;\n"
"    border-radius: 7;\n"
"    border: 4px solid #1592ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2264ff;\n"
"    border: 4px solid #2264ff;\n"
"}")
        self.btn_theme.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/images/icon-white-moon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_theme.setIcon(icon)
        self.btn_theme.setIconSize(QtCore.QSize(37, 37))
        self.btn_theme.setCheckable(False)
        self.btn_theme.setObjectName("btn_theme")
        self.btn_info = QtWidgets.QPushButton(self.centralwidget)
        self.btn_info.setGeometry(QtCore.QRect(1147, 60, 43, 43))
        self.btn_info.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #1592FF;\n"
"    border-radius: 7;\n"
"    border: 4px solid #1592ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2264ff;\n"
"    border: 4px solid #2264ff;\n"
"}")
        self.btn_info.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/images/icon-white-info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_info.setIcon(icon1)
        self.btn_info.setIconSize(QtCore.QSize(38, 38))
        self.btn_info.setCheckable(False)
        self.btn_info.setObjectName("btn_info")
        self.btn_lang = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lang.setGeometry(QtCore.QRect(1200, 60, 43, 43))
        self.btn_lang.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #1592FF;\n"
"    border-radius: 7;\n"
"    border: 4px solid #1592ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2264ff;\n"
"    border: 4px solid #2264ff;\n"
"}")
        self.btn_lang.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../WebstormProjects/untitled/public/united-kingdom.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_lang.setIcon(icon2)
        self.btn_lang.setIconSize(QtCore.QSize(30, 30))
        self.btn_lang.setCheckable(False)
        self.btn_lang.setObjectName("btn_lang")
        self.step1_background = QtWidgets.QLabel(self.centralwidget)
        self.step1_background.setGeometry(QtCore.QRect(17, 160, 471, 301))
        self.step1_background.setStyleSheet("background-color: #F2F2F2;\n"
"border-radius: 20;")
        self.step1_background.setText("")
        self.step1_background.setObjectName("step1_background")
        self.step2_background = QtWidgets.QLabel(self.centralwidget)
        self.step2_background.setGeometry(QtCore.QRect(17, 500, 471, 301))
        self.step2_background.setStyleSheet("background-color: #F2F2F2;\n"
"border-radius: 20;")
        self.step2_background.setText("")
        self.step2_background.setObjectName("step2_background")
        self.step3_background = QtWidgets.QLabel(self.centralwidget)
        self.step3_background.setGeometry(QtCore.QRect(510, 160, 300, 641))
        self.step3_background.setStyleSheet("background-color: #F2F2F2;\n"
"border-radius: 20;")
        self.step3_background.setText("")
        self.step3_background.setObjectName("step3_background")
        self.step1_lable = QtWidgets.QLabel(self.centralwidget)
        self.step1_lable.setGeometry(QtCore.QRect(30, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.step1_lable.setFont(font)
        self.step1_lable.setStyleSheet("background-color: #F2F2F2;\n"
"color: rgb(21, 146, 255);\n"
"\n"
"")
        self.step1_lable.setObjectName("step1_lable")
        self.step2_lable = QtWidgets.QLabel(self.centralwidget)
        self.step2_lable.setGeometry(QtCore.QRect(30, 510, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.step2_lable.setFont(font)
        self.step2_lable.setStyleSheet("background-color: #F2F2F2;\n"
"color: rgb(21, 146, 255);\n"
"\n"
"")
        self.step2_lable.setObjectName("step2_lable")
        self.step3_lable = QtWidgets.QLabel(self.centralwidget)
        self.step3_lable.setGeometry(QtCore.QRect(525, 170, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.step3_lable.setFont(font)
        self.step3_lable.setStyleSheet("background-color: #F2F2F2;\n"
"color: rgb(21, 146, 255);\n"
"\n"
"")
        self.step3_lable.setObjectName("step3_lable")
        self.entry_name = QtWidgets.QCheckBox(self.centralwidget)
        self.entry_name.setGeometry(QtCore.QRect(530, 250, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.entry_name.setFont(font)
        self.entry_name.setStyleSheet("background-color: #F2F2F2;")
        self.entry_name.setChecked(True)
        self.entry_name.setTristate(False)
        self.entry_name.setObjectName("entry_name")
        self.entry_identifier = QtWidgets.QCheckBox(self.centralwidget)
        self.entry_identifier.setEnabled(True)
        self.entry_identifier.setGeometry(QtCore.QRect(530, 220, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.entry_identifier.setFont(font)
        self.entry_identifier.setStyleSheet("background-color: #F2F2F2;\n"
"")
        self.entry_identifier.setCheckable(True)
        self.entry_identifier.setChecked(True)
        self.entry_identifier.setTristate(False)
        self.entry_identifier.setObjectName("entry_identifier")
        self.protein_name = QtWidgets.QCheckBox(self.centralwidget)
        self.protein_name.setGeometry(QtCore.QRect(530, 310, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.protein_name.setFont(font)
        self.protein_name.setStyleSheet("background-color: #F2F2F2;")
        self.protein_name.setChecked(True)
        self.protein_name.setTristate(False)
        self.protein_name.setObjectName("protein_name")
        self.status = QtWidgets.QCheckBox(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(530, 280, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.status.setFont(font)
        self.status.setStyleSheet("background-color: #F2F2F2;")
        self.status.setChecked(True)
        self.status.setTristate(False)
        self.status.setObjectName("status")
        self.org_c = QtWidgets.QCheckBox(self.centralwidget)
        self.org_c.setGeometry(QtCore.QRect(530, 370, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.org_c.setFont(font)
        self.org_c.setStyleSheet("background-color: #F2F2F2;")
        self.org_c.setChecked(True)
        self.org_c.setTristate(False)
        self.org_c.setObjectName("org_c")
        self.gene = QtWidgets.QCheckBox(self.centralwidget)
        self.gene.setGeometry(QtCore.QRect(530, 400, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.gene.setFont(font)
        self.gene.setStyleSheet("background-color: #F2F2F2;")
        self.gene.setChecked(True)
        self.gene.setTristate(False)
        self.gene.setObjectName("gene")
        self.protein_existence = QtWidgets.QCheckBox(self.centralwidget)
        self.protein_existence.setGeometry(QtCore.QRect(530, 430, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.protein_existence.setFont(font)
        self.protein_existence.setStyleSheet("background-color: #F2F2F2;")
        self.protein_existence.setChecked(True)
        self.protein_existence.setTristate(False)
        self.protein_existence.setObjectName("protein_existence")
        self.org_s = QtWidgets.QCheckBox(self.centralwidget)
        self.org_s.setGeometry(QtCore.QRect(530, 340, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.org_s.setFont(font)
        self.org_s.setStyleSheet("background-color: #F2F2F2;")
        self.org_s.setChecked(True)
        self.org_s.setTristate(False)
        self.org_s.setObjectName("org_s")
        self.id = QtWidgets.QCheckBox(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(530, 550, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.id.setFont(font)
        self.id.setStyleSheet("background-color: #F2F2F2;")
        self.id.setChecked(True)
        self.id.setTristate(False)
        self.id.setObjectName("id")
        self.mass = QtWidgets.QCheckBox(self.centralwidget)
        self.mass.setGeometry(QtCore.QRect(530, 490, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mass.setFont(font)
        self.mass.setStyleSheet("background-color: #F2F2F2;")
        self.mass.setChecked(True)
        self.mass.setTristate(False)
        self.mass.setObjectName("mass")
        self.category = QtWidgets.QCheckBox(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(530, 520, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.category.setFont(font)
        self.category.setStyleSheet("background-color: #F2F2F2;")
        self.category.setChecked(True)
        self.category.setTristate(False)
        self.category.setObjectName("category")
        self.length = QtWidgets.QCheckBox(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(530, 460, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.length.setFont(font)
        self.length.setStyleSheet("background-color: #F2F2F2;")
        self.length.setChecked(True)
        self.length.setTristate(False)
        self.length.setObjectName("length")
        self.seq_length = QtWidgets.QCheckBox(self.centralwidget)
        self.seq_length.setGeometry(QtCore.QRect(530, 610, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.seq_length.setFont(font)
        self.seq_length.setStyleSheet("background-color: #F2F2F2;")
        self.seq_length.setChecked(True)
        self.seq_length.setTristate(False)
        self.seq_length.setObjectName("seq_length")
        self.occurrence = QtWidgets.QCheckBox(self.centralwidget)
        self.occurrence.setGeometry(QtCore.QRect(530, 640, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.occurrence.setFont(font)
        self.occurrence.setStyleSheet("background-color: #F2F2F2;")
        self.occurrence.setChecked(True)
        self.occurrence.setTristate(False)
        self.occurrence.setObjectName("occurrence")
        self.sequence = QtWidgets.QCheckBox(self.centralwidget)
        self.sequence.setGeometry(QtCore.QRect(530, 580, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sequence.setFont(font)
        self.sequence.setStyleSheet("background-color: #F2F2F2;")
        self.sequence.setChecked(True)
        self.sequence.setTristate(False)
        self.sequence.setObjectName("sequence")
        self.position = QtWidgets.QCheckBox(self.centralwidget)
        self.position.setGeometry(QtCore.QRect(530, 670, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.position.setFont(font)
        self.position.setStyleSheet("background-color: #F2F2F2;")
        self.position.setChecked(True)
        self.position.setTristate(False)
        self.position.setObjectName("position")
        self.relative = QtWidgets.QCheckBox(self.centralwidget)
        self.relative.setGeometry(QtCore.QRect(530, 760, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.relative.setFont(font)
        self.relative.setStyleSheet("background-color: #F2F2F2;")
        self.relative.setChecked(True)
        self.relative.setTristate(False)
        self.relative.setObjectName("relative")
        self.nter = QtWidgets.QCheckBox(self.centralwidget)
        self.nter.setGeometry(QtCore.QRect(530, 700, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nter.setFont(font)
        self.nter.setStyleSheet("background-color: #F2F2F2;")
        self.nter.setChecked(True)
        self.nter.setTristate(False)
        self.nter.setObjectName("nter")
        self.cter = QtWidgets.QCheckBox(self.centralwidget)
        self.cter.setGeometry(QtCore.QRect(530, 730, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cter.setFont(font)
        self.cter.setStyleSheet("background-color: #F2F2F2;")
        self.cter.setChecked(True)
        self.cter.setTristate(False)
        self.cter.setObjectName("cter")
        self.blueStep1 = QtWidgets.QLabel(self.centralwidget)
        self.blueStep1.setGeometry(QtCore.QRect(30, 230, 445, 211))
        self.blueStep1.setStyleSheet("background-color: rgb(21, 146, 255);\n"
"border-radius: 15;")
        self.blueStep1.setText("")
        self.blueStep1.setObjectName("blueStep1")
        self.blueStep2 = QtWidgets.QLabel(self.centralwidget)
        self.blueStep2.setGeometry(QtCore.QRect(30, 570, 445, 211))
        self.blueStep2.setStyleSheet("background-color: rgb(21, 146, 255);\n"
"border-radius: 15;")
        self.blueStep2.setText("")
        self.blueStep2.setObjectName("blueStep2")
        self.step1Text = QtWidgets.QLabel(self.centralwidget)
        self.step1Text.setGeometry(QtCore.QRect(102, 230, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.step1Text.setFont(font)
        self.step1Text.setStyleSheet("background-color: rgb(21, 146, 255);\n"
"color: rgb(255, 255, 255);")
        self.step1Text.setObjectName("step1Text")
        self.step2Text = QtWidgets.QLabel(self.centralwidget)
        self.step2Text.setGeometry(QtCore.QRect(96, 570, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.step2Text.setFont(font)
        self.step2Text.setStyleSheet("background-color: rgb(21, 146, 255);\n"
"color: rgb(255, 255, 255);")
        self.step2Text.setObjectName("step2Text")
        self.proteinsInput = QtWidgets.QLineEdit(self.centralwidget)
        self.proteinsInput.setGeometry(QtCore.QRect(40, 280, 425, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.proteinsInput.setFont(font)
        self.proteinsInput.setStyleSheet("border-radius: 13px;")
        self.proteinsInput.setText("")
        self.proteinsInput.setObjectName("proteinsInput")
        self.peptidesInput = QtWidgets.QLineEdit(self.centralwidget)
        self.peptidesInput.setGeometry(QtCore.QRect(40, 620, 425, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.peptidesInput.setFont(font)
        self.peptidesInput.setStyleSheet("border-radius: 13px;")
        self.peptidesInput.setObjectName("peptidesInput")
        self.or_step1 = QtWidgets.QLabel(self.centralwidget)
        self.or_step1.setGeometry(QtCore.QRect(235, 360, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.or_step1.setFont(font)
        self.or_step1.setStyleSheet("background-color: rgb(21, 146, 255);\n"
"color: rgb(255, 255, 255);")
        self.or_step1.setObjectName("label")
        self.or_step2 = QtWidgets.QLabel(self.centralwidget)
        self.or_step2.setGeometry(QtCore.QRect(235, 700, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.or_step2.setFont(font)
        self.or_step2.setStyleSheet("background-color: rgb(21, 146, 255);\n"
"color: rgb(255, 255, 255);")
        self.or_step2.setObjectName("label_2")
        self.import_step1 = QtWidgets.QLabel(self.centralwidget)
        self.import_step1.setGeometry(QtCore.QRect(100, 390, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.import_step1.setFont(font)
        self.import_step1.setStyleSheet("background-color: rgb(21, 146, 255);\n"
"color: rgb(255, 255, 255);")
        self.import_step1.setObjectName("label_3")
        self.import_step2 = QtWidgets.QLabel(self.centralwidget)
        self.import_step2.setGeometry(QtCore.QRect(100, 730, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.import_step2.setFont(font)
        self.import_step2.setStyleSheet("background-color: rgb(21, 146, 255);\n"
"color: rgb(255, 255, 255);")
        self.import_step2.setObjectName("label_4")
        self.btn_input_proteins = QtWidgets.QPushButton(self.centralwidget)
        self.btn_input_proteins.setGeometry(QtCore.QRect(250, 390, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_input_proteins.setFont(font)
        self.btn_input_proteins.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #ffffff;\n"
"    border-radius: 7;\n"
"    border: 2px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dfdfdf;\n"
"}")
        self.btn_input_proteins.setObjectName("btn_input_file_2")
        self.btn_input_peptides = QtWidgets.QPushButton(self.centralwidget)
        self.btn_input_peptides.setGeometry(QtCore.QRect(250, 730, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_input_peptides.setFont(font)
        self.btn_input_peptides.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #ffffff;\n"
"    border-radius: 7;\n"
"    border: 2px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dfdfdf;\n"
"}")
        self.btn_input_peptides.setObjectName("btn_input_file_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(840, 560, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    text-align: center;\n"
"    border: 1px solid #1592ff;\n"
"    border-radius: 10px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(21, 146, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setDisabled(False)
        self.step1_background_2 = QtWidgets.QLabel(self.centralwidget)
        self.step1_background_2.setGeometry(QtCore.QRect(830, 160, 411, 461))
        self.step1_background_2.setStyleSheet("background-color: #F2F2F2;\n"
"border-radius: 20;")
        self.step1_background_2.setText("")
        self.step1_background_2.setObjectName("step1_background_2")
        self.info_lable = QtWidgets.QLabel(self.centralwidget)
        self.info_lable.setGeometry(QtCore.QRect(830, 210, 391, 251))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.info_lable.setFont(font)
        self.info_lable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info_lable.setStyleSheet("background-color: #F2F2F2;")
        self.info_lable.setWordWrap(True)
        self.info_lable.setIndent(35)
        self.info_lable.setObjectName("label_5")
        self.step3_lable_2 = QtWidgets.QLabel(self.centralwidget)
        self.step3_lable_2.setGeometry(QtCore.QRect(985, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.step3_lable_2.setFont(font)
        self.step3_lable_2.setStyleSheet("background-color: #F2F2F2;\n"
"color: rgb(21, 146, 255);\n"
"\n"
"")
        self.step3_lable_2.setObjectName("step3_lable_2")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(910, 480, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #ffffff;\n"
"    border-radius: 15;\n"
"    border: 3px solid #1592ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dfdfdf;\n"
"}")
        self.btn_start.setObjectName("btn_input_file_4")
        self.btn_open_results = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_results.setEnabled(False)
        self.btn_open_results.setGeometry(QtCore.QRect(830, 650, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_open_results.setFont(font)
        self.btn_open_results.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #ffffff;\n"
"    border-radius: 15;\n"
"    border: 3px solid #1592ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dfdfdf;\n"
"}\n"
"QPushButton:disabled {\n"
"    color: rgb(177, 177, 177);\n"
"    background-color: #ffffff;\n"
"    border-radius: 15;\n"
"    border: 3px solid #1592ff;\n"
"}")
        self.btn_open_results.setAutoDefault(False)
        self.btn_open_results.setDefault(False)
        self.btn_open_results.setFlat(False)
        self.btn_open_results.setObjectName("btn_input_file_5")
        self.btn_clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_all.setGeometry(QtCore.QRect(1040, 720, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_clear_all.setFont(font)
        self.btn_clear_all.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #ffffff;\n"
"    border-radius: 15;\n"
"    border: 3px solid #1592ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dfdfdf;\n"
"}")
        self.btn_clear_all.setObjectName("btn_input_file_6")
        self.btn_reset_filters = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset_filters.setGeometry(QtCore.QRect(830, 720, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_reset_filters.setFont(font)
        self.btn_reset_filters.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #ffffff;\n"
"    border-radius: 15;\n"
"    border: 3px solid #1592ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dfdfdf;\n"
"}")
        self.btn_reset_filters.setObjectName("btn_input_file_7")
        self.btn_del_results = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del_results.setEnabled(False)
        self.btn_del_results.setGeometry(QtCore.QRect(1040, 650, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_del_results.setFont(font)
        self.btn_del_results.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #ffffff;\n"
"    border-radius: 15;\n"
"    border: 3px solid #1592ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dfdfdf;\n"
"}\n"
"QPushButton:disabled {\n"
"    color: rgb(177, 177, 177);\n"
"    background-color: #ffffff;\n"
"    border-radius: 15;\n"
"    border: 3px solid #1592ff;\n"
"}")
        self.btn_del_results.setObjectName("btn_input_file_8")
        self.app_name.raise_()
        self.logo.raise_()
        self.btn_theme.raise_()
        self.btn_info.raise_()
        self.btn_lang.raise_()
        self.step1_background.raise_()
        self.step2_background.raise_()
        self.step3_background.raise_()
        self.step1_lable.raise_()
        self.step2_lable.raise_()
        self.step3_lable.raise_()
        self.entry_name.raise_()
        self.entry_identifier.raise_()
        self.protein_name.raise_()
        self.status.raise_()
        self.org_c.raise_()
        self.gene.raise_()
        self.protein_existence.raise_()
        self.org_s.raise_()
        self.id.raise_()
        self.mass.raise_()
        self.category.raise_()
        self.length.raise_()
        self.seq_length.raise_()
        self.occurrence.raise_()
        self.sequence.raise_()
        self.position.raise_()
        self.relative.raise_()
        self.nter.raise_()
        self.cter.raise_()
        self.blueStep1.raise_()
        self.blueStep2.raise_()
        self.step1Text.raise_()
        self.step2Text.raise_()
        self.proteinsInput.raise_()
        self.peptidesInput.raise_()
        self.or_step1.raise_()
        self.or_step2.raise_()
        self.import_step1.raise_()
        self.import_step2.raise_()
        self.btn_input_proteins.raise_()
        self.btn_input_peptides.raise_()
        self.step1_background_2.raise_()
        self.info_lable.raise_()
        self.step3_lable_2.raise_()
        self.progressBar.raise_()
        self.btn_start.raise_()
        self.btn_open_results.raise_()
        self.btn_clear_all.raise_()
        self.btn_reset_filters.raise_()
        self.btn_del_results.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.theme = "light"
        self.setupFilters()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_name.setText(_translate("MainWindow", "UniPeptides"))
        self.step1_lable.setText(_translate("MainWindow", "Step 1"))
        self.step2_lable.setText(_translate("MainWindow", "Step 2"))
        self.step3_lable.setText(_translate("MainWindow", "Step 3"))
        self.entry_name.setText(_translate("MainWindow", " Entry name"))
        self.entry_identifier.setText(_translate("MainWindow", " Entry identifier"))
        self.protein_name.setText(_translate("MainWindow", " Protein name"))
        self.status.setText(_translate("MainWindow", " Status"))
        self.org_c.setText(_translate("MainWindow", " Organism (common name)"))
        self.gene.setText(_translate("MainWindow", " Gene name"))
        self.protein_existence.setText(_translate("MainWindow", " Protein existence"))
        self.org_s.setText(_translate("MainWindow", " Organism (scientific name)"))
        self.id.setText(_translate("MainWindow", " Peptide ID"))
        self.mass.setText(_translate("MainWindow", " Mass (Da)"))
        self.category.setText(_translate("MainWindow", " Category"))
        self.length.setText(_translate("MainWindow", " Length"))
        self.seq_length.setText(_translate("MainWindow", " Sequence length"))
        self.occurrence.setText(_translate("MainWindow", " Occurrence"))
        self.sequence.setText(_translate("MainWindow", " Sequence"))
        self.position.setText(_translate("MainWindow", " Position"))
        self.relative.setText(_translate("MainWindow", " Relative (per 1000 amino acids)"))
        self.nter.setText(_translate("MainWindow", " Amino acid from the N-terminus"))
        self.cter.setText(_translate("MainWindow", " Amino acid from the C-terminus"))
        self.step1Text.setText(_translate("MainWindow", "Enter one or more protein"))
        self.step2Text.setText(_translate("MainWindow", "Enter one or more peptides"))
        self.proteinsInput.setPlaceholderText(_translate("MainWindow", " Q14050, P05067"))
        self.peptidesInput.setPlaceholderText(_translate("MainWindow", " VGLPNSR, HGPLGPL"))
        self.or_step1.setText(_translate("MainWindow", "OR"))
        self.or_step2.setText(_translate("MainWindow", "OR"))
        self.import_step1.setText(_translate("MainWindow", "Import TXT file"))
        self.import_step2.setText(_translate("MainWindow", "Import TXT file"))
        self.btn_input_proteins.setText(_translate("MainWindow", "Select a file"))
        self.btn_input_peptides.setText(_translate("MainWindow", "Select a file"))
        self.info_lable.setText(_translate("MainWindow", "The process of searching for peptides and creating Excel spreadsheets takes time, depending on the number of proteins, peptides, the quality of the Internet connection, efficiency uniprot.org"))
        self.step3_lable_2.setText(_translate("MainWindow", "Step 4"))
        self.btn_start.setText(_translate("MainWindow", "Start creating"))
        self.btn_open_results.setText(_translate("MainWindow", "Open results"))
        self.btn_clear_all.setText(_translate("MainWindow", "Clear all"))
        self.btn_reset_filters.setText(_translate("MainWindow", "Reset filters"))
        self.btn_del_results.setText(_translate("MainWindow", "Deleate results"))
        self.btn_start.clicked.connect(self.send_proteins)
        self.btn_input_peptides.clicked.connect(self.open_database)
        self.btn_input_proteins.clicked.connect(self.open_input)
        self.btn_theme.clicked.connect(self.change_theme)
        self.btn_open_results.clicked.connect(self.open_dir)
        self.btn_del_results.clicked.connect(self.del_results)
        self.btn_clear_all.clicked.connect(self.clear_all)

    def send_proteins(self):
        self.prot_value = self.proteinsInput.text()
        self.peptides_value = self.peptidesInput.text()
        if len(self.peptides_value) > 1:
            with open("config.json", "r") as cfg:
                config_data = json.load(cfg)
                config_data["peptides"]["value"].extend(filter(None, re.split('[;, .]+', self.peptides_value)))
            with open("config.json", "w") as cfg:
                json.dump(config_data, cfg, indent=4)
        try:
            save_path = QFileDialog.getExistingDirectory()
            self.proteinsInput.setText("")
            self.peptidesInput.setText("")
            with open("config.json", "r") as cfg:
                config_data = json.load(cfg)
                config_data["savePath"]["value"] = save_path
                config_data["excelFilters"]["entryIdentifier"] = self.entry_identifier.isChecked()
                config_data["excelFilters"]["entryName"] = self.entry_name.isChecked()
                config_data["excelFilters"]["entryType"] = self.status.isChecked()
                config_data["excelFilters"]["fullName"] = self.protein_name.isChecked()
                config_data["excelFilters"]["scientificName"] = self.org_s.isChecked()
                config_data["excelFilters"]["commonName"] = self.org_c.isChecked()
                config_data["excelFilters"]["genes"] = self.gene.isChecked()
                config_data["excelFilters"]["proteinExistence"] = self.protein_existence.isChecked()
                config_data["excelFilters"]["length"] = self.length.isChecked()
                config_data["excelFilters"]["massDa"] = self.mass.isChecked()
                config_data["excelFilters"]["category"] = self.category.isChecked()
                config_data["excelFilters"]["id"] = self.id.isChecked()
                config_data["excelFilters"]["sequence"] = self.sequence.isChecked()
                config_data["excelFilters"]["sequence_length"] = self.seq_length.isChecked()
                config_data["excelFilters"]["occurrence"] = self.occurrence.isChecked()
                config_data["excelFilters"]["relative"] = self.relative.isChecked()
                config_data["excelFilters"]["position"] = self.position.isChecked()
                config_data["excelFilters"]["nter"] = self.nter.isChecked()
                config_data["excelFilters"]["cter"] = self.cter.isChecked()
            with open("config.json", "w") as cfg:
                json.dump(config_data, cfg, indent=4)
            if len(self.prot_value) > 1:
                try:
                    with open("config.json", "r") as cfg:
                        config_data = json.load(cfg)
                        config_data["proteins"]["value"].extend(filter(None, re.split('[;, .]+', self.prot_value)))

                    with open("config.json", "w") as cfg:
                        json.dump(config_data, cfg, indent=4)
                    try:
                        self.progressBar.setMaximum(0)
                        self.progressBar.setEnabled(True)
                        self.btn_open_results.setEnabled(False)
                        self.btn_del_results.setEnabled(False)
                        self.btn_start.setEnabled(False)
                        self.btn_input_proteins.setEnabled(False)
                        self.progressBar.setEnabled(True)
                        self.backgroundStream = QProcess()
                        self.backgroundStream.finished.connect(self.finish)
                        self.backgroundStream.start("run-back.cmd")
                    except Exception as e:
                        print(e)
                except BaseException as e:
                    print(e)
                    #self.proteinErrorMessage(line=line)

            else:
                try:
                        self.progressBar.setMaximum(0)
                        self.progressBar.setEnabled(True)
                        self.btn_start.setEnabled(False)
                        self.btn_input_proteins.setEnabled(False)
                        self.progressBar.setEnabled(True)
                        self.backgroundStream = QProcess()
                        self.backgroundStream.finished.connect(self.finish)
                        self.backgroundStream.start("run-back.cmd")
                except Exception as e:
                        print(e)
        except:
                pass

    def finish(self):
        self.backgroundStream = None
        self.btn_start.setEnabled(True)
        self.btn_del_results.setEnabled(True)
        self.btn_open_results.setEnabled(True)
        self.btn_input_proteins.setEnabled(True)
        self.progressBar.setMaximum(100)
        self.progressBar.setEnabled(False)

        with open("errorLogs.json", "r") as logs:
            json_data = json.load(logs)
        errors_list = json_data["missing"]["proteins"]
        if len(errors_list):
            self.proteinErrorMessage(line=' '.join(errors_list))
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

    def open_database(self):
        try:
            database_path = QFileDialog.getOpenFileName()[0]
            with open(database_path, 'r') as user_peptides:
                user_peptides_list = list(filter(None, re.split('[;, .]+', user_peptides.readline())))
                user_peptides.close()

            with open("config.json", "r") as cfg:
                config_data = json.load(cfg)
                config_data["peptides"]["value"].extend(user_peptides_list)

            with open("config.json", "w") as cfg:
                json.dump(config_data, cfg, indent=4)

            data = database_path.split('/')
            database_path = data[-1]
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ready")
            msg.setText(f"Selected: {database_path}")
            msg.setFixedSize(600, 600)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.btn_input_peptides.setText(f"{database_path}")
            self.btn_input_peptides.adjustSize()
            self.btn_input_peptides.setGeometry(QtCore.QRect(250, 730, self.btn_input_peptides.width() + 5, 31))
        except BaseException:
            pass

    def open_input(self):
        try:
            self.proteins_path = QFileDialog.getOpenFileName()[0]
            with open(self.proteins_path, 'r') as user_proteins:
                user_proteins_list = list(filter(None, re.split('[;, .]+', user_proteins.readline())))
                user_proteins.close()

            with open("config.json", "r") as cfg:
                config_data = json.load(cfg)
                config_data["proteins"]["value"].extend(user_proteins_list)

            with open("config.json", "w") as cfg:
                json.dump(config_data, cfg, indent=4)

            data = self.proteins_path.split('/')
            self.filename = data[-1]
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ready")
            msg.setText(f"Selected: {self.filename}")
            msg.setFixedSize(600, 600)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.btn_input_proteins.setText(f"{self.filename}")
            self.btn_input_proteins.adjustSize()
            self.btn_input_proteins.setGeometry(QtCore.QRect(250, 390, self.btn_input_proteins.width() + 5, 31))
        except BaseException:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setText("Error")
                error_dialog.setInformativeText(f"Unexpected error")
                error_dialog.setWindowTitle("Error")
                error_dialog.exec_()


    def proteinErrorMessage(self, line):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setText("Error")
        error_dialog.setInformativeText(f"Proteins: {','.join(line)}")
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()

    def open_dir(self):
        with open("config.json", "r") as config:
            data = json.load(config)
        path = data["savePath"]["value"]
        os.startfile(path)

    def del_results(self):
        with open("config.json", "r") as config:
            data = json.load(config)
        path = data["savePath"]["value"]
        for protein in data["proteins"]["value"]:
            os.remove(f"{path}/{protein}.xlsx")
        output = ', '.join(data["proteins"]["value"])
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Ready")
        msg.setText(
                f"Ready! Was deleted: {output}"
        )
        msg.setFixedSize(600, 600)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def clear_all(self):
        self.peptidesInput.setText("")
        self.proteinsInput.setText("")

    def change_theme(self):
        if self.theme == "light":
                self.theme ="dark"
                self.logo.setPixmap(QtGui.QPixmap("static/images/Logo_green-transformed.png"))
                self.centralwidget.setStyleSheet("background-color: #3A3A3A;")
                self.app_name.setStyleSheet("color: #30B58E;\n"
                                            "\n"
                                            "")
                self.btn_theme.setStyleSheet("QPushButton {\n"
                                             "    color: black;\n"
                                             "    background-color: #30B58E;\n"
                                             "    border-radius: 7;\n"
                                             "    border: 4px solid #30B58E;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: #228164;\n"
                                             "    border: 4px solid #228164;\n"
                                             "}")
                self.btn_info.setStyleSheet("QPushButton {\n"
                                            "    color: black;\n"
                                            "    background-color: #30B58E;\n"
                                            "    border-radius: 7;\n"
                                            "    border: 4px solid #30B58E;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #228164;\n"
                                            "    border: 4px solid #228164;\n"
                                            "}")
                self.btn_lang.setStyleSheet("QPushButton {\n"
                                            "    color: black;\n"
                                            "    background-color: #30B58E;\n"
                                            "    border-radius: 7;\n"
                                            "    border: 4px solid #30B58E;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #228164;\n"
                                            "    border: 4px solid #228164;\n"
                                            "}")
                self.step1_background.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                                    "border-radius: 20;")
                self.step2_background.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                                    "border-radius: 20;")
                self.step3_background.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                                    "border-radius: 20;")
                self.step1_lable.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                               "color: #30B58E;\n"
                                               "\n"
                                               "")
                self.step2_lable.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                               "color: #30B58E;\n"
                                               "\n"
                                               "")
                self.step3_lable.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                               "color: #30B58E;\n"
                                               "\n"
                                               "")
                self.entry_name.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                              "color: rgb(255, 255, 255);")
                self.entry_identifier.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                                    "color: rgb(255, 255, 255);")
                self.protein_name.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                                "color: rgb(255, 255, 255);")
                self.status.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                          "color: rgb(255, 255, 255);")
                self.org_c.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                         "color: rgb(255, 255, 255);")
                self.gene.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                        "color: rgb(255, 255, 255);")
                self.protein_existence.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                                     "color: rgb(255, 255, 255);")
                self.org_s.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                         "color: rgb(255, 255, 255);")
                self.id.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                      "color: rgb(255, 255, 255);")
                self.mass.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                        "color: rgb(255, 255, 255);")
                self.category.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                            "color: rgb(255, 255, 255);")
                self.length.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                          "color: rgb(255, 255, 255);")
                self.seq_length.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                              "color: rgb(255, 255, 255);")
                self.occurrence.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                              "color: rgb(255, 255, 255);")
                self.sequence.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                            "color: rgb(255, 255, 255);")
                self.position.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                            "color: rgb(255, 255, 255);")
                self.relative.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                            "color: rgb(255, 255, 255);")
                self.nter.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                        "color: rgb(255, 255, 255);")
                self.cter.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                        "color: rgb(255, 255, 255);")
                self.blueStep1.setStyleSheet("background-color: #279084;\n"
                                             "border-radius: 15;")
                self.blueStep2.setStyleSheet("background-color: #279084;\n"
                                             "border-radius: 15;")
                self.step1Text.setStyleSheet("background-color: 20766D;\n"
                                             "color: rgb(255, 255, 255);")
                self.step2Text.setStyleSheet("background-color:#279084;\n"
                                             "color: rgb(255, 255, 255);")
                self.proteinsInput.setStyleSheet("border-radius: 13px;\n"
                                                 "background-color: rgb(255, 255, 255);")
                self.peptidesInput.setStyleSheet("border-radius: 13px;\n"
                                                 "background-color: rgb(255, 255, 255);")
                self.or_step1.setStyleSheet("background-color: #279084;\n"
                                         "color: rgb(255, 255, 255);")
                self.or_step2.setStyleSheet("background-color: #279084;\n"
                                         "color: rgb(255, 255, 255);")
                self.import_step1.setStyleSheet("background-color:#279084;\n"
                                           "color: rgb(255, 255, 255);")
                self.import_step2.setStyleSheet("background-color: #279084;\n"
                                           "color: rgb(255, 255, 255);")
                self.btn_input_proteins.setStyleSheet("QPushButton {\n"
                                                    "    color: black;\n"
                                                    "    background-color: #ffffff;\n"
                                                    "    border-radius: 7;\n"
                                                    "    border: 2px solid #ffffff;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "    background-color: #dfdfdf;\n"
                                                    "}")
                self.btn_input_peptides.setStyleSheet("QPushButton {\n"
                                                    "    color: black;\n"
                                                    "    background-color: #ffffff;\n"
                                                    "    border-radius: 7;\n"
                                                    "    border: 2px solid #ffffff;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "    background-color: #dfdfdf;\n"
                                                    "}")
                self.progressBar.setStyleSheet("QProgressBar {\n"
                                               "    text-align: center;\n"
                                               "    color: #ffffff;\n"
                                               "    border: 2px solid #30B58E;\n"
                                               "    border-radius: 10px;\n"
                                               "}\n"
                                               "QProgressBar::chunk {\n"
                                               "    background-color: #30B58E;\n"
                                               "    border-radius: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "")
                self.step1_background_2.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                                      "color: rgb(255, 255, 255);\n"
                                                      "border-radius: 20;")
                self.info_lable.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                           "color: rgb(255, 255, 255);")
                self.step3_lable_2.setStyleSheet("background-color: rgb(81, 80, 80);\n"
                                                 "color: #30B58E;\n"
                                                 "\n"
                                                 "")
                self.btn_start.setStyleSheet("QPushButton {\n"
                                                    "    color: black;\n"
                                                    "    background-color: #ffffff;\n"
                                                    "    border-radius: 15;\n"
                                                    "    border: 3px solid #279084;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "    background-color: #dfdfdf;\n"
                                                    "}")
                self.btn_del_results.setStyleSheet("QPushButton {\n"
                                                    "    color: black;\n"
                                                    "    background-color: #ffffff;\n"
                                                    "    border-radius: 15;\n"
                                                    "    border: 3px solid #279084;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "    background-color: #dfdfdf;\n"
                                                    "}\n"
                                                    "QPushButton:disabled {\n"
                                                    "    color: rgb(177, 177, 177);\n"
                                                    "    background-color: #ffffff;\n"
                                                    "    border-radius: 15;\n"
                                                    "    border: 3px solid #279084;\n"
                                                    "}")
                self.btn_open_results.setStyleSheet("QPushButton {\n"
                                            "    color: black;\n"
                                            "    background-color: #ffffff;\n"
                                            "    border-radius: 15;\n"
                                            "    border: 3px solid #279084;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #dfdfdf;\n"
                                            "}\n"
                                            "QPushButton:disabled {\n"
                                            "    color: rgb(177, 177, 177);\n"
                                            "    background-color: #ffffff;\n"
                                            "    border-radius: 15;\n"
                                            "    border: 3px solid #279084;\n"
                                            "}")
                self.btn_clear_all.setStyleSheet("QPushButton {\n"
                                            "    color: black;\n"
                                            "    background-color: #ffffff;\n"
                                            "    border-radius: 15;\n"
                                            "    border: 3px solid #279084;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #dfdfdf;\n"
                                            "}\n"
                                            "QPushButton:disabled {\n"
                                            "    color: rgb(177, 177, 177);\n"
                                            "    background-color: #ffffff;\n"
                                            "    border-radius: 15;\n"
                                            "    border: 3px solid #279084;\n"
                                            "}")
                self.btn_reset_filters.setStyleSheet("QPushButton {\n"
                                            "    color: black;\n"
                                            "    background-color: #ffffff;\n"
                                            "    border-radius: 15;\n"
                                            "    border: 3px solid #279084;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #dfdfdf;\n"
                                            "}\n"
                                            "QPushButton:disabled {\n"
                                            "    color: rgb(177, 177, 177);\n"
                                            "    background-color: #ffffff;\n"
                                            "    border-radius: 15;\n"
                                            "    border: 3px solid #279084;\n"
                                            "}")
        else:
                self.theme = "light"
                self.logo.setPixmap(QtGui.QPixmap("static/images/Logo_blue.png"))
                self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.app_name.setStyleSheet("color: rgb(21, 146, 255);\n"
                                            "\n"
                                            "")
                self.btn_theme.setStyleSheet("QPushButton {\n"
                                             "    color: black;\n"
                                             "    background-color: #1592FF;\n"
                                             "    border-radius: 7;\n"
                                             "    border: 4px solid #1592ff;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: #2264ff;\n"
                                             "    border: 4px solid #2264ff;\n"
                                             "}")
                self.btn_info.setStyleSheet("QPushButton {\n"
                                            "    color: black;\n"
                                            "    background-color: #1592FF;\n"
                                            "    border-radius: 7;\n"
                                            "    border: 4px solid #1592ff;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #2264ff;\n"
                                            "    border: 4px solid #2264ff;\n"
                                            "}")
                self.btn_lang.setStyleSheet("QPushButton {\n"
                                            "    color: black;\n"
                                            "    background-color: #1592FF;\n"
                                            "    border-radius: 7;\n"
                                            "    border: 4px solid #1592ff;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #2264ff;\n"
                                            "    border: 4px solid #2264ff;\n"
                                            "}")
                self.step1_background.setStyleSheet("background-color: #F2F2F2;\n"
                                                    "border-radius: 20;")
                self.step2_background.setStyleSheet("background-color: #F2F2F2;\n"
                                                    "border-radius: 20;")
                self.step3_background.setStyleSheet("background-color: #F2F2F2;\n"
                                                    "border-radius: 20;")
                self.step1_lable.setStyleSheet("background-color: #F2F2F2;\n"
                                               "color: rgb(21, 146, 255);\n"
                                               "\n"
                                               "")
                self.step2_lable.setStyleSheet("background-color: #F2F2F2;\n"
                                               "color: rgb(21, 146, 255);\n"
                                               "\n"
                                               "")
                self.step3_lable.setStyleSheet("background-color: #F2F2F2;\n"
                                               "color: rgb(21, 146, 255);\n"
                                               "\n"
                                               "")
                self.entry_identifier.setStyleSheet("background-color: #F2F2F2;")
                self.sequence.setStyleSheet("background-color: #F2F2F2;")
                self.entry_name.setStyleSheet("background-color: #F2F2F2;")
                self.protein_name.setStyleSheet("background-color: #F2F2F2;")
                self.status.setStyleSheet("background-color: #F2F2F2;")
                self.org_c.setStyleSheet("background-color: #F2F2F2;")
                self.gene.setStyleSheet("background-color: #F2F2F2;")
                self.protein_existence.setStyleSheet("background-color: #F2F2F2;")
                self.org_s.setStyleSheet("background-color: #F2F2F2;")
                self.id.setStyleSheet("background-color: #F2F2F2;")
                self.mass.setStyleSheet("background-color: #F2F2F2;")
                self.category.setStyleSheet("background-color: #F2F2F2;")
                self.length.setStyleSheet("background-color: #F2F2F2;")
                self.seq_length.setStyleSheet("background-color: #F2F2F2;")
                self.occurrence.setStyleSheet("background-color: #F2F2F2;")
                self.position.setStyleSheet("background-color: #F2F2F2;")
                self.relative.setStyleSheet("background-color: #F2F2F2;")
                self.nter.setStyleSheet("background-color: #F2F2F2;")
                self.cter.setStyleSheet("background-color: #F2F2F2;")
                self.blueStep1.setStyleSheet("background-color: rgb(21, 146, 255);\n"
                                             "border-radius: 15;")
                self.blueStep2.setStyleSheet("background-color: rgb(21, 146, 255);\n"
                                             "border-radius: 15;")
                self.step1Text.setStyleSheet("background-color: rgb(21, 146, 255);\n"
                                             "color: rgb(255, 255, 255);")
                self.step2Text.setStyleSheet("background-color: rgb(21, 146, 255);\n"
                                             "color: rgb(255, 255, 255);")
                self.proteinsInput.setStyleSheet("border-radius: 13px;")
                self.peptidesInput.setStyleSheet("border-radius: 13px;")
                self.or_step1.setStyleSheet("background-color: rgb(21, 146, 255);\n"
                                            "color: rgb(255, 255, 255);")
                self.or_step2.setStyleSheet("background-color: rgb(21, 146, 255);\n"
                                            "color: rgb(255, 255, 255);")
                self.import_step1.setStyleSheet("background-color: rgb(21, 146, 255);\n"
                                                "color: rgb(255, 255, 255);")
                self.import_step2.setStyleSheet("background-color: rgb(21, 146, 255);\n"
                                                "color: rgb(255, 255, 255);")
                self.btn_input_proteins.setStyleSheet("QPushButton {\n"
                                                      "    color: black;\n"
                                                      "    background-color: #ffffff;\n"
                                                      "    border-radius: 7;\n"
                                                      "    border: 2px solid #ffffff;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QPushButton:pressed {\n"
                                                      "    background-color: #dfdfdf;\n"
                                                      "}")
                self.btn_input_peptides.setStyleSheet("QPushButton {\n"
                                                      "    color: black;\n"
                                                      "    background-color: #ffffff;\n"
                                                      "    border-radius: 7;\n"
                                                      "    border: 2px solid #ffffff;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QPushButton:pressed {\n"
                                                      "    background-color: #dfdfdf;\n"
                                                      "}")
                self.progressBar.setStyleSheet("QProgressBar {\n"
                                               "    text-align: center;\n"
                                               "    border: 1px solid #1592ff;\n"
                                               "    border-radius: 10px;\n"
                                               "}\n"
                                               "QProgressBar::chunk {\n"
                                               "    background-color: rgb(21, 146, 255);\n"
                                               "    border-radius: 10px;\n"
                                               "}\n"
                                               "")
                self.step1_background_2.setStyleSheet("background-color: #F2F2F2;\n"
                                                      "border-radius: 20;")
                self.info_lable.setStyleSheet("background-color: #F2F2F2;")
                self.step3_lable_2.setStyleSheet("background-color: #F2F2F2;\n"
                                                 "color: rgb(21, 146, 255);\n"
                                                 "\n"
                                                 "")
                self.btn_start.setStyleSheet("QPushButton {\n"
                                             "    color: black;\n"
                                             "    background-color: #ffffff;\n"
                                             "    border-radius: 15;\n"
                                             "    border: 3px solid #1592ff;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: #dfdfdf;\n"
                                             "}")
                self.btn_open_results.setStyleSheet("QPushButton {\n"
                                                    "    color: black;\n"
                                                    "    background-color: #ffffff;\n"
                                                    "    border-radius: 15;\n"
                                                    "    border: 3px solid #1592ff;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "    background-color: #dfdfdf;\n"
                                                    "}\n"
                                                    "QPushButton:disabled {\n"
                                                    "    color: rgb(177, 177, 177);\n"
                                                    "    background-color: #ffffff;\n"
                                                    "    border-radius: 15;\n"
                                                    "    border: 3px solid #1592ff;\n"
                                                    "}")

                self.btn_clear_all.setStyleSheet("QPushButton {\n"
                                                 "    color: black;\n"
                                                 "    background-color: #ffffff;\n"
                                                 "    border-radius: 15;\n"
                                                 "    border: 3px solid #1592ff;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "    background-color: #dfdfdf;\n"
                                                 "}")
                self.btn_reset_filters.setStyleSheet("QPushButton {\n"
                                                     "    color: black;\n"
                                                     "    background-color: #ffffff;\n"
                                                     "    border-radius: 15;\n"
                                                     "    border: 3px solid #1592ff;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:pressed {\n"
                                                     "    background-color: #dfdfdf;\n"
                                                     "}")
                self.btn_del_results.setStyleSheet("QPushButton {\n"
                                                   "    color: black;\n"
                                                   "    background-color: #ffffff;\n"
                                                   "    border-radius: 15;\n"
                                                   "    border: 3px solid #1592ff;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:pressed {\n"
                                                   "    background-color: #dfdfdf;\n"
                                                   "}\n"
                                                   "QPushButton:disabled {\n"
                                                   "    color: rgb(177, 177, 177);\n"
                                                   "    background-color: #ffffff;\n"
                                                   "    border-radius: 15;\n"
                                                   "    border: 3px solid #1592ff;\n"
                                                   "}")


if __name__ == "__main__":
    creatingLogs()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
