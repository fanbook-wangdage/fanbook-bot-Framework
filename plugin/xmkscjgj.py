import os
print('欢迎使用项目快速创建工具，该工具可以快速创建一个可以运行的示例bot')
file_name = input('请输入项目名称：')
token=input('请输入bot的token：')
botid=input('请输入bot的长id：')
code="token='"+token+"""'
def onOpen(ws):
    pass
def onMessage(ws, message):
    global token
    message=json.loads(message)#解析json为字典
    if message["action"] =="push":#如果是推送
        if message["data"]["author"]["bot"] == False:#忽略bot消息
            content = json.loads(message["data"]["content"])#这里获取消息内容"""+'\n            if "${@!'+botid+'}" in content["text"]:#筛选@这个机器人的消息，注意这里的botid改为你机器人的长id'+"""\n                #我们将逻辑写在这里
                guild_id=message["data"]["guild_id"]#获取消息来源服务器id
                channel_id=message["data"]["channel_id"]#获取消息来源频道id
                text=content['text'][23:]#去掉@以后的内容
                #发送消息
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
