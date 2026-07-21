# -*- coding: utf-8 -*-
"""
utils.py
公共工具函数
Photo2KML v2.1
"""

import math
import datetime


# --------------------------------------------------
# EXIF GPS 转 十进制度
# --------------------------------------------------
def gps_to_decimal(values):
    """
    EXIF GPS -> Decimal Degrees

    Parameters
    ----------
    values : exifread.utils.Ratio list

    Returns
    -------
    float
    """

    d = float(values[0].num) / float(values[0].den)
    m = float(values[1].num) / float(values[1].den)
    s = float(values[2].num) / float(values[2].den)

    return d + m / 60 + s / 3600


# --------------------------------------------------
# 解析照片时间
# --------------------------------------------------
def parse_time(time_str):
    """
    兼容多种EXIF时间格式
    """

    if not time_str:
        return None

    formats = [

        "%Y:%m:%d %H:%M:%S",

        "%Y-%m-%d %H:%M:%S",

        "%Y/%m/%d %H:%M:%S",

        "%Y:%m:%d %H:%M:%S%z"

    ]

    for fmt in formats:

        try:
            return datetime.datetime.strptime(
                time_str,
                fmt
            )

        except:
            pass

    return None


# --------------------------------------------------
# Haversine计算距离（米）
# --------------------------------------------------
def distance(lat1, lon1, lat2, lon2):
    """
    返回两GPS点之间距离（米）
    """

    R = 6378137.0

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        +
        math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return R * c


# --------------------------------------------------
# 格式化时间
# --------------------------------------------------
def format_time(dt):
    """
    datetime -> 字符串
    """

    if dt is None:
        return ""

    return dt.strftime("%Y-%m-%d %H:%M:%S")


# --------------------------------------------------
# 是否照片文件
# --------------------------------------------------
def is_photo(filename):

    ext = filename.lower()

    return ext.endswith(

        (
            ".jpg",
            ".jpeg",
            ".heic",
            ".tif",
            ".tiff",
            ".png"
        )

    )


# --------------------------------------------------
# 获取文件大小（MB）
# --------------------------------------------------
def file_size(path):

    import os

    return round(
        os.path.getsize(path) / 1024 / 1024,
        2
    )


# --------------------------------------------------
# 当前时间
# --------------------------------------------------
def now():

    return datetime.datetime.now()


# --------------------------------------------------
# 打印分隔线
# --------------------------------------------------
def line():

    print("-" * 60)


# --------------------------------------------------
# 排序
# --------------------------------------------------
def sort_photos(photo_list):
    """
    按时间排序
    """

    return sorted(
        photo_list,
        key=lambda x: x["time"]
    )


# --------------------------------------------------
# 统计
# --------------------------------------------------
def statistics(photo_list):

    total = len(photo_list)

    if total == 0:

        return {
            "count": 0
        }

    return {

        "count": total,

        "first": photo_list[0]["time"],

        "last": photo_list[-1]["time"]

    }