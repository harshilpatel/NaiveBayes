__author__ = "Harshilkumar Patel"
__status__ = "Development"


import logging

logger = logging.getLogger('ml-assignment')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# file_handler = logging.FileHandler("output.log")
# file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
# logger.addHandler(file_handler)
