import logging

logging.basicConfig(filename=r'C:\Users\One\Desktop\nopcom3\logs\log_file.log',
                    format=f"%(asctime)s %(message)s",
                    filemode='a')

# create logger object
logger = logging.getLogger()

# set levels
logger.setLevel(logging.DEBUG)
