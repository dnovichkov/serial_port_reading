# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial_port.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 886)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.main_plot_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_plot_tab.sizePolicy().hasHeightForWidth())
        self.main_plot_tab.setSizePolicy(sizePolicy)
        self.main_plot_tab.setObjectName("main_plot_tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_plot_tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.probe_data_table = QtWidgets.QTableView(self.main_plot_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probe_data_table.sizePolicy().hasHeightForWidth())
        self.probe_data_table.setSizePolicy(sizePolicy)
        self.probe_data_table.setMaximumSize(QtCore.QSize(16777215, 100))
        self.probe_data_table.setObjectName("probe_data_table")
        self.probe_data_table.horizontalHeader().setVisible(False)
        self.probe_data_table.horizontalHeader().setHighlightSections(False)
        self.probe_data_table.verticalHeader().setVisible(False)
        self.probe_data_table.verticalHeader().setHighlightSections(False)
        self.verticalLayout_7.addWidget(self.probe_data_table)
        self.plot_graphics_view = QtWidgets.QGraphicsView(self.main_plot_tab)
        self.plot_graphics_view.setObjectName("plot_graphics_view")
        self.verticalLayout_7.addWidget(self.plot_graphics_view)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.time_label = QtWidgets.QLabel(self.main_plot_tab)
        self.time_label.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_label.setObjectName("time_label")
        self.verticalLayout_6.addWidget(self.time_label)
        self.measurement_duration_label = QtWidgets.QLabel(self.main_plot_tab)
        self.measurement_duration_label.setMaximumSize(QtCore.QSize(200, 20))
        self.measurement_duration_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.measurement_duration_label.setObjectName("measurement_duration_label")
        self.verticalLayout_6.addWidget(self.measurement_duration_label)
        self.measument_durtion_combo_box = QtWidgets.QComboBox(self.main_plot_tab)
        self.measument_durtion_combo_box.setMaximumSize(QtCore.QSize(200, 16777215))
        self.measument_durtion_combo_box.setObjectName("measument_durtion_combo_box")
        self.measument_durtion_combo_box.addItem("")
        self.measument_durtion_combo_box.addItem("")
        self.measument_durtion_combo_box.addItem("")
        self.verticalLayout_6.addWidget(self.measument_durtion_combo_box)
        self.company_label = QtWidgets.QLabel(self.main_plot_tab)
        self.company_label.setMaximumSize(QtCore.QSize(200, 20))
        self.company_label.setObjectName("company_label")
        self.verticalLayout_6.addWidget(self.company_label)
        self.company_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.company_input.setMaximumSize(QtCore.QSize(200, 20))
        self.company_input.setObjectName("company_input")
        self.verticalLayout_6.addWidget(self.company_input)
        self.id_label = QtWidgets.QLabel(self.main_plot_tab)
        self.id_label.setMaximumSize(QtCore.QSize(200, 20))
        self.id_label.setObjectName("id_label")
        self.verticalLayout_6.addWidget(self.id_label)
        self.id_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.id_input.setMaximumSize(QtCore.QSize(200, 20))
        self.id_input.setObjectName("id_input")
        self.verticalLayout_6.addWidget(self.id_input)
        self.location_label = QtWidgets.QLabel(self.main_plot_tab)
        self.location_label.setMaximumSize(QtCore.QSize(200, 20))
        self.location_label.setObjectName("location_label")
        self.verticalLayout_6.addWidget(self.location_label)
        self.location_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.location_input.setMaximumSize(QtCore.QSize(200, 20))
        self.location_input.setObjectName("location_input")
        self.verticalLayout_6.addWidget(self.location_input)
        self.country_label = QtWidgets.QLabel(self.main_plot_tab)
        self.country_label.setMaximumSize(QtCore.QSize(200, 20))
        self.country_label.setObjectName("country_label")
        self.verticalLayout_6.addWidget(self.country_label)
        self.country_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.country_input.setMaximumSize(QtCore.QSize(200, 20))
        self.country_input.setObjectName("country_input")
        self.verticalLayout_6.addWidget(self.country_input)
        self.load_number_id_label = QtWidgets.QLabel(self.main_plot_tab)
        self.load_number_id_label.setMaximumSize(QtCore.QSize(200, 20))
        self.load_number_id_label.setObjectName("load_number_id_label")
        self.verticalLayout_6.addWidget(self.load_number_id_label)
        self.load_number_id_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.load_number_id_input.setMaximumSize(QtCore.QSize(200, 20))
        self.load_number_id_input.setObjectName("load_number_id_input")
        self.verticalLayout_6.addWidget(self.load_number_id_input)
        self.registrated_number_label = QtWidgets.QLabel(self.main_plot_tab)
        self.registrated_number_label.setMaximumSize(QtCore.QSize(200, 20))
        self.registrated_number_label.setObjectName("registrated_number_label")
        self.verticalLayout_6.addWidget(self.registrated_number_label)
        self.registrated_number_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.registrated_number_input.setMaximumSize(QtCore.QSize(200, 20))
        self.registrated_number_input.setObjectName("registrated_number_input")
        self.verticalLayout_6.addWidget(self.registrated_number_input)
        self.treatment_location_label = QtWidgets.QLabel(self.main_plot_tab)
        self.treatment_location_label.setMaximumSize(QtCore.QSize(200, 20))
        self.treatment_location_label.setObjectName("treatment_location_label")
        self.verticalLayout_6.addWidget(self.treatment_location_label)
        self.treatment_location_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.treatment_location_input.setMaximumSize(QtCore.QSize(200, 20))
        self.treatment_location_input.setObjectName("treatment_location_input")
        self.verticalLayout_6.addWidget(self.treatment_location_input)
        self.type_of_material_label = QtWidgets.QLabel(self.main_plot_tab)
        self.type_of_material_label.setMaximumSize(QtCore.QSize(200, 20))
        self.type_of_material_label.setObjectName("type_of_material_label")
        self.verticalLayout_6.addWidget(self.type_of_material_label)
        self.type_of_material_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.type_of_material_input.setMaximumSize(QtCore.QSize(200, 20))
        self.type_of_material_input.setObjectName("type_of_material_input")
        self.verticalLayout_6.addWidget(self.type_of_material_input)
        self.quantity_label = QtWidgets.QLabel(self.main_plot_tab)
        self.quantity_label.setMaximumSize(QtCore.QSize(200, 20))
        self.quantity_label.setObjectName("quantity_label")
        self.verticalLayout_6.addWidget(self.quantity_label)
        self.quantity_inpeu = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.quantity_inpeu.setMaximumSize(QtCore.QSize(200, 20))
        self.quantity_inpeu.setObjectName("quantity_inpeu")
        self.verticalLayout_6.addWidget(self.quantity_inpeu)
        self.verification_label = QtWidgets.QLabel(self.main_plot_tab)
        self.verification_label.setMaximumSize(QtCore.QSize(200, 20))
        self.verification_label.setObjectName("verification_label")
        self.verticalLayout_6.addWidget(self.verification_label)
        self.verificaion_input = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.verificaion_input.setMaximumSize(QtCore.QSize(200, 20))
        self.verificaion_input.setObjectName("verificaion_input")
        self.verticalLayout_6.addWidget(self.verificaion_input)
        self.note_label = QtWidgets.QLabel(self.main_plot_tab)
        self.note_label.setMaximumSize(QtCore.QSize(200, 20))
        self.note_label.setObjectName("note_label")
        self.verticalLayout_6.addWidget(self.note_label)
        self.note_iinput = QtWidgets.QPlainTextEdit(self.main_plot_tab)
        self.note_iinput.setMaximumSize(QtCore.QSize(200, 40))
        self.note_iinput.setObjectName("note_iinput")
        self.verticalLayout_6.addWidget(self.note_iinput)
        self.record_button = QtWidgets.QPushButton(self.main_plot_tab)
        self.record_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.record_button.setObjectName("record_button")
        self.verticalLayout_6.addWidget(self.record_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.main_plot_tab, "")
        self.archive_tab = QtWidgets.QWidget()
        self.archive_tab.setObjectName("archive_tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.archive_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.archive_time_label = QtWidgets.QLabel(self.archive_tab)
        self.archive_time_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.archive_time_label.setObjectName("archive_time_label")
        self.verticalLayout_2.addWidget(self.archive_time_label)
        self.measurements_list_widget = QtWidgets.QListWidget(self.archive_tab)
        self.measurements_list_widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.measurements_list_widget.setObjectName("measurements_list_widget")
        self.verticalLayout_2.addWidget(self.measurements_list_widget)
        self.print_btn = QtWidgets.QPushButton(self.archive_tab)
        self.print_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.print_btn.setObjectName("print_btn")
        self.verticalLayout_2.addWidget(self.print_btn)
        self.save_btn = QtWidgets.QPushButton(self.archive_tab)
        self.save_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout_2.addWidget(self.save_btn)
        self.delete_btn = QtWidgets.QPushButton(self.archive_tab)
        self.delete_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.delete_btn.setObjectName("delete_btn")
        self.verticalLayout_2.addWidget(self.delete_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.plot_graphics_view_2 = QtWidgets.QGraphicsView(self.archive_tab)
        self.plot_graphics_view_2.setObjectName("plot_graphics_view_2")
        self.horizontalLayout_2.addWidget(self.plot_graphics_view_2)
        self.tabWidget.addTab(self.archive_tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 21))
        self.menubar.setObjectName("menubar")
        self.menuPorts = QtWidgets.QMenu(self.menubar)
        self.menuPorts.setObjectName("menuPorts")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPorts_settings = QtWidgets.QAction(MainWindow)
        self.actionPorts_settings.setObjectName("actionPorts_settings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuPorts.addAction(self.actionPorts_settings)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuPorts.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.measument_durtion_combo_box.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial port logging"))
        self.time_label.setText(_translate("MainWindow", "00:00:00"))
        self.measurement_duration_label.setText(_translate("MainWindow", "Measument duration"))
        self.measument_durtion_combo_box.setItemText(0, _translate("MainWindow", "24h"))
        self.measument_durtion_combo_box.setItemText(1, _translate("MainWindow", "12h"))
        self.measument_durtion_combo_box.setItemText(2, _translate("MainWindow", "1h"))
        self.company_label.setText(_translate("MainWindow", "Company"))
        self.id_label.setText(_translate("MainWindow", "ID"))
        self.location_label.setText(_translate("MainWindow", "Location"))
        self.country_label.setText(_translate("MainWindow", "Country"))
        self.load_number_id_label.setText(_translate("MainWindow", "Load number ID"))
        self.registrated_number_label.setText(_translate("MainWindow", "Registrated number"))
        self.treatment_location_label.setText(_translate("MainWindow", "Treatment location"))
        self.type_of_material_label.setText(_translate("MainWindow", "Type of material"))
        self.quantity_label.setText(_translate("MainWindow", "Quantity"))
        self.verification_label.setText(_translate("MainWindow", "Verification"))
        self.note_label.setText(_translate("MainWindow", "Note"))
        self.record_button.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_plot_tab), _translate("MainWindow", "Main plot"))
        self.archive_time_label.setText(_translate("MainWindow", "Time of measurement"))
        self.print_btn.setText(_translate("MainWindow", "Print"))
        self.save_btn.setText(_translate("MainWindow", "Save as PDF"))
        self.delete_btn.setText(_translate("MainWindow", "Delete record"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.archive_tab), _translate("MainWindow", "Archive"))
        self.menuPorts.setTitle(_translate("MainWindow", "Ports"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionPorts_settings.setText(_translate("MainWindow", "Port settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


