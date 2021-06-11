import urllib3
import json
http = urllib3.PoolManager()
def lambda_handler(event, context):
    url = "https://hooks.slack.com/services/"
    # 생성한 Webhook URL로 설정
    
    msg = {
        "channel": "#devops",         # 채널 명
        "username": event['Records'][0]['Sns']['Subject'], 
        "text": event['Records'][0]['Sns']['Message'],
        "icon_emoji": ""
    }
    
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',url, body=encoded_msg)
    
    print({"message": event['Records'][0]['Sns']['Message'],
        "status_code": resp.status,
        "response": resp.data})