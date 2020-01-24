# importing the libraries
import sys
import getopt

# taking all the arguments except filename
argv = sys.argv[1:]

# correct username and password
correct_uname = 'Varun'
correct_password = '123456'

# write a try catch block
try:

	# colon means a value is expected
	opts, args = getopt.getopt(argv, "u:p:", ["uname=", "password="])

	print(opts, args)

	if len(opts) != 2:
		print('usage: cmd_getopt_tutorial -u <uname> -p <password> or')
		print('usage: cmd_getopt_tutorial --uname <uname> --password <password>')

	# we need the values for uname and password which we typed on the command line
	for opt, arg in opts:
		if opt == '-u' or opt == '--uname':
			uname = arg
		elif opt == '-p' or opt == '--password':
			password = arg

	# username and password verification
	if uname == correct_uname and password == correct_password:
		print('Username and password are correct!')
	else:
		print('Username and password are incorrect!')

except getopt.GetoptError:	# if any option is not recognized
	print('One or more option(s) are not recognized or not in correct format')
	print('usage: cmd_getopt_tutorial -u <uname> -p <password> or')
	print('usage: cmd_getopt_tutorial --uname <uname> --password <password>')



	
