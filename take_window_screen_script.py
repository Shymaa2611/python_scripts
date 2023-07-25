import autopy
msg="screen shot using python"
sub="screen shot"
program=autopy.alert.alert(msg,sub,"ok","cancel")
if program==True:
    sc=autopy.bitmap.capture_screen()
    sc.save("D:\\Django\\DjangoProject\\pythonProject\\photo.png")
else:
    print('close')