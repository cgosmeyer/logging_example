import logging.config
from os import path

# See https://stackoverflow.com/questions/23161745/python-logging-file-config-keyerror-formatters
abs_path = path.dirname(path.abspath(__file__)).split('/')[:-1]
abs_path = '/'.join(abs_path)
log_file_path = path.join(abs_path, 'logging.ini')

# See https://stackoverflow.com/questions/13649664/how-to-use-logging-with-pythons-fileconfig-and-configure-the-logfile-filename
logging.config.fileConfig(log_file_path, defaults={'repopath': abs_path}, disable_existing_loggers=False)