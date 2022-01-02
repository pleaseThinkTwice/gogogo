import random
import time


import xlsxwriter
from bs4 import BeautifulSoup
import requests
import re
findNumber=re.compile(r"\d*")

# 初始化 x y 坐标
def ini_cell():
    user=['mid','name','sex','sign','level','fans_medal[show]?','fans_medal[wear]','vip[label][text]','following','follower']
    user_ch=['用户的id','用户的姓名','用户的性别','用户的签名（0,1）','用户的等级','有没有展示粉丝牌?','有没有佩戴粉丝牌','vip','关注数','粉丝数']
    favorite=['id','media_count','n_moive','type','title','duration','bv_id','id','cnt_info[collect]','cnt_info[play]','cnt_info[danmaku]']
    favorite_ch = ['收藏夹id', '视频数量', '这页的第几个视频','视频的类型', '视频的标题', '视频的时长', '视频的bv_id','视频的id', '视频的收藏数', '视频的播放数',
                '视频的弹幕数']
    moive=['播放量','弹幕数',"投稿时间","全站排行榜最高", "点赞数", "投币数", "分享数", "视频的up主的粉丝数"]
    tag=['n_tag','tag_id','tag_name','tag_type','subscribed_count','archive_count','featured_count']
    tag_ch = ['这个视频的第几个tag','标签的id', '标签的名字', 'tag的类型 new_channel还是old_channel','标签的订阅数', '这个标签下的视频投稿数', '这个标签下的精选视频数']
    # tag_type=='new_channel'
    l1=user+favorite+moive+tag
    l2=user_ch+favorite_ch+moive+tag_ch
    return l2,l1
def tag(info,n):

    tag=[n,info['data'][n]['tag_id'],info['data'][n]['tag_name'],info['data'][n]['tag_type'],
         info['data'][n]['subscribed_count'],info['data'][n]['archive_count'],
         info['data'][n]['featured_count']]
    l=len(info['data'])
    # print(l)
    return tag,l
def moive(bv_id):
    return moive_info(bv_id)
def user_info(uid):
    info=ask_user_information(uid)
    info2=ask_more_user_info(uid)
    # print(info)
    # print(info2)
    user=[info['data']['mid'],info['data']['name'],info['data']['sex'],info['data']['sign'],info['data']['level'],
          info['data']['fans_medal']['show'],info['data']['fans_medal']['wear'],
          info['data']['vip']['label']['text'],
          info2['data']['following'],info2['data']['follower']]

    return user
def favor_info(favorite_id):
    url = "https://api.bilibili.com/x/v3/fav/resource/list"
    params = param(favorite_id, 1)
    response = requests.get(url=url, params=params, headers=head())
    info = response.json()
    return info
def favorite_info(favorite_id,n):
    url = "https://api.bilibili.com/x/v3/fav/resource/list"
    params = param(favorite_id, 1)
    response = requests.get(url=url, params=params, headers=head())
    info = response.json()
    favorite=[info['data']['info']['id'],info['data']['info']['media_count'],n,info['data']['medias'][n]['type'],
              info['data']['medias'][n]['title'],info['data']['medias'][n]['duration'],
              info['data']['medias'][n]['bv_id'],info['data']['medias'][n]['id'],
              info['data']['medias'][n]['cnt_info']['collect'],
              info['data']['medias'][n]['cnt_info']['play'],
              info['data']['medias'][n]['cnt_info']['danmaku']]
    return favorite,len(info['data']['medias'])
def random_consecutive_number_list(m,n,step):
    consecutive_number_list=[]
    for i in range(m,n):
        consecutive_number_list.append(m+i*step)
    # random.shuffle(consecutive_number_list)
    return consecutive_number_list
def main():

    start = time.time()
    workbook = xlsxwriter.Workbook('final2.xlsx')  # 新建excel表
    worksheet = workbook.add_worksheet('sheet1')
    l1,l2=ini_cell()
    worksheet.write_row('A1', l1)
    worksheet.write_row('A2', l2)
    n=3
    uid_list=random_consecutive_number_list(1,1200,1000)
    print("随机列表生成成功")
    # print(uid_list)
    # exit()
    try:
        for i in uid_list:
            try:
                print(i)
                time.sleep(0.8)
                media_id_list = normal_json_media_id(i)
                user_information=user_info(i)
                # print("user信息提取成功")
                print("成功提取一个人")
            except Exception as result:
                print(result)
            finally:
                continue
    except Exception as result:
        print(result)
    finally:
        workbook.close()
    end = time.time()
    print (end - start)
    exit()

def param(media_id,pn):
    params = {
        'media_id': 61989503,  # 收藏夹中的这个参数会不相同
        'pn': 1,
        'ps': 20,
        'keyword': '',
        'order': 'mtime',
        'type': 0,
        'tid': 0,
        'platform': 'web',
        'jsonp': 'jsonp',
    }
    params["media_id"]=media_id
    params["pn"] =pn
    return params
