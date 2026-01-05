# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:52:22 2021

@author: ts-guangjie.qi
 删除操作
"""
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import os
from common.FileUnit import FileUnit

# =============================================================================
bat_file = 'batlist'
repStr = 'path.'
suffix_ttl = 'ttl'
const_de =' ='
# =============================================================================

class DeleteBtnUI:
    def __init__(self, master=None):
        self.master = master
        self.confDict = {}
        self.r_value = IntVar()
        self.r_value2 = IntVar()
        self.radioKeyList = []
        self.filepath = ''
        self.groupFileList = []
        self.showDetailFlag = False
        self.rownum=0
        self.detailFlag=0
        self.maxListSize=0
        self.detailFrame = Frame(self.master)
        self.groupFilePath=''
        self.checkSelect = []
        self.deleteFileList = []
        self.groupName=''
        self.cnfFileCnt=0
        # self.detailTagFrame = Frame(self.master)
        self.createWidget()
# =============================================================================
# 退出按钮
# =============================================================================
    def loginQuit(self):
        answer = tk.messagebox.askyesno("提示","确定直接退出吗？")
        if answer: # 如果点击确定，会返回一个True的值，否则False
            self.master.destroy()# 销毁主窗口
# =============================================================================
# 获取 所有组数据
# conf.Properties文件 内容
# =============================================================================
    def getGroupList(self):
        file = FileUnit()
        self.confDict = file.getConfContent()
        # print(self.confDict)
# =============================================================================
# detail tagName显示 不使用
# =============================================================================
    def detailTag(self):
        # Label样式
        self.detailTagFrame=Frame(self.master)
        font_style_title=("微软雅黑", 12, "bold")
        conf_label_title={'font':font_style_title}
        textVal=""
        if(self.showDetailFlag):
            textVal= "detailList"
        Label(self.master,text=textVal,cnf=conf_label_title).grid(row=self.rownum,ipadx=5)
        
        return self.detailTagFrame

# =============================================================================
# 选择组radio按钮的操作        
# =============================================================================
    def selectGrop(self):
        file = FileUnit()
        # print(self.r_value.get())
        i = self.r_value.get() -1
        self.groupName = self.radioKeyList[i].replace(repStr,'')
        self.groupFilePath = self.filepath + self.groupName
        self.groupFileList = file.getFileListByPathSuffix(self.groupFilePath,suffix_ttl)
        self.cnfFileCnt= len(self.groupFileList)
        filePathList = []
        for filename in self.groupFileList:
            filePathList.append(self.groupFilePath+FileUnit().getSeparator()+filename)
        self.deleteFileList=filePathList
        self.showDetailFlag = False
        # print('selectGroup',self.groupName)
        self.detailFrame.grid_forget()
        
# =============================================================================
# 选择明细radio按钮操作        
# =============================================================================
    def selectDetail(self):
        file = FileUnit()
        # print(self.r_value.get())
        i = self.r_value.get() -1
        self.groupName = self.radioKeyList[i].replace(repStr,'')
        self.groupFilePath = self.filepath + self.groupName
        self.groupFileList = file.getFileListByPathSuffix(self.groupFilePath,suffix_ttl)
        self.cnfFileCnt= len(self.groupFileList)
        # print(self.groupFileList)
        self.showDetailFlag = True
        self.detailShow()

# =============================================================================
#   checBoxkSelect处理      
# =============================================================================
    def checBoxkSelect(self):
        filePathList = []
        i=0
        for filename in self.groupFileList:
            if (self.checkSelect[i].get()==1):
               filePathList.append(self.groupFilePath+FileUnit().getSeparator()+filename)
            i=i+1
        self.deleteFileList=filePathList
        # print(filePathList)


# =============================================================================
# detail 明细checkbox显示
# =============================================================================
    def detailShow(self):
        self.detailFrame.grid_forget()
        self.detailFrame=Frame(self.master)
        self.checkSelect=[]
        k = self.rownum
        self.detailFlag = self.detailFlag + 1
        s=0
        if (self.showDetailFlag==True):
            for dfilename in self.groupFileList:
                self.checkSelect.append(tk.IntVar())
                checkVar = tk.IntVar()
                k = k + 1
                check = Checkbutton(self.detailFrame, text=dfilename, variable=self.checkSelect[s],command=self.checBoxkSelect)
                check.grid(row=k, column=1, sticky=W)
                s=s+1
                # print('filename--',dfilename)
        self.detailFrame.grid(row=k+1,column=1)
# =============================================================================
# 删除处理
# =============================================================================
    def deleteCmd(self):
        answer = messagebox.askyesno("提示","确定删除吗？")
        if answer: # 如果点击确定，会返回一个True的值，否则False
            for fileName in self.deleteFileList:
                fileNameBat = fileName.replace(".ttl", ".bat")
                os.remove(fileName)
                os.remove(fileNameBat)
                
            if(not self.showDetailFlag):
                # 1.删除文件(组)
                os.rmdir(self.groupFilePath)
                # conf文件更新
                # 组更新(conf.properties|dict.properties)
                # print("delete")
                file = FileUnit()
                delStr = repStr+self.groupName+const_de
                file.delConfUpdate(delStr, "conf.properties")
                file.delConfUpdate(delStr, "dict.properties")
                self.master.destroy()# 销毁主窗口
            else:
                 # 2.删除文件(明细)
                 # print("delete detail")
                 # 刷新内容 
                 if (self.cnfFileCnt==len(self.deleteFileList)):
                     os.rmdir(self.groupFilePath)
                     file = FileUnit()
                     delStr = repStr+self.groupName+const_de
                     file.delConfUpdate(delStr, "conf.properties")
                     file.delConfUpdate(delStr, "dict.properties")
                     self.master.destroy()# 销毁主窗口
                 self.selectDetail()
                         
# =============================================================================
# 按钮方法
# =============================================================================
    def createLoginOutButton(self):
        button_delete = Button(self.master,text='退出')
        button_delete.config(bg='#FF7F24',width='8',padx=2,pady=5)
        button_delete.config(command=self.loginQuit)
        button_delete.place(x=400,y=5)

    def createDeleteButton(self):
        button_delete = Button(self.master,text='删除')
        button_delete.config(bg='#FF7F24',width='8',padx=2,pady=5)
        button_delete.config(command=self.deleteCmd)
        button_delete.place(x=320,y=5)
        
# =============================================================================
#   主方法
# =============================================================================
    def createWidget(self):
        self.master.geometry("500x400+500-100")
        self.master.title("Delete item")
        self.filepath = FileUnit.getRootPath(self,"marco") + bat_file +FileUnit.getSeparator(self)
        # Label样式
        font_style_title=("微软雅黑", 12, "bold")
        conf_label_title={'font':font_style_title}
        font_style=("微软雅黑", 10, "bold")
        conf_label={'font':font_style}
        i=0
        Label(self.master,text="GroupList",cnf=conf_label_title).grid(row=i,ipadx=5,ipady=15,column=0)
        # 获取组List
        self.getGroupList()
        j=0
        k=1
        for dictKey,dictVal in self.confDict.items():
            # print(dictKey,dictVal)
            i=i+1
            Label(self.master, text=dictKey,cnf=conf_label).grid(row=i,column=1,sticky=tk.W)
            Radiobutton(self.master,text='组',variable=self.r_value,value=k,command=self.selectGrop).grid(row=i,column=2,sticky=tk.W)
            self.radioKeyList.append(dictKey)
            k=k+1
            Radiobutton(self.master,text='明细',variable=self.r_value,value=k,command=self.selectDetail).grid(row=i,column=3,sticky=tk.W)
            self.radioKeyList.append(dictKey)
            j = j + 1
            k=k+1
        
        self.rownum = i+1
        Label(self.master,text="detailList",cnf=conf_label_title).grid(row=self.rownum,ipadx=5)
        # 分隔符
        b=ttk.Separator(self.master,orient='horizontal')
        b.grid(row = self.rownum+1, columnspan=4, sticky=tk.N+tk.E+tk.S+tk.W)
        self.createDeleteButton()
        self.createLoginOutButton()
        
if __name__ == '__main__':      
    root = Tk()
    app = DeleteBtnUI(root)
    root.mainloop()