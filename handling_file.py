import os
import shutil
import function_support as ex_func

	# Move XML file to right directory (xml files) ----------------------------------
def handling_file(file_name,output_directory) :
	print(output_directory)
	#Rename process
	new_name_xml = 'MBMW-' + file_name + '.xml'
	os.rename('MBMW Message Viewer.xml', new_name_xml)
	log_text = 'handling file - XML file has been renamed'
	ex_func.notification(log_text)

	#Move to the directory
	shutil.move(new_name_xml, output_directory)
	log_text = 'handling file - XML file has been moved to "output folder"'
	ex_func.notification(log_text)
	# -------------------------------------------------------------------------------
	
	return new_name_xml		#Return XML file name

def handling_file_V4(file_name,browse_from,output_directory) :

	output_xml = trim_xml_name(browse_from)

	#Rename process
	new_name_xml = 'MBMW-' + file_name + '.xml'
	os.rename(output_xml, new_name_xml)
	log_text = 'handling file - XML file has been renamed'
	ex_func.notification(log_text)

	#Move to the directory
	shutil.move(new_name_xml, output_directory)
	log_text = 'handling file - XML file has been moved to "output folder"'
	ex_func.notification(log_text)
	# -------------------------------------------------------------------------------
	
	return new_name_xml		#Return XML file name

def trim_xml_name(str_input):

	str_len = len(str_input)

	running_num = 0
	found_XML = 0
	for i in str_input :
		running_num += 1
		if i == '\\' :
			found_XML = running_num
			

	return str_input[found_XML:str_len]
