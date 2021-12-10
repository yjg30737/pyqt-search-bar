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

## Example
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

Result

Result that label, close button exist

![image](https://user-images.githubusercontent.com/55078043/145547732-50cd6c6b-3511-4e6c-86c3-b07b1449a5ce.png)

Result that shows the search bar only

![image](https://user-images.githubusercontent.com/55078043/145549188-8b004289-53c1-4b97-a36c-c3e568800ad3.png)

