import requests#http请求
import sentry_sdk
sentry_sdk.init(
    dsn="https://ebd37d227cb63c566f410978aaa17948@o4507525750521856.ingest.us.sentry.io/4507866056491008",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

import json#json数据处理
import traceback#错误捕获
import urllib.request
import time#延时
import platform
import psutil
import ctypes
import subprocess
import sys#系统组件
import os#系统组件
import datetime
import chardet
import websocket#ws接口链接
import base64#请求体编码
import threading
import queue
import ssl
import tkinter as tk#图形界面
import hashlib
import uuid
import time
import urllib.parse
import fanbookbotapi
from collections import OrderedDict
from tqdm import tqdm#进度条
from pygments import highlight#高亮
from pygments.lexers import JsonLexer#高亮
from pygments.formatters import TerminalFormatter#高亮
from colorama import init, Fore, Back, Style#高亮
from tkinter import filedialog
from datetime import datetime

initial_text = '''

'''

v=5.294#统一版本

app_secret = 'dJcPo1dQHeMgDn1s8MQr'
app_key = 'ww0qqc0UHMsFtDUhGbh0'
userform = 'web'

def fixed_encodeURIComponent(value: str) -> str:
    return urllib.parse.quote(value, safe='~()*!.\'')

def get_signature(signature_map: dict) -> str:
    # 对字段按键进行排序
    sorted_fields = OrderedDict(sorted(signature_map.items()))
    # 将键值对转换为字符串并连接
    chain = '&'.join(f"{key}={value}" for key, value in sorted_fields.items())
    # 在末尾添加appSecret
    chain = chain + '&' + app_secret
    # 对结果进行URL编码
    encoded_chain = fixed_encodeURIComponent(chain)
    # 生成md5签名
    signature = hashlib.md5(encoded_chain.encode('utf-8')).hexdigest()
    return signature

try:
    file_name = "info.ini"
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, file_name)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            print('正在初始化配置')
            file.write(initial_text)
            print('初始化配置完成')
except Exception as e:
    error=traceback.format_exc()
    print("写入/读取配置错误:\n"+str(error))

try:
    with open("info.ini", 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    with open("info.ini", 'r', encoding=encoding) as file:
        code = file.read()
        exec(code, globals())  # 在全局命名空间中执行文件中的代码
except Exception as e:
    print("发生错误:"+str(e))

try:
    def check_file_exists(file_path):
        return os.path.exists(file_path)


    def download_file(url, save_path):
        try:
            response = requests.get(url)
            with open(save_path, 'wb') as file:
                file.write(response.content)
        except Exception as e:
            error=traceback.format_exc()
            print("下载/检测更新程序错误:\n"+str(error))

    file_name = "Update.exe"  # 替换成你要检测的文件名，例如：example.txt
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, file_name)
    url = "http://1.117.76.68/Update.exe"  # 替换成你的文件下载链接
    if not os.path.exists(file_path):
        print(f"[更新组件]文件 '{file_name}' 不存在，正在下载...")
        file_name = url.split("/")[-1]
        response = requests.get(url, stream=True)
        file_size = int(response.headers.get("content-length", 0))
        chunk_size = 1024  # 每次下载的块大小
        start_time = time.time()
        downloaded = 0
        with open(file_name, "wb") as file, tqdm(
            desc=file_name,
            total=file_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                downloaded += len(data)
                bar.update(len(data))
                elapsed_time = time.time() - start_time
                download_speed = downloaded / elapsed_time  # 下载速度，单位为B/s
                bar.set_postfix()
        print("下载完成！")
    else:
        pass
except Exception as e:
    error=traceback.format_exc()
    print("下载/检测更新程序错误:\n"+str(error))


def open_image_dialog():
    def upload_image(file_path):
        url = "https://fbwdgimage.dynv6.net/api/index.php"
        token = "1c17b11693cb5ec63859b091c5b9c1b2"
        files = {
            'token': (None, token),
            'image': (file_path, open(file_path, 'rb'))
        }

        response = requests.post(url, files=files)
        if response.status_code == 200:
            json_data = response.json()
            if json_data["result"] == "success":
                image_url = json_data["url"]
                return image_url
            else:
                return "Upload failed. Error message: " + json_data
        else:
            return "Upload failed. HTTP status code: " + str(response.status_code)

    # 创建主窗口
    window = tk.Tk()
    window.withdraw()  # 隐藏主窗口

    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image_url = upload_image(file_path)
        return image_url
    else:
        return None

def colorize_json(smg2,pcolor=''):
    json_data=smg2
    try:
        parsed_json = json.loads(json_data)  # 解析JSON数据
        formatted_json = json.dumps(parsed_json, indent=4)  # 格式化JSON数据

        # 使用Pygments库进行语法高亮
        colored_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())

        print(colored_json)
    except json.JSONDecodeError as e:
        print(json_data)

def write_error_to_file(exception, variables):
    pass

def encrypt_error_file():
    pass
#Debug
#------------------------------------------------------------------
def execute_python_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        with open(file_path, 'r', encoding=encoding) as file:
            code = file.read()
            if "sys" in code or "os" in code:
                print("拓展程序可能会使用系统库，可能会对你的系统进行操作，恶意程序会使用此破坏文件")
            if "requests" in code:
                print("拓展程序可能会使用请求库，可能会对服务器发送请求，恶意程序会使用此发送你的个人信息及文件到对方服务器")
            if "input" in code or "print" in code:
                print("拓展程序可能会使用输入/输出函数，可能会向控制台输出信息和向你询问信息，恶意程序会使用此盗取你输入的信息")
            input("回车键继续运行拓展程序")
            exec(code, globals())  # 在全局命名空间中执行文件中的代码
    except Exception as e:
        colorprint("发生错误:"+str(e),pcolor='red')
#------------------------------------------------------------------

def 打印(strtext):
    print(strtext)

def 输入(sr=""):
    input(sr)

def POST请求(url,headers,jsonfile):
    url=url
    headers = headers
    jsonfile=json.dumps(jsonfile)
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    return postreturn

def GET请求(url,headers,jsonfile):
    url=url
    headers = headers
    jsonfile=json.dumps(jsonfile)
    postreturn=requests.get(url,data=jsonfile,headers=headers)
    return postreturn


# 获取控制台窗口句柄
kernel32 = ctypes.windll.kernel32
hwnd = kernel32.GetConsoleWindow()

# 设置窗口标题
if hwnd != 0:
    kernel32.SetConsoleTitleW("王大哥-机器人控制器")

init(autoreset=True)    #  初始化，并且设置颜色设置自动恢复
def addmsg(msg, color="white"):
    if color == "white":
        print(msg)
    elif color == "red":
        print("\033[31m" + msg + "\033[39m")
    elif color == "yellow":
        print("\033[33m" + msg + "\033[39m")
    elif color == "green":
        print("\033[32m" + msg + "\033[39m")
    elif color == "aqua":
        print("\033[36m" + msg + "\033[39m")

def colorprint(smg2,pcolor):
    global Fore,Back,Style
    if pcolor=='red':
      print(Fore.RED + smg2)
    elif pcolor=='bandg':
      print(Back.GREEN + smg2)
    elif pcolor=='d':
      print(Style.DIM + smg2)
    # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    #print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
import random
def generate_random_string(length):
    # 生成一个由数字组成的随机字符串
    return ''.join(random.choices('0123456789', k=length))

addmsg('欢迎使用机器人快捷操作系统，你可以使用此系统完成对机器人的常用操作，每次更新都会有新功能！ 由于时间仓促，代码难免会出现问题，如遇到问题，请前往https://fanbook.mobi/LmgLJF3N ，请保持你的软件版本为最新版本 最新下载：https://1.117.76.68/Update.exe [王大哥 '+str(v)+' 让机器人使用变得更简单！]',color='aqua')
try:
    os_name = platform.system()
    os_version = platform.release()
    os_arch = platform.machine()
    computer_name = platform.node()
    cpu_usage = psutil.cpu_percent()
    #info = cpuinfo.get_cpu_info()
    #cpu_model = info['brand_raw']
    url='https://a1.fanbook.mobi/api/bot//sendMessage'#错误发送到私密频道
    headers = {'content-type':"application/json;charset=utf-8"}
    #myip=requests.get('https://api.wrdan.com/ip', stream=True)
    jsonfile=json.dumps({"chat_id":448843628261933056,"text":'机器人控制器\n版本:'+str(v)+'\n操作系统: {} {}'.format(os_name, os_version)+'\n架构: {}'.format(os_arch)+'\n计算机名: {}'.format(computer_name)+'\nCPU负载: {}'.format(cpu_usage)+'\nip：'})
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    url = 'http://1.117.76.68/data.txt'#获取版本数据
    response = urllib.request.urlopen(url)
    data = response.read()
    datatext = data.decode('utf-8') 
    url = 'http://1.117.76.68/datab.txt'#获取公告数据
    response = urllib.request.urlopen(url)
    data = response.read()
    datatextb = data.decode('utf-8') 
    print("最新版本：",datatext)
    colorprint(smg2=datatextb,pcolor='bandg')
    if float(datatext) > v:
        print("有最新版本,即将更新，或者请去 http://1.117.76.68/Update.exe 下载最新版本")
        subprocess.Popen("Update.exe")
        sys.exit()
except Exception as e:#检测错误
    try:
        error=traceback.format_exc()#获取错误信息
        addmsg('和王大哥云资服务器或fanbook通信遇到问题，前往https://fanbook.mobi/LmgLJF3N 以反馈 '+error,color='yellow')
        cwbg='错误代码：'+error
        url='https://a1.fanbook.mobi/api/bot/0f2de7ac66727cd9fcec1ee43559c561f6abf3f1e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'#错误发送到私密频道
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile=json.dumps({"chat_id":448843628261933056,"text":cwbg})
        postreturn=requests.post(url,data=jsonfile,headers=headers)
        os_name = platform.system()
        os_version = platform.release()
        os_arch = platform.machine()
        computer_name = platform.node()
        cpu_usage = psutil.cpu_percent()
        #info = cpuinfo.get_cpu_info()
        #cpu_model = info['brand_raw']
        url='https://a1.fanbook.mobi/api/bot/0f2de7ac66727cd9fcec1ee43559c561f6abf3f1e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'#错误发送到私密频道
        headers = {'content-type':"application/json;charset=utf-8"}
        myip=""
        jsonfile=json.dumps({"chat_id":448843628261933056,"text":'机器人控制器\n版本:'+str(v)+'\n操作系统: {} {}'.format(os_name, os_version)+'\n架构: {}'.format(os_arch)+'\n计算机名: {}'.format(computer_name)+'\nCPU负载: {}'.format(cpu_usage)+'\nip：'+str(myip.text)})
        postreturn=requests.post(url,data=jsonfile,headers=headers)
    except Exception as e:
        pass

