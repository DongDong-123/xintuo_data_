# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 17:43
# @Author  : liudongyang
# @FileName: process_data.py
# @Software: PyCharm
import os

file_name_list = ["account", "address", "apply_contract", "beneficiary", "cert", "contact", "contract_balance", "organization", "person", "relation", "transaction", "trust_contract"]


def get_file_list():
    """
    读取文件列表，拼接全路径，返回列表
    :return:
    """
    path = "E:\\0工作\\外贸信托\\数据\\信托数据\\新建文件夹"
    file_list = os.listdir(path)

    full_files = [os.path.join(path,file) for file in file_list]
    full_files.pop(0)
    return full_files


def read_file(file):
    """
    读数据
    :param file:
    :return:
    """
    with open(file, 'r',encoding='utf-8') as f:
        data_line = f.readlines()
    title = data_line.pop(0)

    return data_line, title


def write_data(data, filename):
    """
    写入文件
    :param data:
    :param filename:
    :return:
    """
    with open(filename, '+a',encoding='utf-8') as f:
        f.writelines(data)


def process_account_data(data_lines, titles, date):
    """
    处理account
    :param data_lines:
    :param titles: CSNM|CSTP|CATP|CATP_ORI|CBCN|CTNM|CBNM|CABA|IDFT|RSCD
    :param file_name:
    :return:
    """
    file = 'account_20190520.txt'
    new_name = "account_{}.txt".format(date)
    datas, titles = read_file(file)
    save_datas = []
    save_datas.append(titles)

    for data in datas:
        data_list = data.split("|")
        data_list = [elem.strip() for elem in data_list]
        # 修改数据
        data_list[0] = ''

        save_datas.append("|".join(data_list))

    write_data(save_datas, new_name)



def process_contract_balance_data():
    pass

def run():
    full_list = get_file_list()
    for file in full_list:
        datas, title = read_file(file)
        process_account_data()



if __name__ == "__main__":
    # run()
    datas = ['1','2','3','4','5']
    write_data(datas, 'abc.txt')