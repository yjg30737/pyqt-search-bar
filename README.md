# pyqt-search-bar
PyQt search bar

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-search-bar`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a>

## Feature
* Providing `searched(text: str)` signal to activate user-defined method after search.
* Set place holder directly with `setPlaceHolder(text: str)`.
* Available to execute the search with either pressing enter or pressing the search button.
* Toggled search button based on whether searchLineEdit(type is QLineEdit) is empty or not.
* Being able to get searchLineEdit and searchButton, closeButton to let user customize on their own.
* Being able to set the label of the search bar with `setLabel(visibility: bool, text: str)`.
* Being able to close the search bar with `setCloseBtn(visibility: bool)`.
* Set search/close button's icon with `setSearchIcon(icon_filename: str)`, `setCloseIcon(icon_filename: str)`. Note: Icon should be SVG file.
* Get search bar, search line edit, search/close button with `getSearchBar`, `getSearchLineEdit`, `getSearchButton`, `getCloseButton` to change style or feature.

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
    searchBar.setPlaceHolder('Input the text...')
    searchBar.show()
    app.exec_()
```

#### Result

Empty search bar (search button is disabled)

![image](https://user-images.githubusercontent.com/55078043/167742517-108289ad-4560-4636-bbcf-f311700c8e06.png)

Search bar which is not empty (search button is enabled)

![image](https://user-images.githubusercontent.com/55078043/167742674-9270435a-18f9-47fb-abf3-9144cb3d5035.png)

See Also
* <a href="https://github.com/yjg30737/pyqt-instant-search-bar">pyqt-instant-search-bar</a> - for instant search feature
