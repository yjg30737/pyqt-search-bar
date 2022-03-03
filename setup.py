from setuptools import setup, find_packages

setup(
    name='pyqt-search-bar',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_search_bar.style': ['lineedit.css', 'search_bar.css', 'widget.css'],
                  'pyqt_search_bar.ico': ['close.svg', 'search.svg']},
    description='PyQt search bar',
    url='https://github.com/yjg30737/pyqt-search-bar.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main'
    ]
)