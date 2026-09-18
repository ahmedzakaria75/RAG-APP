from .BaseController import Base_Controller
from fastapi import UploadFile
from models import ResponseSignals 



class Data_Controller(Base_Controller):


    def __init__(self):
        super().__init__()
        self.MB_TO_BYTE=1024 * 1024


    def validate_uploaded_file(self,file:UploadFile): 

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignals.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_SIZE * self.MB_TO_BYTE:
            return False , ResponseSignals.FILE_SIZE_EXCEEDED.value


        return True , ResponseSignals.FILE_UPLOADED_SUCCESS.value

