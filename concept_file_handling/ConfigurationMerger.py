import json
import logging
class ConfigurationMerger:
  def __init__(self,defaultConfigFile,userConfileFile):
    self.defaultConfigFile=defaultConfigFile
    self.userConfileFile=userConfileFile
  
  def readFromJsonFile(self,jsonFile):
    try:
        with open(jsonFile, "r") as dfile:
        # Use json.load() to convert the file content to a Python dictionary
          data = json.load(dfile)
          return data
    except FileNotFoundError:
      print(f"Error: The file {jsonFile} was not found. Please check the file path.")
    except json.JSONDecodeError as e:
      print(f"Error: Failed to decode JSON from the file: {e}")
  
  def writeIntoJsonFile(self,jsonFile,data):
    try:
        with open(jsonFile, 'w', encoding='utf-8') as jfile:
          json.dump(data, jfile, indent=4, ensure_ascii=False)
    except FileNotFoundError:
      print(f"Error: The file {jsonFile} was not found. Please check the file path.")
    except json.JSONDecodeError as e:
      print(f"Error: Failed to decode JSON from the file: {e}")
  
  def logger(self,msg):
    logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w' # 'a' for append (default), 'w' for overwrite
    )
    logging.warning(msg)
     
  def mergeFiles(self,outputConfigFile):
    newData={}
    defaultData = self.readFromJsonFile(self.defaultConfigFile);
    userData = self.readFromJsonFile(self.userConfileFile);
    for key in userData.keys():
      if key in defaultData.keys():
          newData[key]=userData[key]
      else:
        self.logger(f"Key{key} does not present in the {self.defaultConfigFile}")
    self.writeIntoJsonFile(outputConfigFile,newData)
    

config=ConfigurationMerger("./concept_file_handling/log/default.json","./concept_file_handling/log/user.json")
config.mergeFiles("./concept_file_handling/log/final_config.json")


    