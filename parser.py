'''
project:		OCEANVIEW
filename:		parser.py

description:	Keylog parser to track user interaction, single file

author:			Chris Vantine
'''

# command_list continues to follow original keys when binary names change
command_list = {}
command_list['cd'] ='cd'
command_list['ls'] = 'ls'
command_list['ps'] = 'ps'
command_list['iptables'] = 'iptables'
command_list['grep'] = 'grep'
command_list['alias'] = 'alias'


def track_cd_rec(args, meta):
	'''
	track_cd_rec is a recursive helper function for track_cd

	PARAMETERS
	args:   (list) arguments in a bash command
	meta:   (dict) metadata to modify

	RETURNS
	str:    new working directory
	'''
	work_dir = meta['work_dir']
	print(args)

	if len(args) == 1 or args[1] == '':
		return work_dir
	elif args[1][0] == '/':
		work_dir = args[1]
	elif args[1][0:2] == '..':
		if work_dir == '~':
			work_dir = "/home"
		else:
			work_split = work_dir.split("/")
			work_split = work_split[:-1]
			work_dir = "/"
			for item in work_split:
				if len(work_dir) == 1:
					work_dir = work_dir + item
				else:
					work_dir = work_dir + '/' + item
		meta['work_dir'] = work_dir
		args[1] = args[1][3:]
		work_dir = track_cd_rec(args, meta)
	elif args[1][0] == '.':
		work_split = args
		work_split[1] = work_split[1][2:]
		work_dir = track_cd_rec(work_split, meta)
	else:
		if len(work_dir) == 1:
			work_dir = meta['work_dir'] + args[1]
		else:
			work_dir = meta['work_dir'] + "/" + args[1]

	return work_dir


def track_cd(args, meta):
	'''
	track_cd tracks the current working directory as the user changes dirs

	PARAMETERS
	args:   (list) arguments in a bash command
	meta:   (dict) metadata to modify

	RETURNS
	None
	'''
	work_dir = meta['work_dir']
	print(args)

	if len(args) == 1:
		work_dir = '~'
	elif len(args) > 2:
		if args[2] == '&':
			track_command(args[3:], meta)
		elif args[2] == '&&':
			track_command(args[3:], meta)
		elif args[2] == '|':
			track_command(args[3:], meta)
	elif args[1] == '~':
		work_dir = '~'
	else:
		work_dir = track_cd_rec(args, meta)

	meta['work_dir'] = work_dir

	return None


def track_command(args, meta):
	'''
	track_command tracks user interaction during the logged session

	PARAMETERS
	args:   (list) arguments in a bash command
	meta:   (dict) metadata to modify

	RETURNS
	None
    '''
	if args[0] == command_list['cd']:
		track_cd(args, meta)
		print(meta['work_dir'])
	elif args[0] == command_list['ls']:
		pass
	elif args[0] == command_list['ps']:
		pass
	elif args[0] == command_list['iptables']:
		pass
	elif args[0] == command_list['grep']:
		pass
	elif args[0] == command_list['alias']:
		pass
	else:
		pass

	return None


def parse_file(filename):
	'''
	parse_file parses a keylog file, printing findings

	PARAMETERS
	filename:   (str) the name of the file to parse

	RETURNS
	None
	'''
	log = open(filename)

	meta = {}
	user_info = log.readline().split(",")
	meta['user'] = user_info[0]
	meta['session'] = user_info[1][:-1]

	print("User ", meta['user'], " on ", meta['session'])
	meta['work_dir'] = log.readline().rstrip("\n")
	print("Working in ", meta['work_dir'])

	for line in log:
		line = line.rstrip("\n")
		args = line.split(" ")
		track_command(args, meta)

	return None


def main():
	'''
	main is the main function of the program
	'''
	filename = "testlog"
	parse_file(filename)


if __name__ == "__main__":
	main()