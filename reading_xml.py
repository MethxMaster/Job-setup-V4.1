# All imporrt files --------------------------------------------
import xml.etree.ElementTree as et
import os
import shutil
import function_support as ex_func
import datetime
# --------------------------------------------------------------
def reading_xml(appress_ui,file_name,output_directory) :
	# Starting XML file -------------
	print(file_name)
	print(output_directory)
	xml_file_dir = output_directory + '/MBMW-' + file_name + '.xml'
	tree = et.parse(xml_file_dir)
	root = tree.getroot()

	log_text = 'Reading - XML has been opened and get the data'
	ex_func.update_progress(appress_ui,40)
	ex_func.notification(log_text)
	# -------------------------------

	# Set local variable ------------
	xml_content = {}
	xml_batt = {}
	xml_running_num = 1
	# -------------------------------

	for elm in root.findall(".//"):	#Get XML data from each line

		#Reset dictionary of battery
		xml_batt = {}

		#Get data from XML to variable (prepare data for adding to dictionary)
		batt_sequence = str(elm.attrib.get('PKMBMW_MSG'))
		batt_station = str(elm.attrib.get('Station'))
		batt_id = str(elm.attrib.get('Barcode1'))
		batt_data_error = str(elm.attrib.get('CustomData2'))
		batt_creatdate = str(elm.attrib.get('Createdate'))

		if batt_sequence != 'None' :	#Check empty data

			# Add dictionary for battery ----------
			xml_batt['number'] = batt_sequence
			xml_batt['station'] = batt_station
			xml_batt['id'] = batt_id
			xml_batt['error'] = batt_data_error
			xml_batt['date-time'] = batt_creatdate
			# -------------------------------------

			# Add dictionary for whole list -------
			xml_content['transaction_' + str(xml_running_num)] = xml_batt
			# -------------------------------------

			xml_running_num += 1 	#Update running number

	log_text = 'Reading - All data have been recieved to dictionary parameter type'
	ex_func.notification(log_text)

	return xml_content #Return dictionnary data

#if __name__ == '__main__':
#	x = datetime.datetime.now()
#	reading_xml('MBMW-20210827-152102.xml',x)

#######################################################################################################
#                                                                                                     #
#                                             END SCRIPT                                              #
#                                                                                                     #
#######################################################################################################