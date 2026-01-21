import time
class LogFilePruner:
  def __init__(self,logfileLocation):
    self.logfileLocation=logfileLocation
  
  def getErrorLog(self, keyword,outputFileLocation):
    log=""
    f2=open(outputFileLocation,"w")
    f=open(self.logfileLocation,"r")
    content=f.readlines();
    for line in content:
      if keyword in line:
        log=line+str(time.time())
        f2.write(log)
    f.close()
    f2.close()


logFile=LogFilePruner("./concept_file_handling/log/serverLog.txt")
logFile.getErrorLog("ERROR","./concept_file_handling/log/error_report.txt")      