def ask_favorite_information(uid):
    headers = head()
    params = {
        'media_id': 61989503,  # 收藏夹中的这个参数会不相同
        'pn': 1,
        'ps': 20,
        'keyword': '',
        'order': 'mtime',
        'type': 0,
        'tid': 0,
        'platform': 'web',
        'jsonp': 'jsonp',
    }
def print_detail_tag_info(info):
    print(info)
    for i in info["data"]:
        print(i)
        print(type(i))
        # print(info["data"][i])
        # print(type(info["data"][i]))
def print_favor_info(info):
    print(info)
    for i in info["data"]:
        print(i)
        print(type(i))
        print(info["data"][i])
        print(type(info["data"][i]))
def print_user_info(info):
    print(info)
    for i in info["data"]:
        print(i)
        print(type(i))
        print(info["data"][i])
        print(type(info["data"][i]))
def ask_user_information(uid):
    headers = head()
    params={
        'mid': 17,
        # 需要改mid
        'jsonp': 'jsonp'
    }
    url = "https://api.bilibili.com/x/space/acc/info"
    params['mid']=uid
    response = requests.get(url=url, params=params, headers=headers)
    normal_json = response.json()
    # print(normal_json)
    return normal_json
def ask_more_user_info(uid):
    headers = head()
    params = {
        'vmid': 17,
        # 需要改mid
        'jsonp': 'jsonp'
    }
    params['vmid'] = uid
    url="https://api.bilibili.com/x/relation/stat"
    response = requests.get(url=url, params=params, headers=headers)
    normal_json = response.json()
    return normal_json
def sort_user_info(info):
    l1=[]
    l2=[]
    for i in info["data"]:
        l1.append(i)
        if(type(info["data"][i])==dict):
            l2.append(" ")
        else:
            l2.append(str(info["data"][i]))
    len2=len(l2)
    if len2<29:
        for i in range(29-len2):
            l2.append(" ")
    return l1,l2
def sort_favorites_info(info):
    l1 = []
    l2 = []
    # print(info["data"]["info"])
    for i in info["data"]["info"]:
        l1.append(i)
        if(type(info["data"]["info"][i])==dict):
            l2.append(" ")
        else:
            l2.append(info["data"]["info"][i])
    for i in info["data"]["medias"]:
        for j in i:
            l1.append(j)
            if (type(i[j]) == dict):
                l2.append(" ")
            else:
                l2.append(str(i[j]))
    len2=len(l2)
    if len2<397:
        for i in range(397-len2):
            l2.append(" ")
    return l1, l2
def sort_tags_info(info):
    l1=[]
    l2=[]
    for i in info["data"]:
        for j in i:
            l1.append(j)
            if (type(i[j]) == dict):
                l2.append(" ")
            else:

                l2.append(str(i[j]))
    len2=len(l2)
    if len2<208:
        for i in range(208-len2):
            l2.append(" ")

    return l1, l2

def head():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    return headers
def Get_detailed_video_information(movie_id):
    headers=head()
    url=Get_detailed_video_url(movie_id)
    response = requests.get(url=url, headers=headers)
    normal_json = response.json()
    return normal_json

def Get_detailed_video_url(movie_id):
    url="https://api.bilibili.com/x/web-interface/view/detail/tag?aid="+str(movie_id)
    return url
def get_media_id(uid):
    return normal_json_media_id(uid)
def get_media_count(uid):
    return media_count(uid)
def get_uid_url(uid):
    url="https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid="+str(uid)+"&jsonp=jsonp"
    # print(url)
    # https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=17&jsonp=jsonp
    return url
def askUrl_normal_json(uid):
    # 返回收藏夹的信息
    headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
        }
    url=get_uid_url(uid)
    response=requests.get(url=url,headers=headers)
    normal_json =response.json()
    return normal_json
def normal_json_media_id(uid):
    normal_json= askUrl_normal_json(uid)
    media_id=[]
    if normal_json["data"]==  None:
        return []
    else:
        if str(type(normal_json["data"]["list"]))=="<class 'NoneType'>":
            return []
        for i in range(len(normal_json["data"]["list"])):
            media_id.append(normal_json["data"]["list"][i]["id"])
    return media_id
def media_count(uid):
    normal_json= askUrl_normal_json(uid)
    media_count=[]
    if normal_json["data"]==None:
        return media_count
    else:
        for i in range(len(normal_json["data"]["list"])):
            media_count.append(normal_json["data"]["list"][i]["media_count"])
    return media_count

def moive_info(bv_id):
    url = "https://www.bilibili.com/video/"+str(bv_id)
    html = requests.get(url, head())
    html.encoding = "utf-8"
    soup = BeautifulSoup(html.text, "html.parser")
    l = []
    for i in soup.find_all('div', class_="video-data"):
        l += i.get_text("|", strip=True).split("|")
    if len(l)==3:
        l.append("")
    for i in soup.find_all('div', class_="ops"):
        l += i.get_text("|", strip=True).split("|")
    for i in soup.find_all('i', class_="van-icon-general_addto_s"):
        # print(i.parent.contents[2])
        x = re.findall(findNumber, str(i.parent.contents[2]))
        l.append(x[6])
    return l[0:8]
if __name__ == '__main__':
    main()