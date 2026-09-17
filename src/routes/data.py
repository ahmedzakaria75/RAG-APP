from fastapi import APIRouter
from fastapi import UploadFile


data_router = APIRouter(
    prefix = "/api/v1",
    tags = ["api_v1"]
)

@data_router.get("Upload/{project_id}/")
def uploadfile(project_id:str , file:uploadfile):

    #validate uploaded file 
    pass

    
