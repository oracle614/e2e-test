class CategoryMap(object):

    def categeoryMapList(self,categeoryDict,sourceList):
        for key,value in zip(categeoryDict.keys(),categeoryDict.values()):
            if key == sourceList[3]:
                sourceList[3] = value
        return sourceList

    #收入类别映射
    def incomeCategoryMapList(self,sourceList):
        incomeCategory = {
                            '利息收入':['1','1'],
                            '回收借出资金(收入)':['2','1'],
                            '收到临时借入款(收入)':['2','2'],
                            '收回投资利息(收入)':['3','1'],
                            '收回投资本金(收入)':['3','2'],
                            '收到投资款':['3','3'],
                            '银行贷款(收入)':['3','4'],
                            '应收账款':['4','1']
                          }
        return self.categeoryMapList(incomeCategory,sourceList)

    #支出类别映射
    def outcomeCategeoryMapList(self,sourceList):
        outcomeCategeory = {
                                '银行费用':['1','1'],
                                '临时借出资金':['2','1'],
                                '归还临时借入':['2','2'],
                                '对外投资款':['3','1'],
                                '归还银行贷款':['3','2'],
                                '贷款利息':['3','3'],
                                '应付工资奖金':['4','1'],
                                '应付社保费':['4','2'],
                                '应付公积金':['4','3'],
                                '应付劳务费':['4','4'],
                                '应交增值税':['5','1'],
                                '应交城建税':['5','2'],
                                '应交教育费附加':['5','3'],
                                '应交地方教育附加':['5','4'],
                                '应交个税':['5','5'],
                                '应交印花税':['5','6'],
                                '应交所得税':['5','7'],
                                '应付账款':['6','1']
                            }
        return self.categeoryMapList(outcomeCategeory,sourceList)

    #收票-普票 类别映射
    def inputInvoiceCategeoryCommMapList(self,sourceList):
        inputInvoiceCategeoryComm = {
                                    '福利费': ['1', '1'], 
                                    '劳务费': ['1', '2'],
                                    '招待费': ['2', '1'],
                                    '办公费': ['2', '2'],
                                    '快递费': ['2', '3'], 
                                    '通讯费': ['2', '4'], 
                                    '维修费': ['2', '5'], 
                                    '财产保险费': ['2', '6'], 
                                    '设备租赁费':['2', '7'], 
                                    '银行费用': ['2', '8'], 
                                    '差旅费': ['3', '1'], 
                                    '交通费': ['3', '2'], 
                                    '汽油费': ['3', '3'], 
                                    '路桥费': ['3', '4'], 
                                    '汽车维修费': ['3', '5'], 
                                    '汽车保险': ['3', '6'], 
                                    '物流费': ['3', '7'], 
                                    '房租费': ['4', '1'], 
                                    '物业费': ['4', '2'], 
                                    '水费': ['4', '3'], 
                                    '电费': ['4', '4'], 
                                    '仓储费': ['4', '5'], 
                                    '装修费': ['4', '6'], 
                                    '广告费': ['5', '1'], 
                                    '宣传费': ['5', '2'], 
                                    '研发费': ['5', '3'], 
                                    '会议费': ['5', '4'], 
                                    '服务费': ['5', '5'], 
                                    '咨询费': ['5', '6'], 
                                    '认证费': ['5', '7'], 
                                    '专利费': ['5', '8'], 
                                    '工会经费': ['5', '9'], 
                                    '其他': ['5', '10'], 
                                    '行政罚款': ['6', '1'], 
                                    '税务滞纳金': ['6', '2'], 
                                    '印花税': ['7', '1'], 
                                    '残保金': ['7', '2'], 
                                    '减免税款': ['7', '3'], 
                                    '原材料': ['8', '1'], 
                                    '商品产品': ['8', '2']
                                }
        return self.categeoryMapList(inputInvoiceCategeoryComm,sourceList)

    #收票-专票 类别映射
    def inputInvoiceCategeorySpecMapList(self,sourceList):
        inputInvoiceCategeorySpec = {
                                        '福利费': ['1', '1'], 
                                        '招待费': ['2', '1'],
                                        '办公费': ['2', '2'],
                                        '快递费': ['2', '3'], 
                                        '通讯费': ['2', '4'], 
                                        '维修费': ['2', '5'], 
                                        '财产保险费': ['2', '6'], 
                                        '设备租赁费':['2', '7'], 
                                        '银行费用': ['2', '8'], 
                                        '差旅费': ['3', '1'], 
                                        '交通费': ['3', '2'], 
                                        '汽油费': ['3', '3'], 
                                        '路桥费': ['3', '4'], 
                                        '汽车维修费': ['3', '5'], 
                                        '汽车保险': ['3', '6'], 
                                        '物流费': ['3', '7'], 
                                        '房租费': ['4', '1'], 
                                        '物业费': ['4', '2'], 
                                        '水费': ['4', '3'], 
                                        '电费': ['4', '4'], 
                                        '仓储费': ['4', '5'], 
                                        '装修费': ['4', '6'], 
                                        '广告费': ['5', '1'], 
                                        '宣传费': ['5', '2'], 
                                        '研发费': ['5', '3'], 
                                        '会议费': ['5', '4'], 
                                        '服务费': ['5', '5'], 
                                        '咨询费': ['5', '6'], 
                                        '认证费': ['5', '7'], 
                                        '专利费': ['5', '8'], 
                                        '工会经费': ['5', '9'], 
                                        '其他': ['5', '10'], 
                                        '原材料': ['6', '1'], 
                                        '商品产品': ['6', '2']
                                    }
        return self.categeoryMapList(inputInvoiceCategeorySpec,sourceList)

    #开票 类别映射
    def outputInvoiceCategeoryMapList(self,sourceList):
        outputInvoiceCategeory = {
                                    '商品销售':['1','1'],
                                    '服务收入':['2','1']
                                 }
        for key,value in zip(outputInvoiceCategeory.keys(),outputInvoiceCategeory.values()):
            if key == sourceList[4]:
                sourceList[4] = value

        return sourceList