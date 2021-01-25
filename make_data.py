# -*- coding: utf-8 -*-
# @Time    : 2020-06-24 22:18
# @Author  : liudongyang
# @FileName: make_data.py
# @Software: PyCharm
# 生成数据
from faker import Faker
from Common import CommonFunction
comm = CommonFunction()
fake = Faker(locale='zh_CN')


class MakeData:
    def __init__(self, cust_type,trade_time):
        self.CSNM = None
        self.CTNM = None
        self.cust_type = cust_type
        self.unit_code = None
        self.TCID = None
        self.data_date = trade_time
    def make_org(self, num):
        """
        机构数据
        :return:
        """
        self.CSNM = 'org_{}'.format(num)  # 客户号  必填,
        CCUP = comm.make_yes_no()  # 上游客户标识  1：是 0：否,
        CCMD = comm.make_yes_no()  # 中游客户标识  ,
        CCDW = comm.make_yes_no()  # 下游客户标识  ,
        CTTP = comm.make_CTTP_data()  # 客户类型  ,  01：法人;03：个体工商户；04：其他组织
        self.CTNM = comm.org_name()  # 客户名称  必填, 基本项
        CTEN = ''  # 拼音/英文名称  ,
        CITP = comm.cert_type('2')  # 证件类型（报送）  必填, 基本项
        CITP_ORI = CITP  # 证件类型（原值）  必填, 基本项
        CTID = comm.org_cert_num()  # 证件号码  必填, 基本项
        CIVT = comm.make_enable_date()  # 证件有效期  , 基本项
        RGTP = ''  # 登记注册类型  ,
        RGNO = ''  # 登记注册号  ,
        CTVC = comm.make_CTVC_data()  # 行业（报送）  必填, 基本项
        CTVC_ORI = comm.make_CTVC_data()  # 行业（原值）  必填, 基本项
        CRNM = comm.make_name_data(3)  # 法定代表人姓名  必填, 基本项
        CRNT = comm.chiose_country()  # 法定代表人国籍  必填, 基本项
        CRIT = comm.cert_type('1')  # 法定代表人证件类型（报送）  必填, 基本项
        CRIT_ORI = CRIT  # 法定代表人证件类型（原值）  必填, 基本项
        CRID = fake.ssn(min_age=24, max_age=56)  # 法定代表人证件号码  必填, 基本项
        CRVT = comm.make_enable_date()   # 法定代表人证件有效期  , 基本项
        CTNT = comm.chiose_country()  # 注册国家  ,
        FDDT = comm.make_date(beg=-20, end=-1)  # 成立日期  ,
        CPTL = '100000'  # 注册资金  ,
        CRCY = comm.make_tctp_data()  # 注册资金币种  ,
        PUCP = '100000'  # 实收资本  ,
        EECP = ''  # 企业经济成份  ,
        TAST = ''  # 企业总资产  ,
        TLBT = ''  # 企业总负债  ,
        ENUM = ''  # 企业人员规模  ,
        SCTP = ''  # 企业经济规模  ,
        CBSC = ''  # 经营范围  ,
        ABAN = comm.make_name_data(3)  # 授权办理人姓名  ,
        ABNT = comm.chiose_country()  # 授权办理人国籍  ,
        ABIT = comm.make_ABIT_data()  # 授权办理人证件类型（报送）  ,
        ABIT_ORI = ABIT  # 授权办理人证件类型（原值）  ,
        ABAI = fake.ssn(min_age=24, max_age=56)  # 授权办理人证件号码  ,
        ABVT = comm.make_enable_date()  # 授权办理人证件有效期限  ,
        ATEL = ''  # 授权办理人联系电话  ,
        ADNT = comm.chiose_country()  # 地区国家  必填,
        ADPV = ''  # 地区省  ,
        ADCT = ''  # 地区市  ,
        ADDC = ''  # 地区县  ,
        ADDR = comm.make_address()  # 详细地址  必填, 基本项
        PSCD = ''  # 邮编  ,
        LKNM = fake.name()  # 联系人姓名  ,
        LDUT = ''  # 联系人职务  ,
        CMBL = fake.phone_number()  # 手机  必填
        CTEL = comm.random_num(9)  # 固定电话  必填 基本项
        CEML = comm.make_email_data()  # 电子邮箱  ,
        CSIO = comm.make_yes_no()  # 是否境外  0:境内，1：境外,
        RLTP = ''  # 关联方类型  ,
        RGDT = comm.make_date(beg=-20, end=0)  # 开立日期  必填,
        CSDT = ''  # 注销日期  ,
        CHNL = comm.make_chnl_data()  # 建立渠道  必填,
        CMGR = comm.make_CMGR_data()  # 客户经理  ,
        ISCA = comm.make_yes_no()  # 是否合作机构  ,
        CCRK = ''  # 合作机构信用等级  ,
        CTGR = ''  # 合作机构分类  ,
        ACTP = ''  # 核算类型  ,
        CONM = ''  # 所属合作机构客户号  ,
        ISSB = comm.make_yes_no()  # 是否同业机构  1:是 0:否,
        ISMB = comm.make_yes_no()  # 是否托管行  1:是 0:否,
        ISIA = comm.make_yes_no()  # 是否投资顾问  1:是 0:否,
        ISLA = comm.make_yes_no()  # 是否贷款运用方  1:是 0:否,
        MBRC_ORI = comm.make_mbrc_ori_data()  # 管理机构（原值）  必填,
        CTST = comm.cust_status_2()  # 客户状态  必填,
        REMK = fake.sentence()  # 备注  ,
        RSCD = comm.make_RSCD_data()  # 来源系统编码  必填,
        BNNM = fake.name()  # 控股股东或实际控制人姓名  ,
        BITP = comm.make_ABIT_data()  # 控股股东或实际控制人证件类型（报送）  ,
        BITP_ORI = BITP  # 控股股东或实际控制人证件类型（原值）  ,
        BNID = fake.ssn(min_age=24, max_age=56)  # 控股股东或实际控制人证件号码  ,
        BIVT = comm.make_enable_date()  # 控股股东或实际控制人证件有效期  ,
        MBRC_MULTI = comm.make_MBRC_MULTI_data()  # 相关部门-存在多个部门，用逗号分隔  必填,
        BEON = comm.make_BEON_data()  # 受益所有人标识  ,1：有受益所有人 2：豁免
        EMRS = comm.make_EMRS_data()  # 豁免原因  ,

        all_col = [self.CSNM, CCUP, CCMD, CCDW, CTTP, self.CTNM, CTEN, CITP, CITP_ORI, CTID, CIVT, RGTP, RGNO, CTVC, CTVC_ORI, CRNM, CRNT, CRIT, CRIT_ORI, CRID, CRVT, CTNT, FDDT, CPTL, CRCY, PUCP, EECP, TAST, TLBT, ENUM, SCTP, CBSC, ABAN, ABNT, ABIT, ABIT_ORI, ABAI, ABVT, ATEL, ADNT, ADPV, ADCT, ADDC, ADDR, PSCD, LKNM, LDUT, CMBL, CTEL, CEML, CSIO, RLTP, RGDT, CSDT, CHNL, CMGR, ISCA, CCRK, CTGR, ACTP, CONM, ISSB, ISMB, ISIA, ISLA, MBRC_ORI, CTST, REMK, RSCD, BNNM, BITP, BITP_ORI, BNID, BIVT, MBRC_MULTI, BEON, EMRS]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_person(self, num):
        """
        个人数据
        :return:
        """
        self.CSNM = 'per_{}'.format(num)  # 客户号  必填，
        CCUP = comm.make_yes_no()  # 上游客户标识  ，
        CCMD = comm.make_yes_no()  # 中游客户标识  ，
        CCDW = comm.make_yes_no()  # 下游客户标识  ，
        CTNM = comm.make_name_data()  # 客户名称  必填，基本项
        CTEN = ''  # 拼音/英文名称  ，
        CITP = comm.make_ABIT_data()  # 证件类型（报送）  必填，
        CITP_ORI = CITP  # 证件类型（原值）  必填，基本项
        CTID = fake.ssn(min_age=24, max_age=56)  # 证件号码  必填，基本项
        CIVT = comm.make_enable_date()  # 证件有效期  必填，基本项
        CTSX = comm.make_CTSX_data()  # 性别  必填，基本项
        CTNT = comm.chiose_country()  # 国籍  必填，基本项
        CTNA = ''  # 民族  ，
        CTBD = comm.make_date(-40,-15)  # 出生日期  必填，基本项
        EDCT = ''  # 学历  ，
        CTVC = comm.make_CTVC_data2()  # 职业(报送)  ，
        CTVC_ORI = CTVC  # 职业(原值)  必填，基本项
        WKPL = ''  # 工作单位  ，
        WTVC = ''  # 工作行业  ，
        WKPS = ''  # 职位  ，
        PICM = ''  # 个人年收入  ，
        FICM = comm.random_num(6)  # 家庭年收入  ，
        MRGE = ''  # 婚姻状况  ，
        ADNT = comm.chiose_country()  # 地址国家  必填，
        ADPV = ''  # 地址省  ，
        ADCT = ''  # 地址市  ，
        ADDC = ''  # 地址区县  ，
        ADDR = fake.address()  # 详细地址  必填，基本项
        PSCD = ''  # 邮编  ，
        CMBL = fake.phone_number()  # 手机  必填，基本项
        CTEL = ''  # 固定电话  ，
        CEML = fake.email()  # 电子邮箱  ，
        CSIO = comm.make_yes_no_unused()  # 是否境外  必填， 1	境内， 0境外
        TRLV = ''  # 风险承受等级  ，
        RLTP = ''  # 关联方类型  必填，
        RGDT = comm.make_date(-20,-3)  # 开立日期  必填，
        CSDT = ''  # 注销日期  ，
        CHNL = comm.make_chnl_data()  # 建立渠道  必填，
        CMGR = comm.make_CMGR_data()  # 客户经理  必填，
        CONM = ''  # 所属合作机构的客戶号  ，
        MBRC_ORI = comm.make_mbrc_ori_data()  # 管理机构（原值）  必填，
        CTST = comm.make_yes_no()  # 客户状态  必填， 0失效,1生效
        REMK = ''  # 备注  ，
        RSCD = comm.make_RSCD_data()  # 来源系统编码  必填，
        MBRC_MULTI = comm.make_MBRC_MULTI_data()  # 相关部门-存在多个部门，用逗号分隔  必填，

        # all_col = [self.csnm, ctnm, ctsnm, cten, ctsen, busi_name, appli_country, sub_company, former_name, citp, citp_nt, ctid, ctid_edt, state, city, address, post_code, tel, fax, m_state, m_city, m_address, m_post_code, m_tel, m_fax, pr_mr_ms, pr_name, pr_title, pr_phone, pr_fax, pr_email, pr_address, sec_mr_ms, sec_name, sec_title, sec_phone, sec_fax, sec_email, sec_address, aml_mr_ms, aml_name, aml_title, aml_phone, aml_fax, aml_email, aml_address, client_tp, lfa_type, lfa_type_explain, fud_date, assets_size, country, other_oper_country, desc_business, tin, busi_type, ctvc, indu_code, indu_code_nt, crnm, crit, crit_nt, crid, crid_edt, reg_cptl, reg_cptl_code, remark_ctvc, eecp, scale, rgdt, cls_dt, unit_code, remark, stat_flag_ori, stat_flag, mer_unit, cmgr, act_cd, acc_type1, bank_acc_name, cabm, country_2, statement_type, reals, complex, clear, data_crdt, data_cruser, data_updt, data_upuser]
        all_col = [self.CSNM, CCUP, CCMD, CCDW, CTNM, CTEN, CITP, CITP_ORI, CTID, CIVT, CTSX, CTNT, CTNA, CTBD, EDCT, CTVC, CTVC_ORI, WKPL, WTVC, WKPS, PICM, FICM, MRGE, ADNT, ADPV, ADCT, ADDC, ADDR, PSCD, CMBL, CTEL, CEML, CSIO, TRLV, RLTP, RGDT, CSDT, CHNL, CMGR, CONM, MBRC_ORI, CTST, REMK, RSCD, MBRC_MULTI]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_cert(self):
        """证件信息"""
        CSNM = self.CSNM  # 客户号  必填
        CSTP = self.cust_type  # 客户类型  必填
        CITP = comm.make_ABIT_data()  # 证件类型（报送）  必填
        CITP_ORI = CITP  # 证件类型（原值）  必填  基本项
        CTID = fake.ssn(min_age=24, max_age=56)  # 证件号码  必填  基本项
        CIVT = comm.make_enable_date()  # 证件有效期  必填  基本项
        ISNT = ''  # 证件签发国家
        ISUT = ''  # 证件签发机关
        ISDT = ''  # 证件签发日期
        IDFT = '1'  # 是否主证件  必填
        RSCD = comm.make_RSCD_data()  # 来源系统编码  必填

        all_col = [CSNM, CSTP, CITP, CITP_ORI, CTID, CIVT, ISNT, ISUT, ISDT, IDFT, RSCD]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_address(self):
        """地址信息"""

        CSNM = self.CSNM  # 客户号 必填
        CSTP = self.cust_type  # 客户类型 必填
        ADTP = comm.make_address_type()  # 地址类型 必填
        LKNM = comm.make_name_data()  # 联系人姓名
        ADNT = 'CHN'  # 国家代码
        ADPV = ''  # 省代码
        ADCT = ''  # 市代码
        ADDC = ''  # 区县代码
        ADDR = comm.make_address()  # 详细地址 必填  基本项
        PSCD = ''  # 邮编
        IDFT = '1'  # 是否主地址 必填
        RSCD = comm.make_RSCD_data()  # 来源系统编码 必填

        all_col = [CSNM, CSTP, ADTP, LKNM, ADNT, ADPV, ADCT, ADDC, ADDR, PSCD, IDFT, RSCD]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_connect(self):
        """
        联系信息
        :return:
        """
        CSNM = self.CSNM  # 客户号 必填
        CSTP = self.cust_type  # 客户类型 必填
        LKNM = comm.make_name_data()  # 联系人姓名
        LDUT = ''  # 联系人职务
        CMBL = fake.phone_number()  # 手机
        CTEL = ''  # 固定电话
        CEML = fake.email()  # 电子邮箱
        CFAX = ''  # 传真
        IDFT = '1'  # 是否主联系 必填
        RSCD = comm.make_RSCD_data()  # 来源系统编码

        all_col = [CSNM, CSTP, LKNM, LDUT, CMBL, CTEL, CEML, CFAX, IDFT, RSCD]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_relation(self):
        """
        关系人表
        :return:
        """
        CSNM = self.CSNM  # 客户号  必填
        CSTP = self.cust_type  # 客户类型  必填
        RLTP = comm.make_RLTP_data()  # 关系类型  必填
        RCNM = ''  # 关系人客户号
        RCTP = self.cust_type  # 关系人类别  必填
        RLNM = comm.make_name_data(3)  # 关系人姓名/名称  必填
        RCNT = comm.chiose_country()  # 关系人国籍/国家
        RITP = comm.make_ABIT_data()  # 关系人证件类型(报送)
        RITP_ORI = RITP  # 关系人证件类型(原值)
        RTID = fake.ssn(min_age=24, max_age=56)  # 关系人证件号码
        RTVT = comm.make_enable_date()  # 关系人证件有效期
        RTEL = ''  # 关系人联系电话
        HPER = ''  # 持股比例
        HAMT = comm.make_hold_amt()  # 持股金额
        RSCD = comm.make_RSCD_data()  # 来源系统编码
        BLTP = ''  # 受益所有人所属类型
        RLAD = ''  # 关系人地址
        IS_AVAILABLE = '1'  # 是否有效

        all_col = [CSNM, CSTP, RLTP, RCNM, RCTP, RLNM, RCNT, RITP, RITP_ORI, RTID, RTVT, RTEL, HPER, HAMT, RSCD, BLTP, RLAD, IS_AVAILABLE]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_account(self):
        """银行信息"""
        CSNM = self.CSNM  # 客户号 必填
        CSTP = self.cust_type  # 客户类型 必填
        CATP_ORI = comm.make_bank_account_type()  # 银行账户类型(原值) 必填
        CATP = CATP_ORI  # 银行账户类型(报送) 必填
        CBCN = comm.random_num(18)  # 银行账户号 必填
        CTNM = comm.make_name_data()  # 银行账户名称 必填
        CBNM = comm.make_cabm_data()  # 银行账户开户行名称 必填
        CABA = '北京'  # 银行账户开户地
        IDFT = '1'  # 是否主账户 必填
        RSCD = comm.make_RSCD_data()  # 来源系统编码 必填

        all_col = [CSNM, CSTP, CATP, CATP_ORI, CBCN, CTNM, CBNM, CABA, IDFT, RSCD]
        return '|'.join([str(a) if a is not None else '' for a in all_col])

    def make_trust_contract(self, num):
        """
        资产委托合同
        :return:
        """
        TCSN = comm.random_num(20)  # 合同ID  必填
        TCTP = comm.make_TITP_data()  # 合同类型  必填
        TCNM = '资产委托合同名称{}'.format(num)  # 合同名称  必填
        PJNO = comm.random_str(5) + comm.random_num(10)  # 项目编号  必填
        PJNM = '资产委托合同项目名称{}'.format(num)  # 项目名称  必填
        PJTP = ''  # 项目类型
        CSTP = self.cust_type  # 委托人类别  必填  1:个人 2机构
        CTTP = comm.make_CTTP_data()  # 委托人类型
        CSNM = comm.random_num(15)  # 委托人客户号  必填
        COBN = comm.make_cabm_data()  # 委托人开户行名称  必填
        CATP = ''  # 委托人账号类型（报送）
        CATP_ORI = comm.make_BATP_ORI_data()  # 委托人账号类型（原值）  必填
        COAN = fake.bban()  # 委托人开户行账号  必填
        CADR = 'CHN100000'  # 委托人开户行所在地
        ABAN = fake.name()  # 授权业务办理人姓名
        ABIT = comm.make_ABIT_data()  # 授权业务办理人证件类型（报送）
        ABIT_ORI = ABIT  # 授权业务办理人证件类型（原值）
        ABAI = fake.ssn(min_age=24, max_age=56)  # 授权业务办理人证件号码
        ABVT = comm.make_enable_date()  # 授权业务办理人证件有效期
        SIDT = comm.make_date(-4,-1)  # 签订时间  必填
        EPDT = comm.make_date(-1,5)  # 到期时间  必填
        CPRD = comm.make_date()  # 合同期间  必填
        CCUR = comm.make_tctp_data()  # 合同币种  必填
        TAMT = comm.make_tcat_data()  # 合同金額/份额  必填
        CAMT = '20'  # 当前金額/份额  必填
        PMTD = comm.make_pmtd_data()  # 合同交付方式 01：资金结算；99：其他  必填
        CGTP = '1'  # 收费类型  必填
        IVST = comm.make_IVST_data()  # 资金投向  必填
        PCSF = ''  # 财产分类  必填
        CBTS = comm.make_CBTS_data()  # 出资财产来源  必填
        TPRS = comm.make_TPRS_data(CBTS)  # 出资财产来源说明
        TPDT = comm.make_date()  # 信托财产交付日期  必填
        BSTP = comm.make_bstp_data()  # 业务类型  必填
        BSKD = comm.make_bskd_data()  # 业务种类（受益类型）  必填
        TRTP = comm.make_trtp_data()  # 信托类型  必填
        CFNO = ''  # 初始委托合同号
        CLNO = ''  # 受益权来源合同号
        ZAMT = comm.make_hold_amt()  # 委托转让合同的转让金额
        ZFVL = ''  # 转让合同的公允价值
        RCMO = ''  # 推介来源机构
        RCMP = ''  # 推介地类型
        RCMD = ''  # 推介地名称
        SLMD = comm.make_SLMD_data()  # 销售方式  必填
        SCHN = comm.make_SCHN_data(SLMD)  # 销售途径  直销/代销  必填
        BPTP = ''  # 受益权类型
        BPNM = ''  # 受益权名称
        PYBR = ''  # 预期收益率
        TCST = comm.make_yes_no()  # 合同状态  1有效0无效 必填
        IMCN = ''  # 投资顾问或管理者客户号
        MBRC = comm.make_MBRC_data()  # 合同管理部门  必填
        TABN = comm.make_cabm_data()  # 信托财产专户开户行名称  必填
        TAAN = fake.bban()  # 信托财产专户账号  必填
        RSCD = comm.make_RSCD_data()  # 来源系统编码  必填
        self.TCID = comm.random_str(5) + comm.random_num(12)  # 信托合同号/受益权转让登记号  必填

        all_col = [TCSN, TCTP, TCNM, PJNO, PJNM, PJTP, CSTP, CTTP, CSNM, COBN, CATP, CATP_ORI, COAN, CADR, ABAN, ABIT, ABIT_ORI, ABAI, ABVT, SIDT, EPDT, CPRD, CCUR, TAMT, CAMT, PMTD, CGTP, IVST, PCSF, CBTS, TPRS, TPDT, BSTP, BSKD, TRTP, CFNO, CLNO, ZAMT, ZFVL, RCMO, RCMP, RCMD, SLMD, SCHN, BPTP, BPNM, PYBR, TCST, IMCN, MBRC, TABN, TAAN, RSCD, self.TCID]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_beneficiary(self):
        """
        受益人
        :return:
        """
        TCSN = comm.random_num(20)  # 合同ID 必填
        BNCN = ''  # 受益人客户号
        BNNM = fake.name()  # 受益人姓名/名称 必填
        BITP = comm.make_ABIT_data()  # 受益人证件类型（报送） 必填
        BITP_ORI = BITP  # 受益人证件类型（原值） 必填
        BNID = fake.ssn(min_age=24, max_age=56)  # 受益人证件号码 必填
        BIVT = comm.make_enable_date()  # 受益人证件有效期 必填
        BATP = '11'  # 受益人账号类型（报送） 必填
        BATP_ORI = comm.make_BATP_ORI_data()  # 受益人账号类型（原值） 必填
        BOAN = fake.bban()  # 受益人开户行账号 必填
        BOBN = comm.make_cabm_data()  # 受益人开户行名称 必填
        BOBA = 'CHN100000'  # 受益人开户行所在地
        RLMK = '说明'  # 委托人与受益人关系说明 必填
        BNTP = ''  # 受益人类型
        BNMD = ''  # 受益人分配模式
        RSCD = comm.make_RSCD_data()  # 来源系统编码 必填
        TCID = self.TCID  # 信托合同号/受益权转让登记号 必填

        all_col = [TCSN, BNCN, BNNM, BITP, BITP_ORI, BNID, BIVT, BATP, BATP_ORI, BOAN, BOBN, BOBA, RLMK, BNTP, BNMD, RSCD, TCID]
        return '|'.join([str(a) if a is not None else '' for a in all_col])

    def make_apply_contract(self, num):
        """
        资产运用合同
        :return:
        """
        TCSN = comm.random_num(20)  # 合同ID  必填
        TCTP = comm.make_TITP_data()  # 合同类型  必填
        TCNM = '应用合同名称{}'.format(num)  # 合同名称  必填
        PJNO = comm.random_str(5) + comm.random_num(10)  # 项目编号  必填
        PJNM = '应用同项目名称{}'.format(num)  # 项目名称  必填
        PJTP = comm.make_PJTP_data()  # 项目类型  必填
        CSTP = comm.make_comm_re_1_2()  # 运用方类别  必填  1,个人2机构
        CTTP = comm.make_CTTP_data()  # 运用方类型  必填
        CSNM = comm.random_str(12)  # 运用方客户号  必填
        LOBN = comm.make_cabm_data()  # 运用方开户行名称  必填
        LATP = ''  # 运用方账号类型（报送）  必填
        LATP_ORI = comm.make_BATP_ORI_data()  # 运用方账号类型（原值）  必填
        LOAN = fake.bban()  # 运用方开户行账号  必填
        LADR = 'CHN100000'  # 运用方开户行所在地
        ABAN = fake.name()  # 授权业务办理人姓名
        ABIT = comm.make_ABIT_data()  # 授权业务办理人证件类型（报送）
        ABIT_ORI = ABIT  # 授权业务办理人证件类型（原值）
        ABAI = fake.ssn(min_age=25, max_age=50)  # 授权业务办理人证件号码
        ABVT = comm.make_enable_date()  # 授权业务办理人证件有效期
        SIDT = comm.make_date(-3,-1)  # 签订时间  必填
        EPDT = comm.make_date()  # 到期时间  必填
        CPRD = comm.make_date()  # 合同期间  必填
        CCUR = comm.make_tctp_data()  # 合同币种  必填
        TAMT = comm.make_hold_amt2()  # 合同金额  必填
        CAMT = '20'  # 当前金額/份额  必填
        PMTD = comm.make_pmtd_data()  # 合同交付方式  必填
        CLMT = ''  # 授信额度
        LNDT = ''  # 运用端放款日期
        IVST = comm.make_IVST_data()  # 资金投向  必填
        MUPM = comm.make_MUPM_data()  # 管理运用处分方式  必填
        FIVF = comm.make_FIVF_data()  # 投融资形式  必填
        GRTM = comm.make_GRTM_data()  # 担保方式  必填
        GRCN = ''  # 担保人客户号
        FPMT = '1111'  # 第一还款来源  必填
        SPMT = ''  # 第二还款来源
        RCMO = ''  # 来源机构
        BSTP = comm.make_bstp_data()  # 业务类型  必填
        TCST = comm.make_yes_no()  # 合同状态  1有效0无效 必填
        PYBR = '0.5'  # 预期收益率  必填
        MBRC = comm.make_MBRC_data()  # 合同管理部门  必填
        CPCN = ''  # 中介合作机构客户号
        IMCN = ''  # 投资顾问或管理者客户号
        RSCD = comm.make_RSCD_data()  # 来源系统编码  必填
        TCID = self.TCID  # 信托合同号/受益权转让登记号  必填

        all_col = [TCSN, TCTP, TCNM, PJNO, PJNM, PJTP, CSTP, CTTP, CSNM, LOBN, LATP, LATP_ORI, LOAN, LADR, ABAN, ABIT, ABIT_ORI, ABAI, ABVT, SIDT, EPDT, CPRD, CCUR, TAMT, CAMT, PMTD, CLMT, LNDT, IVST, MUPM, FIVF, GRTM, GRCN, FPMT, SPMT, RCMO, BSTP, TCST, PYBR, MBRC, CPCN, IMCN, RSCD, TCID]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_contract_balance(self):
        """
        合同余额表
        :return:
        """
        TSDT = fake.date()  # 统计日期 必填
        TCSN = comm.random_num(18)  # 合同ID 必填
        TCTP = comm.make_comm_re_1_2()  # 委托/运用合同  1委托，2运用 必填
        CAMT = '21'  # 当前金額/份额 必填
        RSCD = comm.make_RSCD_data()  # 来源系统编码 必填
        CSNM = self.CSNM  # 客户号
        CSTP = self.cust_type  # 客户类型
        TCID = self.TCID  # 信托合同号/受益权转让登记号 必填

        all_col = [TSDT, TCSN, TCTP, CAMT, RSCD, CSNM, CSTP, TCID]
        return '|'.join([str(a) if a is not None else ''  for a in all_col])

    def make_transaction(self):
        """
        交易表
        :return:
        """
        TICD = comm.random_str(5) + comm.random_num(12)  # 业务标识号  必填
        TCSN = self.TCID  # 信托合同号/受益权转让登记号  必填
        CSTP = self.cust_type  # 客户类别  必填
        CSNM = self.CSNM  # 客户号  必填
        CTNM = comm.make_name_data(3)  # 客户名称  必填
        CITP = comm.make_ABIT_data()  # 客户证件类型（报送）  必填
        CITP_ORI = CITP  # 客户证件类型（原值）  必填
        CTID = fake.ssn(min_age=24, max_age=56)  # 客户证件号码  必填
        CBAT = ''  # 客户的银行账号类型（报送）  必填
        CBAT_ORI = comm.make_BATP_ORI_data()  # 客户的银行账号类型（原值）  必填
        CBAC = fake.bban()  # 客户的银行账号  必填
        COBN = CTNM  # 客户银行账号开户名称  必填
        CABM = comm.make_cabm_data()  # 客户银行账号的开户行名称  必填
        CABD = 'CHN100000'  # 客户银行账号的开户所在地
        TSDT = self.data_date  # 交易日期  必填
        BSTP = comm.make_bstp_data()  # 业务类型  必填
        TRTP = comm.make_trtp_data()  # 交易类型   必填
        TSTP = comm.make_tstp_data()  # 交易方式  必填
        TPFD = comm.make_TPFD_data()  # 资产流动方向 01:收 02:付  必填
        TCCT = comm.make_tctp_data()  # 交易币种  必填
        TCCA = comm.make_hold_amt()  # 交易金额  必填
        TCCA_CNY = round(TCCA/7,2)  # 交易金额（折人民币）
        TCRT = ''  # 汇率
        TRIO = comm.make_yes_no()  # 跨境标识  0：境内 1：跨境 必填
        REMK = fake.sentence()  # 备注（交易说明、用途）  必填
        TABA = comm.make_cabm_data()  # 信托财产专户开户行名称  必填
        TAAN = fake.bban()  # 信托财产专户账号  必填
        BINO = ''  # 票据号
        IMCN = ''  # 投资顾问或管理人客户号
        MBRC = comm.make_mbrc_ori_data()  # 管理机构  必填
        RSCD = comm.make_RSCD_data()  # 来源系统编码  必填
        TCID = self.TCID  # 信托合同号/受益权转让登记号  必填

        all_col = [TICD, TCSN, CSTP, CSNM, CTNM, CITP, CITP_ORI, CTID, CBAT, CBAT_ORI, CBAC, COBN, CABM, CABD, TSDT, BSTP, TRTP, TSTP, TPFD, TCCT, TCCA, TCCA_CNY, TCRT, TRIO, REMK, TABA, TAAN, BINO, IMCN, MBRC, RSCD, TCID]

        return '|'.join([str(a) if a is not None else ''  for a in all_col])
