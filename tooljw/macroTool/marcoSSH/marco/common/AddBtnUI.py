#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/5/2021 22:35
# @Author  : 
# @File    : addBtnUI.py
# @Software: IntelliJ IDEA
# 追加按钮的相关操作
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
from common.FileUnit import FileUnit
from common.Util import Properties

# =============================================================================
# ttpmacro.properties"
ttpmaro_name = "ttpmacro.properties"
ttpmacro_path= 'ttpmacro.path'
ttpmacro_host= 'ttpmacro.host'
ttpmacro_user= 'ttpmacro.user'
ttpmacro_pwd= 'ttpmacro.pwd'
const_equal_sign = str(' = ')
# =============================================================================

# =============================================================================
# dict.properties
conf_dict_file= "dict.properties"
# =============================================================================

# =============================================================================
# conf.properties
const_path ="path."
conf_conf_file = "conf.properties"
conf_ttpmacro_file = "ttpmacro.properties"
# =============================================================================


# =============================================================================
# bat ttl file path
batPath="batlist"
const_template_bat = "bat_template.bat"
const_suffix_ttl = ".ttl"
const_suffix_bat = ".bat"
const_login_temp = "login_tempalte.ttl"
const_SSH_temp = "ssh_template.ttl"

# bat ttl file replace content
ttl_host = '@loginhost'
ttl_user = '@loginuser'
ttl_pwd = '@pwd'
ttl_sshUrl = '@sshUrl'

bat_marco_path = '@ttpmarcoPath'
bat_ttl_file ='@ttlFile'
# =============================================================================


class AddBtnUI(Frame):
    # lableVar=StringVar()
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.marcoEXEPath=StringVar()
        self.cb1val= StringVar()
        self.dicttmaro={}
        self.values_ttpmacro=()
        self.chpath=IntVar()
        self.comboxstate=StringVar()
        self.comboxObj=None
        self.hostEnteryObj=None
        self.userEnteryObj=None
        self.pwdEnteryObj=None
        self.chhost=IntVar()
        self.enteryHostVal=StringVar()
        self.chuser=IntVar()
        self.enteryUserVal=StringVar()
        self.chpwd=IntVar()
        self.enteryPwdVal=StringVar()
        self.rootpath=''
        self.templateVal=StringVar()
        self.enteryGroupHanVal=StringVar() # 组别名
        self.enteryGroupEngVal=StringVar() # 组别名（英）
        self.enteryGroupDtlName=StringVar() # 组别明细名
        self.templatePath=''
        self.batFilePath=''
        self.batListPath=''
        self.sshUser = StringVar()
        self.sshUrl = StringVar()
        self.createWidget()
        


    def tempalteSelection(self,event):
        self.templateVal.set(self.cb1val.get())
        # print(self.templateVal)

    def ttpmacroSelection(self,event):
        filename = filedialog.askopenfilename()
        self.marcoEXEPath.set(filename)
        # print(filename)
     
    def getTtpmacroProp(self,path):
        # ttpmacro.properties内容获取
        dictProperties = Properties(path).getProperties()
        # print(dictProperties)
        return dictProperties

    def updatemacroProp(self):
        # 更新ttpmacro.properties"
        print("更新ttpmacro.properties")
        
    def checkTtpmacro(self,dictxxx):
        # print(self.chonvalue)
        # print('OK')
        ttpmacro_path =dicttmaro.get('ttpmacro.path')
        # print(ttpmacro_path)
        
                
    def getCheckPath(self):
        if self.chpath.get()==1:
            self.comboxObj['state']='disabled'
            self.marcoEXEPath.set(self.dicttmaro.get('ttpmacro.path'))
            # print("checked")
        else:
            self.comboxObj['state']='normal'
            self.marcoEXEPath.set(self.templateVal.get())
            # print("un checked")

    def getCheckHost(self):
        if self.chhost.get()==1:
            self.enteryHostVal.set(self.dicttmaro.get('ttpmacro.host'))
            self.hostEnteryObj['state']='readonly'
        else:
            self.hostEnteryObj['state']='normal'
            self.enteryHostVal.set('input')
            
    def getCheckUser(self):
        if self.chuser.get()==1:
            self.enteryUserVal.set(self.dicttmaro.get('ttpmacro.user'))
            self.userEnteryObj['state']='readonly'
        else:
            self.enteryUserVal.set('input')
            self.userEnteryObj['state']='normal'

    def getCheckPwd(self):
        if self.chpwd.get()==1:
            self.enteryPwdVal.set(self.dicttmaro.get('ttpmacro.pwd'))
            self.pwdEnteryObj['state']='readonly'
        else:
            self.enteryPwdVal.set('input')
            self.pwdEnteryObj['state']='normal'
        
    def loginQuit(self):
        answer = tk.messagebox.askyesno("提示","确定直接退出吗？")
        if answer: # 如果点击确定，会返回一个True的值，否则False
            self.master.destroy()# 销毁主窗口
            
