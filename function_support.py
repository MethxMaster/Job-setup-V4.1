# All imporrt files ---------------------------------------------------------------
import time
import datetime
import logging

# ---------------------------------------------------------------------------------

# Delay  --------------------------------------------------------------------------
def delay(time_second) :
	time.sleep(time_second)
# ---------------------------------------------------------------------------------

# Notification --------------------------------------------------------------------
def notification(str_input = '-') :
	current_time = datetime.datetime.now()
	print(current_time.strftime('%Y-%m-%d %H:%M:%S | ') + str_input)
	logging.info(str_input)
	
# ---------------------------------------------------------------------------------

# Stop running system -------------------------------------------------------------
def stop_running() :
	log_text = 'Running script finished'
	notification(log_text)
	raise SystemExit	#Stop running
# ---------------------------------------------------------------------------------

def update_progress(appress_ui,percent_probressbar):
	appress_ui.progressBar_RunningInfo_progressBar.setProperty("value",percent_probressbar)

def notify_gui(appress_ui,text_input):
	str_monitor = text_input
	print(appress_ui)
    #appress_ui.Monitor_RunningInfo_plainTextEdit.insertPlainText(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S | ' + str_monitor + '\n'))

def default_directory(input_str):

	looptime  = 2
	count_loop = 0

	while count_loop < looptime :

		str_len = len(input_str)

		running_num = 0
		found_XML = 0
		for i in input_str :
			running_num += 1
			if i == '\\' :
				found_XML = running_num

		input_str = input_str[:found_XML-1]
		count_loop += 1

	return input_str