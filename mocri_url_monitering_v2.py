from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import urllib.request, urllib.error
import subprocess
import pyautogui as gui

class Mocri:
    
    def __init__(self):
        
        # self.cmd_list = ['yt', 'yt stop']
        self.path = "your text path which is witten login pass and mailadress"
        self.freespace_path = "your free space path"

        ##### driver option
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", { ## 1:allow, 2:block
            "profile.default_content_setting_values.media_stream_mic": 1,#allow mic
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.notifications": 2,
        })
        options.add_experimental_option('detach', True)
        options.add_experimental_option('excludeSwitches', ['enable-logging']) #自動制御log非表示
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)


    #### wait
    def wait(self, xpath):
        ## wait process
        wait = WebDriverWait(self.driver, 20) #この秒数待つ
        wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def join_freespace(self):
        try:
            gui.moveTo(5, 200,2)	
            gui.doubleClick()
            # ok_button = self.driver.find_element(By.XPATH, '//span[contains(text(), "OK")]/..')
            # ok_button.click()
            time.sleep(2)
            free_space = self.driver.find_element(By.XPATH, '//div[contains(text(), "参加者一覧を表示")]/../../../../div[1]')
            free_space.click()
        except Exception as ex:
            pass
            
    #### main
    def login(self):
        try:
            #### setting ####
            path = self.path #password and mailadress text path
            with open(path) as f:
                lines = f.readlines()
            mail_address = lines[0]
            password = lines[1]

            ##### scrap ####
            self.driver.get(self.freespace_path)
            # self.driver.set_window_size(1920,1080)
            self.driver.maximize_window()  #最大化
            window_size = self.driver.get_window_size()
            print(window_size)
            self.wait('//span[contains(text(), "メールアドレスでログイン")]/..')
            mail_button = self.driver.find_element(By.XPATH, '//span[contains(text(), "メールアドレスでログイン")]/..')
            mail_button.click()
            time.sleep(1)
            self.wait('//input[contains(@type, "text")]')
            mail_input = self.driver.find_element(By.XPATH, '//input[contains(@type, "text")]')
            mail_input.send_keys(mail_address)
            password_input = self.driver.find_element(By.XPATH, '//input[contains(@type, "password")]')
            password_input.send_keys(password)
            login_button = self.driver.find_element(By.XPATH, '//span[(text()="ログイン")]/..')
            login_button.click()
            time.sleep(1)
            self.wait('//span[contains(text(), "フリースペースに参加")]/..')
            free_space = self.driver.find_element(By.XPATH, '//span[contains(text(), "フリースペースに参加")]/..') #一回目のログインのみに使用
            free_space.click()
            time.sleep(1)
            enter_room_button = self.driver.find_element(By.XPATH, '//span[(text()="入室")]/..')
            enter_room_button.click()
            time.sleep(1)

            #### 入室後 ################
            ## wait process
            load_wait = WebDriverWait(self.driver, 20)
            load_wait.until(EC.presence_of_all_elements_located)
            time.sleep(10)
            popup_button = self.driver.find_element(By.XPATH, '//span[(text()="次へ")][last()]/..')
            popup_button.click()
            time.sleep(3)
            popup_button = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[14]/div/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/button')
            popup_button.click()
            time.sleep(3)
            popup_button = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[14]/div/div/div[1]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/button')
            popup_button.click()

            #twitter share button
            try:
                twitter_button = self.driver.find_element(By.XPATH, '//button[contains(@class, "style_closebutton__LNYIE")]')
                twitter_button.click()
                time.sleep(1)
            except Exception as e:
                print("there is not twitter button")

            print("success entering freespace!!")
        except Exception as ex:
            print("[error!!] 入室に失敗しました")
            print(ex)

    def to_bot(self,cmd):
        if '@' in cmd:
            print("@ bot")
            return True
        return False

    def text_analyze(self, cmd):
        text = ""
        if "help" in cmd:
            text = "help:この説明，yt: youtube再生，stop:停止，@が文字に含まれる:定型文返す"
        else:
            text = "Botです"
        return text

    def send_message(self, cmd):
        gui.moveTo(5,200,1)
        gui.doubleClick()
        time.sleep(2)
        textarea = self.driver.find_element(By.XPATH, '//*[@class="style_textarea__4WBOt"]')
        textarea.click()
        text = self.text_analyze(cmd)
        time.sleep(3)
        textarea.send_keys(text)
        time.sleep(1)
        textarea.send_keys(Keys.ENTER)

    def cmd_check(self, p_tag_message):
        if p_tag_message in self.cmd_list:
            return True
        else:
            return False

    def url_check(self, url):
        try:
            f = urllib.request.urlopen(url)
            print ("[corect url] OK:" + url )
            f.close()
            return True
        except:
            print ("NotFound:" + url)
            return False    

    def play_audio(self, p_tag_message, a_tag_message):
        # if self.cmd_check(p_tag_message):
        cmd = p_tag_message
        url = a_tag_message
        if cmd == 'yt stop':
            print(cmd)
            print("process kill...")
            subprocess.run("taskkill /im mpv.exe /F")
        elif 'yt' in cmd:
            if self.url_check(url):
                print(cmd)
                subprocess.run("taskkill /im mpv.exe /F")
                time.sleep(1)
                cmd = "mpv --vid=no "+ url
                subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
        elif self.to_bot(cmd):
            self.send_message(cmd)
        else:
            cmd = ""
            print("pass..")
        

    def run(self):
        pre_chat_count = 0
        post_chat_count = 0
        p_tag_message = ""
        a_tag_message = ""
        while(True):
            
            free_space = self.driver.find_elements(By.XPATH, '//div[contains(text(), "参加者一覧を表示")]')
            if len(free_space) == 1:##退出させられた場合
                print("退出しました")
                break

            messages = self.driver.find_elements(By.XPATH, '//div[contains(@class, "style_infiniteRow")]')
            post_chat_count = len(messages)
            if pre_chat_count < post_chat_count:
                print(post_chat_count)
                try:
                    p_tag_message = self.driver.find_element(By.XPATH, '//div[contains(@class, "style_infiniteRow")][1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/p[1]').text
                    p_tag_message.encode('utf-8')
                    p_tag_message.replace(' ', '')
                    print("p取得メッセージ",p_tag_message)
                    a_tag_message = self.driver.find_element(By.XPATH, '//div[contains(@class, "style_infiniteRow")][1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]').text
                    a_tag_message.encode('utf-8')
                    a_tag_message.replace(' ', '')
                    print("a取得メッセージ",a_tag_message)

                    if not p_tag_message == "":
                        self.play_audio(p_tag_message, a_tag_message)
                    else:
                        pass
                    
                    
                except NoSuchElementException as ex:
                    if not p_tag_message == "":
                        self.play_audio(p_tag_message, a_tag_message)
                    else:
                        pass
                
                pre_chat_count = post_chat_count
            
            time.sleep(1)
            

if __name__ == "__main__":
    mocri = Mocri()
    mocri.login()
    mocri.run()

    # ## freespace 待ち状態
    # time.sleep(10)
    # while(True):
    #     print("待機中です...")
    #     try:
    #         element = mocri.driver.find_elements(By.XPATH, '//div[contains(text(), "参加者一覧を表示")]')
    #         print(len(element))
    #         if len(element) == 1:
    #             mocri.join_freespace()
    #             mocri.run()
    #         else:
    #             print("There are not any free spaces...")
    #     except:
    #         pass
    #     time.sleep(120)
        
    