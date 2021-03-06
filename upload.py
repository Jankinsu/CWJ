# -*- coding: utf-8 -*-
"""
本项目核心代码来于：https://github.com/abadfox233/ncov ,本项目实现该功能的action全自动实现
"""
import sys
import getopt
import os
import Utils
import requests
'''
    if cookie_file !="" and message_file !="":
        cookie = Utils.load_cookie_from_file(cookie_file)
        upload_message = Utils.load_upload_message_file(message_file)
        Utils.upload_ncov_message(cookie, upload_message=upload_message)
        sys.exit(1)
        
'''
'''
    use_age = """
    Error: upload.py -u <username> -p <password> -f <upload_message_file_path>
        or: upload.py -c <cookie_path>  -f <upload_message_file_path>
        or: upload.py --username=<username> --password=<password> --message_file=<upload_message_file_path>
        or: upload.py --cookie=<cookie_path> --message_file=<upload_message_file_path>        
            """

    try:
        opts, args = getopt.getopt(argv, "hu:p:f:c:", ["help", "username=", "password=", "message_file=", "cookie="])

    except getopt.GetoptError:
        print(use_age)
        sys.exit(2)

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(use_age)
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-c", "--cookie"):
            cookie_file = arg
        elif opt in ("-f", "--message_file"):
            message_file = arg
'''
def main():    
    username = os.environ["U"]
    password = os.environ["P"]
    token = os.environ["TOK"]
    noti_url = "http://www.pushplus.plus/send?token=" + token + "&title=晨午检提交结果&content="
    cookie_file = ""
    message_file = "upload.txt"
    if cookie_file != "" and message_file != "":
        cookie = Utils.load_cookie_from_file(cookie_file)
        upload_message = Utils.load_upload_message_file(message_file)
        Utils.upload_ncov_message(cookie, upload_message=upload_message)
    if username != "" and message_file != "" and password != "":
        cookie_file = Utils.COOKIE_FILE_NAME
        print("use username and password to upload message, cookie file is save to " + cookie_file)
        Utils.get_cookie_from_login(username, password, cookie_file)
        cookie = Utils.load_cookie_from_file(cookie_file)
        upload_message = Utils.load_upload_message_file(message_file)
        noti = Utils.upload_ncov_message(cookie, upload_message=upload_message)
        noti_url = noti_url + noti
        r = requests.get(noti_url)
if __name__ == "__main__":
    main()
