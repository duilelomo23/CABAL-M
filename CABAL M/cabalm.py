import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time
import datetime

# 获取当前时间
Online_rewards = 20        #約1秒一次 5分鐘點擊~ 怕沒有執行任務
times = 0                 #判斷當前小時時間
heartbeat = 0             #心跳 判斷幾次搜索到模擬器存在
# 定義要搜索的圖片列表
target_images = ['1.png', '2.png', '3.png', '4.png', '5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png']
auto = False  #自動分配
sure = False  #屬性確認
close_m = True  #模擬器存在才執行腳本
count = False   #判斷條件是否出現才執行5

while True:
    # 捕獲整個螢幕的截圖
    Online_rewards -= 1
    print(Online_rewards,'倒數')
    if Online_rewards == 1:
        pyautogui.press('~')
        Online_rewards = 20
    screen = np.array(ImageGrab.grab())


    #禮物合
    # current_time = datetime.datetime.now()
    # hour = current_time.hour
    # if hour > times:
    #     pyautogui.press('Esc')
    #     time.sleep(0.5)
    #     pyautogui.press('shift')
    #     time.sleep(0.5)
    #     pyautogui.press('7')
    #     time.sleep(0.5)
    #     pyautogui.press('Esc')      
    #     time.sleep(0.5)
    #     pyautogui.press('~')  
    #     time.sleep(0.5)
    #     times = hour


    # 是否找到目標圖片   
    found_target = False


    # 遍歷目標圖片列表
    for target_image in target_images:
        # print(target_image)
        
        # 讀取目標圖片
        target = cv2.imread(target_image, cv2.IMREAD_COLOR)
        target = target.astype(np.uint8)

        # 在截取的螢幕上搜索目標圖片
        res = cv2.matchTemplate(screen, target, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        # 如果找到目標圖片
        if len(loc[0]) > 0:       
            #Found_target找到圖片
            found_target = True
            close_m = True
            heartbeat=0


            #尋找雷電模擬文字  類心跳 判斷模擬器是否存在
            if target_image == '8.png':          
                # print('存在')   
                continue
    
            
            if target_image == '4.png': # 4 才能執行 5
                count = True
                continue

            #未找到4 跳出  不執行5
            if  target_image == '5.png' and count == False:         
                continue

            #如果找到1 .14 自動分配和屬性確定 執行5
            if target_image == '1.png':     
                print('找到1')
                pyautogui.press('0')
                time.sleep(0.3)
                pyautogui.press('1')
                time.sleep(0.3)
                pyautogui.press('n')
                time.sleep(1)
                pyautogui.press('~')
                continue
                # auto = True
            # if target_image == '14.png':
            #     print('找到14')
            #     sure = True
            # if auto == True and sure == True:
            #     print('1.14找到')
            #     count = True
    
                       
            # close_m= 搜索到雷電模擬器才執行點擊動作
            if close_m == True:        
                    
                # 計算目標圖片的中心位置
                h, w, _ = target.shape
                target_x, target_y = loc[1][0] + w // 2, loc[0][0] + h // 2


                # 將滑鼠移動到目標圖片的右上角並點擊左鍵
                pyautogui.moveTo(target_x + w // 2, target_y - h // 2)
                pyautogui.click()
                time.sleep(0.1)
                print('執行',target_image)


                # if target_image == '10.png':  ??
                #     close_m = False
                #     continue


                #如果執行5 重新判斷是否有條件符合
                if target_image == '5.png':      
                    auto = False
                    sure = False
                    count = False

                    

                #出現6延遲1.5秒
                if target_image == '6.png':      
                    time.sleep(1.5)



                #如果進入省電模式 移動滑鼠
                if target_image == '13.png':      
                    pyautogui.moveRel(0, -100)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveRel(300, 0,duration=0.5)
                    time.sleep(1)
                    pyautogui.mouseUp(button='left')
                    time.sleep(0.2)
                    print('123')
                    continue

                pyautogui.press('~')


    # 如果沒有找到任何目標圖片,可以在這裡執行其他操作
    if not found_target:
        close_m = False
        print("沒有找到任何目標圖片")

        #找不到所有圖片10次 結束腳本ˇ
        heartbeat += 1                      
        if heartbeat == 10:
            break
        print(heartbeat)


    # 暫停一小段時間,避免CPU使用率過高
    time.sleep(0.1)
