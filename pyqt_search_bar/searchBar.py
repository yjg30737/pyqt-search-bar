import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QGridLayout, QLabel, \
    QHBoxLayout, QApplication
from PyQt5.QtCore import Qt, pyqtSignal


class SearchBar(QWidget):
    # ex) searchBar.searched.connect(myMethod)
    # str is searched text
    searched = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # search bar label
        self.__label = QLabel()
        self.__closeBtn = QPushButton()
        self.__btns = []

        self._initUi()

    def _initUi(self):
        self.__searchLineEdit = QLineEdit()
        self.__searchBtn = QPushButton()

        self.__btns.append(self.__searchBtn)
        self.__btns.append(self.__closeBtn)

        self.__searchBar = QWidget()
        self.__searchBar.setObjectName('searchBar')

        lay = QHBoxLayout()
        lay.addWidget(self.__searchLineEdit)
        lay.addWidget(self.__searchBtn)
        self.__searchBar.setLayout(lay)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(2)

        self.__searchLineEdit.textChanged.connect(self.__searchLineEditTextChanged)
        self.__searchLineEdit.setFocus()

        self.__searchBtn.setEnabled(False)
        self.setAutoFillBackground(True)

        # Signal will be activated if user presses enter button or
        # presses search button with the mouse cursor
        self.__searchLineEdit.returnPressed.connect(self.__search)
        self.__searchBtn.clicked.connect(self.__search)

        self.__label.setText('Search')

        self.__label.setVisible(False)
        self.__closeBtn.setVisible(False)

        lay = QHBoxLayout()
        lay.addWidget(self.__label)
        lay.addWidget(self.__searchBar)
        lay.addWidget(self.__closeBtn)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(2)

        self._topWidget = QWidget()
        self._topWidget.setLayout(lay)

        searchBarLayout = QGridLayout()
        searchBarLayout.addWidget(self._topWidget)

        searchWidget = QWidget()
        searchWidget.setLayout(searchBarLayout)

        lay = QGridLayout()
        lay.addWidget(searchWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        self.__setStyle()

        self.setLayout(lay)

    def __search(self, text=None):
        text = text if text else self.__searchLineEdit.text()
        self.searched.emit(text)

    # ex) searchBar.setCloseBtn(True)
    def setCloseBtn(self, visibility: bool = True):
        self.__closeBtn.setVisible(visibility)
        self.__closeBtn.clicked.connect(self.__hideSearchBar)

    # ex) searchBar.setLabel(True, 'Search Text')
    def setLabel(self, visibility: bool = True, text=None):
        if text:
            self.__label.setText(text)
        self.__label.setVisible(visibility)

    def __setStyle(self):
        border_style = 'QWidget#searchBar { border: 1px solid gray; }'

        rel_dirname = os.path.dirname(os.path.relpath(__file__, os.getcwd()))

        css_file_path = os.path.join(rel_dirname, r'style/lineedit.css')
        css_file = open(css_file_path)
        lineedit_style_code = css_file.read()
        css_file.close()

        css_file_path = os.path.join(rel_dirname, r'style/button.css')
        css_file = open(css_file_path)
        btn_style_code = css_file.read()
        css_file.close()

        for btn in self.__btns:
            btn.setStyleSheet(btn_style_code)

        search_btn_ico = 'ico/search.png'
        close_btn_ico = 'ico/close.png'

        self.__searchLineEdit.setStyleSheet(lineedit_style_code)
        self.__searchBar.setStyleSheet(border_style)
        self.__searchBtn.setIcon(QIcon(os.path.join(rel_dirname, search_btn_ico)))
        self.__closeBtn.setIcon(QIcon(os.path.join(rel_dirname, close_btn_ico)))

        self.setStyleSheet('QWidget { padding: 5px; }')

    def setPlaceHolder(self, text: str):
        self.__searchLineEdit.setPlaceholderText(text)

    def getSearchBar(self):
        return self.__searchLineEdit

    def getSearchButton(self):
        return self.__searchBtn

    def getCloseButton(self):
        return self.__closeBtn

    def __searchLineEditTextChanged(self):
        self.__searchBtn.setEnabled(self.__searchLineEdit.text().strip() != '')

    def showSearchBar(self, layout):
        self.__execShowSearchBar(layout)

    def __execShowSearchBar(self, layout):
        if isinstance(layout, QGridLayout):
            layout.addWidget(self, 0, 0, 1, 1, Qt.AlignTop)
            self.__searchLineEdit.setFocus()

    def __hideSearchBar(self):
        self.hide()

    def showEvent(self, e):
        self.__searchLineEdit.setFocus()