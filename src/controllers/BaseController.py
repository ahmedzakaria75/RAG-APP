from helpers.config import get_settings
import os 
import random 
import string 

class Base_Controller:

    def __init__(self):
        self.app_settings = get_settings()

        self.Base_dir = os.path.dirname(os.path.dirname(__file__))   # src
        self.files_dir = os.path.join(
            self.Base_dir,
            "assets/files"
        )


    def generate_random_string(self, length: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))




    
        