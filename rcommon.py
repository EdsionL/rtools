from rconfig import *
import commands

def getVersion():
	return "1.1";

def getConfig(cfgname):
	cfg = globals()[cfgname]

	# Scan the ip of configuration
	if cfg:
		if cfg['host'].startswith('-cmd-'):
			cmd = cfg['host'][5:]
			cfg['host'] = commands.getoutput(cmd)

		elif cfg['host'].startswith('-func-'):
			func_name = cfg['host'][6:]
			func = globals()[func_name]
			cfg['host'] = func()

	print('IP[%s]: %s' % (cfgname,cfg['host']))

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
