# YYGRP-U8
用友 GRP-U8 UploadFileData批量检测脚本_!
![图片](https://github.com/user-attachments/assets/b349f9b8-7483-4aa7-b963-252bb0337d4e)
```shell
漏洞描述：
用友 GRP-U8 UploadFileData接口存在任意文件上传漏洞，攻击者通过漏洞可以获取服务器权限

资产搜索：
FOfa:app="用友-GRP-U8"

使用说明：
python3 checkMain.py --url htttp://www.xxx.com 即可进行单个漏洞检测
python3 checkMain.py --file targetUrl.txt 即可对选中文档中的网址进行批量检测
python3 checkMain.py --help 查看更多详细帮助信息
```

