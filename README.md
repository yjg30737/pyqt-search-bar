# pyqt-search-bar
PyQt search bar

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-search-bar.git --upgrade```

## Feature
* Being able to set the label of the search bar with ```setLabel(visibility: bool, text: str)```
* Being able to close the search bar with ```setCloseBtn(visibility: bool)```
* Providing ```searched(text: str)``` signal to activate user-defined method after search
* Set place holder directly with ```setPlaceHolder(text: str)```
* Available to execute the search with either pressing enter or pressing the search button
* Toggled search button based on whether searchLineEdit(type is QLineEdit) is empty or not.
* Being able to get searchLineEdit and searchButton, closeButton to let user customize on their own

## Example
### Basic
Code Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_search_bar import SearchBar


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    searchBar = SearchBar()
    searchBar.searched.connect(print)
    searchBar.setCloseBtn(True)
    searchBar.setLabel(True, 'abc')
    searchBar.setPlaceHolder('abcd')
    searchBar.show()
    app.exec_()
```

#### Result

Result that label, close button exist

![image](https://user-images.githubusercontent.com/55078043/145547732-50cd6c6b-3511-4e6c-86c3-b07b1449a5ce.png)

Result that shows the search bar only

![image](https://user-images.githubusercontent.com/55078043/145549188-8b004289-53c1-4b97-a36c-c3e568800ad3.png)

### Interaction with QCompleter and QListWidget
Code Example
```python
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QCompleter, QStackedWidget, \
    QPushButton, QHBoxLayout, QMessageBox
from pyqt_search_bar import SearchBar


class SearchBarExampleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        searchBarVisibilityToggleBtn = QPushButton('Show search bar')
        searchBarVisibilityToggleBtn.setCheckable(True)
        searchBarVisibilityToggleBtn.setChecked(True)
        searchBarVisibilityToggleBtn.toggled.connect(self.__searchBarVisibilityToggled)

        refreshBtn = QPushButton('Refresh')
        refreshBtn.clicked.connect(self.__refresh)

        lay = QHBoxLayout()
        lay.addWidget(searchBarVisibilityToggleBtn)
        lay.addWidget(refreshBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        btnsWidget = QWidget()
        btnsWidget.setLayout(lay)

        self.__searchBar = SearchBar()
        self.__searchBar.searched.connect(self.__searched)
        self.__searchBar.setPlaceHolder('abcd')

        lorem_str = '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat risus aliquam, placerat purus nec, efficitur risus. Proin sed accumsan orci, vel sagittis elit. Maecenas porta enim id condimentum maximus. Nullam imperdiet vel ipsum eget aliquet. Maecenas ac ullamcorper orci, eu elementum tortor. Curabitur turpis urna, hendrerit dignissim lacus ac, auctor feugiat erat. Quisque felis magna, rhoncus eget hendrerit sit amet, fermentum et mauris. Proin at sodales urna. Fusce feugiat nisi id est faucibus, nec laoreet massa tempor. Etiam auctor urna sed consequat pellentesque. Ut sit amet scelerisque nibh. Vestibulum nec finibus ex. Pellentesque pretium hendrerit augue, a egestas turpis elementum quis. Nunc lectus felis, dapibus ac ante nec, tristique sodales felis. Morbi egestas malesuada accumsan. Donec vulputate, eros in ullamcorper vulputate, elit leo lacinia ex, vel aliquet metus turpis at quam.
        Fusce pellentesque tincidunt est nec egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; In suscipit ipsum eget finibus tincidunt. Duis blandit, neque molestie scelerisque volutpat, justo ex facilisis orci, ac tincidunt tortor massa quis dolor. Sed vitae felis auctor, eleifend neque vitae, blandit purus. Nulla risus urna, dapibus ut cursus et, dignissim non elit. Nam malesuada sollicitudin accumsan. Nam ut suscipit dolor, a laoreet urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sed dui nec mauris elementum hendrerit quis non diam. Mauris in diam eu est congue molestie. Sed dignissim felis nibh.
        '''
        lorem_str = lorem_str.replace('.', '') 
        lorem_str = lorem_str.replace(',', '')
        lorem_str_lst = lorem_str.split()

        completer = QCompleter(lorem_str_lst)
        self.__searchBar.setCompleter(completer)

        self.__listWidget = QListWidget()
        self.__listWidget.addItems(lorem_str_lst) # QListWidget which contained texts to be searched
        
        self.__resultListWidget = QListWidget() # QListWidget for search result
        
        self.__listStackedWidget = QStackedWidget() # In order to place listWidget and result list widget the same area
        self.__listStackedWidget.addWidget(self.__listWidget)
        self.__listStackedWidget.addWidget(self.__resultListWidget)

        lay = QVBoxLayout()
        lay.addWidget(btnsWidget)
        lay.addWidget(self.__searchBar)
        lay.addWidget(self.__listStackedWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

    def __searched(self, text):
        items = self.__listWidget.findItems(text, Qt.MatchFixedString | Qt.MatchCaseSensitive)
        if items:
            self.__resultListWidget.clear()
            for item in items:
                text = item.text()
                self.__resultListWidget.addItem(text)
                self.__listStackedWidget.setCurrentWidget(self.__resultListWidget) # Show result widget
        else:
            QMessageBox.information(self, 'Not Found', f"Searched text {text} is not found.")
        
    def __searchBarVisibilityToggled(self, f):
        self.__searchBar.setVisible(f)

    def __refresh(self):
        self.__resultListWidget.clear()
        self.__listStackedWidget.setCurrentWidget(self.__listWidget) # Back to list widget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    searchBarExampleWindow = SearchBarExampleWindow()
    searchBarExampleWindow.show()
    app.exec_()
```

#### Result

Completer

![image](https://user-images.githubusercontent.com/55078043/145658505-a82e3c3d-c019-4cdb-aa5c-3524f93e246a.png)

Search result

![image](https://user-images.githubusercontent.com/55078043/145658652-030856c1-2bd5-4a19-aa49-307d5caa3cae.png)

Refresh

![image](https://user-images.githubusercontent.com/55078043/145658677-815e9061-2340-4650-943b-74305300b76d.png)

Hide the search bar

![image](https://user-images.githubusercontent.com/55078043/145658690-27d8b13a-3168-4611-b360-162657ddd0f7.png)


