# 快速复制  ctrl + d   删除 ctrl + y
from selenium.webdriver.common.by import By

#启动应用的包名和启动名
sms_app_package = "com.android.settings"
sms_app_activity = ".Settings"

#发送短信功能
# sms_add_btn = By.ID,"com.android.mms:id/action_compose_new"
# sms_edit_receive_number = By.ID,"com.android.mms:id/recipients_editor"
# sms_edit_send_content = By.ID,"com.android.mms:id/embedded_text_editor"
# sms_btn_send = By.ID,"com.android.mms:id/send_button_sms"

#定位一组元素
# sms_send_lists = By.ID,"com.android.mms:id/text_view"

# 查找按钮
settings_search_btn = By.ID,'com.android.settings:id/search'
settings_search_text = By.ID,'android:id/search_src_text'
settings_back_btn = By.CLASS_NAME,'android.widget.ImageButton'