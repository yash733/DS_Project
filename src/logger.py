import logging
import os
from datetime import datetime

Log_File = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",Log_File)
os.makedirs(logs_path,exist_ok=True) #meaning if even there already exists a file inside the dir keep on appending it

Log_File_Path = os.path.join(logs_path,Log_File)

logging.basicConfig(
    filename=Log_File_Path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO
)