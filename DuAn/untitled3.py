# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 14:07:03 2024

@author: LENOVO
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

class PersonalInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Tạo các thành phần
        self.name_label = QLabel('Họ và tên:')
        self.phone_label = QLabel('Số điện thoại:')
        self.name_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)
        self.save_button = QPushButton('Lưu thông tin', self)
        self.clear_button = QPushButton('Xóa thông tin', self)
        self.display_name_label = QLabel('Họ và tên:')
        self.display_phone_label = QLabel('Số điện thoại:')
        self.error_label = QLabel('')

        # Tạo layout
        vbox = QVBoxLayout()
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.name_label)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.phone_label)
        form_layout.addWidget(self.phone_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)

        display_layout = QVBoxLayout()
        display_layout.addWidget(self.display_name_label)
        display_layout.addWidget(self.display_phone_label)
        display_layout.addWidget(self.error_label)

        vbox.addLayout(form_layout)
        vbox.addLayout(button_layout)
        vbox.addLayout(display_layout)

        self.setLayout(vbox)

        # Thiết lập các kết nối sự kiện
        self.save_button.clicked.connect(self.save_info)
        self.clear_button.clicked.connect(self.clear_info)

        # Thiết lập cửa sổ
        self.setWindowTitle('Quản lý thông tin cá nhân')
        self.show()

    def save_info(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        if not phone.isdigit() or len(phone) != 10:
            self.error_label.setText('Số điện thoại không hợp lệ')
            self.display_name_label.setText('Họ và tên:')
            self.display_phone_label.setText('Số điện thoại:')
        else:
            self.error_label.setText('')
            self.display_name_label.setText(f'Họ và tên: {name}')
            self.display_phone_label.setText(f'Số điện thoại: {phone}')

    def clear_info(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.display_name_label.setText('Họ và tên:')
        self.display_phone_label.setText('Số điện thoại:')
        self.error_label.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PersonalInfoApp()
    sys.exit(app.exec_())
