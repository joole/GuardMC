from ws4py.client.threadedclient import WebSocketClient
import guard_pb2
import threading
import os
import sys
import ctypes
import math
import time
import json
import logging
import NdHttpClient
import NdCalculateUtil
import random



class NdUser():
    def __init__(self):
        self.__user_name     = ""
        self.__user_pwd      = ""
        self.__server_org    = ""
        self.__token_info    = {}
        self.__authorization = ""

    def SetUserName(self, username):
        
    
    def GetJsonValue(self, json_raw, json_key):
        json_obj = json.loads(json_raw)
        return json_obj[json_key]

    def LoginToUCCenter(self):
        UC_SERVER   = "ucbetapi.101.com"
        USER_AGENT  = "99U:GuardClient"
        httpclient  = NdHttpClient.NdHttpClient()
        url         = "https://"+ UC_SERVER + "/v0.93/tokens"
        httpclient.SetRequestUrl(url) 
        httpclient.SetRequestMethod(NdHttpClient.eRequestType.kPost)    
        httpclient.AddRequestHeader("Content-type", "application/json")
        httpclient.AddRequestHeader("Connection", "keep-alive")
        httpclient.AddRequestHeader("Host", UC_SERVER)
        httpclient.AddRequestHeader("Referer", url);  #"https://aqapi.101.com/v0.93/tokens"
        httpclient.AddRequestHeader("Accept", "application/json")
        httpclient.AddRequestHeader("Accept-Language", "zh-CN,zh;q=0.8")
        httpclient.AddRequestHeader("User-Agent", USER_AGENT)
        httpclient.AddRequestHeader("Referer", "https://sign-daily-completion.sdp.101.com/")
        httpclient.AddRequestHeader("Origin", "https://sign-daily-completion.sdp.101.com")
        util        = NdCalculateUtil.NdCalculateUtil()
        md5_pwd     = util.md5Encrypt(self.__user_pwd)
        posFields   = "{\"login_name\":\"" + str(self.__user_name) + "@" + self.__server_org + "\", \"password\":\"" + md5_pwd + "\"}"  
        httpclient.SetPostFields(posFields)
        code        = httpclient.ExecRequest()
        if code <= 0:
            logging.critical("can't connect to server")
            return False
        elif code >= 400:
            err_code = self.GetJsonValue(httpclient.GetResponseContent(), "code")
            err_msg  = self.GetJsonValue(httpclient.GetResponseContent(), "message")    
            logging.error("server repsonse http_code = {0} error_code = {1} error_msg = {2}".format(code, err_code, err_msg))
      
            return False
        else:
            logging.debug("server response error : {0}".format(httpclient.GetResponseContent()))
            token_info  = httpclient.GetResponseContent()
            self.__tokeninfo = token_info
            return True

    def CalcAuthorithem(self, http_method, host, path):
        mic             = random.randint(0, 1000)
        util            = NdCalculateUtil.NdCalculateUtil()
        nonce           = str(int(time.time() *1000) + int(mic)) +":" + str(util.generateMixRandomCode(8))
        rawMac          = nonce + "\n" + http_method + "\n" + path + "\n" + host + "\n"
        mac_key         = self.GetJsonValue(self.__tokeninfo, "mac_key")
        mac             = util.encryptHMac256(rawMac, mac_key)
        access_token    = self.GetJsonValue(self.__tokeninfo, "access_token")
        authorization   = "MAC id=\"" + access_token + "\",nonce=\"" + nonce + "\",mac=\"" + mac + "\""
        return authorization.encode("utf-8")

    def GetAuthRequest(self, pull_card):
        auth                   = guard_pb2.AuthRequest()
        auth.user_id           = user_name
        auth.auth_data         = self.__authorization
        auth.encrypt_key       = "aes256 key"
        auth.appid             = "111-222-333-444"
        auth.pull_card_list    = pull_card
        return self.buildPkt(guard_pb2.Method_Auth, guard_pb2.Method_Class_Request, 1, 0, "", auth.SerializeToString())

    def buildPkt(self, method, method_class, seq, err, err_msg, data):
        pkt                     = guard_pb2.Body()
        pkt.method_id           = method
        pkt.method_class        = method_class
        pkt.seq                 = seq
        pkt.data                = data
        return pkt.SerializeToString()

    def GetDrawCard(self, count):
        pkt                 = guard_pb2.DrawCardRequest()
        pkt.count           = count
        return buildPkt(guard_pb2.Method_DrawCard, guard_pb2.Method_Class_Request, 1, 0, "", pkt.SerializeToString())  
    




