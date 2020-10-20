# -*- coding: utf-8 -*-
# @Time :  15:48
# @AUTHOR : yusheng
# @File : Challenge008.py
# @SoftWore : PyCharm
"""
http://www.pythonchallenge.com/pc/def/integrity.html
https://www.hackingnote.com/en/python-challenge-solutions/level-8
https://docs.python.org/zh-cn/3/library/bz2.html
bz2.decompress(data)
解压缩 data，此参数为一个 字节类对象。
"""
import bz2


un = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 '
                    b'\x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
pw = bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
print(un, pw)