# fanbook-bot-Framework

fanbook机器人框架，无需python环境，甚至无需编码运行机器人  

## 快速上手

### 创建第一个机器人

下载更新工具：124.221.67.43/hj_update.exe  
注意：如非特殊说明，在每一次输入后都按一下回车  
将其放置在一个空文件夹内，然后运行，点击安装  
![image](https://github.com/user-attachments/assets/455d7c8d-c9d6-4ed0-8151-dd69882dde96)  
然后运行main.exe，我们先来初始化一个项目  
![image](https://github.com/user-attachments/assets/04c0f6fe-f5b9-40b7-8406-de00bfe5c900)  
输入2然后回车，然后输入1回车选择项目快速创建工具，然后输入y安装  
![image](https://github.com/user-attachments/assets/14b6ac4d-5f08-400f-bfa8-1cb2e1c99a45)  
然后输入3再输入1来使用拓展  
![image](https://github.com/user-attachments/assets/22e6e066-48bf-403a-a423-4590ad0c9a90)  
现在输入项目名称（例如test） 
然后输入机器人的token  
然后输入机器人的长id  
回车创建  
![image](https://github.com/user-attachments/assets/f8a2a63b-8e60-4d02-b692-32086ad3d9ff)  
然后输入1，再输入上面提示的文件路径即可运行  
![image](https://github.com/user-attachments/assets/0380d93a-b324-4ced-ad5b-e861c6323e4f)  
恭喜你，现在已经成功创建了你的第一个机器人  
![image](https://github.com/user-attachments/assets/0b19c98c-bb1f-41a0-8318-f4b307e322ed)  

## 常见问题

缺少.NET组件  
![image](https://github.com/user-attachments/assets/15947e73-c352-4e4a-9fb4-f4981d847247)  
出现该问题的解决方法：  
点击Download it now，下载并安装运行库即可  

## 内置函数

内置了fanbookbotapi库，可以不需要导库直接写函数名，文档：  
https://pypi.org/project/fanbookbotapi/  
日志输出：  
```python
logger.debug
logger.info
logger.warning
logger.error
logger.critical
```
比如说：  
```python
logger.info("开始初始化")
```
