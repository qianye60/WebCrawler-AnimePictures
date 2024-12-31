from DrissionPage import Chromium
import DrissionPage.errors
import os
import json

#os.chdir(os.path.dirname(__file__)) Drission会根据os模块的工作路径来确定相对路径位置，所以要用这个来更改当前工作路径为py文件所在
if not os.path.exists("pictures"):#判断文件夹是否存在
    os.mkdir("pictures")#创建

class picture:
    def __init__(self,setlist):
        self.browser = Chromium()
        self.tab = self.browser.latest_tab
        self.setlist = setlist
        self.url = f"https://anime-pictures.net/posts?page={str(setlist["location"][0])}&search_tag={setlist["search_tag"]}&denied_tags={setlist["denied_tag"]}&order_by={setlist["order_by"]}&ldate={setlist["ldate"]}&lang=zh-cn"
        if self.setlist["islocation"] != '1':
            self.setlist["location"] = [0,0]
    def login_set(self):
        self.tab.get("https://anime-pictures.net/login?lang=zh-cn")
        self.tab.ele("xpath://tbody/tr[1]/td[2]/input").clear().input(self.setlist["username"])
        self.tab.ele("xpath://tbody/tr[2]/td[2]/input").clear().input(self.setlist["password"])
        self.tab.wait(1,2)
        button = self.tab.ele("xpath://*[@id=\"svelte\"]/div/div[1]/div[1]/div/div/form/table/tbody/tr[3]/td[2]/input").click()
        self.tab.wait(1, 2)
        self.tab.get("https://anime-pictures.net/settings")
        self.tab.ele("xpath://tbody/tr[6]/td[2]/input").clear().input(self.setlist["imagenumber"])
        self.tab.ele("xpath://div[2]/div[2]/div[2]/input").click()
    def crawler(self):
        self.tab.set.download_path("pictures")#设置下载路径
        #爬取页
        while True:
            self.url = f"https://anime-pictures.net/posts?page={str(setlist["location"][0])}&search_tag={setlist["search_tag"]}&denied_tags={setlist["denied_tag"]}&order_by={setlist["order_by"]}&ldate={setlist["ldate"]}&lang=zh-cn"
            self.tab.get(self.url)
            #等待页面加载完成
            self.tab.wait.doc_loaded(3)
            div = self.tab.ele("xpath://*[@id=\"svelte\"]/div//div[2]")
            picture_elements = div.eles("xpath://span/a/@href")
            picture_elements = picture_elements[self.setlist["location"][1]:]
            #爬取张
            for picture_element in picture_elements:
                #进入张
                self.tab.get("https://anime-pictures.net"+picture_element)
                #隐式等待按钮加载
                self.tab.wait.ele_displayed('xpath://span[2]/a[@title="下载图片"]', timeout=3)
                #单击下载按钮
                self.tab.ele('xpath://span[2]/a[@title="下载图片"]').click()
                #等待下载开始
                self.tab.wait.download_begin()
                print("开始下载-第%d页 第%d张" % (self.setlist["location"][0],setlist["location"][1]))
                #等待下载结束
                self.tab.wait.downloads_done()
                self.tab.wait(0.5,1.2)
                print("下载完成！")
                self.setlist["location"][1] = (self.setlist["location"][1] + 1) % (int(self.setlist["imagenumber"]))
                with open("C:\\Users\\Public\\setting.json", "r+",encoding='utf-8') as f:
                    json.dump(setlist, f)
                self.tab.wait(0.5,1.5)
            self.setlist["location"][0] = self.setlist["location"][0] + 1
    def start(self):
        self.login_set()
        self.tab.wait(0.5,0.8)
        self.crawler()

if __name__ == '__main__':
    # 初始化默认设置
    setlist = {
        "username": "",
        "password": "",
        "imagenumber": "",
        "search_tag": "",
        "denied_tag": "",
        "order_by": "",
        "ldate": "",
        "islocation": "",
        "location":[0,0]
    }

    # 尝试读取文件内容
    try:
        with open("C:\\Users\\Public\\setting.json", "r+",encoding='utf-8') as f:
            setlist = json.load(f)
            if setlist["username"] == "":
                print("首次使用,请将以下1,2,3,4全部设置一遍:")
    except FileNotFoundError:
        print("首次使用,请将以下1,2,3,4全部设置一遍:")

    # 设置参数
    while True:
        print(f"当前所有参数:{setlist}")
        flag = int(input("——————————功能——————————\n1.设置账号密码\n2.修改每页张数\n3.设置爬取标签\n4.是否记录爬取位置\n输入数字调用相应功能(“0”开始):"))
        if flag == 1:
            setlist["username"] = input("请输入账号:")
            setlist["password"] = input("请输入密码:")
        elif flag == 2:
            setlist["imagenumber"] = input("每页张数:")
        elif flag == 3:
            setlist["search_tag"] = input("search_tag=")
            setlist["denied_tag"] = input("denied_tag=")
            setlist["order_by"] = input("order_by:\nstars_date:按评分日期\ndate:按日期\ndate_r:按日期（倒序）\nrating:按评分\nviews:按下载量\nsize:按大小\ntag_num:按标签数\n请输入:")
            setlist["ldate"] = input("ldate:\n0:任何时间\n1:过去一周\n2:过去一个月\n3:过去一天\n4:过去6个月\n5:过去一年\n6:过去两年\n7:过去三年\n请输入:")
        elif flag == 4:
            setlist["islocation"] = input("是否开启(0关闭 1开启):")
            set_location = int(input("是否设置页和张的位置(0不是 1是):"))
            if set_location == 1:
                setlist["location"][0] = int(input("输入页数:"))
                setlist["location"][1] = int(input("输入张数:"))
        else:
            break
        # 保存设置到文件
        with open("C:\\Users\\Public\\setting.json", "w", encoding='utf-8') as f:
            json.dump(setlist, f)
        os.system("cls")


    # 调用爬虫
    crawler = picture(setlist)
    crawler.start()
