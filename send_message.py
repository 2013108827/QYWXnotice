import requests
import json

message = ""    #建议把这个加在全部代码的最前面，以防出现变量未定义的报错
agentid = "xxxx"    #这里填你自建应用的AgentId


#直接按照格式调用send_message就可以了
def send_message(title, message):
    n = ""
    with open('token.txt', 'r') as f:   #默认从当前路径下读取token.txt文件里的access-token码,如果需要指定文件夹请改为'/var/tmp/token.txt'这种格式
        token = f.readline()
        token = token[:-1]
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % token
    message1 = message.encode("utf-8")  # 计算message使用utf-8编码有多少个字节，多于512个字节就要分多个消息发送
    # print("message1的长度是" + str(len(message1)))
    for i in range(int(len(message1) / 512) + 1):
        if n == "":
            message2 = message1[i * 512:(i + 1) * 512]
        elif int(n) > 0:
            message2 = message1[n:n + 512]
        for e in range(10):
            try:
                message2.decode("utf-8")
            except:
                message2 = message1[i * 512:(i + 1) * 512 - e - 1]
                n = (i + 1) * 512 - e - 1
            else:
                data = {
                    "touser": "@all",
                    "msgtype": "textcard",
                    "agentid": str(agentid),
                    "textcard": {
                        "title": str(title),
                        "description": str(message2.decode("utf-8")),
                        "url": "URL",
                    },
                    "duplicate_check_interval": 180,
                }
                data = json.dumps(data, ensure_ascii=False)
                response = requests.post(url=url, data=data.encode("utf-8").decode("latin1"))
                print(response.json())
                break
               



if __name__ == '__main__':

    #这个if可有可无，仅是当信息超长时先发送个信息超长的提醒消息而已
    if int(len(message.encode("utf-8")) / 512) +1 > 1:
        print("信息超长，将分为"+ str(int(len(message.encode("utf-8")) / 512) +1)+ "次发送,请注意查收")
        send_message("测试", ("信息超长，将分为"+ str(int(len(message.encode("utf-8")) / 512) +1))+ "次发送")
    send_message("测试", message)


