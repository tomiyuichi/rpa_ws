from RPA.Browser.Selenium import Selenium

browser = Selenium()
browser.open_available_browser("https://google.com")
print(browser.get_title())
browser.close_browser()
