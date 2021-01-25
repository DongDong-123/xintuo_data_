# -*- coding: utf-8 -*-
# @Time    : 2020-06-25 11:37
# @Author  : liudongyang
# @FileName: schedule.py
# @Software: PyCharm
# 任务调度
import threading
import time
import os
from make_data import MakeData
from save_data import SaveFile
from parm import savenum, stifnum, filenum, zip_floder
from Common import CommonFunction
comm = CommonFunction()
savedata = SaveFile()
# 临时存储生成数据
orgs = []
persons = []
certs = []
addresss = []
contacts = []
relations = []
banks = []
trust_conts = []
beneficiarys = []
app_conts = []
contracts = []
trades = []
# data_path = os.path.join(zip_floder, 'data')
data_path = zip_floder


def person(num, file_date_time):
    currt_time = time.strftime('%Y%m%d', time.localtime())
    makedata = MakeData('1',file_date_time)
    person = makedata.make_person(num)
    persons.append(person)
    cert = makedata.make_cert()
    certs.append(cert)
    address = makedata.make_address()
    addresss.append(address)
    contact = makedata.make_connect()
    contacts.append(contact)
    relation = makedata.make_relation()
    relations.append(relation)
    bank = makedata.make_account()
    banks.append(bank)
    trust_cont = makedata.make_trust_contract(num)
    trust_conts.append(trust_cont)
    beneficiary = makedata.make_beneficiary()
    beneficiarys.append(beneficiary)
    app_cont = makedata.make_apply_contract(num)
    app_conts.append(app_cont)
    contract = makedata.make_contract_balance()
    contracts.append(contract)
    trade = makedata.make_transaction()
    trades.append(trade)



def org(num, file_date_time):
    currt_time = time.strftime('%Y%m%d', time.localtime())
    makedata = MakeData('2',file_date_time)
    org = makedata.make_org(num)
    orgs.append(org)
    cert = makedata.make_cert()
    certs.append(cert)
    address = makedata.make_address()
    addresss.append(address)
    contact = makedata.make_connect()
    contacts.append(contact)
    relation = makedata.make_relation()
    relations.append(relation)
    bank = makedata.make_account()
    banks.append(bank)
    trust_cont = makedata.make_trust_contract(num)
    trust_conts.append(trust_cont)
    beneficiary = makedata.make_beneficiary()
    beneficiarys.append(beneficiary)
    app_cont = makedata.make_apply_contract(num)
    app_conts.append(app_cont)
    contract = makedata.make_contract_balance()
    contracts.append(contract)
    trade = makedata.make_transaction()
    trades.append(trade)



def main(beg, end, stif_time, file_date_time):
    currt_time = time.strftime('%Y%m%d', time.localtime())
    # 日期格式转换
    stif_time = comm.turn_date10(stif_time)
    savetxt = SaveFile()
    # 存储文件
    data_list = [orgs, persons, certs, addresss, contacts, relations, banks, trust_conts, beneficiarys, app_conts,
                 contracts, trades]
    name_list = ["organization", "person", "cert", "address", "contact", "relation", "account", "trust_contract",
                 "beneficiary", "apply_contract", "contract_balance", "transaction"]

    stif_time = comm.turn_date10(stif_time)
    for num in range(beg, end):
        org(num, file_date_time)
        person(num, file_date_time)


    if len(orgs) % filenum == 0:
        for inde, data in enumerate(data_list):
            savetxt.write_to_txt(data, name_list[inde], file_date_time)

            for data_lists in data_list:
                data_lists.clear()
