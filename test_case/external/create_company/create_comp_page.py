from selenium import webdriver
import time

from util.public_page import PublicPage
from .create_comp_elem import *
from util.select_address_page import SelectAddressPage

"""
进入帐套
创建于2017-09-29-五
caicai
"""


class CreateCompPage(object):
    def __init__( self, driver ):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 创建帐套
    def set_comp_base_info( self, create_comp_info ):
        """
        :param create_comp_info: 创建帐套数据
        """
        # compListPage = CompListPage(self.driver)
        # compListPage.go_to_create_comp_page()
        print('create_comp_info=>', create_comp_info)
        self.set_comp_num(create_comp_info[0])
        self.set_comp_name(create_comp_info[1])
        self.select_accounting_standard(create_comp_info[2])
        if create_comp_info[2] == '2013小企业会计准则':
            self.select_property(create_comp_info[3])
        self.select_enable_date(create_comp_info[5])
        # self.submit(create_comp_info[17])

    def set_comp_detail_info( self, create_comp_info ):
        """
        :param create_comp_info:创建帐套数据
        """
        text = '未查到详细信息 填写'
        alert_text = self.get_search_failed_text()
        if text == alert_text:
            self.driver.find_element_by_link_text('填写').click()
            time.sleep(2)
            if self.driver.find_element_by_xpath(legal_person_name_elem).is_displayed():
                self.select_setup_date(create_comp_info[6], create_comp_info[7], create_comp_info[8])
                self.set_legal_person_name(create_comp_info[9])
                self.set_registered_capital(create_comp_info[10])
                self.set_tax_num(create_comp_info[11])
                self.select_industry(create_comp_info[12])
                self.select_comp_address(create_comp_info[13], create_comp_info[14], create_comp_info[15])
                self.submit(create_comp_info[16])
                time.sleep(1)
            else:
                print('－－点击填写按钮失败，填写帐套信息窗口未打开！！')
        else:
            print('名为' + create_comp_info[1] + '的公司已认证，不需要填写帐套信息！')
        self.submit(create_comp_info[17])

    # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    def set_comp_num( self, comp_num ):
        """
        设置帐套编号
        :param comp_num: 帐套编号
        """
        publicPage = PublicPage(self.driver)
        random_num = publicPage.random_num(10000)
        comp_num_loc = self.driver.find_element_by_xpath(comp_num_elem)
        print('comp_num_loc=>', comp_num_loc)
        if comp_num == '' or comp_num == '空校验':
            num = ''
        else:
            num = comp_num + str(random_num)
        print('comp_num=', comp_num)
        print('num=>', num)
        publicPage.set_value(comp_num_loc, num)

    def set_comp_name( self, comp_name ):
        """
        设置帐套名称
        :param comp_name:帐套名称（⚠️当帐套名称为'北京有序科技有限公司'时，用来测试公司已认证的情况）
        """
        public_page = PublicPage(self.driver)
        input_loc = self.driver.find_element_by_xpath(comp_name_elem)
        random_num = public_page.random_num(10000)
        if comp_name == '' or comp_name == '空校验':
            name = ''
        elif comp_name == '北京有序科技有限公司':
            name = comp_name
        else:
            name = comp_name + str(random_num)
        public_page.set_value(input_loc, str(name))

    def select_accounting_standard( self, accounting_standard ):
        """
        选择会计制度
        :param accounting_standard:可选值（2013小企业会计准则、村集体经济组织会计制度）
        """
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_name(accounting_standard_elem)
        publicPage.select_dropdown_item(drop_loc, accounting_standard)

    def select_property( self, account_property ):
        """
        选择帐套性质
        :param account_property: 可选值（一般纳税人、小规模纳税人）
        """
        public_page = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_name(property_elem)
        public_page.select_dropdown_item(drop_loc, account_property)

    def select_enable_date( self, begin_date ):
        """
        :param begin_date: 启用帐套日期，eg：一月、二月...
        """
        public_page = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(enable_date_drop_elem)
        public_page.select_month(drop_loc, begin_date)

    # ------------------------------------------------------------------------------------------------------------------
    # 设置帐套信息弹窗
    def select_setup_date( self, year, month, day ):
        """
        :param year:年（2017，2018...）
        :param month:月（1，2，3...)
        :param day:日(1,2,3...)
        :return:选择帐套成立日期
        """
        publicPage = PublicPage(self.driver)
        calen_drop_loc = self.driver.find_element_by_id(setup_date_elem)
        publicPage.click_elem(calen_drop_loc)

        year_select_loc = self.driver.find_element_by_css_selector('.ui-datepicker-year')
        year_drop_loc = year_select_loc
        publicPage.select_option(year_select_loc, year, year_drop_loc)

        month_select_loc = self.driver.find_element_by_css_selector('.ui-datepicker-month')
        month_drop_loc = month_select_loc
        month_value = int(month) - 1
        publicPage.select_option(month_select_loc, month_value, month_drop_loc)

        day_loc = self.driver.find_element_by_link_text(day)
        publicPage.click_elem(day_loc)

    def set_legal_person_name( self, legal_person_name ):
        """
        :param legal_person_name: 9,法人代表名字
        """
        public_page = PublicPage(self.driver)
        random_num = public_page.random_num(10000)
        input_loc = self.driver.find_element_by_xpath(legal_person_name_elem)
        if legal_person_name == '' or legal_person_name == '空校验':
            name = ''
        else:
            name = legal_person_name + str(random_num)
        public_page.set_value(input_loc, str(name))

    def set_registered_capital( self, registered_capital ):
        """
        :param registered_capital: 注册资本（string）
        """
        public_page = PublicPage(self.driver)
        random_num = public_page.random_num(10000)
        input_loc = self.driver.find_element_by_name(registered_capital_elem)
        if registered_capital == '' or registered_capital == '空校验':
            capital = ''
        else:
            capital = registered_capital + str(random_num)
        public_page.set_value(input_loc, str(capital))

    def set_tax_num( self, tax_num ):
        """
        :param tax_num: 税号（string）
        """
        public_page = PublicPage(self.driver)
        input_loc = self.driver.find_element_by_xpath(tax_num_elem)
        random_num = public_page.random_num(1000000)
        if tax_num == '' or tax_num == '空校验':
            num = ''
        else:
            num = tax_num + str(random_num)
        public_page.set_value(input_loc, str(num))

    def select_industry( self, industry ):
        """
        :param industry:行业性质
        """
        public_page = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_name(industry_drop_elem)
        public_page.select_dropdown_item(drop_loc, industry)

    def select_comp_address( self, province, city, district ):
        """
        :param province: 省份
        :param city: 市
        :param district: 区
        :return: 帐套信息 住所
        """
        prov_drop_loc = self.driver.find_element_by_name(prov_drop_elem)
        city_drop_loc = self.driver.find_element_by_name(city_drop_elem)
        distr_drop_loc = self.driver.find_element_by_name(dist_drop_elem)

        selectAddressPage = SelectAddressPage(self.driver)
        selectAddressPage.select_address(prov_drop_loc, province, city_drop_loc, city, distr_drop_loc, district)

    # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    # 提交／验证

    def submit( self, btn_name ):
        """
        保存／取消
        :param btn_name: 按钮名称，可选值：保存、取消；
        :return:点击按钮；
        """
        if None != btn_name:
            if 'msg' in btn_name:
                if btn_name == 'msg_save':
                    btn_elem = msg_save_btn_elem
                    operation_name = '帐套信息保存'
                elif btn_name == 'msg_cancel':
                    btn_elem = msg_cancel_btn_elem
                    operation_name = '帐套信息取消'
                btn_loc = self.driver.find_element_by_id(btn_elem)
            elif 'create' in btn_name:
                if btn_name == 'create_save':
                    btn_elem = create_btn_elem
                    operation_name = '保存创建'
                elif btn_name == 'create_cancel':
                    btn_elem = cancel_btn_elem
                    operation_name = '取消创建'
                btn_loc = self.driver.find_element_by_xpath(btn_elem)
            public_page = PublicPage(self.driver)
            print('按钮名称：', operation_name)
            public_page.click_elem(btn_loc)
        else:
            return '无操作'

    def get_search_failed_text( self ):
        """
        :return:未查找到详细信息
        """
        publicPage = PublicPage(self.driver)
        text_loc = self.driver.find_element_by_xpath(search_failed_elem)
        text = publicPage.get_value(text_loc)
        print('text=>', text)
        return text
