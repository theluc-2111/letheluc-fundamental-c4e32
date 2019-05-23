from youtube_dl import YoutubeDL
from itune import dsach_bai_hat

def download(x,y):
    options = {'default_search': 'ytsearch','max_downloads': 1}
    dl = YoutubeDL(options)
    dl.download(x,'-',y)

for k in dsach_bai_hat:
    download(k['Song'],k['Singer'])