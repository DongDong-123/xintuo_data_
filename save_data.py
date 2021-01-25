# -*- coding: utf-8 -*-
# @Time    : 2020-06-25 11:54
# @Author  : liudongyang
# @FileName: save_data.py
# @Software: PyCharm
# 存储数据
import pymysql
import os, csv
from readconfig import ReadMySqlConfig
from parm import zip_floder
import time

conf = ReadMySqlConfig()

class ConnectMysql:
    def __init__(self):
        self.host = conf.host()
        self.user = conf.user()
        self.passwd = conf.passwd()
        self.db = conf.db()
        self.port = conf.port()


    def save_to_mysql(self, datas, table_name):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port, charset="utf8")
        curs = conn.cursor()
        for data in datas:
            sql = "insert into {} {} VALUES {}".format(table_name, eval(table_name), tuple(data))
            curs.execute(sql)

        try:
            conn.commit()
        except Exception as e:
            print(e)

        curs.close()
        conn.close()
account          = 'CSNM客户号|CSTP客户类型|CATP银行账户类型(报送)|CATP_ORI银行账户类型(原值)|CBCN银行账户号|CTNM银行账户名称|CBNM银行账户开户行名称|CABA银行账户开户地|IDFT是否主账户|RSCD来源系统编码'
organization     = 'CSNM客户号|CCUP上游客户标识|CCMD中游客户标识|CCDW下游客户标识|CTTP客户类型|CTNM 客户名称|CTEN拼音/英文名称|CITP 证件类型（报送）|CITP_ORI  证件类型（原值）|CTID 证件号码|CIVT 证件有效期|RGTP登记注册类型|RGNO登记注册号|CTVC 行业（报送）|CTVC_ORI 行业(原值)|CRNM （法定代表人姓名）|CRNT （法定代表人国籍）|CRIT 法定代表人证件类型（报送）|CRIT_ORI法定代表人证件类型（原值）|CRID 法定代表人证件号码|CRVT法定代表人证件有效期|CTNT注册国家|FDDT成立日期|CPTL注册资金|CRCY注册资金币种|PUCP实收资本|EECP企业经济成份|TAST企业总资产|TLBT企业总负债|ENUM企业人员规模|SCTP企业经济规模|CBSC经营范围|ABAN授权办理人姓名|ABNT授权办理人国籍|ABIT授权办理人证件类型（报送）|ABIT_ORI授权办理人证件类型（原值）|ABAI授权办理人证件号码|ABVT授权办理人证件有效期限|ATEL授权办理人联系电话|ADNT地区国家|ADPV地区省|ADCT地区市|ADDC地区县|ADDR详细地址|PSCD邮编|LKNM联系人姓名|LDUT联系人职务|CMBL手机|CTEL固定电话|CEML电子邮箱|CSIO是否境外|RLTP关联方类型|RGDT开立日期|CSDT注销日期|CHNL建立渠道|CMGR客户经理|ISCA是否合作机构|CCRK合作机构信用等级|CTGR合作机构分类|ACTP核算类型|CONM所属合作机构客户号|ISSB是否同业机构|ISMB是否同业机构|ISIA是否投资顾问|ISLA是否贷款运用方|MBRC_ORI管理机构（原值）|CTST客户状态|REMK备注|RSCD来源系统编码|BNNM控股股东或实际控制人姓名|BITP控股股东或实际控制人证件类型（报送）|BITP_ORI控股股东或实际控制人证件类型（原值）|BNID控股股东或实际控制人证件号码|BIVT控股股东或实际控制人证件有效期|MBRC_MULTI'
addresse         = 'CSNM|CSTP客户类型|ADTP地址类型|LKNM联系人姓名|ADNT国家代码|ADPV省代码|ADCT市代码|ADDC区县代码|ADDR详细地址|PSCD邮编|IDFT是否主地址|RSCD来源系统编码'
apply_contract   = 'TCSN运用合同号/债权转让登记号|TCTP合同类型|TCNM合同名称|PJNO项目编号|PJNM项目名称|PJTP项目类型|CSTP运用方类别|CTTP运用方类型|CSNM运用方客户号|LOBN运用方开户行名称|LATP运用方账号类型（报送）|LATP_ORI运用方账号类型（原值）|LOAN运用方开户行账号|LADR运用方开户行所在地|ABAN授权业务办理人姓名|ABIT授权业务办理人证件类型（报送）|ABIT_ORI授权业务办理人证件类型（原值）|ABAI授权业务办理人证件号码|ABVT授权业务办理人证件有效期|SIDT签订时间|EPDT到期时间|CPRD合同期间|CCUR合同币种|TAMT合同金额|CAMT当前金額/份额|PMTD合同交付方式|CLMT授信额度|LNDT运用端放款日期|IVST资金投向|MUPM管理运用处分方式|FIVF投融资形式|GRTM担保方式|GRCN担保人客户号|FPMT第一还款来源|SPMT第二还款来源|RCMO来源机构|BSTP业务类型|TCST合同状态|PYBR预期收益率|MBRC合同管理部门|CPCN中介合作机构客户号|IMCN投资顾问或管理者客户号|RSCD来源系统编码|tcid'
person           = 'CSNM客户号|CCUP上游客户标识|CCMD中游客户标识|CCDW下游客户标识|CTNM 客户名称|CTEN拼音/英文名称|CITP证件类型（报送）|CITP_ORI证件类型（原值）|CTID证件号码|CIVT证件有效期|CTSX性别|CTNT国籍|CTNA民族|CTBD出生日期|EDCT学历|CTVC职业|CTVC_ORI职业（原值）|WKPL工作单位|WTVC工作行业|WKPS职位|PICM个人年收入|FICM家庭年收入|MRGE婚姻状况|ADNT地址国家|ADPV地址省|ADCT地址市|ADDC地址区县|ADDR详细地址|PSCD邮编|CMBL手机|CTEL固定电话|CEML电子邮箱|CSIO是否境外|TRLV风险承受等级|RLTP关联方类型|RGDT开立日期|CSDT销户日期|CHNL建立渠道|CMGR客户经理|CONM所属合作机构的客戶号|MBRC_ORI管理机构（原值）|CTST客户状态|REMK备注|RSCD来源系统编码'
cert             = 'CSNM客户号|CSTP客户类型|CITP证件类型（报送）|CITP_ORI证件类型（原值）|CTID证件号码|CIVT证件有效期|ISNT证件签发国家|ISUT证件签发机关|ISDT证件签发日期|IDFT是否主证件|RSCD来源系统编码'
contact          = 'CSNM客户号|CSTP客户类型|RLTP关系类型|RCNM关系人客户号|RCTP关系人类别|RLNM关系人姓名/名称|RCNT关系人国籍/国家|RITP关系人证件类型(报送)|RITP_ORI关系人证件类型(原值)|RTID关系人证件号码|RTVT关系人证件有效期|RTEL关系人联系电话|HPER持股比例|HAMT持股金额|RSCD来源系统编码'
relation         = 'CSNM客户号|CSTP客户类型|RLTP关系类型|RCNM关系人客户号|RCTP关系人类别|RLNM关系人姓名/名称|RCNT关系人国籍/国家|RITP关系人证件类型(报送)|RITP_ORI关系人证件类型(原值)|RTID关系人证件号码|RTVT关系人证件有效期|RTEL关系人联系电话|HPER持股比例|HAMT持股金额|RSCD来源系统编码|BLTP|RLAD|IS_AVAILABLE是否有效'
trust_contract   = 'TCSN信托合同号/受益权转让登记号|TCTP合同类型|TCNM合同名称|PJNO项目编号|PJNM项目名称|PJTP项目类型|CSTP委托人类别|CTTP委托人类型|CSNM委托人客户号|COBN委托人开户行名称|CATP委托人账号类型（报送）|CATP_ORI委托人账号类型（原值）|COAN委托人开户行账号|CADR委托人开户行所在地|ABAN授权业务办理人姓名|ABIT授权业务办理人证件类型（报送）|ABIT_ORI授权业务办理人证件类型（原值）|ABAI授权业务办理人证件号码|ABVT授权业务办理人证件有效期|SIDT签订时间|EPDT到期时间|CPRD合同期间|CCUR合同币种|TAMT合同金額/份额|CAMT当前金額/份额|PMTD合同交付方式|CGTP收费类型|IVST资金投向|PCSF财产分类|CBTS出资财产来源|TPRS出资财产来源说明|TPDT信托财产交付日期|BSTP业务类型|BSKD业务种类（受益类型）|TRTP信托类型|CFNO初始委托合同号|CLNO受益权来源合同号|ZAMT委托转让合同的转让金额|ZFVL转让合同的公允价值|RCMO推介来源机构|RCMP推介地类型|RCMD推介地名称|SLMD销售方式|SCHN销售途径|BPTP受益权类型|BPNM受益权名称|PYBR预期收益率|TCST合同状态|IMCN投资顾问或管理者客户号|MBRC合同管理部门|TABN信托财产专户开户行名称|TAAN信托财产专户账号|RSCD来源系统编码|tcid'
beneficiary      = 'BNCN受益人客户号|BNNM受益人姓名/名称|BITP受益人证件类型（报送）|BITP_ORI受益人证件类型（原值）|BNID受益人证件号码|BIVT受益人证件有效期|BATP受益人账号类型（报送）|BATP_ORI受益人账号类型（原值）|BOAN受益人开户行账号|BOBN受益人开户行名称|BOBA受益人开户行所在地|RLMK委托人与受益人关系说明|BNTP受益人类型|BNMD受益人分配模式|RSCD来源系统编码|TCID信托合同号/受益权转让登记号'
contract_balance = 'TSDT统计日期|TCSN委托/运用合同号|TCTP委托/运用合同(1委托  2运用）|CAMT当前金額/份额|RSCD来源系统编码|CSNM|CSTP|TCID'
transaction      = 'TICD业务标识号|TCSN信托合同号/受益权转让登记号|CSTP客户类别|CSNM客户号|CTNM客户名称|CITP客户证件类型（报送）|CITP_ORI客户证件类型（原值）|CTID客户证件号码|CBAT客户的银行账号类型（报送）|CBAT_ORI客户的银行账号类型（原值）|CBAC客户的银行账号|COBN客户银行账号开户名称|CABM客户银行账号的开户行名称|CABD客户银行账号的开户所在地|TSDT交易日期|BSTP业务类型|TRTP交易类型 |TSTP交易方式|TPFD资产流动方向|TCCT交易币种|TCCA交易金额|TCCA_CNY交易金额（折人民币）|TCRT汇率|TRIO跨境标识|REMK备注（交易说明、用途）|TABA信托财产专户开户行名称|TAAN信托财产专户账号|BINO票据号|IMCN投资顾问或管理人客户号|MBRC管理机构|RSCD来源系统编码'


class SaveFile:
    def __init__(self):
        self.file_path = zip_floder
        self.currt_time = time.strftime('%Y%m%d', time.localtime())


    def write_to_txt(self, data, file_name,file_date_time):
        filename = '_'.join([file_name, file_date_time])

        # print(filename,data)
        filepath = os.path.join(zip_floder, '{}.txt'.format(filename))
        if not os.path.exists(filepath):
            with open(filepath, '+a', encoding='utf-8') as f:
                f.write(eval(file_name)+'\n')
        with open(filepath,'+a', encoding='utf-8') as f:
            f.writelines([line+'\n' for line in data])