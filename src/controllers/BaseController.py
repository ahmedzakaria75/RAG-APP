from helpers.config import get_settings

class Base_Controller:

    def __init__(self):
        self.app_settings = get_settings()

    
        