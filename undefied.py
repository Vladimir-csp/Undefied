#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QHBoxLayout, QVBoxLayout, QTabWidget, QListWidget, QCheckBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):

    # main window
    self.setWindowTitle('Undefied')
    self.setWindowIcon(QIcon.fromTheme('display')) # placeholder
    self.resize(600, 600)

    #### main area structure
    main_area = QTabWidget()
    main_tab1 = QWidget()
    main_tab2 = QWidget()
    main_tab3 = QWidget()
    main_tab4 = QWidget()
    main_area.addTab(main_tab1, 'Applications')
    main_area.addTab(main_tab2, 'Autostart')
    main_area.addTab(main_tab3, 'Directories')
    main_area.addTab(main_tab4, 'Menu')

    #### Applications
    app_sys_list = QListWidget()
    app_usr_list = QListWidget()
    app_show_foreign = QCheckBox('Show hidden and foreign applications')
    app_show_foreign.setToolTip('Show applications which are hidden from the current environment\nby such parameters as Hidden, NotShowIn, OnlyShowIn')

    #### Autostart
    autostart_sys_list = QListWidget()
    autostart_usr_list = QListWidget()
    autostart_show_foreign = QCheckBox('Show hidden and foreign autostart applications')
    autostart_show_foreign.setToolTip('Show autostart applications which are hidden from the current environment\nby such parameters as Hidden, NotShowIn, OnlyShowIn')

    #### Directories
    dir_sys_list = QListWidget()
    dir_usr_list = QListWidget()
    dir_show_foreign = QCheckBox('Show hidden and foreign directories')
    dir_show_foreign.setToolTip('Show destkop directories which are hidden from the current environment\nby such parameters as Hidden, NotShowIn, OnlyShowIn')

    #### Menu
    menu_sys_list = QListWidget()
    menu_usr_list = QListWidget()


    #### bottom buttons
    ## close
    close_btn = QPushButton('Cancel', self)
    close_btn.setToolTip('Close without saving')
    close_btn.resize(close_btn.sizeHint())
    close_btn.clicked.connect(QCoreApplication.instance().quit)

    ## apply
    apply_btn = QPushButton('Apply', self)
    apply_btn.setToolTip('Apply config')
    apply_btn.resize(apply_btn.sizeHint())
#    apply_btn.clicked.connect(QCoreApplication.instance().quit)

    # root layout
    root_layout = QVBoxLayout()

    # Applications layout
    app_root_layout = QVBoxLayout()
    app_lists_layout = QHBoxLayout()
    app_lists_layout.addWidget(app_sys_list)
    app_lists_layout.addWidget(app_usr_list)
    app_root_layout.addLayout(app_lists_layout)
    app_root_layout.addWidget(app_show_foreign)
    main_tab1.setLayout(app_root_layout)

    # Autostart layout
    autostart_root_layout = QVBoxLayout()
    autostart_lists_layout = QHBoxLayout()
    autostart_lists_layout.addWidget(autostart_sys_list)
    autostart_lists_layout.addWidget(autostart_usr_list)
    autostart_root_layout.addLayout(autostart_lists_layout)
    autostart_root_layout.addWidget(autostart_show_foreign)
    main_tab2.setLayout(autostart_root_layout)

    # Applications layout
    dir_root_layout = QVBoxLayout()
    dir_lists_layout = QHBoxLayout()
    dir_lists_layout.addWidget(dir_sys_list)
    dir_lists_layout.addWidget(dir_usr_list)
    dir_root_layout.addLayout(dir_lists_layout)
    dir_root_layout.addWidget(dir_show_foreign)
    main_tab3.setLayout(dir_root_layout)

    # Applications layout
    menu_layout = QHBoxLayout()
    menu_layout.addWidget(menu_sys_list)
    menu_layout.addWidget(menu_usr_list)
    main_tab4.setLayout(menu_layout)

    # Bottom row of buttons
    bottom_row = QHBoxLayout()
    bottom_row.addStretch()
    bottom_row.addWidget(apply_btn)
    bottom_row.addWidget(close_btn)

    # Fill root_layout with main_area nad bottom_row
    root_layout.addWidget(main_area, 1)
    root_layout.addLayout(bottom_row)

    self.setLayout(root_layout)

    self.show()

#  def listItem(self):

if __name__ == '__main__':

  app = QApplication(sys.argv)
  ex = MainWindow()
  sys.exit(app.exec_())
