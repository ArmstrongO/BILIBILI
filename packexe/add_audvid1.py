import os

while 1:
    audio1=input("by:木子 v1.0版\n请输入audio文件名称\n例如：audio1.mp4")
    video=input("请输入video文件名称\n例如：video.mp4")
    output=input("请输入输出文件名称\n例如：output.mp4")
    file1 = audio1
    file2 = video
    result = output
    os.system(f"ffmpeg.exe -i {file1} -i {file2} -acodec copy -vcodec copy {result}")



# 将audio1.mp4 与 video.mp4合并 输出output.mp4
# ffmpeg.exe -i audio1.mp4 -i video.mp4 -acodec copy -vcodec copy output.mp4
