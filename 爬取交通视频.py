from pytube import Playlist
import pafy
from multiprocessing import Pool
import os

class YoutubeVideoDownload():
    def __init__(self,video_path,list_url):
        self.video_path = video_path
        self.list_url = list_url

    def get_video_list(self):
        pl = Playlist(self.list_url)
        url_lists = pl.parse_links()
        data = ["https://www.youtube.com" + i for i in url_lists]
        return data


    def get_video_info(self,detail_url):
        print(detail_url)
        video = pafy.new(detail_url)
        v_best = video.getbest()
        v_best.download(self.video_path)


if __name__ == '__main__':
    p = Pool(4)
    video_path = "videos/Traffic CCTV"
    list_url = "https://www.youtube.com/watch?v=5_XSYlAfJZM"
    yotubo = YoutubeVideoDownload(video_path,list_url)
    res = p.map(yotubo.get_video_info, yotubo.get_video_list())