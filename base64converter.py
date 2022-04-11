import base64

class Base64Converter:
  def __init__(self, path) -> None:
      # read image in binary format
      fileReader = open(path, 'rb')
      self.image = fileReader.read()
  
  def encode(self) -> str:
    if self.image:
     encoded_string = base64.b64encode(self.image)
     return encoded_string.decode('utf-8')
    else:
      raise ValueError