# -*- coding: utf-8 -*-
"""
exporter.py

Photo2KML v2.1

输出:
    Photos.kml
    Photos.gpx
    PhotoLocations.csv

"""


import csv
import os

import simplekml
import gpxpy
import gpxpy.gpx

from utils import format_time



# ==================================================
# CSV 导出
# ==================================================

def export_csv(
        photos,
        output="PhotoLocations.csv"
):

    """
    导出CSV
    """


    with open(
        output,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:


        writer = csv.writer(f)


        writer.writerow(
            [
                "文件名",
                "时间",
                "纬度",
                "经度",
                "相机",
                "路径"
            ]
        )


        for p in photos:


            writer.writerow(
                [
                    p["file"],

                    format_time(
                        p["time"]
                    ),

                    p["lat"],

                    p["lon"],

                    p.get(
                        "camera",
                        ""
                    ),

                    p["path"]
                ]
            )



    print(
        "CSV生成:",
        output
    )





# ==================================================
# GPX 导出
# ==================================================

def export_gpx(
        photos,
        output="Photos.gpx"
):

    """
    生成GPX轨迹
    """


    gpx = gpxpy.gpx.GPX()


    track = gpxpy.gpx.GPXTrack(
        name="Photo Track"
    )


    gpx.tracks.append(
        track
    )


    segment = gpxpy.gpx.GPXTrackSegment()


    track.segments.append(
        segment
    )



    for p in photos:


        point = gpxpy.gpx.GPXTrackPoint(

            latitude=p["lat"],

            longitude=p["lon"],

            time=p["time"]

        )


        segment.points.append(
            point
        )



    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:


        f.write(
            gpx.to_xml()
        )


    print(
        "GPX生成:",
        output
    )





# ==================================================
# KML 导出
# ==================================================

def export_kml(
        photos,
        output="Photos.kml"
):

    """
    Google Earth KML
    """



    kml = simplekml.Kml()



    # --------------------------
    # 创建轨迹线
    # --------------------------

    line = kml.newlinestring(

        name="Photo Route"

    )


    line.coords = [

        (
            p["lon"],
            p["lat"]
        )

        for p in photos

    ]


    line.style.linestyle.width = 4



    # --------------------------
    # 创建照片点
    # --------------------------

    folder = kml.newfolder(

        name="Photos"

    )



    for p in photos:


        point = folder.newpoint(

            name=p["file"]

        )


        point.coords = [

            (
                p["lon"],
                p["lat"]
            )

        ]



        point.description = (

            "<b>照片:</b>"

            + p["file"]

            + "<br>"

            +

            "<b>时间:</b>"

            +

            format_time(
                p["time"]
            )

            +

            "<br>"

            +

            "<b>坐标:</b>"

            +

            str(
                p["lat"]
            )

            +

            ","

            +

            str(
                p["lon"]
            )

        )



        if p.get(
            "camera",
            ""
        ):


            point.description += (

                "<br><b>相机:</b>"

                +

                p["camera"]

            )



    kml.save(
        output
    )


    print(
        "KML生成:",
        output
    )





# ==================================================
# 一键导出
# ==================================================

def export_all(
        photos,
        folder=None
):

    """
    一次生成全部文件
    """


    if folder is None:

        folder=os.getcwd()



    export_csv(

        photos,

        os.path.join(
            folder,
            "PhotoLocations.csv"
        )

    )


    export_gpx(

        photos,

        os.path.join(
            folder,
            "Photos.gpx"
        )

    )


    export_kml(

        photos,

        os.path.join(
            folder,
            "Photos.kml"
        )

    )



    print(
        "\n全部导出完成"
    )





# ==================================================
# 测试
# ==================================================

if __name__ == "__main__":

    print(
        "exporter.py 模块"
    )