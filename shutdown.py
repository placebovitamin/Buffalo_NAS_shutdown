"""
Pyhton code to shutdown Buffallo NAS (TeraStation TS5410D)
Change 'xxx.xxx.xxx.xxx' to the IP adress of your NAS
Change 'password' to the password of admin
"""
import requests
import ast

def shutdownNAS():
    # IP adress
    ip = 'xxx.xxx.xxx.xxx'
    # credentials
    user = 'admin'
    pw  = 'password'
    
    # Start session
    with requests.Session() as session:
        # URL of Buffalo NAS API 
        url = 'http://'+ip+'/nasapi'
        # Login in NAS
        login = {"jsonrpc":"2.0","method":"Auth.login","params":{"username":user,"password":pw},"id":"9999"}
        response_login = session.post(url, json = login)
        # Get SID of session
        dictSession = ast.literal_eval(response_login.text)
        sid = dictSession['result']['sid']
        # Send Shutdown command
        shutdown=  {"jsonrpc":"2.0","method":"System.shutdown","params":{"sid":sid},"id":"9999"}
        response_shutdown = session.post(url, json =  shutdown)
        
if __name__ == "__main__":
    shutdownNAS()
