# -*- coding: utf8 -*- 

import os
import sys

SERVICE_PATH = 'DropShot.workflow'
SCRIPT_PATH = 'dropshot.py'
CONFIG_PATH = '.config'
SERVICES_ROOT = os.path.join(os.environ['HOME'], "Library/Services/")
SCRIPTS_DIR_PATH = os.path.join(os.environ['HOME'], "Scripts/")


if __name__ == "__main__":
	assert os.path.isdir(SERVICE_PATH), "DropShot service not found."
	assert os.path.isfile(SCRIPT_PATH), "dropshot.py script not foud"

	if not os.path.isdir(SCRIPTS_DIR_PATH):
		print "\tCreating Scripts folder..."
		os.makedirs(SCRIPTS_DIR_PATH)

	if not os.path.isfile(CONFIG_PATH):
		user_id = raw_input("Enter your DropBox user id number: ")
		
		while len(user_id) == 0:
			print "DropBox user id number can't be blank."
			user_id = raw_input("Enter your DropBox user id number: ")

		dropbox_public_path = raw_input("Enter your DropBox Public folder path [~/DropBox/Public/]: ")

		if len(dropbox_public_path) == 0:
			dropbox_public_path = os.path.join(os.environ['HOME'], "DropBox/Public/")

		config_file = open('.config', 'w')
		config_file.write("{} {}".format(user_id, dropbox_public_path))


	print "\tCopying DropShot service..."
	os.system('cp -r "{}" {}'.format(SERVICE_PATH, SERVICES_ROOT))

	print "\tCopying DropShot script..."
	os.system('cp {} {}'.format(SCRIPT_PATH, SCRIPTS_DIR_PATH))
	os.system('cp {} {}'.format(CONFIG_PATH, SCRIPTS_DIR_PATH))
