class SecureDataVault:
  def __init__(self,fileLocation):
    self.fileLocation=fileLocation

  def encodeData(self,key,outputFile):
    with open(self.fileLocation, 'rb') as f:
      byte_data = f.read()
      encodeData = bytearray(b ^ key for b in byte_data)
      with open(outputFile,'wb') as bFile:
        bFile.write(encodeData)
  
  def decodeData(self,key,encodedFile):
    with open(encodedFile,"rb") as bFile:
      encodeData=bFile.read()
      decodeData = bytearray(b ^ key for b in encodeData)
      print(decodeData)


secure=SecureDataVault("./concept_file_handling/log/api_keys.txt")
secure.encodeData(121,"./concept_file_handling/log/vault.bin")
secure.decodeData(121,"./concept_file_handling/log/vault.bin")