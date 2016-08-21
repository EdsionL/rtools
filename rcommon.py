from rconfig import *

def getConfig(cfgname):
	cfg = globals()[cfgname]
	#TODO find host
	return cfg

def getStringField(cfg, key, default):
	value = None
	try:
		value = cfg[key]
	except Exception, e:
		pass
	
	if  value == None or value == '':
		value = default
	return value
