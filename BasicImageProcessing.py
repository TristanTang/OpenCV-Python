#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/25 17:19
# @Author  : TangWang
# @Site    : 
# @File    : BasicImageProcessing.py
# @Software: PyCharm

import cv2

image = cv2.imread('img/tangwang.jpg')

cv2.namedWindow('a_window', cv2.WINDOW_AUTOSIZE)

font = cv2.text

cv2.imshow('a_window', image)
cv2.imwrite('img/tangwang1.jpg', image)

cv2.waitKey(0)