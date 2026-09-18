from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from helpers.config import get_settings , Settings


data_router = APIRouter(
    prefix = "/api/v1",
    tags = ["api_v1"]
)

@data_router.post("Upload/{project_id}/")
def uploadfile(project_id:str , file:UploadFile,
               app_settings : Settings=Depends(get_settings)):

    #validate uploaded file 
    pass

    