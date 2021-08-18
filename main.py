from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import asyncio
import time

YOU = "//span[@aria-label = 'You:']"
WHATSAPP_WEB_LINK = 'https://web.whatsapp.com/'

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
		self.driver.get(WHATSAPP_WEB_LINK)

		time.sleep(3) # to scan QR Code during this time
		self.message_bar = self.driver.find_element_by_xpath("//div[@class = '_2A8P4']")
		self.search_bar = self.driver.find_element_by_xpath("//div[@class = '_2_1wd copyable-text selectable-text']")
		self.exit_sb_button = self.driver.find_element_by_xpath("//div[@class='_1rPZq _2w7RB']")
		# exit left pane search bar (sb = search bar)
		self.last_msg_id = self.get_last_text_msg_id()

	def is_connected(self):
		if self.driver.title == 'WhatsApp':
			return True
		return False

	def quit_driver(self):
		self.driver.quit()
	
	
	def send_message(self, message: str):
		'''
			send a text message
		'''
		self.message_bar.send_keys(message + Keys.RETURN)
		# time.sleep(1.8)
		# if self.message_sent():
		# 	return True
		# return False
	
	def send_file(self, file: str):
		attach_icon = self.driver.find_element_by_xpath("//span[@data-icon = 'clip']")
		attach_icon.click()
		media_file = self.driver.find_element_by_xpath("//span[@data-icon = 'attach-image']")
		media_file.click()
		# to add a file pyGUI will be used
		# to add the path to file

		media_send_button = self.driver.find_element_by_xpath("//span[@data-icon = 'send']")
		media_send_button.click()
		# self.last_msg_time = time.localtime().tm_min

	def message_sent(self):
		'''
			if text message is sent or not 
		'''
		if self.driver.find_elements_by_xpath(YOU+"//..//span[@aria-label = ' Sent ']"):
			return True
		return False
	
	def message_delivery(self):
		if driver.find_elements_by_xpath(YOU+"//..//span[aria-label = ' Delivered ']"):
			return True
		return False

	def message_read(self):
		'''
			if text message is seen by participent (or everyone: in group)
		'''
		if driver.find_elements_by_xpath(YOU+"//..//span[aria-label = ' Read ']"):
			return True
		return False

	def get_last_text_msg_id(self):
		'''
			returns the last message data-id
		'''
		id = driver.find_elements_by_xpath("div[@tabindex='-1']")[-3].get_attribute('data-id')
		return id