# =============================================================================
# 确认按钮按下之后，更新 dicttmaro 
# =============================================================================
    def updateDicttmaro(self):
        # print('update--before--',self.dicttmaro)
        dictMaroUpdate={
            ttpmacro_path : self.marcoEXEPath.get(),
            ttpmacro_host : self.enteryHostVal.get(),
            ttpmacro_user : self.enteryUserVal.get(),
            ttpmacro_pwd :self.enteryPwdVal.get()
            }
        self.dicttmaro.update(dictMaroUpdate)

# =============================================================================
# check ttpmacro.properties是否更新执行
# =============================================================================
    def checkUpdateFlg(self):
        if ((len(self.marcoEXEPath.get()) == 0 or self.marcoEXEPath.get().isspace())
           or (len(self.enteryHostVal.get()) == 0 or self.enteryHostVal.get().isspace())
           or (len(self.enteryUserVal.get()) == 0 or self.enteryUserVal.get().isspace())
           or (len(self.enteryPwdVal.get()) == 0 or self.enteryPwdVal.get().isspace())) :
           return False
        else:
            print("更新ttpmacro.properties内容")
            return True
        
# =============================================================================
# ttpmacro.properties 
# =============================================================================
    def ttpmacroUpdate(self):
        if (not self.checkUpdateFlg()):
            return False
        print('ttpmacro.properties','更新做成OK')
        ttpmacroFile=self.rootpath+"conf" +FileUnit.getSeparator(self) + conf_ttpmacro_file
        # 更新Dicttmaro内容
        self.updateDicttmaro()
        FileUnit.alterMacroProperFile(self,ttpmacroFile,self.dicttmaro)

# =============================================================================
# dict.properties
# =============================================================================
    def dictConfUpdate(self):
        new_str =''
        old_str =''
        dictConfs={}
        dictConfFile= self.rootpath+"conf" + FileUnit.getSeparator(self) + conf_dict_file
        dictConfs= Properties(dictConfFile).getProperties()
        newKey = const_path + self.enteryGroupEngVal.get()
        createFlg = FALSE
        if (len(dictConfs) > 0 ):
            if (newKey in dictConfs):
                for dictKey,dictVal in dictConfs.items():
                    old_str = dictKey + const_equal_sign + dictVal
                    new_str = old_str
                    if (dictKey == newKey):
                        new_str = newKey + const_equal_sign + str(self.enteryGroupHanVal.get())
                    FileUnit.alterProperFile(self, dictConfFile, old_str, new_str)
            else:
                createFlg = TRUE
        else:
            createFlg = TRUE
        
        if (createFlg == TRUE):
            new_str = newKey + const_equal_sign + self.enteryGroupHanVal.get()
            old_str = new_str
            FileUnit.alterProperFile(self, dictConfFile, old_str, new_str)
        
