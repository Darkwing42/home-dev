import os

app_list = ['app', 'app/resources', 'app/models']
test_list = ['test']
config_list = ['config']

config_files = ['config/__init__.py', 'config/config.py']
test_files = ['test/__init__.py']
main_files = ['run.py', '.gitignore', 'requirements.txt', 'README.md', 'manage.py']
app_files = ['app/__init__.py', 'app/resources/__init__.py', 'app/models/__init__.py']

def makedirs(list_of_dirs):
	for each in list_of_dirs:
		os.mkdir(each)
def create_files(list_of_files):
	for each in list_of_files:
		f = open(each, "w")
		f.close()

def main():
	makedirs(app_list)
	makedirs(config_list)
	makedirs(test_list)

	create_files(config_files)
	create_files(main_files)
	create_files(test_files)
	create_files(app_files)






if __name__ == '__main__':
	main()
