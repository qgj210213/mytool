# python3 读取配置文件 properties
class Properties(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.properties = {}

    def __getDict(self, dictName, key, value):
        dictName[key] = value
        return

    def getProperties(self):
        try:
            pro_file = open(self.fileName, 'Ur', encoding='UTF-8')
            for line in pro_file.readlines():
                line = line.strip().replace('\n', '')
                if line.find("#") != -1:
                    line = line[0:line.find('#')] #将注释前的内容赋值给line
                if line.find('=') > 0:
                    strs = line.split('=')
                    pkey = strs[0]
                    pValue = line[len(pkey)+1:] #将'='号后面的值给pValue
                    self.__getDict(self.properties, pkey.strip(), pValue.strip())
        except Exception as e:
            raise e
        else:
            pro_file.close()
        return self.properties



