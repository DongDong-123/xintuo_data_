# -*- coding: utf-8 -*-
# @Time    : 2020-06-24 22:14
# @Author  : liudongyang
# @FileName: run.py
# @Software: PyCharm
# 启动文件
from parm import datannum, zip_floder
from schedule import main
import os
import zipfile
import time
import datetime
from Common import CommonFunction
comm = CommonFunction()

current_path = os.getcwd()


def get_parm():
    with open(os.path.join(current_path, 'parm.txt'), 'r', encoding='utf-8') as f:
        res = f.read()

    parm = res.split(',')
    n = int(parm[0])
    t = int(parm[1])


    return n, t


def updtae_parm(n, pt):
    """执行完后，写入最新的编号和跑批日期"""
    # pt = process_time(pt)
    with open(os.path.join(current_path, 'parm.txt'), 'w', encoding='utf-8') as f:
        f.write("{},{}".format(n, pt))


def running():
    n, t = get_parm()
    start_time = time.time()
    o = datannum
    t = 20200920
    for m in range(1):
        print('客户号起始编号{}'.format(n))
        print('数据交易日期{}'.format(t))
        # st = datetime.datetime.strptime(str(t), "%Y%m%d")
        # file_date_time = str(st)[:10]
        file_date_time = str(t)
        # stif_time = "{}100000".format(t)
        stif_time = "{}".format(t)

        main(n, n + o, stif_time, file_date_time)
        n += o
        t += 1
        t = int(comm.process_time(t))  # 处理日期

        # 添加控制文件
        with open(os.path.join(zip_floder,'{}.txt'.format(file_date_time)), 'w') as f:
            pass

    end_time = time.time()
    print("执行时间：", end_time - start_time)  # 13

    updtae_parm(n, t)


if __name__ == "__main__":
    running()