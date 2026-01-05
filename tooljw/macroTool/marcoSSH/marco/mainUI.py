# import tkinter.messagebox
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Separator
from common.FileUnit import FileUnit
from common.FileUnit import conf_name
from common.FileUnit import dict_name
import tkinter as tk
import os

from tkinter.ttk import Combobox
from common.AddBtnUI import AddBtnUI 
from common.DeleteBtnUI import DeleteBtnUI 

class Application(Frame):
    dictBat = []
    space = "".rjust(40)

    """初始话构造函数"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createAddButton()
        self.createDeleteButton()
        self.createQuitButton()
        # self.grid(row=1,columnspan=2)
        self.place(x=5,y=50)
        self.rootBtn=None
        self.createWidget()

    def loginQuit(self):
        answer = tk.messagebox.askyesno("提示","确定直接退出吗？")
        if answer: # 如果点击确定，会返回一个True的值，否则False
            self.master.destroy()# 销毁主窗口
    def addCmd(self):
        top = Toplevel(self.master)
        add = AddBtnUI(master=top)
    def deleteCmd(self):
        top = Toplevel(self.master)
        delete = DeleteBtnUI(master=top)
        
    def createAddButton(self):
        button_add = Button(self.master,text='追加修改')
        button_add.config(bg='#8EE5EE',width='8',padx=2,pady=5)
        button_add.config(command=self.addCmd)
        button_add.place(x=20,y=10)
        
    def createDeleteButton(self):
        button_delete = Button(self.master,text='删除')
        button_delete.config(bg='#FF7F24',width='8',padx=2,pady=5)
        button_delete.config(command=self.deleteCmd)
        button_delete.place(x=100,y=10)
        
    def createQuitButton(self):
        button_Quit = Button(self.master,text='退出')
        button_Quit.config(bg='#FF7F24',width='8',padx=2,pady=5,command = self.loginQuit)
        button_Quit.place(x=180,y=10)

    def createWidget(self):
        """创建组件"""
        self.createOptionMenuList()
        i = 0
        for i in range(len(self.pvlist)):
            self.pvlist[i].trace("w", self.callback)

    def createOptionMenuList(self):
        self.pvlist = []
        file = FileUnit()
        dict_conf = file.getDictMap(conf_name)
        # print('mainUI--dict_conf--',dict_conf)
        dict_name_map = file.getDictMap(dict_name)
        envList = dict_conf.keys()
        for i in range(len(envList)):
            self.pvlist.append(StringVar(self.master))

        j = 0
        for groupName in envList:
            self.createOptionMenuByCenter(groupName, dict_conf, dict_name_map, j)
            j = j + 1
# =============================================================================
# 补充空格      
# =============================================================================
    # def addSpace(self,textVal):
    #     editVal=''
    #     if len(textVal)>=20:
    #         return textVal
    #     else:
    #         for num in range(20-len(textVal)):
    #             editVal = editVal+' '
    #         return textVal+editVal
        
    def optionContentEdit(self,contents):
        clist = []
        for cval in contents:
            clist.append(cval.replace(".bat", ""))
        return clist

    def createOptionMenuByCenter(self, groupName, dictMaps, labelMap, index):
        groupContents = self.getContentListByCenter(groupName)
        contents= self.optionContentEdit(groupContents)
        self.dictBat.append(dictMaps.get(groupName))
        labelName = labelMap.get(groupName)
        self.pvlist[index].set(self.space)
        self.createLabel(index, labelName)
        # print('contents--',contents)
        self.om = OptionMenu(self, self.pvlist[index], *contents)
        self.om.grid(row=index, column=2, sticky=W+E, padx=1, pady=1, ipadx=1)

    def getContentListByCenter(self, groupName):
        file = FileUnit()
        path = file.getFilePathByCenter(groupName)
        dirs = file.getFileListByPath(path)
        return dirs

    def getFilePathByCenter(self, groupName):
        file = FileUnit()
        path = file.getFilePathByCenter(groupName)
        return path

    def createLabel(self, index, labelName):
        self.labelLeft = Label(self, text=labelName,  width=10, height=2)
        self.labelLeft.grid(row=index, column=0, sticky=SW)

    def callback(self, *args):
        i =0
        while (i<len(self.pvlist)):
            if (str(self.pvlist[i]) == args[0]):
                self.doBat(self.dictBat[i], self.pvlist[i].get())
                break
            i = i+1
            
    def editBat(self,batfileName):
        if '.bat' in batfileName:
            return batfileName
        else:
            return batfileName+".bat"
    def doBat(self, path, batName):
        # print(path)
        separator = FileUnit().getSeparator()
        # print(path + separator + batName)
        self.run_bat(path + separator + self.editBat(batName))

    def run_bat(self, batFile):
        print(batFile)
        os.system(batFile)


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x500+100-100")
    root.title("teraterm SSH")
    app = Application(master=root)
    root.mainloop()