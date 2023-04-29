import requests
import os
import json
import urllib3

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Accept': 'application/json, text/plain, */*'
}
save_path = ''


def get_json(url_pre, tag_id, url_fix):
    url = url_pre + tag_id + url_fix
    urllib3.disable_warnings ()
    request = requests.get ( url=url, headers=header, verify=False )
    json_data = json.loads ( request.text )
    return json_data


def creat_text(book_name, path):
    global save_path
    save_path = path + "/" + book_name
    os.makedirs ( save_path, exist_ok=True )
    text_path = save_path + '/' + book_name + '.txt'
    if os.path.exists ( text_path ):
        with open ( text_path, 'a', encoding="utf-8" ) as f:
            f.seek ( 0 )
            f.truncate ()
    with open ( text_path, 'a', encoding="utf-8" ) as f:
        f.write ( '#OUT,' + save_path + '\n' )


def write_text(course_id, book_name, course_name):
    course_url_pre = 'https://s-file-1.ykt.cbern.com.cn/zxx/s_course/v1/x_class_hour_activity/'
    course_url_fix = '/resources.json'
    course_data = get_json ( course_url_pre, course_id, course_url_fix )
    course_m3u8 = course_data[0]['video_extend']['urls'][-1]['urls'][0]
    down_msg = course_name + ',' + course_m3u8 + '\n'
    text_path = save_path + '/' + book_name + '.txt'
    with open ( text_path, 'a', encoding="utf-8" ) as f:
        f.write ( down_msg )


def get_m3u8(tag_id, path):
    tag_url_pre = 'https://s-file-1.ykt.cbern.com.cn/zxx/s_course/v2/business_courses/'
    tag_url_fix = '/course_relative_infos/zh-CN.json'
    tag_data = get_json ( tag_url_pre, tag_id, tag_url_fix )
    activity_set_id = tag_data['course_detail']['activity_set_id']
    activity_url_pre = 'https://s-file-1.ykt.cbern.com.cn/zxx/s_course/v2/activity_sets/'
    activity_url_fix = '/fulls.json'
    activity_data = get_json ( activity_url_pre, activity_set_id, activity_url_fix )
    book_name = activity_data['activity_set_name']
    nodes = activity_data['nodes']
    creat_text ( book_name, path )
    for child_nodes in nodes:
        first_title = child_nodes['node_name'].split ()[0] if ' ' in child_nodes['node_name'] else ''
        first_title = first_title + ' ' if first_title else ''
        for course_nodes in child_nodes['child_nodes']:
            if course_nodes['child_nodes']:
                sec_title = course_nodes['node_name'].split ()[0] if ' ' in course_nodes['node_name'] else ''
                sec_title = sec_title + ' ' if sec_title else ''
                for course_node in course_nodes['child_nodes']:
                    course_id = course_node['node_id']
                    course_name = first_title + sec_title + course_node['node_name']
                    course_name = course_name.replace ( ',', ' ' )
                    print ( course_name )
                    write_text ( course_id, book_name, course_name )

            else:
                course_id = course_nodes['node_id']
                course_name = first_title + course_nodes['node_name']
                course_name = course_name.replace ( ',', ' ' )
                print ( course_name )
                write_text ( course_id, book_name, course_name )


print ( "------半自动下载国家云平台m3u8格式视频课程-------\n" )
path = input ( '请输入【课程视频】保存路径：' )
tag_id = input ( '请输入需要下载的课程ID：' )
get_m3u8 ( tag_id, path )
input ( '抓取完毕，按任意键关闭窗口。' )