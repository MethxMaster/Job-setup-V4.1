# All imporrt files ---------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import shutil
import function_support as ex_func
import datetime
import time
# ---------------------------------------------------------------------------------




def loading_xml_fx(appress_ui,current_time) :

	print(current_time)
	# Delay ---------------------------------------------------------------------------
	refresh_time = 2
	reload_time = 5
	loading_time = 10
	idle_time = 20
	# ---------------------------------------------------------------------------------

	# Directory -----------------------------------------------------------------------
	save_xml_dir = os.getcwd()			#save XML
	execute_chrome_path = os.getcwd() + '/driver/Chrome driver/chromedriver.exe'	#Chorme driver
	# ---------------------------------------------------------------------------------

	# Set http ------------------------------------------------------------------------
	username_com = 'jirameth.k'		#Username
	password_com = 'Tesm0014'		#Password
	jobsetup_address = 'http://' + username_com + ':' + password_com + '@192.168.21.212/Reports/Pages/Report.aspx?ItemPath=%2fReports%2fMBMW+Message+Viewer'
	ip_address = jobsetup_address	#ip address to get WM
	# ---------------------------------------------------------------------------------

	# Set Chrome options --------------------------------------------------------------
	chrome_option_set = Options()
	chrome_option_set.add_experimental_option('prefs',{
				'download.default_directory': save_xml_dir,
				'safebrowsing.enabled': True
													})
	# ---------------------------------------------------------------------------------

	# Get Chrome ----------------------------------------------------------------------
	driver = webdriver.Chrome(executable_path = execute_chrome_path , chrome_options = chrome_option_set)
	driver.get(ip_address)
	log_text = 'Loading - Chrome browser has been opened'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,3)

	driver.maximize_window()
	log_text = 'Loading - Maximized process'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,3)

	ex_func.delay(loading_time)
	# ---------------------------------------------------------------------------------

	#date_from = driver.find_element_by_name('ctl32$ctl04$ctl03$txtValue')		
	#date_to = driver.find_element_by_name('ctl32$ctl04$ctl05$txtValue')
	#date_to = driver.find_element_by_xpath("//div[@id='ctl32_ctl04_ctl05']//input[@name='ctl32$ctl04$ctl05$txtValue']")
	#display_rows = driver.find_element_by_name('ctl32$ctl04$ctl19$ddValue')
	#view_report = driver.find_element_by_id('ctl32_ctl04_ctl00')


	date_str = current_time.strftime('%x')

	#Clear date-from
	driver.find_element_by_name('ctl32$ctl04$ctl03$txtValue').clear()
	log_text = 'Loading - Clear "dateform"'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,13)
	ex_func.delay(reload_time)


	#Date-from (calendar)
	str_input = date_str + ' 12:00:01 AM'
	driver.find_element_by_name('ctl32$ctl04$ctl03$txtValue').send_keys(str_input)
	log_text = 'Loading - date-from information has been filled'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,19)
	ex_func.delay(reload_time)


	#Clear date-to
	driver.find_element_by_name('ctl32$ctl04$ctl05$txtValue').clear()
	ex_func.delay(reload_time)

	#driver.find_element_by_xpath("//div[@id='ctl32_ctl04_ctl05']//input[@name='ctl32$ctl04$ctl05$txtValue']").clear()
	driver.find_element_by_name('ctl32$ctl04$ctl05$txtValue').clear()
	log_text = 'Loading - Clear "dateto"'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,29)
	ex_func.delay(reload_time)


	str_input = date_str + ' 11:59:59 PM'
	#driver.find_element_by_xpath("//div[@id='ctl32_ctl04_ctl05']//input[@name='ctl32$ctl04$ctl05$txtValue']").send_keys(str_input)
	driver.find_element_by_name('ctl32$ctl04$ctl05$txtValue').send_keys(str_input)
	log_text = 'Loading - date-from information has been filled'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,34)
	ex_func.delay(reload_time)

	#Display rows (dropdown)

	driver.find_element_by_name('ctl32$ctl04$ctl19$ddValue').click()
	ex_func.delay(reload_time)
	str_input = 'ALL'
	driver.find_element_by_name('ctl32$ctl04$ctl19$ddValue').send_keys(str_input)
	log_text = 'Loading - display-rows has been selected to all'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,39)
	ex_func.delay(reload_time)

	#Message filter
	driver.find_element_by_name('ctl32$ctl04$ctl09$ddDropDownButton').click() #Dropdown
	ex_func.delay(reload_time)
	driver.find_element_by_name('ctl32$ctl04$ctl09$divDropDown$ctl02').click() #Deselect "ALL MESSAGE TYPES"
	ex_func.delay(reload_time)
	driver.find_element_by_name('ctl32$ctl04$ctl09$divDropDown$ctl04').click() #Select "DCM"
	log_text = 'Loading - message filter has been selected DCM'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,54)
	ex_func.delay(reload_time)


	#View reports (button)
	driver.find_element_by_id('ctl32_ctl04_ctl00').click()
	log_text = 'Loading - view-report button has been clicked'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,59)
	ex_func.delay(reload_time)

	#Save (dropdown)
	driver.find_element_by_id('ctl32_ctl05_ctl04_ctl00_ButtonLink').click()
	log_text = 'Loading - save-dropdown button has been clicked'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,64)
	ex_func.delay(reload_time)

	#Save XML
	driver.find_element_by_xpath("//div[@id='ctl32_ctl05_ctl04_ctl00_Menu']//a[@title='XML file with report data']").click()
	log_text = 'Loading - Downloaded XML'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,69)
	ex_func.delay(reload_time)

	#Close browser
	ex_func.delay(idle_time)
	driver.close()
	log_text = 'Loading - Close Chrome browser'
	ex_func.notification(log_text)
	ex_func.update_progress(appress_ui,98)


#if __name__ == '__main__':
	#loading_xml(datetime.datetime.now())
#######################################################################################################
#                                                                                                     #
#                                             END SCRIPT                                              #
#                                                                                                     #
#######################################################################################################