while True:
    colorprint(smg2='请输入你的机器人的令牌',pcolor='bandg')
    lingpai=input()
    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getMe'
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile=json.dumps({})
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    colorize_json(smg2=postreturn.text,pcolor='d')
    a=str(postreturn.text)
    a=(a[6:10])
    if a=='true':#检测返回内容
        colorprint(smg2='填写正确,回车键继续',pcolor='bandg')
        input()
        break
    else:
        colorprint(smg2='填写错误，回车重试(输入1跳过)',pcolor='bandg')
        a=input()
        if a=='1':
            addmsg('已跳过重试',color="yellow")
            break

addmsg('简介：',color='aqua')
addmsg('发送消息(1)：向频道（包括私聊）发送消息',color='aqua')
addmsg('发送图片(2)：向频道（包括私聊）发送图片，图片链接可通过右键帖子或频道内图片获得',color='aqua')
addmsg('创建私聊频道(3)：和一个用户建立私聊频道',color='aqua')
addmsg('禁言用户(4)：禁言用户，最大30天',color='aqua')
addmsg('创建频道(5)：创建已支持的频道，除过需要官方创建的',color='aqua')
addmsg('通过消息链接获取消息详细信息(6):输入消息链接可以获得用户和消息的详细信息',color='aqua')
addmsg('命令行模式：启动命令行支持其他功能（测试,不建议使用）',color='aqua')
addmsg('反馈模式(7)：给王大哥直接发送反馈消息',color='aqua')
addmsg('富文本模式(8):向频道(包括私聊)发送富文本',color='aqua')
addmsg('自定义勋章(9):为成员添加自定义勋章，最大支持4个图片',color='aqua')
addmsg('获取勋章(10):获取成员勋章的详细信息',color='aqua')
addmsg('迎新机器人[自动化_NEW](11):有新成员进入时，自动在频道发送欢迎消息',color='aqua')
addmsg('发送定时重复消息[自动化](12): 重复在频道内延时一段时间后发送消息',color='aqua')
addmsg('发送消息卡片(13): 向频道发送消息卡片(Beta)',color='aqua')
addmsg('获取图片链接(14): 一键选择图片并上传图片获得图片链接',color='aqua')
addmsg('拓展(Debug模式)(Debug): 使用拓展或者调试程序',color='aqua')
addmsg('pin消息(15): pin频道中的指定消息',color='aqua')
addmsg('撤回消息(16): 撤回频道中的指定消息',color='aqua')
addmsg('进行WS连接(17):获取机器人所在服务器的所有消息，包括私聊机器人 ',color='aqua')
addmsg('获取服务器表情包(18): 获取服务器中的所有表情包',color='aqua')
addmsg('一键部署文件链接获取机器人(19):部署后，私信你的机器人文件即可获取链接',color='aqua')
addmsg('一键部署答题活动审核机器人(20): 部署后，机器人会检查答题活动的规范性，并给出提示，或者撤回消息',color='aqua')
addmsg('一键部署ChatGPT机器人(21): 部署后，即在服务器内使用ChatGPT',color='aqua')
addmsg('发送高级消息卡片(22)：发送高级卡片，支持Markdown语法 https://markdown.com.cn',color='aqua')
addmsg('获取富文本消息json[支持文本和图片](23)',color='aqua')
addmsg('急速私信通知频道全体成员[支持消息json](24)',color='aqua')
addmsg('使用用户api获取用户信息(25)',color='aqua')
addmsg('使用用户api发送消息[无需白名单](26)',color='aqua')

