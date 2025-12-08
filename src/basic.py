# Basic unit testing module with logging and environment variable loading


import logging 
from dotenv import load_dotenv
import os
import time 

#logger prefrences
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#logger.debug("")
#logger.info("")
#logger.warning("")
#logger.error(")
#logger.critical("")


# load dotenv variables
load_dotenv()
BCGW_USERNAME = os.getenv('BCGW_USERNAME')
BCGW_PASSWORD = os.getenv('BCGW_PASSWORD')
W_DRIVE = os.getenv('W_DRIVE_TEST_LOC')
O_PATH = os.getenv('O_PATH')

class basic_tests:
    def __init__(self):
        self.bcgw_username = BCGW_USERNAME
        self.bcgw_password = BCGW_PASSWORD
        self.w_drive = W_DRIVE
        self.o_path = O_PATH

        self.w_test_path = os.path.join(self.w_drive, "unit_test_folder")

    time_start = time.perf_counter()
    time_stop = time.perf_counter()



    def create_structure(self):
        start = time.perf_counter()  # fresh timestamp each call
        deliverables_loc = os.path.join(self.w_test_path, "deliverables")
        documents_loc= os.path.join(self.w_test_path, "documents")
        restricted_loc = os.path.join(self.w_test_path, "restricted")
        source_data_loc = os.path.join(self.w_test_path, "source_data")
        tools_loc = os.path.join(self.w_test_path, "tools")
        work_loc = os.path.join(self.w_test_path, "work")
        if os.path.exists(self.w_test_path):
            logger.info("Test folder already exists at %s", self.w_test_path)
        else:
            os.makedirs(self.w_test_path, exist_ok=True)
            logger.info("Created test folder at %s", self.w_test_path) 
        os.makedirs(deliverables_loc, exist_ok=True)
        os.makedirs(documents_loc, exist_ok=True)
        os.makedirs(restricted_loc, exist_ok=True)
        os.makedirs(source_data_loc, exist_ok=True)
        os.makedirs(tools_loc, exist_ok=True)
        os.makedirs(work_loc, exist_ok=True)
        stop = time.perf_counter()
        logger.info("Created folder structure in %.4f seconds", stop - start)   


    def create_txt(self):
        start = time.perf_counter()
        txt_path = os.path.join(self.w_test_path, "documents", "test_file.txt")
        with open(txt_path, 'w') as f:
            f.write('''"Three Rings for the Elven-kings under the sky,
                        Seven for the Dwarf-lords in their halls of stone,
                        Nine for Mortal Men, doomed to die,
                        One for the Dark Lord on his dark throne
                        In the Land of Mordor where the Shadows lie.
                        One Ring to rule them all, One Ring to find them,
                        One Ring to bring them all and in the darkness bind them.
                        In the Land of Mordor where the Shadows lie."''')
        stop = time.perf_counter()
        logger.info("Created test text file in %.4f seconds", stop - start)
    
    
    
