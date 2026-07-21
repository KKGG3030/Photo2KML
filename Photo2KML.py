# -*- coding: utf-8 -*-
"""
Photo2KML.py

Photo2KML v2.1

照片GPS生成:
    KML
    GPX
    CSV

"""

import os
import sys
import time

from datetime import datetime
from logger import init_logger
from exif_reader import scan_folder
from exporter import export_all



VERSION = "2.1"



# ==================================================
# 获取程序目录
# ==================================================

def get_app_path():

    """
    获取程序运行目录

    兼容:
    python运行
    exe运行
    """

    if getattr(
        sys,
        "frozen",
        False
    ):

        return os.path.dirname(
            sys.executable
        )

    else:

        return os.path.dirname(
            os.path.abspath(__file__)
        )




# ==================================================
# 主程序
# ==================================================

def main():


    start_time = time.time()


    # 当前目录

    app_path = get_app_path()
# 输出目录

    output_path = os.path.join(
        app_path,
        "Photo2KML_Output_" +
    datetime.now().strftime("%Y%m%d_%H%M%S")
        )


    # 不存在则创建

    if not os.path.exists(output_path):

        os.makedirs(
            output_path
        )         



    # 日志

    logger = init_logger(
        output_path
    )


    logger.info(
        "Photo2KML v%s",
        VERSION
    )


    logger.info(
        "扫描目录: %s",
        app_path
    )



    print()

    print(
        "=" * 60
    )

    print(
        " Photo2KML v",
        VERSION
    )

    print(
        "=" * 60
    )



    try:


        # --------------------------
        # 扫描照片
        # --------------------------

        logger.info(
            "开始扫描照片..."
        )


        photos = scan_folder(
            app_path
        )


        if len(photos) == 0:


            logger.warning(
                "没有找到有效GPS照片"
            )


            print(
                "\n没有找到包含GPS信息的照片"
            )


            try:
               print("\n程序结束")
            except EOFError:
                pass

            return



        logger.info(
            "有效照片数量: %s",
            len(photos)
        )



        print()

        print(
            "有效照片:",
            len(photos)
        )



        # --------------------------
        # 导出
        # --------------------------

        logger.info(
            "开始生成文件..."
        )


        export_all(
            photos,
            output_path
        )


        # --------------------------
        # 统计
        # --------------------------

        cost = (
            time.time()
            -
            start_time
        )


        logger.info(
            "完成，耗时 %.2f 秒",
            cost
        )


        print()

        print(
            "=" * 60
        )

        print(
            "生成完成!"
        )

        print()

        print(
            "输出目录:"
        )

        print(
            app_path
        )

        print()

        print(
            "文件:"
        )

        print(
            "  Photos.kml"
        )

        print(
            "  Photos.gpx"
        )

        print(
            "  PhotoLocations.csv"
        )

        print()

        print(
            "耗时:",
            round(cost,2),
            "秒"
        )

        print(
            "=" * 60
        )



        logger.info(
            "程序正常结束"
        )



    except Exception as e:


        logger.exception(
            "程序异常"
        )


        print()

        print(
            "发生错误:"
        )

        print(
            e
        )



    print("\n程序结束")




if __name__ == "__main__":

    main()