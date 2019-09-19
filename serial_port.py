# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial_port.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 801))
        self.tabWidget.setObjectName("tabWidget")
        self.main_plot_tab = QtWidgets.QWidget()
        self.main_plot_tab.setObjectName("main_plot_tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.main_plot_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 861, 761))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.view_vbox_layout = QtWidgets.QVBoxLayout()
        self.view_vbox_layout.setObjectName("view_vbox_layout")
        self.probe_data_table = QtWidgets.QTableView(self.horizontalLayoutWidget)
        self.probe_data_table.setMaximumSize(QtCore.QSize(16777215, 200))
        self.probe_data_table.setObjectName("probe_data_table")
        self.view_vbox_layout.addWidget(self.probe_data_table)
        self.plot_graphics_view = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.plot_graphics_view.setObjectName("plot_graphics_view")
        self.view_vbox_layout.addWidget(self.plot_graphics_view)
        self.horizontalLayout.addLayout(self.view_vbox_layout)
        self.control_vbox_layout = QtWidgets.QVBoxLayout()
        self.control_vbox_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.control_vbox_layout.setObjectName("control_vbox_layout")
        self.time_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.time_label.setMaximumSize(QtCore.QSize(200, 20))
        self.time_label.setObjectName("time_label")
        self.control_vbox_layout.addWidget(self.time_label)
        self.measurement_duration_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.measurement_duration_label.setMaximumSize(QtCore.QSize(200, 20))
        self.measurement_duration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.measurement_duration_label.setObjectName("measurement_duration_label")
        self.control_vbox_layout.addWidget(self.measurement_duration_label)
        self.measument_durtion_spinbox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.measument_durtion_spinbox.setMaximumSize(QtCore.QSize(200, 20))
        self.measument_durtion_spinbox.setObjectName("measument_durtion_spinbox")
        self.control_vbox_layout.addWidget(self.measument_durtion_spinbox)
        self.company_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.company_label.setMaximumSize(QtCore.QSize(200, 20))
        self.company_label.setObjectName("company_label")
        self.control_vbox_layout.addWidget(self.company_label)
        self.company_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.company_input.setMaximumSize(QtCore.QSize(200, 20))
        self.company_input.setObjectName("company_input")
        self.control_vbox_layout.addWidget(self.company_input)
        self.id_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.id_label.setMaximumSize(QtCore.QSize(200, 20))
        self.id_label.setObjectName("id_label")
        self.control_vbox_layout.addWidget(self.id_label)
        self.id_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.id_input.setMaximumSize(QtCore.QSize(200, 20))
        self.id_input.setObjectName("id_input")
        self.control_vbox_layout.addWidget(self.id_input)
        self.location_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.location_label.setMaximumSize(QtCore.QSize(200, 20))
        self.location_label.setObjectName("location_label")
        self.control_vbox_layout.addWidget(self.location_label)
        self.location_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.location_input.setMaximumSize(QtCore.QSize(200, 20))
        self.location_input.setObjectName("location_input")
        self.control_vbox_layout.addWidget(self.location_input)
        self.country_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.country_label.setMaximumSize(QtCore.QSize(200, 20))
        self.country_label.setObjectName("country_label")
        self.control_vbox_layout.addWidget(self.country_label)
        self.country_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.country_input.setMaximumSize(QtCore.QSize(200, 20))
        self.country_input.setObjectName("country_input")
        self.control_vbox_layout.addWidget(self.country_input)
        self.load_number_id_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.load_number_id_label.setMaximumSize(QtCore.QSize(200, 20))
        self.load_number_id_label.setObjectName("load_number_id_label")
        self.control_vbox_layout.addWidget(self.load_number_id_label)
        self.load_number_id_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.load_number_id_input.setMaximumSize(QtCore.QSize(200, 20))
        self.load_number_id_input.setObjectName("load_number_id_input")
        self.control_vbox_layout.addWidget(self.load_number_id_input)
        self.registrated_number_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.registrated_number_label.setMaximumSize(QtCore.QSize(200, 20))
        self.registrated_number_label.setObjectName("registrated_number_label")
        self.control_vbox_layout.addWidget(self.registrated_number_label)
        self.registrated_number_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.registrated_number_input.setMaximumSize(QtCore.QSize(200, 20))
        self.registrated_number_input.setObjectName("registrated_number_input")
        self.control_vbox_layout.addWidget(self.registrated_number_input)
        self.treatment_location_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.treatment_location_label.setMaximumSize(QtCore.QSize(200, 20))
        self.treatment_location_label.setObjectName("treatment_location_label")
        self.control_vbox_layout.addWidget(self.treatment_location_label)
        self.treatment_location_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.treatment_location_input.setMaximumSize(QtCore.QSize(200, 20))
        self.treatment_location_input.setObjectName("treatment_location_input")
        self.control_vbox_layout.addWidget(self.treatment_location_input)
        self.type_of_material_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.type_of_material_label.setMaximumSize(QtCore.QSize(200, 20))
        self.type_of_material_label.setObjectName("type_of_material_label")
        self.control_vbox_layout.addWidget(self.type_of_material_label)
        self.type_of_material_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.type_of_material_input.setMaximumSize(QtCore.QSize(200, 20))
        self.type_of_material_input.setObjectName("type_of_material_input")
        self.control_vbox_layout.addWidget(self.type_of_material_input)
        self.quantity_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.quantity_label.setMaximumSize(QtCore.QSize(200, 20))
        self.quantity_label.setObjectName("quantity_label")
        self.control_vbox_layout.addWidget(self.quantity_label)
        self.quantity_inpeu = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.quantity_inpeu.setMaximumSize(QtCore.QSize(200, 20))
        self.quantity_inpeu.setObjectName("quantity_inpeu")
        self.control_vbox_layout.addWidget(self.quantity_inpeu)
        self.verification_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.verification_label.setMaximumSize(QtCore.QSize(200, 20))
        self.verification_label.setObjectName("verification_label")
        self.control_vbox_layout.addWidget(self.verification_label)
        self.verificaion_input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.verificaion_input.setMaximumSize(QtCore.QSize(200, 20))
        self.verificaion_input.setObjectName("verificaion_input")
        self.control_vbox_layout.addWidget(self.verificaion_input)
        self.note_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.note_label.setMaximumSize(QtCore.QSize(200, 20))
        self.note_label.setObjectName("note_label")
        self.control_vbox_layout.addWidget(self.note_label)
        self.note_iinput = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.note_iinput.setMaximumSize(QtCore.QSize(200, 40))
        self.note_iinput.setObjectName("note_iinput")
        self.control_vbox_layout.addWidget(self.note_iinput)
        self.record_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.record_button.setObjectName("record_button")
        self.control_vbox_layout.addWidget(self.record_button)
        self.horizontalLayout.addLayout(self.control_vbox_layout)
        self.tabWidget.addTab(self.main_plot_tab, "")
        self.archive_tab = QtWidgets.QWidget()
        self.archive_tab.setObjectName("archive_tab")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.archive_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 931, 771))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.archive_time_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.archive_time_label.setObjectName("archive_time_label")
        self.verticalLayout_2.addWidget(self.archive_time_label)
        self.measurements_list_widget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.measurements_list_widget.setObjectName("measurements_list_widget")
        self.verticalLayout_2.addWidget(self.measurements_list_widget)
        self.print_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.print_btn.setObjectName("print_btn")
        self.verticalLayout_2.addWidget(self.print_btn)
        self.save_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout_2.addWidget(self.save_btn)
        self.delete_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.delete_btn.setObjectName("delete_btn")
        self.verticalLayout_2.addWidget(self.delete_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.plot_graphics_view_2 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_2)
        self.plot_graphics_view_2.setObjectName("plot_graphics_view_2")
        self.horizontalLayout_2.addWidget(self.plot_graphics_view_2)
        self.tabWidget.addTab(self.archive_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 21))
        self.menubar.setObjectName("menubar")
        self.menuPorts = QtWidgets.QMenu(self.menubar)
        self.menuPorts.setObjectName("menuPorts")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPorts_settings = QtWidgets.QAction(MainWindow)
        self.actionPorts_settings.setObjectName("actionPorts_settings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuPorts.addAction(self.actionPorts_settings)
        self.menubar.addAction(self.menuPorts.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial port logging"))
        self.time_label.setText(_translate("MainWindow", "00:00:00"))
        self.measurement_duration_label.setText(_translate("MainWindow", "Measument duration"))
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
        self.delete_btn.setText(_translate("MainWindow", "Delete file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.archive_tab), _translate("MainWindow", "Archive"))
        self.menuPorts.setTitle(_translate("MainWindow", "Ports"))
        self.actionPorts_settings.setText(_translate("MainWindow", "Port settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))