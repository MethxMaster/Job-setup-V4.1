from openpyxl import Workbook
import function_support as ex_func


# Excel
def create_excel(first_battery,file_name,output_directory) :
	
	first_batt = first_battery


	station_list = ['L1_1710','L1_1720','L1_2600','L1_2700','L1_2800','L1_3000',
					'L1_2200','L1_3100','L1_3200','L1_3400','L1_3500','L1_3600',
					'L1_3710','L1_3720','L1_3900','L1_4000','L1_4100']


	workbook = Workbook()
	sheet = workbook.active

	log_text = 'Excel - excel file has been created'
	ex_func.notification(log_text)

	sheet.append(['Station','Transaction row','Battery ID','date-time','Verified'])
	log_text = 'Excel - the headed was created'
	ex_func.notification(log_text)

	for st in station_list:
		
		if first_batt[st]['error-message'] == '' :
			if first_batt[st]['battery'] == '-' :
				str_append = [st,first_batt[st]['sequence'],first_batt[st]['battery'],first_batt[st]['date-time'],'-']
			else :
				str_append = [st,first_batt[st]['sequence'],first_batt[st]['battery'],first_batt[st]['date-time'],'pass']
		else :
			str_append = [st,first_batt[st]['sequence'],first_batt[st]['battery'],first_batt[st]['date-time'],'Need to be verified : ' + first_batt[st]['error-message']]

		sheet.append(str_append)


	excel_name = 'output-' + file_name + '.xlsx'
	print(output_directory + '/' + excel_name + '.xlsx')####
	workbook.save(filename = output_directory + '/' + excel_name + '.xlsx')
	log_text = 'Excel - excel file has been saved'
	ex_func.notification(log_text)


	


#if __name__ == '__main__':
#	main()