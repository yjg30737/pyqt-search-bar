from PyQt5.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, \
    QHBoxLayout, QCompleter
from PyQt5.QtCore import Qt, pyqtSignal
from pyqt_resource_helper import PyQtResourceHelper
from pyqt_svg_button import SvgButton


class SearchBar(QWidget):
    # ex) searchBar.searched.connect(myMethod)
    # str is searched text
    searched = pyqtSignal(str)
    instantSearched = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # search bar label
        self.__label = QLabel()
        self.__closeBtn = SvgButton()
        self.__btns = []

        self._initUi()

    def _initUi(self):
        self.__searchLineEdit = QLineEdit()
        self.__searchBtn = SvgButton()

        self.__btns.append(self.__searchBtn)
        self.__btns.append(self.__closeBtn)

        self.__searchBar = QWidget()
        self.__searchBar.setObjectName('searchBar')

        lay = QHBoxLayout()
        lay.addWidget(self.__searchLineEdit)
        lay.addWidget(self.__searchBtn)
        self.__searchBar.setLayout(lay)
        lay.setContentsMargins(0, 0, 2, 0)
        lay.setSpacing(2)

        self.__searchLineEdit.textChanged.connect(self.__searchLineEditTextChanged)
        self.__searchLineEdit.textChanged.connect(self.__instantSearch)
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

        lay = QGridLayout()
        lay.addWidget(self._topWidget)

        searchWidget = QWidget()
        searchWidget.setLayout(lay)
        lay.setContentsMargins(0, 0, 0, 0)

        lay = QGridLayout()
        lay.addWidget(searchWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        self.__setStyle()

        self.setLayout(lay)

    def __instantSearch(self, text=None):
        text = text if text else self.__searchLineEdit.text()
        self.instantSearched.emit(text)

    def __search(self, text=None):
        text = text if text else self.__searchLineEdit.text()
        self.searched.emit(text)

    # ex) searchBar.setCloseBtn(True)
    def setCloseBtnVisible(self, visibility: bool = True):
        self.__closeBtn.setVisible(visibility)
        self.__closeBtn.clicked.connect(self.__hideSearchBar)

    # ex) searchBar.setLabel(True, 'Search Text')
    def setLabel(self, visibility: bool = True, text=None):
        if text:
            self.__label.setText(text)
        self.__label.setVisible(visibility)

    def __setStyle(self):
        self.__searchBtn.setIcon('ico\search.svg')
        self.__closeBtn.setIcon('ico\close.svg')
        PyQtResourceHelper.setStyleSheet([self.__searchLineEdit, self.__searchBar, self],
                                         ['style/lineedit.css', 'style/search_bar.css', 'style/widget.css'])

    def setSearchIcon(self, icon_filename: str):
        self.__searchBtn.setIcon(icon_filename)

    def setCloseIcon(self, icon_filename: str):
        self.__closeBtn.setIcon(icon_filename)

    def setPlaceHolder(self, text: str):
        self.__searchLineEdit.setPlaceholderText(text)

    def getSearchBar(self):
        return self.__searchLineEdit

    def getSearchLineEdit(self):
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

    def setCompleter(self, completer: QCompleter):
        self.__searchLineEdit.setCompleter(completer)

    def showEvent(self, e):
        self.__searchLineEdit.setFocus()