from PyQt6 import QtCore, QtGui
from main import Create_plot, Excelopener
from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6 import QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.counter = 0
        self.tabel = None
        self.data = None
        self.filename = None

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FrameforPlot = QtWidgets.QFrame(parent=self.centralwidget)
        self.FrameforPlot.setGeometry(QtCore.QRect(370, 0, 431, 621))
        self.FrameforPlot.setStyleSheet("background-color: rgb(76, 108, 115);")
        self.FrameforPlot.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.FrameforPlot.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.FrameforPlot.setObjectName("FrameforPlot")
        self.hint_label = QtWidgets.QLabel(parent=self.FrameforPlot)
        self.hint_label.setGeometry(QtCore.QRect(60, 40, 410, 300))
        self.hint_label.setStyleSheet("color: rgb(213, 233, 242);\n"
                                      "font: 14pt \"source-serif-pro;serif\";")
        self.hint_label.setObjectName("Hint Label")
        self.filters_label = QtWidgets.QLabel(parent=self.FrameforPlot)
        self.filters_label.setGeometry(QtCore.QRect(170, 20, 81, 71))
        self.filters_label.setStyleSheet("color: rgb(213, 233, 242);\n"
                                         "font: 14pt \"source-serif-pro;serif\";")
        self.filters_label.setObjectName("filters_label")
        self.Create_NEw_plor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Create_NEw_plor.setGeometry(QtCore.QRect(120, 530, 141, 21))
        self.Create_NEw_plor.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Create_NEw_plor.setStyleSheet("background-color: rgb(191, 209, 217);\n"
                                           "border: 6px;\n"
                                           "border-radius: 4px;\n"
                                           "font: 12pt \"\"Times New Roman\"\";\n"
                                           "")
        self.Create_NEw_plor.setObjectName("Create_NEw_plor")
        self.TypeBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.TypeBox.setGeometry(QtCore.QRect(20, 50, 130, 20))
        self.TypeBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.TypeBox.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                   "padding-left: 10px;\n"
                                   "border-radius: 4px;\n"
                                   "")
        self.TypeBox.setObjectName("TypeBox")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.FlterOnOFF = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.FlterOnOFF.setGeometry(QtCore.QRect(20, 370, 70, 16))
        self.FlterOnOFF.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.FlterOnOFF.setMouseTracking(False)
        self.FlterOnOFF.setTabletTracking(True)
        self.FlterOnOFF.setStyleSheet("font: 10pt \"\"Times New Roman\"\";")
        self.FlterOnOFF.setObjectName("FlterOnOFF")
        self.color = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.color.setGeometry(QtCore.QRect(20, 80, 130, 20))
        self.color.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                 "padding-left: 10px;\n"
                                 "border: 1px;\n"
                                 "border-radius: 4px;\n"
                                 "")
        self.color.setObjectName("color")
        self.max_row = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.max_row.setGeometry(QtCore.QRect(20, 190, 130, 20))
        self.max_row.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                   "padding-left: 10px;\n"
                                   "border: 1px;\n"
                                   "border-radius: 4px;\n"
                                   "")
        self.max_row.setObjectName("max_row")
        self.min_row = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.min_row.setGeometry(QtCore.QRect(20, 220, 130, 20))
        self.min_row.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                   "padding-left: 10px;\n"
                                   "border: 1px;\n"
                                   "border-radius: 4px;\n"
                                   "")
        self.min_row.setObjectName("min_row")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 50, 141, 21))
        self.label.setStyleSheet("font: 10pt \"\"Times New Roman\"\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 120, 141, 16))
        self.label_3.setStyleSheet("font: 10pt \"\"Times New Roman\"\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 150, 131, 16))
        self.label_4.setStyleSheet("font: 10pt \"\"Times New Roman\"\";")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 120, 130, 20))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox.setStyleSheet("padding-left: 10px;\n"
                                    "border-radius: 4px;\n"
                                    "font: 10pt \"\"Times New Roman\"\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 150, 130, 20))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_2.setStyleSheet("padding-left: 10px;\n"
                                      "border-radius: 4px;\n"
                                      "font: 10pt \"\"Times New Roman\"\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.Change_tabel_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Change_tabel_button.setGeometry(QtCore.QRect(20, 390, 131, 23))
        self.Change_tabel_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Change_tabel_button.setStyleSheet("background-color: rgb(191, 209, 217);\n"
                                               "border: 6px;\n"
                                               "border-radius: 4px;\n"
                                               "font: 12pt \"\"Times New Roman\"\";\n"
                                               "")
        self.Change_tabel_button.setObjectName("Change_tabel_button")
        self.max_row_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.max_row_2.setGeometry(QtCore.QRect(20, 250, 130, 20))
        self.max_row_2.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                     "padding-left: 10px;\n"
                                     "border: 1px;\n"
                                     "border-radius: 4px;\n"
                                     "")
        self.max_row_2.setObjectName("max_row_2")
        self.set_x_label = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.set_x_label.setGeometry(QtCore.QRect(20, 280, 130, 20))
        self.set_x_label.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                       "padding-left: 10px;\n"
                                       "border: 1px;\n"
                                       "border-radius: 4px;\n"
                                       "")
        self.set_x_label.setObjectName("set x label")
        self.add_plot_buton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_plot_buton.setGeometry(QtCore.QRect(20, 420, 131, 23))
        self.add_plot_buton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_plot_buton.setStyleSheet("background-color: rgb(191, 209, 217);\n"
                                          "border: 6px;\n"
                                          "border-radius: 4px;\n"
                                          "font: 12pt \"\"Times New Roman\"\";\n"
                                          "")
        self.set_y_label = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.set_y_label.setGeometry(QtCore.QRect(20, 310, 130, 20))
        self.set_y_label.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                       "padding-left: 10px;\n"
                                       "border: 1px;\n"
                                       "border-radius: 4px;\n"
                                       "")
        self.set_y_label.setObjectName("set y label")
        self.add_plot_buton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_plot_buton_2.setGeometry(QtCore.QRect(20, 450, 131, 23))
        self.add_plot_buton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_plot_buton_2.setStyleSheet("background-color: rgb(191, 209, 217);\n"
                                            "border: 6px;\n"
                                            "border-radius: 4px;\n"
                                            "font: 12pt \"\"Times New Roman\"\";\n"
                                            "")
        self.add_plot_buton_2.setObjectName("add_plot_buton_2")
        self.add_plot_buton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_plot_buton_3.setGeometry(QtCore.QRect(160, 390, 181, 23))
        self.add_plot_buton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_plot_buton_3.setStyleSheet("background-color: rgb(191, 209, 217);\n"
                                            "border: 6px;\n"
                                            "border-radius: 4px;\n"
                                            "font: 12pt \"\"Times New Roman\"\";\n"
                                            "")
        self.add_plot_buton_3.setObjectName("add_plot_buton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_file()
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hint_label.setText(_translate("MainWindow",
                                           f"How to create a plot:\n1. choose a type of plot\n2. enter a color\n3. choose a 2 different columns from list\n4. set max and min row\n5. set title and labels"))
        self.Create_NEw_plor.setText(_translate("MainWindow", "Create new plot"))
        self.TypeBox.setItemText(0, _translate("MainWindow", "plot"))
        self.TypeBox.setItemText(1, _translate("MainWindow", "bar"))
        self.TypeBox.setItemText(2, _translate("MainWindow", "scatter"))
        self.TypeBox.setItemText(3, _translate("MainWindow", "step"))
        self.TypeBox.setItemText(4, _translate("MainWindow", "stem"))
        self.FlterOnOFF.setText(_translate("MainWindow", "Filter"))
        self.color.setPlaceholderText(_translate("MainWindow", "choose color"))
        self.max_row.setWindowIconText(_translate("MainWindow", "set max row"))
        self.min_row.setWindowIconText(_translate("MainWindow", "set min row"))
        self.label.setText(_translate("MainWindow", "choose a plot type"))
        self.label_3.setText(_translate("MainWindow", "set the 1-st column"))
        self.label_4.setText(_translate("MainWindow", "set the 2-nd column"))
        self.Change_tabel_button.setText(_translate("MainWindow", "Change tabel"))
        self.max_row_2.setPlaceholderText(_translate("MainWindow", "set title"))
        self.set_x_label.setPlaceholderText(_translate("MainWindow", "set x label"))
        self.set_y_label.setPlaceholderText(_translate("MainWindow", "set y label"))
        self.add_plot_buton.setText(_translate("MainWindow", "Add new plot"))
        self.add_plot_buton_2.setText(_translate("MainWindow", "delete plot"))
        self.add_plot_buton_3.setText(_translate("MainWindow", "change type of plot"))

    def create_data(self):
        self.counter += 1
        column1 = self.comboBox.currentText()
        column2 = self.comboBox_2.currentText()
        color = self.color.text()
        x_label = self.set_x_label.text()
        y_label = self.set_y_label.text()
        title = self.max_row_2.text()
        max_row = int(self.max_row.text())
        min_row = int(self.min_row.text())
        plot_type = self.TypeBox.currentText()
        self.data = Create_plot(column1, column2, max_row=max_row, min_row=min_row, tabel=self.filename[0],
                                type_of_plot=plot_type, color=color)
        if x_label and y_label:
            self.data.set_labels(x_label, y_label)
            print(1, bool(x_label), bool(y_label))
        elif not x_label and not y_label:
            self.data.set_labels(column1, column2)
            print(2)
        elif x_label and not y_label:
            self.data.set_labels(x_label, column2)
            print(3)
        elif not x_label and y_label:
            self.data.set_labels(column1, y_label)
            print(4)

        if title:
            self.data.set_title(title)
        else:
            self.data.set_title(f"Figure {self.counter}")

    def creating_pandas_tabel(self, filename):
        self.tabel = Excelopener(filename[0], 1, 1).create_a_table_in_py()
        self.create_combobox(self.tabel)
        print("creating tabel: completed")

    def create_combobox(self, tabel):
        _translate = QtCore.QCoreApplication.translate
        a = [column for column in tabel]
        for i in range(len(a)):
            self.comboBox_2.addItem("")
            self.comboBox.addItem("")
        for name_of_columns in a:
            self.comboBox.setItemText(a.index(name_of_columns), _translate("MainWindow", name_of_columns))
            self.comboBox_2.setItemText(a.index(name_of_columns), _translate("MainWindow", name_of_columns))
        print("combobox: completed")

    def add_functions(self):
        self.Create_NEw_plor.clicked.connect(self.create_data)
        self.Create_NEw_plor.clicked.connect(self.plot_data)
        self.Create_NEw_plor.clicked.connect(self.show_plot)
        self.add_plot_buton.clicked.connect(self.add_plot)
        self.Change_tabel_button.clicked.connect(self.open_file)
        print("add functions: completed")

    def delete_tabel(self, index):
        self.data.delete_plot(index)
        print("delete: completed")

    def open_file(self):
        dialog = QtWidgets.QFileDialog(parent=self.centralwidget)
        dialog.exec()
        self.filename = (dialog.selectedFiles())
        self.creating_pandas_tabel(self.filename)
        print("Check: completed")

    def add_plot(self):
        column1 = self.comboBox.currentText()
        column2 = self.comboBox_2.currentText()
        self.data.add_new_plot(column1, column2, "scatter", "blue")
        print("plot is append")
        self.data.show_plot()

    def plot_data(self):
        self.data.plot_data()
        print("data is create")

    def show_plot(self):
        self.data.show_plot()
        print("plot is show")

    def save_plot(self):

        file_dialog = QFileDialog(parent=self.centralwidget)
        file_dialog.close()
        file_dialog.exec()
        file_path, _ = file_dialog.getSaveFileName()
        print(file_path, _)

        if file_path:
            self.data.save_plot(file_path)

        print("plot is save")


class Ui_NewplotWindow(object):
    def __init__(self, main_data):
        self.data = main_data

    def setupUi(self, NewplotWindow):
        NewplotWindow.setObjectName("NewplotWindow")
        NewplotWindow.resize(700, 600)
        NewplotWindow.setStyleSheet("")
        self.NewplotWindow = NewplotWindow
        self.comboBox = QtWidgets.QComboBox(parent=NewplotWindow)
        self.comboBox.setGeometry(QtCore.QRect(20, 120, 130, 20))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox.setStyleSheet("padding-left: 10px;\n"
                                    "border-radius: 4px;\n"
                                    "font: 10pt \"\"Times New Roman\"\";")
        self.comboBox.setObjectName("comboBox")
        self.Change_tabel_button = QtWidgets.QPushButton(parent=NewplotWindow)
        self.Change_tabel_button.setGeometry(QtCore.QRect(20, 390, 131, 23))
        self.Change_tabel_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Change_tabel_button.setStyleSheet("background-color: rgb(191, 209, 217);\n"
                                               "border: 6px;\n"
                                               "border-radius: 4px;\n"
                                               "font: 12pt \"\"Times New Roman\"\";\n"
                                               "")
        self.Change_tabel_button.setObjectName("Change_tabel_button")
        self.label_4 = QtWidgets.QLabel(parent=NewplotWindow)
        self.label_4.setGeometry(QtCore.QRect(160, 150, 131, 16))
        self.label_4.setStyleSheet("font: 10pt \"\"Times New Roman\"\";")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=NewplotWindow)
        self.label_3.setGeometry(QtCore.QRect(160, 120, 141, 16))
        self.label_3.setStyleSheet("font: 10pt \"\"Times New Roman\"\";")
        self.label_3.setObjectName("label_3")
        self.add_new_polt = QtWidgets.QPushButton(parent=NewplotWindow)
        self.add_new_polt.setGeometry(QtCore.QRect(120, 530, 141, 21))
        self.add_new_polt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_new_polt.setStyleSheet("background-color: rgb(191, 209, 217);\n"
                                        "border: 6px;\n"
                                        "border-radius: 4px;\n"
                                        "font: 12pt \"\"Times New Roman\"\";\n"
                                        "")
        self.add_new_polt.setObjectName("Create_NEw_plor")
        self.label = QtWidgets.QLabel(parent=NewplotWindow)
        self.label.setGeometry(QtCore.QRect(160, 50, 141, 21))
        self.label.setStyleSheet("font: 10pt \"\"Times New Roman\"\";")
        self.label.setObjectName("label")
        self.TypeBox = QtWidgets.QComboBox(parent=NewplotWindow)
        self.TypeBox.setGeometry(QtCore.QRect(20, 50, 130, 20))
        self.TypeBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.TypeBox.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                   "padding-left: 10px;\n"
                                   "border-radius: 4px;\n"
                                   "")
        self.TypeBox.setObjectName("TypeBox")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.max_row = QtWidgets.QLineEdit(parent=NewplotWindow)
        self.max_row.setGeometry(QtCore.QRect(20, 190, 130, 20))
        self.max_row.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                   "padding-left: 10px;\n"
                                   "border: 1px;\n"
                                   "border-radius: 4px;\n"
                                   "")
        self.max_row.setObjectName("max_row")
        self.FrameforPlot = QtWidgets.QFrame(parent=NewplotWindow)
        self.FrameforPlot.setGeometry(QtCore.QRect(370, 0, 431, 621))
        self.FrameforPlot.setStyleSheet("background-color: rgb(76, 108, 115);")
        self.FrameforPlot.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.FrameforPlot.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.FrameforPlot.setObjectName("FrameforPlot")
        self.filters_label = QtWidgets.QLabel(parent=self.FrameforPlot)
        self.filters_label.setGeometry(QtCore.QRect(120, 0, 81, 71))
        self.filters_label.setStyleSheet("color: rgb(213, 233, 242);\n"
                                         "font: 14pt \"source-serif-pro;serif\";")
        self.filters_label.setObjectName("filters_label")
        self.min_row_2 = QtWidgets.QLineEdit(parent=NewplotWindow)
        self.min_row_2.setGeometry(QtCore.QRect(20, 280, 130, 20))
        self.min_row_2.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                     "padding-left: 10px;\n"
                                     "border: 1px;\n"
                                     "border-radius: 4px;\n"
                                     "")
        self.min_row_2.setObjectName("min_row_2")
        self.comboBox_2 = QtWidgets.QComboBox(parent=NewplotWindow)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 150, 130, 20))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox_2.setStyleSheet("padding-left: 10px;\n"
                                      "border-radius: 4px;\n"
                                      "font: 10pt \"\"Times New Roman\"\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.max_row_2 = QtWidgets.QLineEdit(parent=NewplotWindow)
        self.max_row_2.setGeometry(QtCore.QRect(20, 250, 130, 20))
        self.max_row_2.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                     "padding-left: 10px;\n"
                                     "border: 1px;\n"
                                     "border-radius: 4px;\n"
                                     "")
        self.max_row_2.setObjectName("max_row_2")
        self.FlterOnOFF = QtWidgets.QCheckBox(parent=NewplotWindow)
        self.FlterOnOFF.setGeometry(QtCore.QRect(20, 370, 70, 16))
        self.FlterOnOFF.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.FlterOnOFF.setMouseTracking(False)
        self.FlterOnOFF.setTabletTracking(True)
        self.FlterOnOFF.setStyleSheet("font: 10pt \"\"Times New Roman\"\";")
        self.FlterOnOFF.setObjectName("FlterOnOFF")
        self.color = QtWidgets.QLineEdit(parent=NewplotWindow)
        self.color.setGeometry(QtCore.QRect(20, 80, 130, 20))
        self.color.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                 "padding-left: 10px;\n"
                                 "border: 1px;\n"
                                 "border-radius: 4px;\n"
                                 "")
        self.color.setObjectName("color")
        self.min_row = QtWidgets.QLineEdit(parent=NewplotWindow)
        self.min_row.setGeometry(QtCore.QRect(20, 220, 130, 20))
        self.min_row.setStyleSheet("font: 10pt \"\"Times New Roman\"\";\n"
                                   "padding-left: 10px;\n"
                                   "border: 1px;\n"
                                   "border-radius: 4px;\n"
                                   "")
        self.min_row.setObjectName("min_row")

        self.retranslateUi(NewplotWindow)
        QtCore.QMetaObject.connectSlotsByName(NewplotWindow)
        self.add_functions()
        self.click_handler()
        print(self.data)

    def retranslateUi(self, NewplotWindow):
        _translate = QtCore.QCoreApplication.translate
        NewplotWindow.setWindowTitle(_translate("NewplotWindow", "Form"))
        self.Change_tabel_button.setText(_translate("NewplotWindow", "Change tabel"))
        self.label_4.setText(_translate("NewplotWindow", "set the 2-nd column"))
        self.label_3.setText(_translate("NewplotWindow", "set the 1-st column"))
        self.add_new_polt.setText(_translate("NewplotWindow", "Add new plot"))
        self.label.setText(_translate("NewplotWindow", "choose a plot type"))
        self.TypeBox.setItemText(0, _translate("NewplotWindow", "plot"))
        self.TypeBox.setItemText(1, _translate("NewplotWindow", "bar"))
        self.TypeBox.setItemText(2, _translate("NewplotWindow", "scatter"))
        self.TypeBox.setItemText(3, _translate("NewplotWindow", "step"))
        self.TypeBox.setItemText(4, _translate("NewplotWindow", "stem"))
        self.max_row.setPlaceholderText(_translate("NewplotWindow", "set max row"))
        self.filters_label.setText(_translate("NewplotWindow", "Fileters"))
        self.min_row_2.setPlaceholderText(_translate("NewplotWindow", "set label"))
        self.max_row_2.setPlaceholderText(_translate("NewplotWindow", "set title"))
        self.FlterOnOFF.setText(_translate("NewplotWindow", "Filter"))
        self.color.setPlaceholderText(_translate("NewplotWindow", "choose color"))
        self.min_row.setPlaceholderText(_translate("NewplotWindow", "set min row"))

    def click_handler(self):
        dialog = QtWidgets.QFileDialog(parent=self.NewplotWindow)
        dialog.exec()
        self.filename = (dialog.selectedFiles())
        self.creating_pandas_tabel(dialog.selectedFiles())
        print("Check: completed")

    def add_functions(self):
        self.add_new_polt.clicked.connect(self.add_plot)
        self.Change_tabel_button.clicked.connect(self.click_handler)
        print("add functions: completed")

    def create_combobox(self, tabel):
        _translate = QtCore.QCoreApplication.translate
        a = [column for column in tabel]
        for i in range(len(a)):
            self.comboBox_2.addItem("")
            self.comboBox.addItem("")
        for name_of_columns in a:
            self.comboBox.setItemText(a.index(name_of_columns), _translate("MainWindow", name_of_columns))
            self.comboBox_2.setItemText(a.index(name_of_columns), _translate("MainWindow", name_of_columns))
        print("combobox: completed")

    def add_plot(self):
        column1 = self.comboBox.currentText()
        column2 = self.comboBox_2.currentText()
        color = self.color.text()
        max_row = int(self.max_row.text())
        min_row = int(self.min_row.text())
        plot_type = self.TypeBox.currentText()
        self.data.add_new_plot(column1, column2, plot_type, color=color)
        print("plot: append")

    def creating_pandas_tabel(self, filename):
        tabel = Excelopener(filename[0]).create_a_table_in_py()
        self.create_combobox(tabel)
        print("creating tabel: completed")

    def delete_tabel(self, index):
        self.data.delete_plot(index)
        print("delete: completed")

    def title_set(self, title):
        self.data.set_title(title)

    def labels_set(self, labels_x, label_y):
        self.data.set_labels(labels_x, label_y)

    def plot_data(self):
        self.data.plot_data()

    def show_plot(self):
        self.data.show_plot()
