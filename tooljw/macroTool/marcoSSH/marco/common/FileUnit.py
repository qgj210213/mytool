from common.Util import Properties
import platform
import os
import os.path
import re,os
conf_name = "conf.properties"
dict_name = "dict.properties"
conf_path = "../conf"
const_login = "path.login"
const_dev = "path.dev"
const_ichikawa = "path.ichikawa"
const_kwn = "path.kawanishi"
const_nagareym = "path.nagareym"
const_rba = "path.rba"
const_bat = ".bat"
# =============================================================================
# #
const_equal_sign = str(' = ')
# =============================================================================

# 共通クラス
class FileUnit:
    def __init__(self,master = None):
        self.master = master

    def getConfFilePath(self, conf_file_name):
        pathRoot = self.getRootPath("marco")+ self.getSeparator() + "conf"
        path = pathRoot + self.getSeparator() + conf_file_name
        # print('path--',path)
        return path

    def getConfContent(self):
        path = self.getConfFilePath(conf_name)
        dictProperties = Properties(path).getProperties()
        return dictProperties
    
    def getFilePathByCenter(self, center):
        path = self.getConfFilePath(conf_name)
        dictProperties = Properties(path).getProperties()
        file_path = dictProperties.get(center)
        return file_path

    def getDictMap(self, dict_file_name):
        path = self.getConfFilePath(dict_file_name)
        dictMaps = Properties(path).getProperties()
        return dictMaps

    def getFileListByPath(self, path):
        dirList = []
        dirs = os.listdir(path)
        for file in dirs:
            if (file.__contains__(const_bat)):
                dirList.append(file)
        return dirList

    def getFileListByPathSuffix(self, path,suffix):
        dirList = []
        dirs = os.listdir(path)
        for file in dirs:
            if (file.__contains__(suffix)):
                dirList.append(file)
        return dirList

    def getFileListBycenter(self, center):
         file_path = self.getFilePathByCenter(center)
         dirList = []
         dirs = os.listdir(file_path)
         for file in dirs:
             if (file.__contains__(const_bat)):
                 dirList.append(file)
         return dirList

    def getEnvList(self):
        envList = [const_login, const_dev, const_ichikawa, const_kwn, const_nagareym, const_rba]
        return envList
    
    # 返回当前进程的工作目录
    def getPrjCurrentpath(self):
        prjPath = os.getcwd()
        return prjPath

    def getAbsPath(self,str):
        absPath = os.path.abspath(str)
        return absPath

    def getSeparator(self):
        if 'Windows' in platform.system():
            separator = '\\'
        else:
            separator = '/'
        return separator
    
    def getRootPath(self, splitDir=""):
        root_path = os.path.abspath(os.path.dirname('__file__')).split(splitDir)[0]
        return root_path


# =============================================================================
#     指定文件修改更新（conf properties）
# =============================================================================
    def alterProperFile(self,file,old_str,new_str):
        # 1.读取文件
        with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
            new_flg=False
            for line in f1:
                print(line)
                if (old_str in line):
                    # 替换文件
                    new_flg=True
                    lineNew = line.replace(old_str, new_str)
                    f2.write(lineNew)
                else:
                    # print(new_str)
                    f2.write(line)
            if new_flg==False:
                f2.write("\n"+new_str)

            f1.close()
            f2.close()
            os.remove(file)
            os.rename("%s.bak" % file, file)
# =============================================================================
#     指定文件修改更新（macro properties）
# =============================================================================
    def alterMacroProperFile(self,file,dictmarco):
        # 1删除文件
        os.remove(file)
        with open(file, "w", encoding="utf-8") as fd:
            for dkey,dval in dictmarco.items():
                line = dkey + const_equal_sign + dval + "\n"
                fd.write(line)
        fd.close()
                
# =============================================================================
# 替换文件内容
# =============================================================================
    def fileContentReplace(self, file, replaceDict):
        # 1.原样读取文件
        f1 = open(file, 'r', encoding='utf-8', newline='')
        content = f1.read()
        f1.close()
        # 2.替换文件内容
        repContent=None
        for repMark ,repVal in replaceDict.items():
            repContent = content.replace(repMark,repVal)
            content = repContent
        # 3.写入替换文件
        with open(file, 'w', encoding='utf-8', newline='') as f2:
            f2.write(repContent)
            f2.close()
        
        
        
# =============================================================================
# 创建文件
# 1.检查文件路径是否存在，不存在创建
# 2.文件存在删除并按照templte文件创建
# 3.不存在则按照templte文件创建
# =============================================================================
    def createFile(self,templateFile,newFile,createDir):
        existsFlg = False
        existsFlg = os.path.exists(newFile)
        # print('existsFlg',existsFlg)
        if (existsFlg == True):
            os.remove(newFile)
        else:
            if (not(os.path.exists(createDir))):
                os.mkdir(createDir)
            
        # 打开文件
        with open(templateFile, 'r', encoding='utf-8', newline='') as fd, open(newFile, 'w' , encoding='utf-8',newline='') as fc:
            # 写入文件
            fc.writelines(fd)
            fc.close()
# =============================================================================
# 删除按钮处理
# conf.properties
# dict.properties
# 跟更新内容
# 
# =============================================================================
    def delConfUpdate(self,delStr,fileName):
        pathRoot = self.getRootPath("marco")+ self.getSeparator() + "conf"
        filePath = pathRoot+self.getSeparator()+fileName
        # 1.读取文件
        with open(filePath,"r",encoding="utf-8", newline='') as f:
            lines = f.readlines()
        f.close()
        # 2.重新写入文件将删除文件跳过
        with open(filePath, 'w', encoding='utf-8', newline='') as fw:
            for line in lines:
                if delStr in line:
                    continue
                fw.write(line)
            fw.close()
        


# 实例化类
# file='C:/qgjWorkSpace/workSpace/PythonWork/pyBase/Tool/PyTeraterm/conf/conf1.properties'
# dictKey='path.login'
# dictVal='C:/qgjWorkSpace/qgjWmsWork/makuro/macroList/loginx'
# dictValNew='C:/qgjWorkSpace/qgjWmsWork/makuro/macroList/login/new'
# old_str=dictKey+" = "+ dictVal
# new_str=dictKey+" = "+ dictValNew
# FileUnit.alterProperFile(file,old_str,new_str)

# test createFile
# templateFile1 = 'C:/qgjWorkSpace/workSpace/PythonWork/pyBase/Tool/PyTeraterm/template/login_tempalte.ttl'
# createFile1 = 'C:/qgjWorkSpace/workSpace/PythonWork/pyBase/Tool/PyTeraterm/batlist/login/login.ttl'
# cdir ='C:/qgjWorkSpace/workSpace/PythonWork/pyBase/Tool/PyTeraterm/batlist/login/'
# FileUnit.createFile(None,templateFile1,createFile1,cdir)

# =============================================================================
# test fileContentReplace
# ttl_host = '@loginhost'
# ttl_user = '@loginuser'
# ttl_pwd = '@pwd'
# fileName = 'C:/qgjWorkSpace/workSpace/PythonWork/pyBase/Tool/PyTeraterm/batlist/login.ttl'
# replaceDict = {ttl_host:'xxx.local',ttl_user:'ts-qiguangji01',ttl_pwd:'itforce1!'}
# FileUnit.fileContentReplace(None,fileName,replaceDict)
# print(replaceDict)
# =============================================================================
