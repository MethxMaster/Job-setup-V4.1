import function_support as ex_func

def analyzing_data(xml_data_input) :

	xml_data = xml_data_input
	log_text = 'Analyzing - The data are being analyzed'
	ex_func.notification(log_text)

	maximum_default = 0
	running_number = 1
	first_battery = {}
	sub_dictionary_first_battery = {}

	station_list = ['L1_1710','L1_1720','L1_2600','L1_2700','L1_2800','L1_3000',
					'L1_2200','L1_3100','L1_3200','L1_3400','L1_3500','L1_3600',
					'L1_3710','L1_3720','L1_3900','L1_4000','L1_4100']
	sub_dictionary_first_battery = {'sequence': maximum_default,'battery':'-','error-message':'','date-time':'-'}
	
	for index in station_list :
		first_battery[index] = sub_dictionary_first_battery
		running_number += 1

	for trans in xml_data :
		for list_st in station_list :
			if xml_data[trans]['station'] == list_st :
				if int(xml_data[trans]['number']) > int(first_battery[list_st]['sequence']) :

					found_acceptable_error = False

					if (xml_data[trans]['station'] == 'L1_2700') and (xml_data[trans]['error'] != '') :
						found_acceptable_error = True

					if found_acceptable_error == False  : #st2700 and error-code do exist
						draft = {}
						draft['sequence'] = xml_data[trans]['number']
						draft['battery'] = xml_data[trans]['id']
						draft['error-message'] = xml_data[trans]['error']

						str_date = str(xml_data[trans]['date-time'])
						str_time = str(xml_data[trans]['date-time'])
						str_modify = str_date[:10] + ' ' + str_time[11:19]
						draft['date-time'] = str_modify


						first_battery[list_st] = draft

	log_text = 'Analyzing - The data have been analyzed'
	ex_func.notification(log_text)
	return first_battery


#if __name__ == '__main__':
	#y = analyzing_data('x')
	#print(y)
