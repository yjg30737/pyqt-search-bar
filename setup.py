from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-search-bar',
    version='0.0.14',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_search_bar.style': ['lineedit.css', 'search_bar.css', 'widget.css'],
                  'pyqt_search_bar.ico': ['close.svg', 'search.svg']},
    description='PyQt search bar',
    url='https://github.com/yjg30737/pyqt-search-bar.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper>=0.0.1',
        'pyqt-svg-button>=0.0.1'
    ]
)