from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import status
from fastapi.responses import JSONResponse
import aiofiles

from helpers.config import get_settings , Settings
from controllers.DataController import Data_Controller
from controllers.ProjectController import Project_Controller
from models.ResponseEnum import ResponseSignals
import logging 

logger = logging.getLogger("uvicorn.error")


data_router = APIRouter(
    prefix = "/api/v1",
    tags = ["api_v1_data"]
)

@data_router.post("/Upload/{project_id}/data")
async def uploadfile(project_id:str , file:UploadFile,
               app_settings : Settings=Depends(get_settings)):

        #validate uploaded file 
        data_controller = Data_Controller()
        is_valid,Response_signal = data_controller.validate_uploaded_file(file=file)

        if not is_valid :
            return JSONResponse(
                status_code =status.HTTP_400_BAD_REQUEST, 
                content = {
                    "signal" : Response_signal
                }
            )

        
        project_dir_path = Project_Controller().get_project_path(project_id=project_id)

        file_path , file_id = data_controller.generate_unique_file_path(
            orig_file_name=file.filename,
            project_id=project_id
        )


        try:
            async with aiofiles.open(file_path,"wb") as f : 
                while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                    await f.write(chunk)

        except Exception as e :

            logger.error(f"Error While Uploading file : {e}")

            return JSONResponse(
                        status_code =status.HTTP_400_BAD_REQUEST, 
                        content = {
                            "signal" : ResponseSignals.FILE_UPLOADED_FAILED.value
                        }
                    )


        return JSONResponse(
            content={
                "signal" : ResponseSignals.FILE_UPLOADED_SUCCESS.value,
                "file_id" :file_id
            }
        )
            

            


                    
        
        
        

        

    


    

    