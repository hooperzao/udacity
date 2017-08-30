# -*- coding: utf-8 -*-
# @Time      : 030/8/30/17 11:48 AM
# @Author    : Hooper Chao
# @File      : movie
# @Created by: PyCharm
import webbrowser as wb


class Movie():
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        wb.open(self.trailer_youtube_url)

