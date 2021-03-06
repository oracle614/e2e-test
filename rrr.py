import unittest,time,os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from HTMLTestRunner import HTMLTestRunner
from test_case.transaction.record_outcome_spec import RecordOutcomeSpec
from test_case.transaction.record_income_spec import RecordIncomeSpec
from test_case.transaction.record_transfer_spec import RecordTransterSpec
from test_case.transaction.outcome_voucher_spec import OutcomeVoucherSpec
from test_case.invoice.record_input_invoice_spec import RecordInputInvoiceSpec
from test_case.invoice.record_output_invoice_spec import RecordOutputInvoiceSpec
from test_case.finance.voucher.generate_voucher_spec import GenerateVoucherSpec
from test_case.fixedassets.record_fixed_spec import RecordFixedSpec
from test_case.fixedassets.record_intangible_spec import RecordIntangibleSpec
from test_case.finance.voucher.record_business_spec import RecordBusinessSpec
from test_case.business_flow.positive_flow_spec import PositiveFlowSpec
from test_case.business_flow.positive_flow_specb import PositiveFlowSpec1
# from test_case.dashbaord.assistant_dashbaord_spec import AssistantDashbaordSPec
from test_case.dashbaord.assistant_dashbaord_spec import AssistantDashbaordSPec
import queue
import threading

#发送邮件
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    user = '18514509382@163.com'
    password = 'yang115817'
    sender = '18514509382@163.com'
    receiver = 'yangchunhong@concordya.com'

    msg = MIMEMultipart()
    msg['From'] = '18514509382@163.com'
    msg['Subject'] = Header(u'自动化测试报告','utf8').encode()
    msg['To'] = 'yangchunhong@concordya.com'
    msg.attach(MIMEText(mail_body,'html','utf-8'))
    smtp = smtplib.SMTP(smtpserver,25)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

#查找最新的测试报告
def find_new_report(testReport):
    lists = os.listdir(testReport)
    lists.sort(key=lambda fn:os.path.getmtime(testReport + '//' + fn))
    file_new = os.path.join(testReport,lists[-1])
    return file_new

class MyThread(threading.Thread):

    def __init__(self, func, args=(), name=''):
        super(MyThread, self).__init__(target=func, args=args, name=name)
        self.name = name
        self.func = func
        self.args = args


    def run(self):
        self.func.run(suite)
        while True:
            if  myqueue.empty() == False:
                suite = myqueue.get()
                self.func.run(suite)
            else:
                break

testcase=['test1','test2']

myqueue = queue.Queue(maxsize = 10)

for i in testcase:
    suite = unittest.TestSuite()
    suite.addTest(PositiveFlowSpec1(i))
    myqueue.put(suite)

