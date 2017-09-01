#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 001/9/1/17 10:47
# @Author  : Hooper Chao @ SHOU
# @File    : entertainment_center
# @Software: PyCharm

import media as md
import fresh_tomatoes as ft


dunkirk = md.Movie(
    'Dunkirk',
    2017,
    'Christopher Nolan',
    'War',
    'Allied soldiers from Belgium, the British Empire and France are surrounded \
    by the German army and evacuated during a fierce battle in World War II.',
    'http://img5.mtime.cn/pi/2017/07/13/103450.79960035_1000X1000.jpg',
    'http://static1.mtime.cn/static/flash/outplayer.swf?vid=66563')

valerian = md.Movie(
    'Valerian',
    2017,
    'Luc Besson',
    'Sci-fi',
    'A dark force threatens Alpha, a vast metropolis and home to species from a \
    thousand planets. Special operatives Valerian and Laureline must race to identify \
    the marauding menace and safeguard not just Alpha, but the future of the universe.',
    'http://img5.mtime.cn/pi/2017/08/14/115211.32169432_1000X1000.jpg',
    'http://static1.mtime.cn/static/flash/outplayer.swf?vid=67128'
)

manchester = md.Movie(
    'Manchester by the Sea',
    2016,
    'Kenneth Lonergan',
    'Story',
    'A depressed uncle is asked to take care of his teenage nephew after the boy\'s father dies.',
    'http://img5.mtime.cn/pi/2017/08/09/101128.52954182_1000X1000.jpg',
    'http://static1.mtime.cn/static/flash/outplayer.swf?vid=62225'
)

cars3 = md.Movie(
    'Cars 3',
    2016,
    'Brian Fee',
    'Animation',
    'Lightning McQueen sets out to prove to a new generation of racers that he\'s \
    still the best race car in the world.',
    'http://img5.mtime.cn/pi/2017/01/10/155015.69219630_1000X1000.jpg',
    'http://static1.mtime.cn/static/flash/outplayer.swf?vid=66586'
)

spider_man = md.Movie(
    'Spider-Man: Homecoming',
    2017,
    'Jon Watts',
    'Sci-fi',
    'Peter Parker tries to balance his life as an ordinary high school \
    student in Queens with his superhero alter-ego Spider-Man, and must confront \
    a new menace prowling the skies of New York City.',
    'http://img5.mtime.cn/pi/2017/03/28/154939.57450149_1000X1000.jpg',
    'http://static1.mtime.cn/static/flash/outplayer.swf?vid=67381'
)

planet_of_the_apes = md.Movie(
    'The Planet of the Apes',
    2017,
    'Matt Reeves',
    'Sci-fi',
    'After the apes suffer unimaginable losses, Caesar wrestles with his darker \
    instincts and begins his own mythic quest to avenge his kind.',
    'http://img5.mtime.cn/pi/2017/03/31/145152.18675846_1000X1000.jpg',
    'http://static1.mtime.cn/static/flash/outplayer.swf?vid=67010'
)
movies = [dunkirk, valerian, manchester, cars3, spider_man, planet_of_the_apes]
ft.open_movies_page(movies)
