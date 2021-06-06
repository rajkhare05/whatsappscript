from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class whatsApp:
	def __init__(self, headless = False):
		options = Options()
		# headless flag can be used
		# if the QR Code is already scanned somehow
		if headless:
			options.add_argument('--headless')
		
		# Chromium driver is default
		# firefox and other drivers can be used in future
		self.driver = webdriver.Chrome(options = options)

		# assuming the QR Code is already scanned
		# and "keep me signed in" is enabled (possibility)
		self.driver.get('https://web.whatsapp.com/')

		time.sleep(3) # to scan QR Code during this time
		self.message_bar = self.driver.find_element_by_xpath("//div[@class = '_2A8P4']")
		self.last_msg_time = None

	def is_connected():
		if self.driver.title == 'WhatsApp':
			return True
		return False

	def quit_driver():
		self.driver.quit()
	
	def send_message(message: str):
		'''
			send a text message
		'''
		self.message_bar.send_keys(message + Keys.RETURN)
	
	def send_file(file: str):
		attach_icon = self.driver.find_element_by_xpath("//span[@data-icon = 'clip']")
		attach_icon.click()
		media_file = self.driver.find_element_by_xpath("//span[@data-icon = 'attach-image']")
		media_file.click()
		# to add a file pyGUI will be used
		# to add the path to file

		media_send_button = self.driver.find_element_by_xpath("//span[@data-icon = 'send']")
		media_send_button.click()
		# self.last_msg_time = time.localtime().tm_min

	def message_sent():
		'''
			check if text message is delivered or not 
		'''
		if self.driver.find_elements_by_xpath("//span[@dir='ltr']//span"):
			pass