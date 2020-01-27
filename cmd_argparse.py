#importing the libraries
import argparse
import getpass

# correct username and password
correct_uname = 'Varun'
correct_password = '123456'

# instantiate the parser
parser = argparse.ArgumentParser(description = 'Username and password verification')

#adding the arguments
parser.add_argument('-u', '--uname', dest = 'uname', help = 'specify the username')
parser.add_argument('-p', '--password', dest = 'password', nargs='?', help = 'specify the password')

# parse the arguments
args = parser.parse_args()

if args.password == None:
	args.password = getpass.getpass()

# print the arguments
#print(args.uname, args.password)

# username and password verification
if correct_uname == args.uname and correct_password == args.password:
	print('Username and password are correct!')
else:
	print('Username and password are incorrect!')










