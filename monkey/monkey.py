from data.raad_yaml import OpenYaml
import gevent
import os

def get_devices():
    command_result = ("adb devices")  # 执行adb命令用于判断设备是否连接正常
    mydevice = os.popen ( command_result )  # 执行adb 命令
    mystr = mydevice.read ()  # 获取命令后的内容
    splits = mystr[25:41]  # 获取设备号
    mal = OpenYaml ()  # 读取yaml 文件

    if splits in mal.getdata ()['data']['phone']:
        """
        phone：设备号 如果更换可在 yaml 文件中更改
        判断设备是否连接成功，如果未连接或者连接成功设备号不正确不执行~
        """
        print ( '设备连接正常，开始执行Monkey命令~' )
        MonkeyCmd = "adb shell monkey -p %s --pct-touch %s -v -v -v --ignore-crashes --ignore-timeouts %s - s %s --throttle %s  1>%s 2>%s" \
                    % (mal.getdata ()['data']['packages'],  # 测试的包名
                       mal.getdata ()['data']['touch'],  # 显示详细信息，随机执行80个事件
                       mal.getdata ()['data']['monkeyclickcount'],  # 点击次数
                       mal.getdata ()['data']['send'],  # 用于指定伪随机数生成器的seed值
                       mal.getdata ()['data']['throttle'],  # 事件的时延，单位是毫秒
                       mal.getdata ()['data']['path_text'],  # 运行日志保存路径
                       mal.getdata ()['data']['error'])  # 错误日志保存路径
        os.popen ( MonkeyCmd )
        """ 如果不执行某些事件，再命令行中注释掉，注意删除对应的 %s 值 """
        print ( '执行命令：', MonkeyCmd )

    else:
        print ( '设备链接失败，请检查设备连接后再试~/或设备号是否正确:', splits )


get_devices ()