# =============================================================================
# conf.properties
# =============================================================================
    def configConfUpdate(self):
        new_str =''
        old_str =''
        newKey = const_path + self.enteryGroupEngVal.get()
        newVal = self.rootpath+batPath + FileUnit.getSeparator(self) + self.enteryGroupEngVal.get()
        createFlg = FALSE
        configConfs={}
        configConfFile= self.rootpath+"conf" + FileUnit.getSeparator(self) + conf_conf_file
        configConfs= Properties(configConfFile).getProperties()
        if (len(configConfs) > 0 ):
            if (newKey in configConfs):
                for dictKey,dictVal in configConfs.items():
                    old_str = dictKey + const_equal_sign + dictVal
                    new_str = old_str
                    if (dictKey == newKey):
                        new_str = newKey + const_equal_sign + newVal
                    FileUnit.alterProperFile(self,configConfFile, old_str, new_str)
            else:
                createFlg = TRUE
        else:
            createFlg = TRUE
        
        if (createFlg == TRUE):
            new_str = newKey + const_equal_sign + newVal
            old_str = new_str
            FileUnit.alterProperFile(self,configConfFile, old_str, new_str)

# =============================================================================
# create and update ttl file
# 1.做成的文件名存在则删除源文件，新规
# 2.做成文件不存在直接新规
# =============================================================================
    def createUpdateLoginTtlFile(self):
        templateFileName = self.templatePath + self.templateVal.get()
        createFileName = self.batListPath + self.enteryGroupEngVal.get() + FileUnit.getSeparator(self) + self.enteryGroupDtlName.get() + const_suffix_ttl
        createdir = self.batListPath + self.enteryGroupEngVal.get()
        FileUnit.createFile(self, templateFileName ,createFileName,createdir)
        replaceDict = {ttl_host : self.dicttmaro.get(ttpmacro_host) ,
                       ttl_user : self.dicttmaro.get(ttpmacro_user) ,
                       ttl_pwd : self.dicttmaro.get(ttpmacro_pwd) }
        FileUnit.fileContentReplace(self, createFileName, replaceDict)
        

    def createUpdateSSHTtlFile(self):
        templateFileName = self.templatePath + self.templateVal.get()
        createFileName = self.batListPath + self.enteryGroupEngVal.get() + FileUnit.getSeparator(self) + self.enteryGroupDtlName.get() + const_suffix_ttl
        createdir = self.batListPath + self.enteryGroupEngVal.get()
        FileUnit.createFile(self, templateFileName ,createFileName,createdir)
        replaceDict = {ttl_host : self.enteryHostVal.get() ,
                       ttl_user : self.enteryUserVal.get(),
                       ttl_pwd : self.enteryPwdVal.get(),
                       ttl_sshUrl : self.sshUrl.get()}
        FileUnit.fileContentReplace(self, createFileName, replaceDict)
        
# =============================================================================
# create and update bat file
# 1.做成的文件名存在则删除源文件，新规
# 2.做成文件不存在直接新规
# =============================================================================
    def createUpdateBatFile(self):
        templateFileName = self.templatePath + const_template_bat
        createFileName = self.batListPath + self.enteryGroupEngVal.get() + FileUnit.getSeparator(self) + self.enteryGroupDtlName.get() + const_suffix_bat
        ttlFileName = self.batListPath + self.enteryGroupEngVal.get()  + FileUnit.getSeparator(self) + self.enteryGroupDtlName.get() +  const_suffix_ttl
        createdir = self.batListPath + self.enteryGroupEngVal.get()
        FileUnit.createFile(self, templateFileName ,createFileName,createdir)
        replaceDict = {bat_marco_path : self.marcoEXEPath.get() ,
                       bat_ttl_file : ttlFileName}
        FileUnit.fileContentReplace(self, createFileName, replaceDict)



# =============================================================================
# 确认按钮事件
# 1.配置文件更新做成
# 2.ttl文件做成（copy tempalte ttl做成）
# 3.bat文件做成（copy tempalte bat做成）
# =============================================================================
    def loginConfirm(self):
