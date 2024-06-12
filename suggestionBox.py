from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QListView,QVBoxLayout
from PyQt5.QtCore import QStringListModel



class SuggestionBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textbox = QLineEdit(self)
        self.textbox.textChanged.connect(self.filter_suggestions)

        # Create a list of suggestions (replace with your data source)
        self.all_suggestions = ["apple", "banana", "cherry", "orange"]

        # Create the QListView
        self.suggestion_list = QListView(self)

        # Create the QStringListModel (model for the list view)
        self.model = QStringListModel(self.all_suggestions, self)
        self.suggestion_list.setModel(self.model)

        self.textbox.setFocus()  # Set focus on the textbox for immediate input

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.suggestion_list)
        self.setLayout(self.layout)

        self.show()

    def filter_suggestions(self, text):
        filtered_suggestions = [s for s in self.all_suggestions if text.lower() in s.lower()]
        self.model.setStringList(filtered_suggestions)

if __name__ == '__main__':
    app = QApplication([])
    window = SuggestionBox()
    app.exec_()
