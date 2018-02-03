from django.views import View
from django.http import HttpResponse
from selenium import webdriver
class runView(View):
	def get(self, request):
		browser = webdriver.Chrome('C:\\Users\\Jordan Liu\\Desktop\\TestYourTech\\webdrivers\\win\\chromedriver.exe')
		browser.get('https://www.google.ca')
		elem = browser.find_element_by_name('q')
		elem.send_keys('how to google')
		elem.submit()
		browser.quit()
		return HttpResponse('Ran test without errors')

