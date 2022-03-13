import requests
import os
import json

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://register.gangsterallstar.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
}

if __name__ == '__main__':
    cwd = os.getcwd()
    file_info = open(cwd + "\\info.txt", encoding='utf-8')

    for info in file_info.readlines():
        info_row = info.split(',')
        discordName = info_row[0]
        email = info_row[1]
        publicAddress = info_row[2]
        twitter = info_row[3]

        body = {'publicAddress': publicAddress,
                'discordName': discordName,
                'hexSignature': '0xweb3',
                'email': email,
                'twitter': twitter}

        response = requests.put("https://allstarsmintapi.azurewebsites.net/Submit", verify=False, headers=headers,
                                data=json.dumps(body))
        print("Request whether successful:" + response.text)

print("All task is finnish!")
