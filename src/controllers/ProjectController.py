from .BaseController import Base_Controller
from fastapi import UploadFile
import re
import random
import string
import os 


class Project_Controller(Base_Controller):

    def __init__(self):
        super().__init__()


    def get_project_path(self,project_id:str):

        project_dir = os.path.join(
            self.files_dir,
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir