# GUI CODE - Daniel Bonilla Urtis
# ++++++++++++++++++++++++++++++++++++++++
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from __feature__ import snake_case, true_property
from functions import my_search

class image_search_app(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.welcome_label = QLabel("Homework 3: Image search")
        self.prompt_label = QLabel("Type in a search word:")
        self.my_lineedit = QLineEdit("")
        self.my_lineedit.minimum_width(250)
        self.my_lineedit.selectAll()
        self.my_btn = QPushButton("Submit")
        self.my_lbl = QLabel('')
        self.my_btn.clicked.connect(self.on_submit)
        self.my_lineedit.returnPressed.connect(self.on_submit)

        self.my_list = ["Pick a manipulation", "Sepia", "Negative", "Grayscale", "Thumbnail", "None"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")

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
        try:
            search_term = self.search_input.text()
            image_path = my_search(search_term)  # Assuming this returns a string path
            if image_path:
                pixmap = QPixmap(image_path)  # Correct usage
                self.image_label.setPixmap(pixmap)
            else: 
                pixmap = QPixmap("no_results.jpg")
                self.image_label.setPixmap(pixmap)
        except Exception as e:
            print(f"Error: {e}")


app = QApplication([])
my_win = image_search_app()
my_win.show()
sys.exit(app.exec())