# =============================================================================
#       文件更新操作
# =============================================================================
        self.ttpmacroUpdate()
        print("do next")
        createFlg = True
        if((len(self.enteryGroupEngVal.get()) == 0 or self.enteryGroupEngVal.get().isspace())
           or (len(self.enteryGroupDtlName.get()) == 0 or self.enteryGroupDtlName.get().isspace())
           or (len(self.enteryGroupHanVal.get()) == 0 or self.enteryGroupHanVal.get().isspace())
           or (len(self.enteryGroupHanVal.get()) == 0 or self.enteryGroupHanVal.get().isspace())
           or (len(self.templateVal.get()) == 0 or self.templateVal.get().isspace())):
            createFlg = False
        if (createFlg==True):
            print('dict.propertiess','更新做成OK')
            self.dictConfUpdate()
            
            print('conf.properties','更新做成OK')
            self.configConfUpdate()
# =============================================================================
#       文件做成
# =============================================================================
            print('ttl文件做成')
            
            if (const_login_temp == self.templateVal.get()):
                self.createUpdateLoginTtlFile()
            elif (const_SSH_temp == self.templateVal.get()):
                self.createUpdateSSHTtlFile()
            else:
                createFlg = False
                print('nothing to do')
            
            print('ttl关联bat文件做成')
            if (createFlg == True):
                self.createUpdateBatFile()
        
        
