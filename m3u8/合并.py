import os


# def mixTss(name):
#     # string前面加上‘r’,是为了告诉编译器这个string是个raw string，不要转义 backslash '\' 。
#     com = r'C:\Users\Administrator\Downloads\M3U8 1.4.7 1114\ffmpeg.exe -f concat -safe 0 -i D:\\ProgramData\\study\\mov\\order.m3u8 -c copy D:\\ProgramData\\study\\mov\\{}.mp4'.format (
#         name )
#     os.system ( com )
#
#
# mixTss ( "hello" )
# print ( "合并完成！" )

read = open(r"C:\Users\Administrator\Documents\WeChat Files\wxid_ldlrwdz67qja21\FileStorage\File\2023-04\2095da82b67988a18a3049b29f49eeee.key", "r")
s = read.readlines()
print(s)