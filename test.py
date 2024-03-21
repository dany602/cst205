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
        self.set_window_role("Image Search Engine")
        set_layout = QVBoxLayout()
        self.resize(400, 300)

        self.search_input = QLineEdit()
        set_layout.add_widget(self.search_input)

# This is where the image manipulation takes place
        # self.manipulation_combo = QComboBox()
        # self.manipulation_combo.add_items(["None", "Sepia", "Negative", "Grayscale", "Thumbnail"])
        # set_layout.add_widget(self.manipulation_combo)

# This is for the button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search)
        self.search_input.returnPressed.connect(self.search)
        set_layout.add_widget(self.search_button)

        self.image_label = QLabel()
        set_layout.add_widget(self.image_label)

        self.set_layout(set_layout)

    @Slot()
    def search(self):
# This part of the code performs the search
        # manipulation = self.manipulation_combo.current_text()
        search_term = self.search_input.text()
        image_path = my_search(search_term)
        # Apply manipulation if selected
        # if manipulation == "None":
        #     image_path = apply_none(image_path)
        # elif manipulation == "Negative":
        #     image_path = apply_negative(image_path)
        # Apply other manipulations similarly
        print(image_path)

# Displays the image chosen from the input above, if not then the no_seults.jpg image should show
        if image_path:
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
        else: 
            pixmap = QPixmap("no_results.jpg")
            self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = image_search_app()
    window.show()
    sys.exit(app.exec())
