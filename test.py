# GUI CODE - Daniel Bonilla Urtis
# ++++++++++++++++++++++++++++++++++++++++
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from __feature__ import snake_case, true_property
from image_info import image_info
from functions import my_search

class image_search_app(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.welcome_label = QLabel("Homework 3: Image Search and Manipulation")
        self.prompt_label = QLabel("Type in a search word:")
        self.my_lineedit = QLineEdit()
        self.my_lineedit.minimum_width = 300
        # self.my_lineedit.select_all()
        self.my_btn = QPushButton("Submit")
        self.my_lbl = QLabel()
        self.my_btn.clicked.connect(self.search)
        self.my_lineedit.returnPressed.connect(self.search)

        self.my_list = ["Choose a manipulation method", "Sepia", "Negative", "Grayscale", "Thumbnail", "None"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel()

        vbox.add_widget(self.welcome_label)
        vbox.add_widget(self.prompt_label)
        vbox.add_widget(self.my_lineedit)
        vbox.add_widget(self.my_lbl)
        
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)

        vbox.add_widget(self.my_btn)

        self.set_layout(vbox)

    @Slot()
    def search(self):
        search_term = self.my_lineedit.text()
        my_index = self.my_combo_box.current_index()
        result = my_search(search_term, my_index)  # Ensure my_search accepts my_index if needed
        if result["status"] == "found":
            pixmap = QPixmap(result["image_path"])
            self.my_lbl.setPixmap(pixmap)
        else:
            self.my_lbl.setText(result["message"])


app = QApplication([])
my_win = image_search_app()
my_win.show()
sys.exit(app.exec())