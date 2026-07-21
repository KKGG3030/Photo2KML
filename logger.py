# -*- coding: utf-8 -*-
"""
logger.py
Photo2KML 日志模块
"""

import logging
import os


LOG_NAME = "Photo2KML.log"


def init_logger(log_dir=None):
    """
    初始化日志

    Parameters
    ----------
    log_dir : str
        日志目录，默认程序当前目录

    Returns
    -------
    logging.Logger
    """

    if log_dir is None:
        log_dir = os.getcwd()

    log_path = os.path.join(log_dir, LOG_NAME)

    logger = logging.getLogger("Photo2KML")

    # 防止重复初始化
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s  [%(levelname)s]  %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # 写入文件
    file_handler = logging.FileHandler(
        log_path,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # 同时输出到控制台
    console = logging.StreamHandler()

    console.setFormatter(formatter)

    logger.addHandler(console)

    logger.info("=" * 60)
    logger.info("Photo2KML 启动")
    logger.info("日志文件：%s", log_path)

    return logger


def close_logger(logger):
    """
    关闭日志
    """

    handlers = logger.handlers[:]

    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)