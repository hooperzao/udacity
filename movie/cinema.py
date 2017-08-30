# -*- coding: utf-8 -*-
# @Time      : 030/8/30/17 11:50 AM
# @Author    : Hooper Chao
# @File      : cinema
# @Created by: PyCharm
import movie
import fresh_tomatoes as ft

guardians = movie.Movie('Guardians of the Galaxy', 'A sci-fi movie from Marvel',
                    'https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=ae7db5f4a9c3793169658e7b8aaddc20/e824b899a9014c08b88b5f570c7b02087af4f494.jpg',
                    'http://v.youku.com/v_show/id_XMjk2ODgxNjk1Mg==.html?spm=a2hww.20023042.md223508.1~3!5~5~5~A')
your_name = movie.Movie('Your Name', 'A Japanese animation movie',
                        'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=f223d39dfa1fbe090853cb460a096756/cb8065380cd791231e35789fa5345982b3b78000.jpg',
                        'http://v.youku.com/v_show/id_XMjk4NzA1OTMzNg==.html?spm=a2hmv.20009921.posterMovieGrid86981.5~5~5~1~3!2~A&lang=%E5%9B%BD%E8%AF%AD')
spider_man = movie.Movie('Spider Man', 'A sci-fi movie from Marvel',
                        'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike272%2C5%2C5%2C272%2C90/sign=a737f591871001e95a311c5dd9671089/95eef01f3a292df5e405106db6315c6035a87387.jpg',
                        'http://v.youku.com/v_show/id_XMjk4Mzc5MTg1Mg==.html?from=y1.2-2.2')
wolf_warrior = movie.Movie('Wolf Warrior 2', 'Action movie from China',
                     'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=3d0251fc5c4e9258b2398ebcfdebba3d/4610b912c8fcc3cef7dc70ab9845d688d43f200d.jpg',
                     'http://v.youku.com/v_show/id_XMjg2OTA2MDM2MA==.html?spm=a2h1n.8261147.around_2.5~5!3~5~5~A')
mif = movie.Movie('Mission Impossible', 'An agent movie about Ethan',
                     'https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign=a54e5370b18f8c54f7decd7d5b404690/18d8bc3eb13533fa889406b0add3fd1f41345b09.jpg',
                     'http://v.youku.com/v_show/id_XMTQwNTUzNjgwMA==.html?from=y1.3-movie-grid-1095-9921.217752.2-1')
cars = movie.Movie('Cars 3', 'An automation movie produced by Walter Disney',
                     'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=a418f3fe2c9759ee5e5d6899d3922873/023b5bb5c9ea15ce9a3177fabc003af33b87b262.jpg',
                     'http://v.youku.com/v_show/id_XMTgzMDA4ODgyMA==.html?spm=a2h1n.8261147.around_2.5~5~5~1!2~3~A')
movies = [guardians, your_name, spider_man, wolf_warrior, mif, cars]
ft.open_movies_page(movies)

