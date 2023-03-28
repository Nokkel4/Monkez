import webbrowser
spamKey = True
limitKey = 1000
while spamKey == True:
    webbrowser.open('https://www.youtube.com/watch?v=Qm-f7r0SPiA&ab_channel=XLordxDuckyX')
    webbrowser.open('https://img1.picmix.com/output/stamp/normal/2/5/3/8/2318352_13db3.gif')
    webbrowser.open('https://media1.giphy.com/media/swpCsxJSgSCxq/giphy.gif')
    if limitKey != 0:
        limitKey -= 1
    elif limitKey == 0:
        spamKey == False
        quit()
    elif limitKey == "Stop":
        print("It is a infinite code. Caution")