# coding=UTF-8
import  json
from pprint import pprint


def estados_json():
	print request.vars
	with open('/home/fernado/web2py/tronco/applications/ubercred/views/estados.json') as json_data:
		json_data = json.load(json_data)
		#print json_data[0]
		#for dado in json_data:
		#	print dado

	return response.json(json_data)
	#return response.render("estados.json")

def cidades_json():
	print request.vars
	with open('/home/fernado/web2py/tronco/applications/ubercred/views/cidades.json') as json_data:
		json_data = json.load(json_data)
		print(json_data)

	return response.json(json_data)	
	#return response.render("cidades.json")
