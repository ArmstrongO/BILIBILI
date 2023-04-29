# 这段代码实现的是从服务器上获取m3u8文件并将其保存到本地的功能
# 首先导入requests、os、json和urllib3等Python库
import requests
import os
import json
import urllib3

# 设置请求的header
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Accept': 'application/json, text/plain, */*'
}

# 设置文件保存的路径
save_path = ''


# 定义一个函数用来获取请求到的JSON数据并返回
def get_json(url_pre, tag_id, url_fix):
    url = url_pre + tag_id + url_fix
    # 忽略SSL证书检查
    urllib3.disable_warnings ()
    # 发送请求
    request = requests.get ( url=url, headers=header, verify=False )
    # 解析JSON数据并返回
    json_data = json.loads ( request.text )
    return json_data


# 定义一个函数用来创建文件夹并在文件夹中创建一个txt文件
def creat_text(book_name, path):
    global save_path
    # 设置文件夹路径
    save_path = path + "/" + book_name
    # 如果文件夹不存在则创建它，存在则什么都不做
    os.makedirs ( save_path, exist_ok=True )
    # 设置txt文件路径
    text_path = save_path + '/' + book_name + '.txt'

    # 如果txt文件已存在，则清空文件内容，重新写入
    if os.path.exists ( text_path ):
        with open ( text_path, 'a', encoding="utf-8" ) as f:
            f.seek ( 0 )
            f.truncate()

    # 写入文件头
    with open(text_path, 'a', encoding="utf-8") as f:
        f.write('#OUT,' + save_path + '\n')



# 定义一个函数用来将课程数据写入txt文件中
def write_text(course_id, book_name, course_name):
    # 定义请求URL的前缀和后缀
    course_url_pre = 'https://s-file-1.ykt.cbern.com.cn/zxx/s_course/v1/x_class_hour_activity/'
    course_url_fix = '/resources.json'
    # 获取课程数据
    course_data = get_json ( course_url_pre, course_id, course_url_fix )
    # 获取课程的m3u8链接
    course_m3u8 = course_data[0]['video_extend']['urls'][-1]['urls'][0]
    # 将课程名和m3u8链接拼接为字符串
    down_msg = course_name + ',' + course_m3u8 + '\n'
    # 设置txt文件路径
    text_path = save_path + '/' + book_name + '.txt'
    # 将数据写入txt文件
    with open ( text_path, 'a', encoding="utf-8" ) as f:
        f.write ( down_msg )


#定义一个函数用来获取m3u8链接数据
def get_m3u8(tag_id, path):
    #定义请求URL的前缀和后缀
    tag_url_pre = 'https://s-file-1.ykt.cbern.com.cn/zxx/s_course/v2/business_courses/'
    tag_url_fix = '/course_relative_infos/zh-CN.json'
    #获取课程数据
    tag_data = get_json(tag_url_pre, tag_id, tag_url_fix)
    #获取活动集ID
    activity_set_id = tag_data['course_detail']['activity_set_id']
    #定义请求URL的前缀和后缀
    activity_url_pre = 'https://s-file-1.ykt.cbern.com.cn/zxx/s_course/v2/activity_sets/'
    activity_url_fix = '/fulls.json'
    #获取活动集数据
    activity_data = get_json(activity_url_pre, activity_set_id, activity_url_fix)
    #获取书名
    book_name = activity_data['activity_set_name']
    #获取节点列表
    nodes = activity_data['nodes']
    #根据书名和保存路径创建txt文件夹
    creat_text(book_name, path)
    #遍历节点列表获取每个课程信息
    for child_nodes in nodes:
        first_title = child_nodes['node_name'].split()[0] if ' ' in child_nodes['node_name'] else ''
        first_title = first_title + ' ' if first_title else ''
        for course_nodes in child_nodes['child_nodes']:
            if course_nodes['child_nodes']:
                sec_title = course_nodes['node_name'].split()[0] if ' ' in course_nodes['node_name'] else ''
                sec_title = sec_title + ' ' if sec_title else ''
                for course_node in course_nodes['child_nodes']:
                    course_id = course_node['node_id']
                    course_name = first_title + sec_title + course_node['node_name']
                    course_name = course_name.replace(',', ' ')
                    print(course_name)
                    write_text(course_id, book_name, course_name)
            else:
                course_id = course_nodes['node_id']
                course_name = first_title + course_nodes['node_name']
                course_name = course_name.replace(',', ' ')
                print(course_name)
                write_text(course_id, book_name, course_name)

print ( "------半自动下载国家云平台m3u8格式视频课程-------\n" )
path = input ( '请输入【课程视频】保存路径：' )
tag_id = input ( '请输入需要下载的课程ID：' )
get_m3u8 ( tag_id, path )
input ( '抓取完毕，按任意键关闭窗口。' )