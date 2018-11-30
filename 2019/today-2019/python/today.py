# Import volapi and a Room interface
from volapi import Room
from subprocess import call
import time 



# beepi will close at the end of this scope
with Room("qwbqjp18", "welcome") as beepi:
    # optional login using a password
    # beepi.user.login("todayin2019")
    # Upload a file under a new filename and save the id
    # id = beepi.upload_file("images/disgusted.jpg", upload_as="mfw.jpg")
    # Show off your file in the chat
    beepi.post_chat(" 我是今天的主持人，大家好，欢迎来到 Today 2019 开发者大会 ！")
    call(['say', '我是今天的主持人，大家好，欢迎来到 Today 2019 开发者大会 ！'])
    # Print out chat messages since you got to the room
    #for msg in beepi.chat_log:
     #   print(msg.nick + ": " + msg.msg)
    time.sleep(3)

    beepi.post_chat(" 今年我们的主题是 ： 使用Today， 来建造一切可能。  ")
    call(['say', ' 今年我们的主题是 ： 使用Today， 来建造一切可能。 '])

    
    time.sleep(200)

    beepi.post_chat("  我想从最近换手机的经历开始说起。 ")
    call(['say', ' 我想从最近换手机的经历开始说起。 '])

    
    time.sleep(200)

    call(['say', ' 首先让我们看看todo管理又有了哪些新动作 '])
    beepi.upload_file("images/1.png", upload_as="改造todo-1.png")
    beepi.upload_file("images/1.png", upload_as="改造todo-2.png")
    beepi.upload_file("images/1.png", upload_as="改造todo-3.png")
    beepi.upload_file("images/1.png", upload_as="改造todo-4.png")


    time.sleep(200)

    beepi.post_chat("  今年Today将加入电影和天气预告，新书推荐、豆瓣同城诸如此类的内容，我们相信，自动提醒功能很棒，能够帮助Today希望留住用户。 ")
    call(['say', ' 今年Today将加入电影和天气预告，新书推荐、豆瓣同城诸如此类的内容，我们相信，自动提醒功能很棒，能够帮助Today希望留住用户。 '])
    beepi.upload_file("images/6.jpeg", upload_as="内容-1.jpeg")
    
    time.sleep(50)


    beepi.post_chat(" 不得不提到Slack，Today正在研究人物关系索引，拓展朋友圈。  ")
    call(['say', ' 不得不提到Slack，Today正在研究人物关系索引，拓展朋友圈。 '])

    
    time.sleep(50)


    beepi.post_chat(" 还有DingDing，今年DingDing将对接更多的第三方接口。  ")
    call(['say', ' 还有DingDing，今年DingDing将对接更多的第三方接口。 '])

    time.sleep(50)


    beepi.post_chat(" 接下来，Today将继续在三方面发力。  ")
    call(['say', ' 接下来，Today将继续在三方面发力。 '])
  

    time.sleep(2)


    beepi.post_chat("  第一是大数据。Today计划用一年的时间做成地图大数据、价格大数据。 ")
    call(['say', ' 第一是大数据。Today计划用一年的时间做成地图大数据、价格大数据。 '])


    time.sleep(200)

    beepi.post_chat(" 第二是硬件。做精美的硬件。 ")
    call(['say', ' 第二是硬件。做精美的硬件。 '])

    time.sleep(200)

    beepi.post_chat(" 第三是写作。这是一个很大很大的话题。  ")
    call(['say', ' 第三是写作。这是一个很大很大的话题。 '])
    beepi.upload_file("images/5.png", upload_as="写作-1.png")

    time.sleep(400)

    beepi.post_chat(" 谢谢大家的到来  ")
    call(['say', ' 谢谢大家的到来，我们明年再见！ '])




