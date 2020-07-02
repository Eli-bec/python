## Install Python
Install the latest version of python and make sure you install pip with it. (by default, it should be installed automatically)  
Test it with `pip3 --version` (`pip` for python2, `pip3` for python3)

## Install Selenium
With pip installed, you can simply install selenium by `pip3 install selenium`  

## Install Driver
To make selenium working, you will also need to install the correct driver according to your browser.  
Drivers can be found here: https://selenium-python.readthedocs.io/installation.html#drivers (you will need to find the version of your browser)  
Extract the zip file and put the executable in your PATH, e.g. `/usr/bin` or `/usr/local/bin`  

## Install BeautifulSoup
`pip3 install beautifulsoup4`

## Install lxml
BeautifulSoup requires the lxml module, fortunatly it can also be install with pip.
`pip3 install lxml`

## Test the Installation
The installation should be done now, you can test it with the following program.  
[test_selenium-chrome.py](test_selenium-chrome.py)
