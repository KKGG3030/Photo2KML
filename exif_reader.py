# -*- coding: utf-8 -*-
"""
exif_reader.py

Photo2KML v2.1
照片EXIF读取模块
"""

import os
import exifread

from utils import (
    gps_to_decimal,
    parse_time,
    is_photo
)


# ==================================================
# 读取单张照片
# ==================================================

def read_photo(path):
    """
    读取单张照片EXIF信息

    返回:
    {
        file,
        path,
        time,
        lat,
        lon,
        camera
    }

    失败返回 None
    """

    try:

        with open(
            path,
            "rb"
        ) as f:

            tags = exifread.process_file(
                f,
                details=False
            )


        # --------------------------
        # GPS检查
        # --------------------------

        if (
            "GPS GPSLatitude" not in tags
            or
            "GPS GPSLongitude" not in tags
        ):
            return None


        lat = gps_to_decimal(
            tags[
                "GPS GPSLatitude"
            ].values
        )


        lon = gps_to_decimal(
            tags[
                "GPS GPSLongitude"
            ].values
        )


        # 南纬
        if (
            "GPS GPSLatitudeRef" in tags
            and
            tags[
                "GPS GPSLatitudeRef"
            ].printable == "S"
        ):
            lat = -lat


        # 西经
        if (
            "GPS GPSLongitudeRef" in tags
            and
            tags[
                "GPS GPSLongitudeRef"
            ].printable == "W"
        ):
            lon = -lon



        # --------------------------
        # 时间
        # --------------------------

        photo_time = None


        if "EXIF DateTimeOriginal" in tags:

            time_str = str(
                tags[
                    "EXIF DateTimeOriginal"
                ]
            )

            photo_time = parse_time(
                time_str
            )


        # 如果没有EXIF时间
        # 使用文件修改时间

        if photo_time is None:

            photo_time = (
                __import__(
                    "datetime"
                )
                .datetime
                .fromtimestamp(
                    os.path.getmtime(path)
                )
            )


        # --------------------------
        # 相机型号
        # --------------------------

        camera = ""


        if "Image Model" in tags:

            camera = str(
                tags[
                    "Image Model"
                ]
            )


        return {

            "file":
                os.path.basename(path),

            "path":
                path,

            "time":
                photo_time,

            "lat":
                lat,

            "lon":
                lon,

            "camera":
                camera

        }


    except Exception as e:

        print(
            "读取失败:",
            path,
            e
        )

        return None



# ==================================================
# 扫描目录
# ==================================================

def scan_folder(folder):
    """
    递归扫描照片目录

    返回照片列表
    """

    photos = []


    total = 0


    for root, dirs, files in os.walk(folder):


        for filename in files:


            if not is_photo(filename):

                continue


            total += 1


            path = os.path.join(
                root,
                filename
            )


            photo = read_photo(
                path
            )


            if photo:


                photos.append(
                    photo
                )



    # 按时间排序

    photos.sort(
        key=lambda x:x["time"]
    )


    print(
        "扫描照片:",
        total
    )

    print(
        "有效GPS:",
        len(photos)
    )


    return photos



# ==================================================
# 测试
# ==================================================

if __name__ == "__main__":


    folder = os.getcwd()


    result = scan_folder(
        folder
    )


    for p in result[:10]:

        print(
            p
        )