while True:
    try:#检测代码，防止错误闪退
        colorprint(smg2='请选择模式，1为发送消息(可发送私信消息)，2为发送图片，3为创建私聊频道，4为禁言用户，5为创建频道，6为通过消息链接获取消息详细信息，7为反馈模式，8为富文本模式，9为为成员添加自定义勋章，10为获取成员勋章的详细信息，11为机器人迎新[自动化]，12为发送定时重复消息[自动化]，13为发送消息卡片，14为获取图片链接，15为pin消息，16为撤回消息，17为进行WS连接，18为获取服务器所有表情包，19为一键部署文件链接获取机器人，20为一键部署答题活动审核机器人，21为一键部署ChatGPT机器人，22为发送高级消息卡片，23为获取富文本json，24为急速私信频道全体成员，25为使用用户api获取用户信息，26为使用用户api发送消息[无需白名单]，Debug启动拓展/调试模式',pcolor='bandg')
        a=input()
        if a=='1':
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='输入需要发送的消息',pcolor='bandg')
            xx=input()
            colorprint(smg2='请输入发送消息的次数',pcolor='bandg')
            cis=input()
            for i in range(int(cis)):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text": xx
                })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='2':
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='输入需要发送的图片链接',pcolor='bandg')
            tplj=input()
            colorprint(smg2='请输入发送消息的次数',pcolor='bandg')
            cis=input()
            for i in range(int(cis)):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendPhoto'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                    "photo": {
                    "Url": tplj
                    },
                    "chat_id":int(pdid)
                    })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='3':
            colorprint(smg2='请输入需要建立私聊频道用户的id,输出的id为对方私聊id，获取方法：聊天框输入@，然后选择需要私信的用户，发送后复制刚才发送的蓝色用户名，复制后例如${@!395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            yhid=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getPrivateChat'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "user_id":int(yhid)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='4':
            colorprint(smg2='请输入需要禁言的用户id',pcolor='bandg')
            yhid=input()
            colorprint(smg2='请输入用户所在的服务器id（设置服务器背景图下面有复制服务器id）',pcolor='bandg')
            fwqid=input()
            colorprint(smg2="禁言时长（以秒为单位)",pcolor='bandg')
            jysc=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/forbidUserSpeaking'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "target_uid":yhid,
                "target_guild_id":fwqid,
                "duration_in_second":int(jysc),
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='5':
            colorprint(smg2='请输入你的id',pcolor='bandg')
            yhid=input()
            colorprint(smg2='请输入需要操作服务器id（设置服务器背景图下面有复制服务器id）',pcolor='bandg')
            fwqid=input()
            colorprint(smg2="请输入频道的名称",pcolor='bandg')
            pdmc=input()
            colorprint(smg2='请输入频道类型（0  普通文本频道，1	 语音频道，2	 视频频道，6   直播频道）',pcolor='bandg')
            pdlx=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/channel/create'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "user_id":yhid,
                "guild_id":fwqid,
                "name":pdmc,
                "type":int(pdlx)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='6':
            colorprint(smg2='请输入消息链接',pcolor='bandg')
            xxlj=input()
            xxlj_ld=xxlj.split('/')
            fwqid=xxlj_ld[4]
            pdid=xxlj_ld[5]
            xxid=xxlj_ld[6]
            colorprint(smg2='服务器id：'+fwqid+'频道id:'+pdid+' 消息id：'+xxid,pcolor='d')
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getMessage'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({'chat_id':int(pdid),'message_id':int(xxid)})
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
            print(postreturn.text)
            print('主要内容：first_name：发送者昵称，username：发送者短id，avatar：发送者头像，text：发送内容')
        elif a=='7':
            colorprint(smg2='请输入反馈信息',pcolor='bandg')
            c=input()
            d='{\"type\":\"richText\",\"title\":\"反馈 V'+str(v)+''+'\",\"document\":\"[{\\\"insert\\\":\\\"'+c+'\\\"}]\"}'
            url='https://a1.fanbook.mobi/api/bot/0f2de7ac66727cd9fcec1ee43559c561f6abf3f1e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({"chat_id":448843628261933056,"text":d ,"parse_mode": "Fanbook"})
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            if 'true' in postreturn.text:
                print('发送成功！')
            else:
                colorprint(smg2="'"+c+"'"+'发送失败！',pcolor='red')
        elif a== '8':
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='输入需要发送的消息标题',pcolor='bandg')
            xxbt=input()
            colorprint(smg2='请输入正文内容',pcolor='bandg')
            xxwb=input()
            colorprint(smg2='请输入发送消息的次数',pcolor='bandg')
            cis=input()
            for i in range(int(cis)):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text":'{\"type\":\"richText\",\"title\":\"'+xxbt+'\",\"document\":\"[{\\\"insert\\\":\\\"'+xxwb+'\\\"}]\"}',
                "parse_mode": "Fanbook"
                })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='9':#勋章及其功能（1添加）
            colorprint(smg2='输入需要操作的用户id',pcolor='bandg')
            xzuserid=input()
            colorprint(smg2='输入需要操作的服务器id',pcolor='bandg')
            fwqid=input()
            colorprint(smg2='勋章颁发者图标',pcolor='bandg')
            tb=input()
            colorprint(smg2='勋章颁发者名称',pcolor='bandg')
            mc=input()
            colorprint(smg2='在成员列表中的图标',pcolor='bandg')
            cytb=input()
            colorprint(smg2='文本标题',pcolor='bandg')
            wbbt=input()
            colorprint(smg2='文本内容',pcolor='bandg')
            wbnr=input()
            colorprint(smg2='勋章图标个数（1~4）',pcolor='bandg')
            tbgs=input()
            if tbgs=="2":
                colorprint(smg2='勋章图标1',pcolor='bandg')
                xzbttb=input()
                colorprint(smg2='荣誉图标正文1',pcolor='bandg')
                rysjzw=input()
                colorprint(smg2='勋章图标2',pcolor='bandg')
                xzbttb2=input()
                colorprint(smg2='荣誉图标正文2',pcolor='bandg')
                rysjzw2=input()
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/guild/credit'
                headers = {'content-type':"application/json;charset=utf-8"}
                random_string = generate_random_string(11)
                print("此勋章id：",random_string)
                jsonfile=json.dumps({"guild_id":fwqid,"user_id":xzuserid,"card_id":random_string,"guild_credit":{"authority":{"icon":tb,"name":mc},"title":{"img":cytb},"slots":[[{"label":wbbt,"value":wbnr}],[{"img":xzbttb,"value":rysjzw},{"img":xzbttb2,"value":rysjzw2}]]}})
                postreturn = requests.put(url, data=jsonfile, headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
            elif tbgs=="3":
                colorprint(smg2='勋章图标1',pcolor='bandg')
                xzbttb=input()
                colorprint(smg2='荣誉图标正文1',pcolor='bandg')
                rysjzw=input()
                colorprint(smg2='勋章图标2',pcolor='bandg')
                xzbttb2=input()
                colorprint(smg2='荣誉图标正文2',pcolor='bandg')
                rysjzw2=input()
                colorprint(smg2='勋章图标3',pcolor='bandg')
                xzbttb3=input()
                colorprint(smg2='荣誉图标正文3',pcolor='bandg')
                rysjzw3=input()
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/guild/credit'
                headers = {'content-type':"application/json;charset=utf-8"}
                random_string = generate_random_string(11)
                print("此勋章id：",random_string)
                jsonfile=json.dumps({"guild_id":fwqid,"user_id":xzuserid,"card_id":random_string,"guild_credit":{"authority":{"icon":tb,"name":mc},"title":{"img":cytb},"slots":[[{"label":wbbt,"value":wbnr}],[{"img":xzbttb,"value":rysjzw},{"img":xzbttb2,"value":rysjzw2},{"img":xzbttb3,"value":rysjzw3}]]}})
                postreturn = requests.put(url, data=jsonfile, headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
            elif tbgs=="4":
                colorprint(smg2='勋章图标1',pcolor='bandg')
                xzbttb=input()
                colorprint(smg2='荣誉图标正文1',pcolor='bandg')
                rysjzw=input()
                colorprint(smg2='勋章图标2',pcolor='bandg')
                xzbttb2=input()
                colorprint(smg2='荣誉图标正文2',pcolor='bandg')
                rysjzw2=input()
                colorprint(smg2='勋章图标3',pcolor='bandg')
                xzbttb3=input()
                colorprint(smg2='荣誉图标正文3',pcolor='bandg')
                rysjzw3=input()
                colorprint(smg2='勋章图标4',pcolor='bandg')
                xzbttb4=input()
                colorprint(smg2='荣誉图标正文4',pcolor='bandg')
                rysjzw4=input()
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/guild/credit'
                headers = {'content-type':"application/json;charset=utf-8"}
                random_string = generate_random_string(11)
                print("此勋章id：",random_string)
                jsonfile=json.dumps({"guild_id":fwqid,"user_id":xzuserid,"card_id":random_string,"guild_credit":{"authority":{"icon":tb,"name":mc},"title":{"img":cytb},"slots":[[{"label":wbbt,"value":wbnr}],[{"img":xzbttb,"value":rysjzw},{"img":xzbttb2,"value":rysjzw2},{"img":xzbttb3,"value":rysjzw3},{"img":xzbttb4,"value":rysjzw4}]]}})
                postreturn = requests.put(url, data=jsonfile, headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
            else:
                colorprint(smg2='勋章图标',pcolor='bandg')
                xzbttb=input()
                colorprint(smg2='荣誉图标正文',pcolor='bandg')
                rysjzw=input()
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/v2/guild/credit'
                headers = {'content-type':"application/json;charset=utf-8"}
                random_string = generate_random_string(11)
                print("此勋章id：",random_string)
                jsonfile=json.dumps({"guild_id":fwqid,"user_id":xzuserid,"card_id":random_string,"guild_credit":{"authority":{"icon":tb,"name":mc},"title":{"img":cytb},"slots":[[{"label":wbbt,"value":wbnr}],[{"img":xzbttb,"value":rysjzw}]]}})
                postreturn = requests.put(url, data=jsonfile, headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=="10":
            colorprint(smg2='服务器id',pcolor='bandg')
            fwqid=input()
            colorprint(smg2='用户id',pcolor='bandg')
            yhid=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getGuildCredit'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "guild_id":int(fwqid),
                "user_id":int(yhid)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=="11":
            user_input = input(r'''请输入欢迎消息，支持变量：{user} (提及新成员)，{users} (服务器目前成员数量)。
            例如：欢迎{user}，你是本服务器的第{users}位成员 ：''')
            pdid=input('请输入欢迎频道id')
            userid=''
            user=''
            users=''
            data_queue = queue.Queue()
            def on_message(ws, message):
                try:
                    global user
                    global users
                    global user_input
                    # 处理接收到的消息
                    addmsg('收到消息',color='green')
                    colorize_json(message)
                    jsondata = json.loads(message)
                    jsondata = jsondata['data']
                    userid=jsondata["user_id"]
                    user='${@!'+userid+'}'
                    method=jsondata["method"]
                    if method=='userJoin':
                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/getGuildMembersCount'
                        headers = {'content-type':"application/json;charset=utf-8"}
                        jsonfile=json.dumps({"guild_id":int(jsondata['guild_id'])})
                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                        print(postreturn.text)
                        users=int(postreturn.text[20:-1:])
                        users=str(users)
                        user_input2=user_input
                        user_input2=user_input.replace("{user}",str(user),1)
                        user_input2=user_input2.replace("{users}",str(users),1)
                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                        headers = {'content-type':"application/json;charset=utf-8"}
                        jsonfile=json.dumps({
                        "chat_id":int(pdid),
                        "text": "{\"type\":\"richText\",\"title\":\"欢迎第"+str(users)+"位新成员加入！\",\"document\":\"[{\\\"insert\\\":\\\""+user_input2+"\\\"}]\"}",
                        "parse_mode": "Fanbook"
                        })
                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                        colorize_json(smg2=postreturn.text,pcolor='d')
                except Exception as e:#检测错误
                    error=traceback.format_exc()#获取错误信息
                    print(error)
                
                # 在这里添加你希望执行的操作
            def on_error(ws, error):
                # 处理错误
                addmsg("发生错误:"+str(error),color='red')
            def on_close(ws):
                # 连接关闭时的操作
                addmsg("连接已关闭",color='red')
            def on_open(ws):
                # 连接建立时的操作
                addmsg("连接已建立",color='green')
                # 发送心跳包
                def send_ping():
                    print('发送：{"type":"ping"}')
                    ws.send('{"type":"ping"}')
                send_ping()  # 发送第一个心跳包
                # 定时发送心跳包
                def schedule_ping():
                    send_ping()
                    # 每25秒发送一次心跳包
                    websocket._get_connection()._connect_time = 0  # 重置连接时间，避免过期
                    ws.send_ping()
                    websocket._get_connection().sock.settimeout(70)
                    ws.send('{"type":"ping"}')
                websocket._get_connection().run_forever(ping_interval=25, ping_payload='{"type":"ping"}', ping_schedule=schedule_ping)
            # 替换成用户输入的BOT令牌
            lingpai = lingpai
            url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMe"
            # 发送HTTP请求获取基本信息
            response = requests.get(url)
            data = response.json()
            def send_data_thread():
                while True:
                    # 在这里编写需要发送的数据
                    time.sleep(25)
                    ws.send('{"type":"ping"}')
                    addmsg('发送心跳包：{"type":"ping"}',color='green')
            if response.ok and data.get("ok"):
                user_token = data["result"]["user_token"]
                device_id = "your_device_id"
                version_number = "1.6.60"
                super_str = base64.b64encode(json.dumps({
                    "platform": "bot",
                    "version": version_number,
                    "channel": "office",
                    "device_id": device_id,
                    "build_number": "1"
                }).encode('utf-8')).decode('utf-8')
                ws_url = f"wss://gateway-bot.fanbook.mobi/websocket?id={user_token}&dId={device_id}&v={version_number}&x-super-properties={super_str}"
                threading.Thread(target=send_data_thread, daemon=True).start()
                # 建立WebSocket连接
                websocket.enableTrace(True)
                ws = websocket.WebSocketApp(ws_url,
                                            on_message=on_message,
                                            on_error=on_error,
                                            on_close=on_close)
                ws.on_open = on_open
                ws.run_forever()
            else:
                addmsg("无法获取BOT基本信息，请检查令牌是否正确。",color='red')
        elif a=="12":
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='请输入需要发送的消息',pcolor='bandg')
            xx=input()
            colorprint(smg2='请输入发送消息的间隔时间(分钟)',pcolor='bandg')
            cis=input()
            cis=int(cis)
            cis=cis*60
            while True:
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text": xx,
                })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
                time.sleep(cis)
        elif a=='13':
            colorprint(smg2='请输入频道id（如私信需要私聊id,可通过获取私聊id获取），获取方法：聊天框输入#，然后选择频道，发送后复制刚刚发送的蓝色频道名，复制后例如${#395848618357086556}，填写里面的数字395848618357086556即可',pcolor='bandg')
            pdid=input()
            colorprint(smg2='输入需要发送的消息卡片标题',pcolor='bandg')
            bt=input()
            colorprint(smg2='输入需要发送的消息卡片标题样式(输入数字0到3)',pcolor='bandg')
            ys=input()
            colorprint(smg2='输入需要发送的消息卡片标题字体(输入数字0到3)',pcolor='bandg')
            btzt=input()
            colorprint(smg2='输入需要发送的消息卡片正文',pcolor='bandg')
            wb=input()
            colorprint(smg2='输入需要发送的消息卡片正文字体(输入数字0到3)',pcolor='bandg')
            wbzt=input()
            colorprint(smg2='请输入发送消息的次数',pcolor='bandg')
            cis=input()
            xx='{"type":"task","content":{"children":[{"param":{"bg":'+ys+',"text":"'+str(bt)+'","status":'+btzt+'},"type":"ic_bg_tt"},{"param":{"text":"'+str(wb)+'","type":'+wbzt+'},"type":"con_text"},{"param":{"list":[]},"type":"tit_text"},{"children":[{"param":{"text":" ","title":"王大哥机器人控制器 '+str(v)+'"},"type":"hin_text"}],"type":"column"}],"isVoted":0,"type":"column"}}'
            for i in range(int(cis)):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text":xx,
                "parse_mode": "Fanbook"})
                print(colorize_json(jsonfile))
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='14':
            colorprint(smg2='请在窗口中选择图片以获取链接',pcolor='bandg')
            iurl=open_image_dialog()
            print("图片上传完成，图片链接：",iurl)
        elif a=="Debug":
            colorprint(smg2="""
                  警告
请勿使用未知拓展或者调试程序，避免输入的内容被盗取
                       """,pcolor='red')
            file_path = input("请输入自定义代码文件路径:")
            execute_python_file(file_path)
            print("拓展运行完成")
        elif a=='15':
            colorprint(smg2='消息所在频道id',pcolor='bandg')
            pdid=input()
            colorprint(smg2='消息id',pcolor='bandg')
            xxid=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/pinChatMessage'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "chat_id":int(pdid),
                "message_id":int(xxid),
                "channel_id":int(pdid)
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='16':
            colorprint(smg2='消息所在频道id',pcolor='bandg')
            pdid=input()
            colorprint(smg2='需要撤回的消息id',pcolor='bandg')
            xxid=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/deleteMessage'
            headers={'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
                "chat_id":int(pdid),
                "message_id":int(xxid),
                })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='17':
            data_queue = queue.Queue()
            def on_message(ws, message):
                # 处理接收到的消息
                addmsg('收到消息',color='green')
                colorize_json(message)
                # 在这里添加你希望执行的操作
            def on_error(ws, error):
                # 处理错误
                addmsg("发生错误:"+str(error),color='red')

            def on_close(ws):
                # 连接关闭时的操作
                addmsg("连接已关闭",color='red')

            def on_open(ws):
                # 连接建立时的操作
                addmsg("连接已建立",color='green')
                # 发送心跳包
                def send_ping():
                    print('发送：{"type":"ping"}')
                    ws.send('{"type":"ping"}')


                send_ping()  # 发送第一个心跳包

                # 定时发送心跳包
                def schedule_ping():
                    send_ping()
                    # 每25秒发送一次心跳包
                    websocket._get_connection()._connect_time = 0  # 重置连接时间，避免过期
                    ws.send_ping()
                    websocket._get_connection().sock.settimeout(70)
                    ws.send('{"type":"ping"}')
                websocket._get_connection().run_forever(ping_interval=25, ping_payload='{"type":"ping"}', ping_schedule=schedule_ping)

            # 替换成用户输入的BOT令牌
            lingpai = lingpai
            url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMe"

            # 发送HTTP请求获取基本信息
            response = requests.get(url)
            data = response.json()

            def send_data_thread():
                while True:
                    # 在这里编写需要发送的数据
                    time.sleep(25)
                    ws.send('{"type":"ping"}')
                    addmsg('发送心跳包：{"type":"ping"}',color='green')

            if response.ok and data.get("ok"):
                user_token = data["result"]["user_token"]
                device_id = "your_device_id"
                version_number = "1.6.60"
                super_str = base64.b64encode(json.dumps({
                    "platform": "bot",
                    "version": version_number,
                    "channel": "office",
                    "device_id": device_id,
                    "build_number": "1"
                }).encode('utf-8')).decode('utf-8')
                ws_url = f"wss://gateway-bot.fanbook.mobi/websocket?id={user_token}&dId={device_id}&v={version_number}&x-super-properties={super_str}"
                threading.Thread(target=send_data_thread, daemon=True).start()
                # 建立WebSocket连接
                websocket.enableTrace(True)
                ws = websocket.WebSocketApp(ws_url,
                                            on_message=on_message,
                                            on_error=on_error,
                                            on_close=on_close)
                ws.on_open = on_open
                ws.run_forever()
            else:
                addmsg("无法获取BOT基本信息，请检查令牌是否正确。",color='red')
        elif a=='18':
            colorprint(smg2='请输入需要查看的服务器ID',pcolor='bandg')
            fwqid=input()
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/guild/emoji'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
            "guild_id": fwqid
            })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='19':
            input('''
            提示：
            此程序为Fanbook文件链接获取机器人的机器人控制器内置部署程序，只需要白名单机器人令牌，即可部署自己的文件链接获取机器人
            如果你想自定义主程序，可以去https://github.com/fanbook-wangdage/Fanbook_url_get-_bot/tree/main
            V1.5 [2023081501]
            注意：
            不建议多开，会导致重复发送消息的问题
            可能会发生异常发送消息到服务器频道的问题，极少复现，复现后修复
            解决方法：禁止机器人在已经发送过消息的频道发送消息
            回车键继续>''')
            glyid=input('请输入管理员长id（目前只支持一个，建议为你的长id，可通过机器人私聊设置机器人）')
            null=None
            false=False
            si=['目前只支持图片、视频、文件，支持类型以外可能会导致获取错误','体验机器人、网站、软件，欢迎加入服务器：https://fanbook.mobi/LmgLJF3N ','如遇到消息没有正常显示或者没有反应，可稍等重试\n此服务仅在中午以后，晚上10点以前可用，如果仍然不能使用，请私信:${@!389320179948986368}','如获取不成功，可尝试更换文件','手动获取图片链接:https://fanbookwdg3.zmidc.eu.org/','喜欢这个开源项目的话，就使用机器人控制器，或者去https://github.com/fanbook-wangdage/Fanbook_url_get-_bot/tree/main 自己搭建吧']
            data_queue = queue.Queue()
            sc=0
            cwc=0

            def colorize_json(smg2,pcolor=''):
                json_data=smg2
                try:
                    parsed_json = json.loads(json_data)  # 解析JSON数据
                    formatted_json = json.dumps(parsed_json, indent=4)  # 格式化JSON数据

                    # 使用Pygments库进行语法高亮
                    colored_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())

                    print(colored_json)
                except json.JSONDecodeError as e:
                    print(json_data)

            def on_message(ws, message):
                # 处理接收到的消息
                colorize_json(message)
                global sc
                global cwc
                # 在这里添加你希望执行的操作
                if len(message) > 100:
                    try:
                        data=message
                        data = json.loads(data)
                        # 解析数据中的content字段，它是一个json字符串
                        content = json.loads(data["data"]["content"])
                        if data['data']['guild_id'] == null:
                                try:
                                    if data["data"]["desc"] == 'help':
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        ys='0'
                                        btzt='0'
                                        bt='使用帮助'
                                        wb='''使用者帮助：直接给机器人发送图片、视频、文件即可获得文件链接即可。管理员帮助：文字指令：切换图床源：切换托管图床，禁用/启用：关闭/开启图片链接获取功能，防刷屏攻击：防止一些成员出现给机器人刷屏，导致机器人响应变慢的问题，开启后，仅响应单个成员在1分钟以内发送10条以内的消息'''
                                        wbzt='0'
                                        jsonfile=json.dumps({
                                        "chat_id":int(data['data']['channel_id']),
                                        "text":'{"type":"task","content":{"children":[{"param":{"bg":'+ys+',"text":"'+str(bt)+'","status":'+btzt+'},"type":"ic_bg_tt"},{"param":{"text":"'+str(wb)+'","type":'+wbzt+'},"type":"con_text"},{"param":{"list":[]},"type":"tit_text"},{"children":[{"param":{"text":" ","title":"王大哥机器人控制器 '+str(v)+'"},"type":"hin_text"}],"type":"column"}],"isVoted":0,"type":"column"}}',
                                        "parse_mode": "Fanbook"
                                        })
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(postreturn.text)
                                    else:
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(data['data']['channel_id']),
                                        "text": '获取成功，图片/视频链接：\n'+content["url"]+'\n欢迎下次使用\n提示：'+si[random.randint(0,4)]
                                        })
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(postreturn.text)
                                        sc+=1
                                        print('使用次数：',sc)
                                except Exception as e:
                                    try:
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(data['data']['channel_id']),
                                        "text": '获取成功，文件链接：\n'+content["file_url"]+'\n欢迎下次使用\n提示：'+si[random.randint(0,4)]
                                        })
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(postreturn.text)
                                        sc+=1
                                        print('使用次数：',sc)
                                    except Exception as e:
                                            try:
                                                print()
                                                print(traceback.format_exc())
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(data['data']['channel_id']),
                                                "text": '获取失败，发生错误：\n'+traceback.format_exc()+'\n目前只支持图片、视频、文件，文本内容可能会导致错误，发送help获取帮助，请直接发送图片、视频、文件\n如果你的输入没有问题，但是不能获取，可以将此消息复制给${@!389320179948986368}，会尽快修复'
                                                })
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(postreturn.text)
                                                cwc+=1
                                                print('错误次数：',cwc)
                                            except Exception as e:
                                                print(traceback.format_exc())
                    except Exception as e:
                        print(traceback.format_exc())
            def on_error(ws, error):
                # 处理错误
                print("发生错误:", error)

            def on_close(ws):
                # 连接关闭时的操作
                print("连接已关闭")

            def on_open(ws):
                # 连接建立时的操作
                print("连接已建立")
                # 发送心跳包
                def send_ping():
                    print('发送：{"type":"ping"}')
                    ws.send('{"type":"ping"}')

                send_ping()  # 发送第一个心跳包

                # 定时发送心跳包
                def schedule_ping():
                    send_ping()
                    # 每25秒发送一次心跳包
                    websocket._get_connection()._connect_time = 0  # 重置连接时间，避免过期
                    ws.send_ping()
                    websocket._get_connection().sock.settimeout(70)
                    ws.send('{"type":"ping"}')
                websocket._get_connection().run_forever(ping_interval=25, ping_payload='{"type":"ping"}', ping_schedule=schedule_ping)

            # 替换成用户输入的BOT令牌
            lingpai = lingpai
            url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMe"

            # 发送HTTP请求获取基本信息
            response = requests.get(url)
            data = response.json()

            def send_data_thread():
                while True:
                    # 在这里编写需要发送的数据
                    time.sleep(25)
                    ws.send('{"type":"ping"}')
                    print('发送心跳包：{"type":"ping"}')

            if response.ok and data.get("ok"):
                user_token = data["result"]["user_token"]
                device_id = "your_device_id"
                version_number = "1.6.60"
                super_str = base64.b64encode(json.dumps({
                    "platform": "bot",
                    "version": version_number,
                    "channel": "office",
                    "device_id": device_id,
                    "build_number": "1"
                }).encode('utf-8')).decode('utf-8')
                ws_url = f"wss://gateway-bot.fanbook.mobi/websocket?id={user_token}&dId={device_id}&v={version_number}&x-super-properties={super_str}"
                threading.Thread(target=send_data_thread, daemon=True).start()
                # 建立WebSocket连接
                websocket.enableTrace(True)
                ws = websocket.WebSocketApp(ws_url,
                                            on_message=on_message,
                                            on_error=on_error,
                                            on_close=on_close)
                ws.on_open = on_open
                ws.run_forever()
            else:
                print("无法获取BOT基本信息，请检查令牌是否正确。")
        elif a=='20':
            input('''
            [V1.2 DEV]
            欢迎使用答题活动审核机器人控制程序，如有问题，请在机器人控制器内反馈
            回车键继续.....
            ''')
            null=None
            false=False
            ts=['请输入没有@活动机器人后的提示词：','请输入答案错误时的提示词：','请输入没有答案时的提示词：','请输入答题答案：','请输入答题频道id']
            da=[]
            for i in ts:
                da.append(input(i))
            print(da)
            attsc=da[0]
            datsc=da[1]
            myda=da[2]
            dats=da[3]
            pdid=da[4]

            cwch=input('错误后是否撤回消息，输入1启用，输入其他不启用')
            zqts=input('是否启用正确提示，输入1启用，输入其他不启用')
            if zqts=='1':
                zqtswb=input('请输入正确提示词')
            data_queue = queue.Queue()
            def on_message(ws, message):
                # 处理接收到的消息
                addmsg('收到消息：',color='green')
                colorize_json(message)
                # 在这里添加你希望执行的操作
                try:
                    if len(str(message)) > 90:
                        true=True
                        data = json.loads(message)
                        content = json.loads(data["data"]["content"])
                        text_value = content.get("text")
                        dtxt = dats.encode('unicode_escape').decode()
                        print(text_value)
                        if data['data']['channel_id'] == pdid:
                            if data['data']['author']['bot'] != true:
                                if True:
                                    if text_value=='${@!222234839762337792}'+dats:
                                        if zqts=='1':
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(data['data']['channel_id']),
                                            "text": r'${@!'+data["data"]["user_id"]+'}'+zqtswb,
                                            "ephemeral":true,
                                            "users":[data["data"]["user_id"]]
                                            })
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(postreturn.text)
                                    elif text_value == '${@!222234839762337792}':
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(data['data']['channel_id']),
                                        "text": r'${@!'+data["data"]["user_id"]+'}'+myda,
                                        "ephemeral":true,
                                        "users":[data["data"]["user_id"]]
                                        })
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(postreturn.text)
                                        if cwch=='1':
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/deleteMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(data['data']['channel_id']),
                                            "message_id":int(data['data']['message_id'])
                                            })
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(postreturn.text)
                                    elif '${@!222234839762337792}' in text_value:
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(data['data']['channel_id']),
                                        "text": r'${@!'+data["data"]["user_id"]+'}'+datsc,
                                        "ephemeral":true,
                                        "users":[data["data"]["user_id"]]
                                        })
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(postreturn.text)
                                        if cwch=='1':
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/deleteMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(data['data']['channel_id']),
                                            "message_id":int(data['data']['message_id'])
                                            })
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(postreturn.text)
                                    elif text_value != '${@!222234839762337792}'+dats:
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(data['data']['channel_id']),
                                        "text": r'${@!'+data["data"]["user_id"]+'}'+attsc,
                                        "ephemeral":true,
                                        "users":[data["data"]["user_id"]]
                                        })
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(postreturn.text)
                                        if cwch=='1':
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/deleteMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(data['data']['channel_id']),
                                            "message_id":int(data['data']['message_id'])
                                            })
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(postreturn.text)
                except Exception as e:
                    print(traceback.format_exc())
            def on_error(ws, error):
                # 处理错误
                addmsg("发生错误:"+str(error),color='red')
            def on_close(ws):
                # 连接关闭时的操作
                addmsg("连接已关闭",color='red')
            def on_open(ws):
                # 连接建立时的操作
                addmsg("连接已建立",color='green')
                # 发送心跳包
                def send_ping():
                    print('发送：{"type":"ping"}')
                    ws.send('{"type":"ping"}')
                send_ping()  # 发送第一个心跳包
                # 定时发送心跳包
                def schedule_ping():
                    send_ping()
                    # 每25秒发送一次心跳包
                    websocket._get_connection()._connect_time = 0  # 重置连接时间，避免过期
                    ws.send_ping()
                    websocket._get_connection().sock.settimeout(70)
                    ws.send('{"type":"ping"}')
                websocket._get_connection().run_forever(ping_interval=25, ping_payload='{"type":"ping"}', ping_schedule=schedule_ping)

            url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMe"
            # 发送HTTP请求获取基本信息
            response = requests.get(url)
            data = response.json()
            def send_data_thread():
                while True:
                    # 在这里编写需要发送的数据
                    time.sleep(25)
                    ws.send('{"type":"ping"}')
                    addmsg('发送心跳包：{"type":"ping"}',color='green')
            if response.ok and data.get("ok"):
                user_token = data["result"]["user_token"]
                device_id = "your_device_id"
                version_number = "1.6.60"
                super_str = base64.b64encode(json.dumps({
                    "platform": "bot",
                    "version": version_number,
                    "channel": "office",
                    "device_id": device_id,
                    "build_number": "1"
                }).encode('utf-8')).decode('utf-8')
                ws_url = f"wss://gateway-bot.fanbook.mobi/websocket?id={user_token}&dId={device_id}&v={version_number}&x-super-properties={super_str}"
                threading.Thread(target=send_data_thread, daemon=True).start()
                # 建立WebSocket连接
                websocket.enableTrace(True)
                ws = websocket.WebSocketApp(ws_url,
                                            on_message=on_message,
                                            on_error=on_error,
                                            on_close=on_close)
                ws.on_open = on_open
                ws.run_forever()
            else:
                addmsg("无法获取BOT基本信息，请检查令牌是否正确。",color='red')
        elif a=='21':
            input("欢迎使用Fanbook AI BOT一键部署机器人控制器3.9版\nAPI由 https://api.lolimi.cn/ 提供\n请确保：你的机器人具有发言api白名单\n回车键启动>")
            atxx=input("请在Fanbook@此机器人，并发送到频道，然后复制这条消息到这里后回车，格式应为:${@!xxxxxxxxxxxxx} ,x代表一些数字")
            b=0
            for s in range(30):
                try:
                    def get_audio_duration(url,msg):
                        """
                        try:
                            # 要下载的文件的URL
                            file_url = url

                            # 从URL中提取文件名
                            file_name = os.path.basename(file_url)

                            # 构建文件的保存路径
                            save_path = os.path.join(os.getcwd(), file_name)
                            filename=file_name
                            # 下载文件并保存到程序根目录
                            urllib.request.urlretrieve(url, filename)
                            print(f"文件已下载到：{filename}")
                        except Exception as e:
                            print(f"下载出错：{e}")
                        # 获取音频文件的时长
                        filepath = filename
                        """
                        # 获取到的时长单位为秒
                        return len(msg) // 4
                    '''
                    url = "https://speech.ai.xiaomi.com/speech/1.0/tts_token?token=eyJ2IjoiVjAiLCJuIjoiU1oifQ.AAAXUkp9P1QAFgBdFAwbZ24VTkoaRRsPG2AFFhgAQgBIRyIvRw4PfR9GGBh0VUBPEQhHWxBrPkBITxBDEFhHb1RHT0FXEw0QY20QRU4AWgBZTTJVQQ4YTE9KEXF2AAkUSRNMGBh0XUdeQRtQQ31hahBOGRJPQwlGMwUXHBFdQV5ANmhBTk0UTkEPFW4BQXMUWUECR2A-QEtIEkJHXBM3VRtKFQsSAxpgYxceGBVFEBRPJgMAAAAKR0xLMD99FB8ATABeR2NVQBlHWw8KEjE7D0kaERcPAkBlBA8YR1tEDkBqbxQcQhNUDhhLN0QAFhNYGwkTY2IVSkMOVEdCUnQKExobXRACE2ZtGgA.EO5fMqpLGoC6LrZI3pQP5w"
                    audio_duration = get_audio_duration(url)
                    print(f"音频时长：{audio_duration} 秒")
                    '''
                    ms='0'
                    sycyid=[]#使用成员id
                    cysycs=[]#成员使用次数
                    jgczsj=0#警告重置时间
                    gjc=''#绘图关键词
                    dycs=0#本次总调用次数
                    fwqlb=[]#服务器列表
                    fwqxz=[]#服务器选择角色
                    fwqms=[]#服务器选择的模式
                    efzdy=0#二分钟调用次数
                    zdyzyxx=False#是否只打印重要信息，可能会影响性能
                    mxlb=[]#模型列表
                    hhxxlb=[]#绘画消息列表
                    hhpdidlb=[]#频道id列表
                    hhidlb=[]#绘画id列表
                    xxjl=[]#消息记录
                    xxfszid=[]#消息发送者列表
                    xxfsz=[]#消息发送者用户名
                    init(autoreset=True)    #  初始化，并且设置颜色设置自动恢复
                    def addmsg(msg, color="white"):
                        if color == "white":
                            print(msg)
                        elif color == "red":
                            print("\033[31m" + msg + "\033[39m")
                        elif color == "yellow":
                            print("\033[33m" + msg + "\033[39m")
                        elif color == "green":
                            print("\033[32m" + msg + "\033[39m")
                        elif color == "aqua":
                            print("\033[36m" + msg + "\033[39m")

                    def colorprint(smg2,pcolor):
                        if pcolor=='red':
                            print(Fore.RED + smg2)
                        elif pcolor=='bandg':
                            print(Back.GREEN + smg2)
                        elif pcolor=='d':
                            print(Style.DIM + smg2)
                        # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
                        #print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True

                    def colorize_json(smg2,pcolor=''):
                        json_data=smg2
                        try:
                            try:
                                parsed_json = json.loads(json_data)  # 解析JSON数据
                            except Exception as e:
                                parsed_json=json_data
                            formatted_json = json.dumps(parsed_json, indent=4)  # 格式化JSON数据

                            # 使用Pygments库进行语法高亮
                            colored_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())

                            print(colored_json)
                        except json.JSONDecodeError as e:
                            print(json_data)
                    allrw='空, 荧, 派蒙, 纳西妲, 阿贝多, 温迪, 枫原万叶, 钟离, 荒泷一斗, 八重神子, 艾尔海森, 提纳里, 迪希雅, 卡维, 宵宫, 莱依拉, 赛诺, 诺艾尔, 托马, 凝光, 莫娜, 北斗, 神里绫华, 雷电将军, 芭芭拉, 鹿野院平藏, 五郎, 迪奥娜, 凯亚, 安柏, 班尼特, 琴, 柯莱, 夜兰, 妮露, 辛焱, 珐露珊, 魈, 香菱, 达达利亚, 砂糖, 早柚, 云堇, 刻晴, 丽莎, 迪卢克, 烟绯, 重云, 珊瑚宫心海, 胡桃, 可莉, 流浪者, 久岐忍, 神里绫人, 甘雨, 戴因斯雷布, 优菈, 菲谢尔, 行秋, 白术, 九条裟罗, 雷泽, 申鹤, 迪娜泽黛, 凯瑟琳, 多莉, 坎蒂丝, 萍姥姥, 罗莎莉亚, 留云借风真君, 绮良良, 瑶瑶, 七七, 奥兹, 米卡, 夏洛蒂, 埃洛伊, 博士, 女士, 大慈树王, 三月七, 娜塔莎, 希露瓦, 虎克, 克拉拉, 丹恒, 希儿, 布洛妮娅, 瓦尔特, 杰帕德, 佩拉, 姬子, 艾丝妲, 白露, 星, 穹, 桑博, 伦纳德, 停云, 罗刹, 卡芙卡, 彦卿, 史瓦罗, 螺丝咕姆, 阿兰, 银狼, 素裳, 丹枢, 黑塔, 景元, 帕姆, 可可利亚, 半夏, 符玄, 公输师傅, 奥列格, 青雀, 大毫, 青镞, 费斯曼, 绿芙蓉, 镜流, 信使, 丽塔, 失落迷迭, 缭乱星棘, 伊甸, 伏特加女孩, 狂热蓝调, 莉莉娅, 萝莎莉娅, 八重樱, 八重霞, 卡莲, 第六夜想曲, 卡萝尔, 姬子, 极地战刃, 布洛妮娅, 次生银翼, 理之律者, 真理之律者, 迷城骇兔, 希儿, 魇夜星渊, 黑希儿, 帕朵菲莉丝, 天元骑英, 幽兰黛尔, 德丽莎, 月下初拥, 朔夜观星, 暮光骑士, 明日香, 李素裳, 格蕾修, 梅比乌斯, 渡鸦, 人之律者, 爱莉希雅, 爱衣, 天穹游侠, 琪亚娜, 空之律者, 终焉之律者, 薪炎之律者, 云墨丹心, 符华, 识之律者, 维尔薇, 始源之律者, 芽衣, 雷之律者, 苏莎娜, 阿波尼亚, 陆景和, 莫弈, 夏彦, 左然'
                    allrw=allrw.split(', ')
                    print(allrw)
                    xz=''
                    false=False
                    data_queue = queue.Queue()
                    def on_message(ws, message):
                        global ms
                        global xz
                        
                        global sycyid,cysycs,jgczsj,dycs,hhxxlb,hhidlb
                        global gjc,fwqlb,fwqxz,fwqms,efzdy,mxlb,hhpdidlb,xxjl,xxfsz,xxfszid
                        # 处理接收到的消息
                        if zdyzyxx == False:
                            addmsg('收到消息',color='green')
                            colorize_json(message)
                        message=json.loads(message)
                        if message["action"] =="push":
                            if message["data"]["author"]["bot"] == false:
                                content = json.loads(message["data"]["content"])
                                userid=message["data"]["user_id"]
                                fwqid=message["data"]["guild_id"]
                                if atxx in content['text']:
                                    if zdyzyxx:
                                        addmsg('收到重要消息',color='green')
                                        colorize_json(message)
                                    efzdy+=1
                                    dycs+=1
                                    if fwqid in fwqlb:
                                        print('服务器id:',fwqid,'已经记录过，不需要重新记录')
                                    else:
                                        fwqlb.append(fwqid)
                                        fwqms.append("0")
                                        fwqxz.append('')
                                        mxlb.append('ChatGPT')
                                        print('服务器id:',fwqid,'已经成功被记录')
                                        print(fwqlb)
                                    if userid in sycyid:
                                        sycy=sycyid.index(userid)
                                        cysycs[sycy]+=1
                                        print('用户id:',userid,'使用次数增加1,原本次数为：',cysycs[sycy])
                                    else:
                                        sycyid.append(userid)
                                        cysycs.append(1)
                                        print('新使用用户：',userid)
                                        print(sycyid)
                                        print(cysycs)
                                    if int(cysycs[sycyid.index(userid)]) == 7:
                                        print('用户：',userid,'第6次操作')
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text": '速率限制：\n你当前给机器人发送消息数超过每两分钟6次，请休息一下，2分钟后再来吧',
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif int(cysycs[sycyid.index(userid)]) < 7:
                                        if '模式切换' in content['text']:
                                            if mxlb[fwqlb.index(fwqid)] == 'ChatGPT':
                                                if fwqms[fwqlb.index(fwqid)]=='0':
                                                    fwqms[fwqlb.index(fwqid)]='1'
                                                    fwqxz[fwqlb.index(fwqid)]=''
                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                    jsonfile=json.dumps({
                                                    "chat_id":int(message["data"]["channel_id"]),
                                                    "text": '回复模式已切换为语音回复模式(默认为派蒙[喵娘属性])\n可通过快捷指令[切换人物]切换',
                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                    })
                                                    print(jsonfile)
                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                                else:
                                                    fwqms[fwqlb.index(fwqid)]='0'
                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                    jsonfile=json.dumps({
                                                    "chat_id":int(message["data"]["channel_id"]),
                                                    "text": '回复模式已切换为文本模式',
                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                    })
                                                    print(jsonfile)
                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                            else:
                                                fwqms[fwqlb.index(fwqid)]='0'
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": '抱歉，暂时只有ChatGPT支持模式切换，其他均为文本输出，请切换模型为ChatGPT再切换模式',
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                        elif '可选人物' in content['text']:
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": '所有可选人物列表：空, 荧, 派蒙, 纳西妲, 阿贝多, 温迪, 枫原万叶, 钟离, 荒泷一斗, 八重神子, 艾尔海森, 提纳里, 迪希雅, 卡维, 宵宫, 莱依拉, 赛诺, 诺艾尔, 托马, 凝光, 莫娜, 北斗, 神里绫华, 雷电将军, 芭芭拉, 鹿野院平藏, 五郎, 迪奥娜, 凯亚, 安柏, 班尼特, 琴, 柯莱, 夜兰, 妮露, 辛焱, 珐露珊, 魈, 香菱, 达达利亚, 砂糖, 早柚, 云堇, 刻晴, 丽莎, 迪卢克, 烟绯, 重云, 珊瑚宫心海, 胡桃, 可莉, 流浪者, 久岐忍, 神里绫人, 甘雨, 戴因斯雷布, 优菈, 菲谢尔, 行秋, 白术, 九条裟罗, 雷泽, 申鹤, 迪娜泽黛, 凯瑟琳, 多莉, 坎蒂丝, 萍姥姥, 罗莎莉亚, 留云借风真君, 绮良良, 瑶瑶, 七七, 奥兹, 米卡, 夏洛蒂, 埃洛伊, 博士, 女士, 大慈树王, 三月七, 娜塔莎, 希露瓦, 虎克, 克拉拉, 丹恒, 希儿, 布洛妮娅, 瓦尔特, 杰帕德, 佩拉, 姬子, 艾丝妲, 白露, 星, 穹, 桑博, 伦纳德, 停云, 罗刹, 卡芙卡, 彦卿, 史瓦罗, 螺丝咕姆, 阿兰, 银狼, 素裳, 丹枢, 黑塔, 景元, 帕姆, 可可利亚, 半夏, 符玄, 公输师傅, 奥列格, 青雀, 大毫, 青镞, 费斯曼, 绿芙蓉, 镜流, 信使, 丽塔, 失落迷迭, 缭乱星棘, 伊甸, 伏特加女孩, 狂热蓝调, 莉莉娅, 萝莎莉娅, 八重樱, 八重霞, 卡莲, 第六夜想曲, 卡萝尔, 姬子, 极地战刃, 布洛妮娅, 次生银翼, 理之律者, 真理之律者, 迷城骇兔, 希儿, 魇夜星渊, 黑希儿, 帕朵菲莉丝, 天元骑英, 幽兰黛尔, 德丽莎, 月下初拥, 朔夜观星, 暮光骑士, 明日香, 李素裳, 格蕾修, 梅比乌斯, 渡鸦, 人之律者, 爱莉希雅, 爱衣, 天穹游侠, 琪亚娜, 空之律者, 终焉之律者, 薪炎之律者, 云墨丹心, 符华, 识之律者, 维尔薇, 始源之律者, 芽衣, 雷之律者, 苏莎娜, 阿波尼亚, 陆景和, 莫弈, 夏彦, 左然\n请使用切换人物指令切换，仅在语音回复模式生效',
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        elif '切换人物' in content['text']:
                                            fwqxz[fwqlb.index(fwqid)]=content['text'][31:-1]
                                            print(fwqxz[fwqlb.index(fwqid)])
                                            if str(fwqxz[fwqlb.index(fwqid)]) in allrw:
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": '人物已切换为:'+fwqxz[fwqlb.index(fwqid)],
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                            else:
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": '找不到你选择的人物：'+fwqxz[fwqlb.index(fwqid)]+'\n请确认你输入的人物在可选人物列表中',
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                        elif '运行节点信息' in content['text']:
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": '当前运行节点信息：\n运行节点名：云服务器1[公用]\nip:1.117.76.68\n参考位置：中国-上海市 腾讯云\n今日累计调用次数：'+str(dycs)+'次\n2分钟内调用次数：'+str(efzdy)+'次\n版本号：3.8\n新功能体验/反馈，欢迎前往：https://fanbook.mobi/LmgLJF3N',
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        elif 'AI绘图' in content['text']:
                                            gjc=content['text'][31:-1]
                                            print('关键词:',gjc)
                                            htmessage=requests.get('https://api.lolimi.cn/api/ai/mj1?key=sWlckPY0hlgaDryj7hnLewOjTU&msg='+str(gjc), stream=True)
                                            print(htmessage.text)
                                            htmessage=json.loads(htmessage.text)
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"请稍等....\n正在努力生成图片，你的图片id为："+str(htmessage['data'])+"\n请在一分钟后再来查看此消息，或者使用命令：[获取绘图图片]来获取生成的图片\n你的关键词/表达式为："+gjc,
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                            hhdata = json.loads(postreturn.text)
                                            hhxxlb.append(hhdata["result"]["message_id"])
                                            hhidlb.append(str(htmessage['data']))
                                            hhpdidlb.append(str(message["data"]["channel_id"]))
                                        elif '获取绘图图片' in content['text']:
                                            gjc=content['text'][33:-1]
                                            print('图片id:',gjc)
                                            htmessage=requests.get('https://api.lolimi.cn/api/ai/mj2?key=sWlckPY0hlgaDryj7hnLewOjTU&id='+str(gjc), stream=True)
                                            print(htmessage.text)
                                            htmessage=json.loads(htmessage.text)
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"{\"type\":\"richText\",\"title\":\"图片获取成功\",\"document\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"进度："+str(htmessage['data'])+"\\\\n\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\""+str(htmessage["imageurl"])+"\\\",\\\"width\\\":1800.0,\\\"height\\\":2912.0,\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}",
                                            "parse_mode": "Fanbook",
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        elif '切换模型' in content['text']:
                                            if 'ChatGPT' in content['text']:
                                                mxlb[fwqlb.index(fwqid)] = 'ChatGPT'
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text":"模型已切换为ChatGPT",
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                            elif '文心一言' in content['text']:
                                                mxlb[fwqlb.index(fwqid)] = '文心一言'
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text":"模型已切换为文心一言",
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                            elif '星火大模型V2.0' in content['text']:
                                                mxlb[fwqlb.index(fwqid)] = '星火大模型V2.0'
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text":"模型已切换为星火大模型V2.0",
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                            else:
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text":"找不到你选择的模型，请重新选择",
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                        else:
                                            if fwqms[fwqlb.index(fwqid)]=='0':
                                                #text=json.loads(content)
                                                print(mxlb[fwqlb.index(fwqid)]+'文本模式回复')
                                                print(content['text'])
                                                print(content['text'][23:])
                                                if mxlb[fwqlb.index(fwqid)] == 'ChatGPT':
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/mfcat3.5.php?type=json&format=0&sx= &msg='+content['text'][23:]+'.', stream=True)
                                                elif mxlb[fwqlb.index(fwqid)] == '文心一言':
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/wx.php?type=json&format=0&msg='+content['text'][23:], stream=True)
                                                elif mxlb[fwqlb.index(fwqid)] == '星火大模型V2.0':
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/xh.php?type=json&format=0&msg='+content['text'][23:]+'.', stream=True)
                                                print(chatmessage.text)
                                                chatmessage=json.loads(chatmessage.text)
                                                print(chatmessage)
                                                n="""
            """
                                                if mxlb[fwqlb.index(fwqid)] == '星火大模型V2.0' or mxlb[fwqlb.index(fwqid)] == '文心一言':
                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                    jsonfile=json.dumps({
                                                    "chat_id":int(message["data"]["channel_id"]),
                                                    "text": chatmessage['data']['output'].replace('\n', n),
                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                    })
                                                    print(jsonfile)
                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                                else:
                                                    chatmessage=chatmessage['data'].replace('\\\\', '\\')
                                                    chatmessage=chatmessage.replace('\\n', n)
                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                    jsonfile=json.dumps({
                                                    "chat_id":int(message["data"]["channel_id"]),
                                                    "text": chatmessage.replace('\\"', '"'),
                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                    })
                                                    print(jsonfile)
                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                            elif fwqms[fwqlb.index(fwqid)]=='1':
                                                print('音频模式回复')
                                                print(content['text'])
                                                print(content['text'][23:])
                                                if fwqxz[fwqlb.index(fwqid)] == '':
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/ys3.5.php?msg='+content['text'][23:], stream=True)
                                                else:
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/ys3.5.php?msg='+content['text'][23:]+'&speaker='+xz, stream=True)
                                                chatmessage=json.loads(chatmessage.text)
                                                print(chatmessage)
                                                print(chatmessage['music'])
                                                url = chatmessage['music']
                                                audio_duration = get_audio_duration(str(url),msg=chatmessage['msg'])
                                                print(f"音频时长：{audio_duration} 秒")
                                                xx='{"type": "voice","url": "'+chatmessage['music']+'","second": '+str(int(audio_duration))+',"isRead": false}'
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": xx,
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                            xxjl.append(mxlb[fwqlb.index(fwqid)]+'模式回复消息:'+content['text'][23:].replace('\n', '')+'，模型回复:'+str(chatmessage).replace('\n', ''))
                                            xxfsz.append('发送者:'+message["data"]["author"]["nickname"]+message["data"]["author"]["username"])
                                            xxfszid.append('userid:'+message['data']["user_id"]+" 服务器id:"+str(fwqid))
                                    else:
                                        print('用户：',userid,'已经操作过快，忽略输入')
                            # 在这里添加你希望执行的操作
                    def on_error(ws, error):
                        # 处理错误
                        addmsg("发生错误:"+str(error),color='red')
                        error=traceback.format_exc()
                        print(error)
                    def on_close(ws):
                        # 连接关闭时的操作
                        addmsg("连接已关闭",color='red')
                    def on_open(ws):
                        # 连接建立时的操作
                        addmsg("连接已建立",color='green')
                        # 发送心跳包
                        def send_ping():
                            print('发送：{"type":"ping"}')
                            ws.send('{"type":"ping"}')
                        send_ping()  # 发送第一个心跳包
                        # 定时发送心跳包
                        def schedule_ping():
                            send_ping()
                            """
                            # 每25秒发送一次心跳包
                            websocket._get_connection()._connect_time = 0  # 重置连接时间，避免过期
                            ws.send_ping()
                            websocket._get_connection().sock.settimeout(70)
                            ws.send('{"type":"ping"}')
                            """
                        #websocket._get_connection().run_forever(ping_interval=25, ping_payload='{"type":"ping"}', ping_schedule=schedule_ping)
                    # 替换成用户输入的BOT令牌
                    lingpai = lingpai
                    url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMe"
                    # 发送HTTP请求获取基本信息
                    response = requests.get(url)
                    data = response.json()
                    def send_data_thread():
                        global sycyid,cysycs,jgczsj,efzdy,hhxxlb,hhidlb,hhpdidlb,xxfsz,xxjl,xxfszid
                        while True:
                            for x in range(3):
                                cpu_res = psutil.cpu_percent(interval=1)
                                
                            print(cpu_res/3)
                            # 在这里编写需要发送的数据
                            time.sleep(17)
                            with open('xxjl.txt', 'w',encoding="utf-8") as file:
                                for item in xxjl:
                                    file.write(f"{item}\n")
                            with open('xxfsz.txt', 'w',encoding="utf-8") as file:
                                for item in xxfsz:
                                    file.write(f"{item}\n")
                            with open('xxfszid.txt', 'w',encoding="utf-8") as file:
                                for item in xxfszid:
                                    file.write(f"{item}\n")
                            ws.send('{"type":"ping"}')
                            addmsg('发送心跳包：{"type":"ping"}',color='green')
                            jgczsj+=1
                            for i in hhidlb:
                                z=hhpdidlb[hhidlb.index(i)]
                                sy=hhidlb.index(i)
                                try:
                                    htmessage=requests.get('https://api.lolimi.cn/api/ai/mj2?key=sWlckPY0hlgaDryj7hnLewOjTU&id='+str(i), stream=True)
                                    print(htmessage.text)
                                    htmessage=json.loads(htmessage.text)
                                    if str(htmessage['data']) != "100%":
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(z),
                                        "text": "{\"type\":\"richText\",\"title\":\"图片正在生成，请稍等...\",\"document\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"进度："+str(htmessage['data'])+"\\\\n\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\""+str(htmessage["imageurl"])+"\\\",\\\"width\\\":1800.0,\\\"height\\\":2912.0,\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}",
                                        "message_id":int(hhxxlb[hhidlb.index(i)]),
                                        "parse_mode": "Fanbook"
                                        })
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                    else:
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(z),
                                        "text": "{\"type\":\"richText\",\"title\":\"图片生成完成\",\"document\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"进度："+str(htmessage['data'])+"\\\\n\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\""+str(htmessage["imageurl"])+"\\\",\\\"width\\\":1800.0,\\\"height\\\":2912.0,\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}",
                                        "message_id":int(hhxxlb[hhidlb.index(i)]),
                                        "parse_mode": "Fanbook"
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                        hhidlb.pop(sy)
                                        hhpdidlb.pop(sy)
                                        hhxxlb.pop(sy)
                                except Exception as e:
                                    try:
                                        if str(htmessage["pointout"]) == "请耐心等待出图":
                                            pass
                                        else:
                                            hhidlb.pop(sy)
                                            hhpdidlb.pop(sy)
                                            hhxxlb.pop(sy)
                                    #hhidlb.pop(sy)
                                    #hhpdidlb.pop(sy)
                                    #hhxxlb.pop(sy)
                                    except Exception as e:
                                        pass
                                    pass
                            print('当前警告重置时间：',str(jgczsj))
                            if jgczsj >= 10:
                                print('警告重置')
                                jgczsj=0
                                efzdy=0
                                sycyid=[]#使用成员id
                                cysycs=[]#成员使用次数
                                #hhpdidlb.clear()
                                #hhidlb.clear()
                                #hhxxlb.clear()
                    if response.ok and data.get("ok"):
                        user_token = data["result"]["user_token"]
                        device_id = "your_device_id"
                        version_number = "1.6.60"
                        super_str = base64.b64encode(json.dumps({
                            "platform": "bot",
                            "version": version_number,
                            "channel": "office",
                            "device_id": device_id,
                            "build_number": "1"
                        }).encode('utf-8')).decode('utf-8')
                        ws_url = f"wss://gateway-bot.fanbook.mobi/websocket?id={user_token}&dId={device_id}&v={version_number}&x-super-properties={super_str}"
                        threading.Thread(target=send_data_thread, daemon=True).start()
                        # 建立WebSocket连接
                        websocket.enableTrace(True)
                        ws = websocket.WebSocketApp(ws_url,
                                                    on_message=on_message,
                                                    on_error=on_error,
                                                    on_close=on_close)
                        ws.on_open = on_open
                        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
                    else:
                        addmsg("无法获取BOT基本信息，请检查令牌是否正确。",color='red')
                    '''
                    xx='{"type": "voice","url": "https://speech.ai.xiaomi.com/speech/1.0/tts_token?token=eyJ2IjoiVjAiLCJuIjoiU1oifQ.AAAXUkp9P1QAFgBdFAwbZ24VTkoaRRsPG2AFFhgAQgBIRyIvRw4PfR9GGBh0VUBPEQhHWxBrPkBITxBDEFhHb1RHT0FXEw0QY20QRU4AWgBZTTJVQQ4YTE9KEXF2AAkUSRNMGBh0XUdeQRtQQ31hahBOGRJPQwlGMwUXHBFdQV5ANmhBTk0UTkEPFW4BQXMUWUECR2A-QEtIEkJHXBM3VRtKFQsSAxpgYxceGBVFEBRPJgMAAAAKR0xLMD99FB8ATABeR2NVQBlHWw8KEjE7D0kaERcPAkBlBA8YR1tEDkBqbxQcQhNUDhhLN0QAFhNYGwkTY2IVSkMOVEdCUnQKExobXRACE2ZtGgA.EO5fMqpLGoC6LrZI3pQP5w","second": '+str(int(audio_duration))+',"isRead": false}'

                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({
                    "chat_id":int(pdid),
                    "text": xx
                    })
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    colorize_json(smg2=postreturn.text,pcolor='d')
                    '{\"type\":\"richText\",\"title\":\"\",\"document\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\"https://fb-cdn.fanbook.mobi/fanbook/app/files/chatroom/unKnow/df8ce32b1e5e6990d4d958343a4b973d.png\\\",\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}","entities":[]}}'
                    '''
                except Exception as e:
                    print(f"出错：{e}")
                    #global b
                    continue
        elif a=='22':
            a=[]
            bt=input("请输入消息卡片标题")
            for i in range(25):
                sr=input("请输入内容，直接回车代表下一行，输入 -继续- 继续发送消息(旁边的两个-(减号)不要忘记)，你还可以输入"+str(25-i)+"次\n")
                if sr == "-继续-":
                    break
                a.append(sr)
            b=""
            print(a)
            for i in range(len(a)):
                b+=',{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"padding\\\":\\\"-167.5,-13,-26,15\\\",\\\"overflow\\\":\\\"clip\\\",\\\"textAlign\\\":\\\"left\\\",\\\"style\\\":{\\\"fontSize\\\":15,\\\"color\\\":\\\"#1F2329\\\"},\\\"data\\\":\\\"'+a[i]+'\\\"}}'
            print(b)
            pdid=input("请输入需要发送的频道id")
            xx="{\"notification\":\""+bt+"\",\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,8,12,8\\\",\\\"width\\\":1500,\\\"backgroundColor\\\":\\\"e5f1ff\\\",\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\""+bt+"\\\",\\\"style\\\":{\\\"color\\\":\\\"#198CFE\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}}},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"padding\\\":\\\"-167.5,0,0,10\\\",\\\"overflow\\\":\\\"clip\\\",\\\"textAlign\\\":\\\"left\\\",\\\"style\\\":{\\\"fontSize\\\":15,\\\"color\\\":\\\"#1F2329\\\"},\\\"data\\\":\\\" \\\"}}"+b+"]}\",\"type\":\"messageCard\"}"
            for i in range(int(input("请输入发送次数"))):
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":int(pdid),
                "text": xx,
                "parse_mode":"Fanbook"
                })
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
        elif a=='23':
            jddata=''
            a=True
            false=False
            d=','
            while a:
                xz=input('请输入富文本类型，0为文字，1为图片，输入-继续-以完成')
                if xz=='0':
                    jddata+="{\\\"insert\\\":\\\""+input('请输入文字内容')+"\\\"}"+d
                elif xz=='1':
                    jddata+="{\\\"insert\\\":{\\\"source\\\":\\\"https://fb-cdn.fanbook.cn/fanbook/app/files/chatroom/image/f23b8f408d3e24ecb5b66f1230c1a415.png\\\",\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}}"+d
                elif xz=='-继续-':
                    a=False
            textdata="{\"type\":\"richText\",\"title\":\""+input("请输入富文本标题")+"\",\"document\":\"["+str(jddata[:-1])+"]\"}"
            textdata=json.dumps(textdata)
            print('富文本生成完成，text数据：')
            print(textdata)
        elif a=='24':
            def get_members(token='',tabs=[{"start":0, "end":99}],guid='',chlid='',userid=''):#获取成员列表
                url=f'https://a1.fanbook.mobi/api/bot/{token}/v2/guild/members'
                headers={'Content-Type': 'application/json'}
                body={
                "guild_id":guid,
                "channel_id":chlid,
                "user_id":userid,
                "ranges":tabs
            }
                body=json.dumps(body)
                r=requests.post(url,headers=headers,data=body)
                return json.loads(r.text)

            def getGuildMembersCount(token='',guid=''):
                '''
                url=f'https://a1.fanbook.mobi/api/bot/{token}/getGuildMembersCount'#获取成员数量
                headers={'Content-Type': 'application/json'}
                body=json.dumps({"guild_id":guid})
                r=requests.post(url,headers=headers,data=body)
                print(r.text)
                return json.loads(r.text)
            '''
                return {'result':0}

            def sendMessage(token='',chlid='',text='',sl=0,yz=0):
                global rok,err,texttype
                url=f'https://a1.fanbook.mobi/api/bot/{token}/getPrivateChat'#获取私聊频道
                headers={'Content-Type': 'application/json'}
                print(chlid)
                body=json.dumps({"user_id":int(chlid)})
                r=requests.post(url,headers=headers,data=body)
                da=json.loads(r.text)
                #print(da)
                if yz==1:
                    if da["ok"]==true or da["ok"]==True:
                        pass
                    else:
                        print(f'发送第{str(sl+1)}条消息失败，获取私信频道失败')
                        err+=1
                        print(da)
                        return da
                    chlid=da["result"]["id"]
                url=f'https://a1.fanbook.mobi/api/bot/{token}/sendMessage'#发送消息
                headers={'Content-Type': 'application/json'}
                if texttype==1 and yz==1:
                    body=json.dumps({"chat_id":int(chlid),"text":str(text),"parse_mode":"Fanbook"})
                else:
                    body=json.dumps({"chat_id":int(chlid),"text":text})
                r=requests.post(url,headers=headers,data=body)
                da=json.loads(r.text)
                if da["ok"]==true or da["ok"]==True:
                    print(f'发送第{str(sl+1)}条消息成功')
                    rok+=1
                else:
                    print(f'发送第{str(sl+1)}条消息失败')
                    print(da)
                    err+=1
                return json.loads(r.text)

            true=True
            rok=0
            err=0
            sl=0
            texttype=0

            token=input('请输入机器人token')
            textdata=input('请输入消息或者消息json数据')
            try:
                textdata=json.loads(textdata)
                texttype=1
            except:
                pass
            chlid=input('请输入被通知成员所在的频道id')
            gid=input('请输入服务器id')
            botid=input('请输入bot id')

            qx=sendMessage(token=token,chlid=chlid,text='1')

            notend=True
            userids=[]
            tabsdata=0

            try:
                if qx["ok"]==true or qx["ok"]==True:
                    print('验证成功，机器人有权限发送消息')
                    rok-=1
                    try:
                        cysl=getGuildMembersCount(token=token,guid=int(gid))['result']
                        print('服务器总成员数量：',str(cysl))
                        try:
                            while notend:
                                cylb=get_members(token=token,guid=gid,userid=botid,chlid=chlid,tabs=[{"start":tabsdata, "end":tabsdata+99}])
                                rangesdata=cylb['result']["ops"][0]
                                #rangesdata=json.loads(rangesdata[0])
                                rangesdata=rangesdata['items']
                                #print(rangesdata)
                                for x in rangesdata:
                                    datatype=x.keys()
                                    datatype=list(datatype)
                                    if datatype[0]=='User':
                                        userids.append(x['User']['user_id'])
                                if len(rangesdata)<99:
                                    print('获取完成')
                                    notend=False
                                    #print(userids)
                                tabsdata+=99
                            #启动多个线程运行sendMessage
                            for x in userids:
                                #print(x)
                                threading.Thread(target=sendMessage,args=(token,x,textdata,sl,1,)).start()
                                sl+=1
                                time.sleep(0.01)
                            time.sleep(5)
                            print(f'发送完成，成功{str(rok)}次，失败{str(err)}次')
                        except:
                            print('获取成员数量失败，你应该检查机器人id和频道id')
                            print(cylb)
                    except:
                        print('获取成员数量失败，你应该检查服务器id')
                else:
                    print('机器人没有权限发送消息或没有发送消息白名单')
                    print(qx)
            except:
                print('token不正确')

            input()
        elif a=='25':
            colorprint('请输入你的用户token',pcolor='bandg')
            Auth=input()
            colorprint('请输入你想要查询的用户长id',pcolor='bandg')
            id=input()
            Nonce=str(uuid.uuid4())
            t=int(time.time() * 1000)

            url = "https://web.fanbook.cn/api/a1/api/user/getUser"

            r = '{\"user_ids\":[\"'+id+'\"],\"guild_id\":null,\"transaction\":\"e5624362-98f1-4d22-9b41-d21226ef03bb\"}'

            # 示例使用
            common_fields = {
                "Nonce": Nonce,
                "Timestamp": t,  # 毫秒级时间戳
                "Authorization": Auth,  # 假设已获取到授权token
                "AppKey": app_key,
                "RequestBody": r,
                "Platform": 'web'
            }

            signature = get_signature(common_fields)
            print(f"Generated Signature: {signature}")

            headers = {
            "Nonce": Nonce,
            'appkey': 'ww0qqc0UHMsFtDUhGbh0',
            'authorization': Auth,
            'language': 'zh-CN',
            'platform': 'web',
            'priority': 'u=1, i',
            'signature': signature,
            'timestamp': str(t),
            'content-type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=r)

            print(response.text)
            colorize_json(response.text)
            r=json.loads(response.text)
            if r['desc']=='成功':
                try:
                    addmsg('获取成功','green')
                    tme=r['data'][0]["joined_at"]
                    timestamp_seconds = int(tme) / 1000
                    dt_object = datetime.fromtimestamp(int(timestamp_seconds))
                    addmsg('用户注册时间：'+str(dt_object),'auqa')
                except:
                    addmsg('解析失败，该用户可能无数据或者是bot','yellow')
                
            else:
                addmsg('获取失败','red')
        elif a=='26':
            addmsg('危险：\n该功能仅供学习、研究使用\n该功能可能导致封号及其他风险，开发者不对其负责\n输入Y回车继续，直接回车退出',color='red')
            if input()=='Y':
                text=input('请输入需要发送的文本：')
                pdid=input('请输入目标频道id：')
                fwqid=input('请输入服务器id：')
                text1='{"type":"text","text":"'+text+'","contentType":0}'
                fanbookbotapi.send_user_message(bot_token=lingpai,channel_id=pdid,guild_id=fwqid,text=text1,decs=text)
        # Increment a counter by one for each button click.
        sentry_sdk.metrics.incr(
            key="yhsy",
            value=1,
            tags={
                "id": str(a),
                "pc_name":str(computer_name)
            }
        )
    except Exception as e:#检测错误
        error=traceback.format_exc()#获取错误信息
        variables = globals()
        write_error_to_file(e, variables)
        encrypt_error_file()
        if 'for int()' in error:
            colorprint(smg2='遇到错误，请重试',pcolor='red')
            colorprint(smg2='错误诊断：数据类型错误，请输入整数',pcolor='red')
        elif 'list index out of range' in error:
            colorprint(smg2='遇到错误，请重试',pcolor='red')
            colorprint(smg2='错误诊断：数据处理错误，请输入正确的数据',pcolor='red')
        else:
            colorprint(smg2='遇到错误，请重试',pcolor='red')
            colorprint(smg2='遇到未知错误：'+error,pcolor='red')
            colorprint(smg2='发生错误，请检查参数，是否发送错误报告(报告不包含机器人令牌等敏感数据,王大哥可见)(Y/N)',pcolor='bandg')
            cw=input()
            if cw=='Y':
                    cwbg='错误模块：'+a+' 版本号：'+str(v)+'，错误代码：'+error
                    url='https://a1.fanbook.mobi/api/bot/0f2de7ac66727cd9fcec1ee43559c561f6abf3f1e202c5a06c2ae4a3f6cf94ab795fbfbe39ad311a18ad1ff314388d1c/sendMessage'#错误发送到私密频道
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({"chat_id":448843628261933056,"text":cwbg})
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    addmsg('已发送',color='aqua')
            else:
                colorprint(smg2='已取消',pcolor='red')

