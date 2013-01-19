# -*- coding: utf8 -*- 

import os
import datetime
import urllib

def warn_no_config_file():
	os.system('rm .config')
	raise Exception("Directory {} not found. Please run 'python install.py' again.".format(dropbox_path))

CONFIG_FILE = os.path.join(os.environ['HOME'], 'Scripts/', '.config')

if __name__ == '__main__':

	assert os.path.isfile(CONFIG_FILE), "No configuration file found. Run 'python install.py' first."

	try:
		user_id, dropbox_path = open(CONFIG_FILE).read().split()
	except Exception, e:
		warn_no_config_file()

	if not os.path.isdir(dropbox_path):
		warn_no_config_file()

	filename = "Screenshot {}.png".format(str(datetime.datetime.now()))
	file_url = "https://dl.dropbox.com/u/{}/{}".format(user_id, urllib.quote(filename))

	os.system('/usr/sbin/screencapture -tpng -i "{}"'.format(os.path.join(dropbox_path, filename)))
	os.system('echo "{}" | pbcopy'.format(file_url))
