import json
import os
pat=input("输入.minecraft文件夹下assets的路径，不跟最后一个斜线\n")
ver=input("输入大版本号，如 1.17\n")
os.chdir(pat)
try:
    fi=open(pat+"/indexes/"+ver+".json","r")
except FileNotFoundError:
    print("无法找到输入路径\n")
    os.system("pause")
else:
    out=input("输入路径以便放置输出文件，不存在会自动创建\n")
    temp=fi.read()
    tempjson=json.loads(temp)
    for i in tempjson['objects']:
        tempstr=i.replace("/","\\")
        templi=tempstr.rsplit(sep="\\")
        tempstr2=("\\".join(templi[0:-1]))
        if os.path.exists(out+"\\"+tempstr2)==False:
            os.makedirs(out+"\\"+tempstr2)
        os.system("copy "+pat+"\\objects\\"+tempjson['objects'][i]["hash"][:2]+"\\"+tempjson['objects'][i]["hash"]+" /B"+" "+out+"\\"+tempstr+" /B")
    print("已完成\n")
    os.system("pause")
    fi.close()
