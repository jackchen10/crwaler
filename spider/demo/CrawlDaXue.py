# -*- coding:utf-8 -*-

from lxml import etree
from selenium import webdriver

# 使用xpath方式找到下拉框中的值，设定{}参数，后续填充
common_url = '//*[@id="content-box"]/div[2]/table/thead/tr/th[6]/div/div[2]/ul/li[{}]'
random_int = range(1, 10)
option = webdriver.ChromeOptions()
# 设置chrome浏览器后台静默运行
option.add_argument('headless')
option.add_argument('--disable-gpu')
# 定义要解析的网页URL
TARGET_URL = "https://www.shanghairanking.cn/rankings/bcur/2020"


# 定义分析网页元素函数
def parse_page():
    # 这里是设定chromedriver的绝对路径，这里对应你自己的路径就可以了，如果报错没有可以直接下一个。
    browser = webdriver.Chrome(executable_path=r'/Applications/devtools/chromedriver', chrome_options=option)
    # 这里进入你需要爬取数据的网页
    # 使进程暂停一段时间，能够让函数能够反应过来并且得到对应的需要的数据
    # time.sleep(2)
    browser.get(TARGET_URL)
    # 这里用的是xpath进行解析，etree.HTML构建xpath解析对象，使用xpath获取下拉框信息
    drop_down_list = []
    e = etree.HTML(browser.page_source)
    for i in random_int:
        # 这里具体到了的下拉框中的一个属性
        url_result = common_url.format(i)
        # print(url_result)

        final_path = url_result + '/text()'
        drop_down_text = e.xpath(final_path)
        # 这里每个对象仅有一个元素，故写死[0]
        # print('第' + str(i) + '个：' + drop_down_text[0])
        drop_down_list.append(drop_down_text[0])

    # 关闭网页
    browser.close()
    return drop_down_list


if __name__ == '__main__':
    text_list = parse_page()
    print(text_list)
    index = 1
    # 循环打印list
    for text in text_list:
        print('下拉框第{}个值：{}'.format(str(index), text))
        index += 1
