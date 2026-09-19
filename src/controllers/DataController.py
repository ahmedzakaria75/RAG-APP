from .BaseController import Base_Controller
from .ProjectController import Project_Controller
from fastapi import UploadFile
from models import ResponseSignals 
import os 
import re 



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


    def generate_unique_file_path(self,orig_file_name :str , project_id:str):

        random_key = self.generate_random_string()    # make random key 
        project_path = Project_Controller().get_project_path(project_id=project_id) # src-> assets-> files-> project_id 

        cleaned_file_name = self.get_clean_file_name(
            orig_file_name=orig_file_name
            )

        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()    # make random key 
            new_file_path = os.path.join(
                        project_path,
                        random_key + "_" + cleaned_file_name
                    )


        return new_file_path, random_key+ "_" + cleaned_file_name



    def get_clean_file_name(self, orig_file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name