if __name__ == '__main__':
    threads = []
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_dir = './report'
    filename = report_dir + '/' + now + '_result.html'
    testReport = open(filename,'wb')
    runner = HTMLTestRunner(stream = testReport,title = "管有账测试报告",description='测试用例执行情况：')
    for i in range(1):
        t = MyThread(runner)
        # t.start()
        threads.append(t)

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    testReport.close()
    # now = time.strftime('%Y-%m-%d %H_%M_%S')
    # report_dir = './report'
    # filename = report_dir + '/' + now + '_result.html'
    # testReport = open(filename,'wb')
    # runner = HTMLTestRunner(stream = testReport,title = "管有账测试报告",description='测试用例执行情况：')
    # runner.run(testSuite)
    # testReport.close()
    # new_report = find_new_report('./report')
    # send_mail(new_report)


 # def spec():
        # testSuite = unittest.TestSuite()

        # #记支出测试
        # testSuite.addTest(RecordOutcomeSpec('test1'))
        # testSuite.addTest(RecordOutcomeSpec('test2'))
        # testSuite.addTest(RecordOutcomeSpec('test3'))
        # testSuite.addTest(RecordOutcomeSpec('test4'))
        # testSuite.addTest(RecordOutcomeSpec('test5'))
        # testSuite.addTest(RecordOutcomeSpec('test6'))
        # testSuite.addTest(RecordOutcomeSpec('test7'))
        # testSuite.addTest(RecordOutcomeSpec('test8'))


        # #记收入测试
        # testSuite.addTest(RecordIncomeSpec('test1'))
        # testSuite.addTest(RecordIncomeSpec('test2'))
        # testSuite.addTest(RecordIncomeSpec('test3'))
        # testSuite.addTest(RecordIncomeSpec('test4'))
        # testSuite.addTest(RecordIncomeSpec('test5'))
        # testSuite.addTest(RecordIncomeSpec('test6'))
        # testSuite.addTest(RecordIncomeSpec('test7'))
        # testSuite.addTest(RecordIncomeSpec('test8'))

        # #记账户互转 *注意：需要新增招商银行账户
        # testSuite.addTest(RecordTransterSpec('test1'))
        # testSuite.addTest(RecordTransterSpec('test2'))
        # testSuite.addTest(RecordTransterSpec('test3'))
        # testSuite.addTest(RecordTransterSpec('test4'))
        # testSuite.addTest(RecordTransterSpec('test5'))
        # testSuite.addTest(RecordTransterSpec('test6'))
        # testSuite.addTest(RecordTransterSpec('test7'))
        # testSuite.addTest(RecordTransterSpec('test8'))

        # # # #记收票测试
        # testSuite.addTest(RecordInputInvoiceSpec('test1'))
        # testSuite.addTest(RecordInputInvoiceSpec('test2'))

        # # #记开票测试
        # testSuite.addTest(RecordOutputInvoiceSpec('test1'))

        # testSuite.addTest(RecordOutputInvoiceSpec('test2'))

        # # #记固定资产
        # testSuite.addTest(RecordFixedSpec('test1'))
        # testSuite.addTest(RecordFixedSpec('test2'))

        # # # #记无形资产
        # testSuite.addTest(RecordIntangibleSpec('test1'))
        # testSuite.addTest(RecordIntangibleSpec('test2'))

        #记所有的业务单：收入、支出、账户互转、收票、开票、固定资产、无形资产
        # testSuite.addTest(RecordBusinessSpec('test1'))
        # testSuite.addTest(RecordBusinessSpec('test2'))
        # testSuite.addTest(RecordBusinessSpec('test3'))
        # testSuite.addTest(RecordBusinessSpec('test4'))
        # testSuite.addTest(RecordBusinessSpec('test5'))
        # testSuite.addTest(RecordBusinessSpec('test6'))
        # testSuite.addTest(RecordBusinessSpec('test7'))
        # testSuite.addTest(RecordBusinessSpec('test8'))
        # testSuite.addTest(RecordBusinessSpec('test9'))
        # testSuite.addTest(RecordBusinessSpec('test10'))

        #业务流程测试
        # testSuite.addTest(PositiveFlowSpec('test1'))
        # testSuite.addTest(PositiveFlowSpec('test2'))
        # testSuite.addTest(PositiveFlowSpec('test3'))
        # testSuite.addTest(PositiveFlowSpec('test4'))
        # testSuite.addTest(PositiveFlowSpec('test5'))
        # testSuite.addTest(PositiveFlowSpec('test6'))
        # testSuite.addTest(PositiveFlowSpec('test7'))
        # testSuite.addTest(PositiveFlowSpec('test8'))
        # testSuite.addTest(PositiveFlowSpec('test9'))
        # testSuite.addTest(PositiveFlowSpec('test10'))
        # testSuite.addTest(PositiveFlowSpec('test11'))

        #会计首页测试（导入）
        # testSuite.addTest(AssistantDashbaordSPec('test1'))
        # testSuite.addTest(AssistantDashbaordSPec('test2'))
        # testSuite.addTest(AssistantDashbaordSPec('test3'))


        #生成凭证测试 *【注意】需要新增招商银行且没有流水记录
        # testSuite.addTest(GenerateVoucherSpec('test1'))
        # testSuite.addTest(GenerateVoucherSpec('test2'))
        # testSuite.addTest(GenerateVoucherSpec('test3'))

        #支出-生成凭证测试
        # testSuite.addTest(OutcomeVoucherSpec('test1'))
        

    