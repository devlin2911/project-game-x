# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 14:31:14 2024

@author: LENOVO
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class TextDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties (title and initial size)
        self.setWindowTitle("Hiển thị tên")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create widgets (QLineEdit, QPushButton, and QLabel)
        self.text_edit = QLineEdit()
        self.display_button = QPushButton("Hiển thị")
        self.result_label = QLabel("")

        # Create a vertical layout
        layout = QVBoxLayout()
        # Add widgets to the layout
        layout.addWidget(self.text_edit)
        layout.addWidget(self.display_button)
        layout.addWidget(self.result_label)
        
        # Set the layout for the central widget
        central_widget.setLayout(layout)
        
        # Connect the button click event to the display_text function
        self.display_button.clicked.connect(self.display_text)

    def display_text(self):
        # Get the text from the QLineEdit and display it in the QLabel
        entered_text = self.text_edit.text()
        self.result_label.setText(f"Tên của bạn là: {entered_text}")

def main():
    # Create a PyQt application
    app = QApplication(sys.argv)
    
    # Create an instance of the TextDisplayApp class
    window = TextDisplayApp()
    
    # Show the window
    window.show()
    
    # Run the application's event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

