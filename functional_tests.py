from selenium import webdriver


browser = webdriver.Firefox(executable_path=r'C:\Program Files\Python36\Scripts\geckodriver-v0.19.1-win64\geckodriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title