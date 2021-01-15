import os, sys

# 将当前路径添加到系统路径中
sys.path.append(os.getcwd())
from util import BoxDriver, BasePage, GetTxt, GetLogger
import tkinter
import tkinter.messagebox


class Work(BasePage):
    def Lonin(self, name='20201221101037', password='12345678'):
        try:
            self.log = GetLogger(r'.\log')
            driver = self.driver
            driver.locate_element('x,//input[@placeholder="请输入您的帐号"]').clear()
            driver.input('x,//input[@placeholder="请输入您的帐号"]', name)
            driver.locate_element('x,//input[@placeholder="请输入您的密码"]').clear()
            driver.input('x,//input[@placeholder="请输入您的密码"]', password)
            driver.click("x,//span[text()='登录']")
            driver.wait(1)
            New_name = driver.locate_element(
                'x,/html/body/div/div/section/header/section/main/ul/li[2]/div[1]/span').text
            self.log.info(f'用户:{New_name}登录成功')
        except Exception as e:
            self.log.warning(f'账号为:{name}登录失败,失败原因:{e}')

    def WriteLog(self, LogPath):
        try:
            driver = self.driver
            driver.click('x,//span[text()="日志管理"]')
            driver.click('x,//div[@id="the-navmenu"]/div/ul/li/ul/li[1]')
            driver.click('x,//span[text()="添加"]')
            driver.wait(2)
            driver.click(
                'x,/html/body/div/div/section/section/main/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div/div[1]/button[1]/span')
            # 点击选择
            driver.click(
                'x,/html/body/div/div/section/section/main/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/span/span/i')
            # 选择对应部门
            driver.click(
                'x,//*[@id="app"]/div/div[1]/div/div[2]/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[12]/div/button/span')
            # 输入工时
            driver.input(
                'x,/html/body/div/div/section/section/main/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[6]/div/div/input',
                1)
            # 输入工作内容
            gettxt = GetTxt()
            contents = gettxt.get(LogPath)
            content = ""
            for text in contents:
                content = content + text + '\n'
            driver.input(
                'x,/html/body/div/div/section/section/main/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[7]/div/div/div/textarea',
                content)
            # 提交
            # driver.click('x,//span[text()="提交"]')
            self.log.info(f"日报提交成功,日志内容为:\n\n{content}")
            # 提示框
            # root = tkinter.Tk()
            # root.withdraw()
            # tkinter.messagebox.showinfo('提示', "日志上传完成")
        except Exception as e:
            self.log.warning(f"日报提交失败,失败原因为:{e}")
            # 提示框
            # root = tkinter.Tk()
            # root.withdraw()
            # tkinter.messagebox.showerror("提示","日志提交失败")
        finally:
            self.driver.quit()
            self.log.info(f"浏览器关闭")


if __name__ == '__main__':
    driver = BoxDriver()
    work = Work(driver)
    # 输入用户名密码
    work.Lonin(name='20201221101037', password='12345678')
    # 工作日志保存位置
    work.WriteLog(r'.\Report\Report.txt')
