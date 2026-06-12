from pytubefix import YouTube

# YouTube(url).streams.get_highest_resolution().download()
# 將網址 url 的 youtube 影片以最高畫質存檔，預設檔名為影片標題
YouTube("網址").streams.get_highest_resolution().download()