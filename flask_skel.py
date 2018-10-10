import os

app_list = ['app', 'app/resources', 'app/models']
test_list = ['test']
config_list = ['config']

config_files = ['config/__init__.py', 'config/config.py']
test_files = ['test/__init__.py']
main_files = ['run.py', '.gitignore', 'requirements.txt', 'README.md', 'manage.py']
app_files = ['app/__init__.py', 'app/resources/__init__.py', 'app/models/__init__.py']

def create_dir(*lists):
	for list in lists:
		print("Using: " + list)
		for each in list:
			print("Creating dir: " + each)
			os.mkdir(each)
def create_files(*lists):
	for list in lists:
		print("Using: " + list)
		for each in list:
			print("Creating file: " + each)
			f = open(each, "w")
			f.close()

def main():
	print("Creating directories")
	print("########################################################")
	print("")
	
	create_dir(app_list, test_list, config_list)
	
	print("")
	print("Creating files")
	print("########################################################")
	print("")
	create_files(main_files, app_files, test_files, config_files)
	






if __name__ == '__main__':
	main()
