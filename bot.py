import requests
import time

print("""
 _______  __   __  ___   ___      __   __    __   __  _______  ______   ___   _______    _______  _______  _______ 
|       ||  |_|  ||   | |   |    |  | |  |  |  | |  ||   _   ||      | |   | |   _   |  |  _    ||       ||       |
|    ___||       ||   | |   |    |  |_|  |  |  |_|  ||  |_|  ||  _    ||   | |  |_|  |  | |_|   ||   _   ||_     _|
|   |___ |       ||   | |   |    |       |  |       ||       || | |   ||   | |       |  |       ||  | |  |  |   |  
|    ___||       ||   | |   |___ |_     _|  |       ||       || |_|   ||   | |       |  |  _   | |  |_|  |  |   |  
|   |___ | ||_|| ||   | |       |  |   |     |     | |   _   ||       ||   | |   _   |  | |_|   ||       |  |   |  
|_______||_|   |_||___| |_______|  |___|      |___|  |__| |__||______| |___| |__| |__|  |_______||_______|  |___|  
                                                                                                        BY RAUSPRETU & Isloka
      
      
      """)

token = "" # Discord Token
message = "<@894277639131504690> vadia gostosa putinha do bonde #EmilyVadiaBot - by RausPretu" # Message being Sent
delay = "10" # Each X minutes
channelid = "943685427246809099" # Channel ID
payload = {
  'content': message
}
headers = {
  'Authorization': token
}

def sendMessage(payload,headers,delay,channelid):
  url = 'https://discord.com/api/v9/channels/'+channelid+'/messages'
  requests.post(url, data=payload, headers=headers)
  time.sleep(int(delay)*60)

while True:
  sendMessage(payload, headers, delay, channelid)
