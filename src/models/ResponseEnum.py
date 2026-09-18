from enum import Enum

class ResponseSignals(Enum):

    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDED ="file size exceeded"
    FILE_UPLOADED_SUCCESS = "file uploaded success"
