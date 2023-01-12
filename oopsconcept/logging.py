import logging
import os
class FileLog():
    def __init__(self):
        logging.basicConfig(filename="file.txt",level=logging.WARNING)

    def operation(self):
        try:
            print(os.popen("fsutil fsinfo drives").read())
            print(os.system('cmd /c "wmic logicaldisk list brief"'))
        #     self.x=int(input("num1"))
        #     self.y=int(input("num2"))
              #print(self.x/self.y)
        except filenotfound as msg:
            logging.exception(msg)
if __name__=='__main__':
    obj=FileLog()
    obj.operation()


