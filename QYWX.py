#建议将此保存为单独文件，每隔1小时运行一次（token码每两个小时过期一次），然后再由send_message函数读取token.txt
import requests

corpid = ""   #企业ID填在双引号里，获取方式参考：https://open.work.weixin.qq.com/api/doc/90000/90135/90665#corpid
corpsecret = ""   #应用的凭证密钥填在双引号里，扫码登陆企业微信选【应用管理】——（【自建】（需要你提前先建好一个应用））——【你自建好的应用】——【Secret】


with open('token.txt','w') as file0:       #获取到的token码默认保存在当年路径下的token.txt里，若要指定保存路径或者文件名，按照此格式'/var/tmp/xxxx.txt'
    # 获取微信access_token
    def get_token():
        payload_access_token = {'corpid': str(corpid), 'corpsecret': str(corpsecret)}
        token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r = requests.get(token_url, params=payload_access_token)
        dict_result = (r.json())
        return dict_result['access_token']

    token=get_token()
    print(token, file=file0)
