import unittest
import time
import os
import smtplib
from HTMLTestRunner import HTMLTestRunner
from test_case.login.login_spec import LoginSpec
from test_case.setting.setting_spec import SettingSpec
from test_case.setting.contact.contact_spec import ContactSpec
from test_case.salary.add_stuff.add_stuff_spec import AddStuffSpec
from test_case.external.enter_comp_spec import EnterCompSpec
from test_case.external.create_comp.create_comp_spec import CreateCompSpec
from test_case.external.user_setting.user_setting_spec import UserSettingSpec

if __name__ == '__main__':
    testSuite = unittest.TestSuite()

    # 登录测试
    # testSuite.addTest(LoginSpec('test_verify_login'))
    # testSuite.addTest(LoginSpec('test_unexit_username'))
    testSuite.addTest(LoginSpec('test_wrong_password'))
    # testSuite.addTest(LoginSpec('test_empty_username'))
    # testSuite.addTest(LoginSpec('test_empty_password'))
    # testSuite.addTest(LoginSpec('test_typeerror_username'))

    # 设置页面
    # testSuite.addTest(SettingSpec('test_go_to_comp_billing_page'))
    # testSuite.addTest(SettingSpec('test_go_to_contact_page'))
    # testSuite.addTest(SettingSpec('test_go_to_mutil_user_page'))
    # testSuite.addTest(SettingSpec('test_go_to_partner_set_page'))
    # testSuite.addTest(SettingSpec('test_go_to_tax_rate_page'))
    # testSuite.addTest(ContactSpec('test_show_add_modal'))

    # 工资
    # testSuite.addTest(AddStuffSpec('test_name_empty'))
    # testSuite.addTest(AddStuffSpec('test_country_empty'))
    # testSuite.addTest(AddStuffSpec('test_id_empty'))
    # testSuite.addTest(AddStuffSpec('test_employed_empty'))
    # testSuite.addTest(AddStuffSpec('test_verify_add_stuff'))
    # testSuite.addTest(AddStuffSpec('test_verify_add_labour'))
    # testSuite.addTest(AddStuffSpec('test_id_repeat'))
    

    # external
    # testSuite.addTest(EnterCompSpec('test_enter_comp'))
    # testSuite.addTest(CreateCompSpec('create_account_book_empty_comp_name'))
    # testSuite.addTest(UserSettingSpec('test_go_to_comp_billing_page'))

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_dir = './report'
    filename = report_dir + '/' + now + '_result.html'
    testReport = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=testReport, title="管有账测试报告", description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()