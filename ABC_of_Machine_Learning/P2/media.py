#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 001/9/1/17 10:47
# @Author  : Hooper Chao @ SHOU
# @File    : media
# @Software: PyCharm
import webbrowser as wb


class Movie:
    """A class about movie factory."""
    def __init__(self, title, year_of_released, director, type, story_line, poster, trailer):
        """Initialize the properties of the class Movie."""
        self.title = title
        self.year_of_released = year_of_released
        self.director = director
        self.type = type
        self.story_line = story_line
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        """Show the trailer in web browser."""
        wb.open(self.trailer)
