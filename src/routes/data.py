from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from helpers.config import get_settings , Settings
from controllers.DataController import Data_Controller


data_router = APIRouter(
    prefix = "/api/v1",
    tags = ["api_v1"]
)

@data_router.post("Upload/{project_id}/")
def uploadfile(project_id:str , file:UploadFile,
               app_settings : Settings=Depends(get_settings)):

    #validate uploaded file 
    data_controller = Data_Controller()
    is_valid,Response_signal = data_controller.validate_uploaded_file(file=file)

    return {
        "did file uploaded" : is_valid,
        "signal":Response_signal
    }


    

    