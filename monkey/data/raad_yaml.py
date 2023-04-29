import yaml, os


path1 = os.path.abspath('../config/config.yaml')
print   (path1)

class OpenYaml:

    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = './config/config.yaml'
        self.data = self.getdata ()

    def getdata(self):
        # 读取yaml的值
        with open ( self.file_name, 'r', encoding='utf-8' ) as f:
            self.data = yaml.load ( f, Loader=yaml.FullLoader )
            return self.data


if __name__ == '__main__':
    tt = OpenYaml ()
    print ( tt.getdata ()['data']['phone'] )