# =============================================================================
#   主方法
# =============================================================================
    def createWidget(self):
        print(self.master)
        self.master.geometry("500x400+500-300")
        self.master.title("Add item")
        self.rootpath = FileUnit.getRootPath(self,"marco") #rootpath
        print('rootPath--',self.rootpath)
        # 获取ttpmacro.properties的值
        self.dicttmaro = self.getTtpmacroProp(self.rootpath+"conf" +FileUnit.getSeparator(self)+ttpmaro_name);
        # print(self.dicttmaro)
        # print(self.rootpath)
        cb1val = self.cb1val
        frame = Frame(self.master)
        frame.pack()
        # Label样式
        font_style=("微软雅黑", 10, "bold")
        conf_label={'font':font_style}
        conf_entry = {'width':'40'}
        # 模板选择
        i=0
        Label(frame,text='模板选择:',cnf=conf_label).grid(row=i)
        # ttpmacro.path
        i=i+1
        Label(frame,text='ttpmacro.path:', cnf=conf_label).grid(row=i)
        # ttpmacro.host
        i=i+1
        Label(frame,text='login.host:', cnf=conf_label).grid(row=i)
        # ttpmacro.user
        i=i+1
        Label(frame,text='login.user:', cnf=conf_label).grid(row=i)
        # ttpmacro.pwd:
        i=i+1
        Label(frame,text='login.pwd:', cnf=conf_label).grid(row=i)
        # 组别名
        i=i+1
        Label(frame,text='组别名（汉）:',cnf=conf_label).grid(row=i)
        # 组别名
        i=i+1
        Label(frame,text='组别名(英):',cnf=conf_label).grid(row=i)
        # 组内明细名
        i=i+1
        Label(frame,text='组内明细名(英):',cnf=conf_label).grid(row=i)
        # SSH URL名
        # i=i+1
        # Label(frame,text='SSH User:',cnf=conf_label).grid(row=i)
        i=i+1
        Label(frame,text='SSH Host:',cnf=conf_label).grid(row=i)
        # SSH URL输入
        # i=i+1
        # Label(frame,text='命令添加:',cnf=conf_label).grid(row=i)
        # 命令添加
        i=i+1
        Label(frame,text='',cnf=conf_label).grid(row=i)
        
        # Content
        # combox
        # 模板选择
        j=0
        
        path = self.rootpath+'template' + FileUnit.getSeparator(self)
        self.templatePath = path
        self.batFilePath = path
        self.batListPath = self.rootpath + batPath + FileUnit.getSeparator(self)
        templates = FileUnit.getFileListByPathSuffix(self,path, ".ttl")
        cb1 = Combobox(frame,width=37,textvariable=cb1val ,values=templates)
        cb1.bind("<<ComboboxSelected>>",self.tempalteSelection)
        cb1.grid(row=j,column=1)
        # ttpmacro.path
        j=j+1
        # values_ttpmacro=('ttpmacro')
        self.comboxstate.set('disabled')
        self.values_ttpmacro=('ttpmacro')
        # print(self.chpath.get())
        self.marcoEXEPath.set(self.templateVal.get())
        cb2=Combobox(frame,width=37,textvariable=self.marcoEXEPath,values=self.values_ttpmacro,state=self.comboxstate)
        cb2.bind("<<ComboboxSelected>>", self.ttpmacroSelection)
        cb2.grid(row=j,column=1) 
        self.comboxObj=cb2
        check = Checkbutton(frame, text="default", variable=self.chpath,command=self.getCheckPath)
        check.grid(row=j,column=2)

        # ttpmacro.host
        j=j+1
        hostObj=Entry(frame,state='normal',textvariable=self.enteryHostVal,cnf=conf_entry)
        hostObj.grid(row=j,column=1)
        self.hostEnteryObj=hostObj
        # print(hostObj)
        # chhost = tk.IntVar()
        check = Checkbutton(frame, text="default", variable=self.chhost,command=self.getCheckHost)
        check.grid(row=j,column=2)
        # ttpmacro.user
        j=j+1
        userObj=Entry(frame,textvariable=self.enteryUserVal,cnf=conf_entry)
        userObj.grid(row=j,column=1)
        self.userEnteryObj=userObj
        # chuser = tk.IntVar()
        check = Checkbutton(frame, text="default", variable=self.chuser,command=self.getCheckUser)
        check.grid(row=j,column=2)
        # ttpmacro.pwd
        j=j+1
        pwdObj=Entry(frame,textvariable=self.enteryPwdVal,cnf=conf_entry)
        pwdObj.grid(row=j,column=1)
        self.pwdEnteryObj=pwdObj
        # chpwd = tk.IntVar()
        check = Checkbutton(frame, text="default", variable=self.chpwd,command=self.getCheckPwd)
        check.grid(row=j,column=2)
        # 组别名（汉）
        j=j+1
        Entry(frame,cnf=conf_entry,textvariable=self.enteryGroupHanVal).grid(row=j,column=1)
        # 组别名（英）
        j=j+1
        Entry(frame,cnf=conf_entry,textvariable=self.enteryGroupEngVal).grid(row=j,column=1)
        
        # 组内明细名
        j=j+1
        Entry(frame,cnf=conf_entry , textvariable=self.enteryGroupDtlName).grid(row=j,column=1)
        # SSH host输入
        j=j+1
        Entry(frame,cnf=conf_entry, textvariable=self.sshUrl).grid(row=j,column=1)
        # 命令添加
        # j=j+1
        # Entry(frame,cnf=conf_entry).grid(row=j,column=1)
        j=j+1
        # btnCnf
        btnCnf = {'background':'#FF7F24','borderwidth':'5','width':11,'padx':2,'pady':5}
        # 按钮位置
        cnt =j
        j=j+1
        Label(frame).grid(row=j,columnspan=3)
        j=j+1
        Label(frame).grid(row=j,columnspan=3)
        # print(j*12)
        Button(frame,text='ttpmacro更新', cnf=btnCnf,command=self.ttpmacroUpdate).place(x=20,y=cnt*27)
        Button(frame,text='作成', cnf=btnCnf,command=self.loginConfirm).place(x=120,y=cnt*27)
        Button(frame,text='退出', cnf=btnCnf,command=self.loginQuit).place(x=220,y=cnt*27)
        print('create add ui')
        
    def getFiledialog(self):
        filename = filedialog.asksaveasfilename()
        return filename
if __name__ == '__main__':
    root = Tk()
    add = AddBtnUI(master=root)
    root.mainloop()