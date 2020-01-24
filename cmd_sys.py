import sys

# username and password verification

uname = "Varun"
password = "123456"

# sys.argv stores the arguments list
print('Arguments\' Length: {}'.format(len(sys.argv)))
print('Arguments: {}'.format(sys.argv))

# check for 3 arguments given or not
if(len(sys.argv) != 3):
	print('usage: python cmd_sys.py <uname> <password>')
	sys.exit()

# check uname and password
if(uname == sys.argv[1] and password == sys.argv[2]):
	print('Username and Password are valid!')
else:
	print('Username and Password are invalid!')

