Chicha Automation Framework
=========================

This Framework is built using:
- Python 3.9.10
- Behave (pip install behave==1.2.6)
- Expects (pip install expects==0.9.0)
- Selenium (pip install selenium==4.8.2)
- Behave HTML formatter (pip install behave-html-formatter==0.9.10)
- YAML (pip install PyYAML==6.0)
- PYODB (pip install pyodbc==4.0.35)
- Requests (pip install requests==2.28.2)

In order to run any test case from this framework a few things are also needed:
 - Chrome
 - A compatible version of Chromedriver for the installed version of Chrome (https://chromedriver.chromium.org/downloads)

Place the driver in a folder somewhere where you won't touch it by accident (E.g: C:\Users\...\Downloads\drivers
- Add the driver to you local ENV PATH.