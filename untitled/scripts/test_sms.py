import os,sys

import pytest

sys.path.append(os.getcwd())

from base.init_driver import get_driver
from page.sms_page import SmsPage
from base.read_yaml import read_yaml_data
import page

#读取sms_send.yaml的数据
def get_data():
    data =  read_yaml_data("sms_send.yaml")
    #{'send_data':['aaa','bbb','ccc']}
    return  data.get("send_data")

class TestSms:

    def setup_class(self):
        #1.初始化driver
        self.driver = get_driver(page.sms_app_package,page.sms_app_activity)
        #2.初始化smspage类
        self.smspage = SmsPage(self.driver)
    def teardown_class(self):
        # 1 退出driver
        self.driver.quit()

    @pytest.mark.parametrize("content", get_data())
    def test_add_receive_number(self,content):
        # 1.点击新增按钮
        self.smspage.click_add_new_sms()
        # 2.输入接收者的内容
        self.smspage.input_receive_sms_number(content)
    def test_back_btn(self):
        self.smspage.settings_btn_back()

    #测试短信业务方法
    # @pytest.mark.parametrize("content", ['aaa', 'bbb', 'ccc'])
    # @pytest.mark.parametrize("content", get_data())
    # def test_send_sms(self,content):
        #1.实现发送内容
        # self.smspage.input_receive_sms_number(content)
        #2.获取发送的类别
        # sms_send_lists = self.smspage.get_sms_send_lists()
        # #3.断言是否发送成功
        # assert content in [i.text for i in sms_send_lists]





