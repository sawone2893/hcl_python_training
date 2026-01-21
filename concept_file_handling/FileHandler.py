import os
class FileHandler:
  def __init__(self,filePath):
    self.filePath=filePath
  
  def readFile(self):
    try:
      fp=open(self.filePath,"r")
      text=fp.read()
    except FileNotFoundError as e:
      print(e)
    else:
      print("File successfully read!")
    finally:
      fp.close()
    return text
  
  def writeFile(self,text):
    try:
      fp=open(self.filePath,"w")
      fp.write(text);
    except FileNotFoundError as e:
       print(e)
    else:
      print("Write operation successfully completed!")
    finally:
      fp.close
  
  def renameFile(self,oldPath,newPath):
    os.rename(oldPath,newPath)

f=FileHandler("./concept_file_handling/test1.txt")
f.writeFile("I love India")
#f.renameFile("./concept_file_handling/test1.txt","./concept_file_handling/test2.txt")
f.writeFile("Welcome Shabbir")
print(f.readFile())