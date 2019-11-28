from time import sleep
from random import randint
from PIL import Image
from TwitterAPI import TwitterAPI
 
MY_CONSUMER_KEY = 'yq78Nj71e0UdRvZcVC7o7i5WR'
MY_CONSUMER_SECRET = 'ya2reRyP2SA5i73oNxYpL08IatLeMSheAgKiMYLfuhP0aB8QMI'
MY_ACCESS_TOKEN_KEY = '948586183302533120-vnR9WW3gD94d6ZHeHiheqZlJsj5GRmD'
MY_ACCESS_TOKEN_SECRET = 'YV6iFwWGTJ6BvjWvZPM3KEMF7MlKALWGHoDJLHNHjsARx'
while True:
    linha1 = 0
    linha2 = 482
    background = Image.open('background.jpg')
    
    for c in range (1,7):
        party = randint(0,151)
        time = Image.open(f'{party}.jpg')
        if c <= 3:
            background.paste(time,(linha1,0))
            linha1 += 483
        else:
            background.paste(time,(linha2,490))
            linha2 += 483
        background.save('time.jpg')

    timecompleto = open('time.jpg','rb')
    data = timecompleto.read()
    api = TwitterAPI(MY_CONSUMER_KEY, MY_CONSUMER_SECRET, MY_ACCESS_TOKEN_KEY, MY_ACCESS_TOKEN_SECRET)
    r = api.request('statuses/update_with_media', {'status':''}, {'media[]':data})
    print(r.status_code)
    sleep(60)



