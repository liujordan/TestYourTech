from selenium import webdriver

class ActionBase(object):

	def __init__(self, *args, **kwargs):
		webdriver_dir = kwargs['webdriver_dir']
		