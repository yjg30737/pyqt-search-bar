from setuptools import setup, find_packages

setup(
    name='pyqt-search-bar',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_search_bar.style': ['button.css', 'lineedit.css'],
                  'pyqt_search_bar.ico': ['close.png', 'search.png']},
    description='PyQt search bar',
    url='https://github.com/yjg30737/pyqt-search-bar.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)