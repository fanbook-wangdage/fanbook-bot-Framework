import os
print('欢迎使用项目快速创建工具，该工具可以快速创建一个可以运行的示例bot')
file_name = input('请输入项目名称：')
token=input('请输入bot的token：')
botid=input('请输入bot的长id：')
code="token='"+token+"""'
from fanbookbotapi import *
import json

# 本段代码由工具自动生成，是一个将你的消息重新发出去的示例，你可以直接运行
# 你可以自由更改onMessage函数里面的代码，但是我建议你保留解析消息的那一部分
# onOpen、onMessage、onError、onClose分别用于连接建立时触发、收到消息时触发、出错时触发、连接关闭时触发，可以使用ws参数来完成一些操作，但是你一般不需要使用这个，发送心跳包将由库自动实现
# 强烈建议在处理消息部分添加try或者在配置编辑器内设置出错时自动重启，onMessage出错时很有可能断开连接并导致程序意外终止

def onOpen(ws):
    pass
def onMessage(ws, message):
    global token
    message=json.loads(message)# 解析json为字典
    if message["action"] =="push":# 如果是推送
        if message["data"]["author"]["bot"] == False:# 忽略bot消息
            content = json.loads(message["data"]["content"])# 这里获取消息内容"""+'\n            if "${@!'+botid+'}" in content["text"]:#筛选@这个机器人的消息，注意这里的botid改为你机器人的长id'+"""\n                # 我们将逻辑写在这里
                guild_id=message["data"]["guild_id"]# 获取消息来源服务器id
                channel_id=message["data"]["channel_id"]# 获取消息来源频道id
                text=content['text'][23:]# 去掉@以后的内容
                # 发送消息
                sendmessage(token,chatid=int(channel_id),type='text',text=text)
            
def onError(ws, error):
    pass
def onClose(ws):
    pass
bot_websocket(token,onOpen,onMessage,onError,onClose)
"""
print('正在创建项目文件夹...')
os.mkdir(file_name)
print('正在创建文件...')
with open(file_name+'/'+file_name+'.py','w',encoding='utf-8') as f:
    f.write(code)
print('创建完成！')
print('现在可以使用主程序的运行文件功能来运行这个示例bot了！\n文件路径输入'+file_name+'/'+file_name+'.py'+'即可运行')
