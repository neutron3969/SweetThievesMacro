import pyautogui as pag
import pytesseract
import time as t
import numpy as np


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"
width,height=pag.size()

def pixel(ratio):
    capture_region=[int(ratio[0]*width),int(ratio[1]*height),int(ratio[2]*width),int(ratio[3]*height)]
    return capture_region
    
def capture(p):
    pag.screenshot('C:/fallguysnick/test.png',region=(p[0],p[1],p[2],p[3]))
    global word
    word=pytesseract.image_to_string('C:\\fallguysnick\\test.png',lang='eng')
    
def normal(mu,sigma,siz,over):
    while True:
        rand_number=np.random.normal(mu,sigma,size=siz)
        if rand_number>over:
            break
    return rand_number
        

rule_ratio=[0.4062,0.15,0.1875,0.0347]
skip_ratio=[0.9492,0.9514,0.0508,0.0486]

rule_pixel=pixel(rule_ratio)
skip_pixel=pixel(skip_ratio)


macro_number=int(input('매크로 횟수(숫자만): '))
shutdown=input('매크로 후 컴퓨터를 종료할려면 \'y\' 입력: ')

print('3초 후 시작합니다...')
t.sleep(1)
print('2초 후 시작합니다...')
t.sleep(1)
print('1초 후 시작합니다...')
t.sleep(1)


score=1
macro_start=t.time()
guardian_number=0
thief_number=0
degrading_start=t.time()
now_first=t.strftime('%Y-%m-%d %H:%M:%S')



while True:
    f=open("C:/fallguysnick/log.txt", 'a')
    print('-----------------------------------------')
    print(score,'번째 달도')
    
    now=t.strftime('%Y-%m-%d %H:%M:%S')
    f.write('%s번째 매크로 시작 시간: %s\n'%(score,now))
    f.close()
    print('현재: 결산 화면 및 대기실')
    while True:
        back_enter_rand=normal(0.6,0.1,1,0.3)

        pag.press("enter",interval=back_enter_rand)
        capture(skip_pixel)

        if 'BACK' in word:
            break

    print('현재: 매칭 및 게임 플레이')
    
    start=t.time()
    while True:
        t.sleep(1)
        capture(rule_pixel)

        if 'GUARDIAN' in word:
            guardian_number=guardian_number+1
            print(guardian_number,'번째 수호자')
            print('재시작')
            back_enter_rand=normal(0.6,0.1,1,0.3)
            pag.press("esc",interval=back_enter_rand)
            back_enter_rand=normal(0.6,0.1,1,0.3)
            pag.press("enter",interval=back_enter_rand)
            score=score+1
            break

        if 'THIEF' in word:
            thief_number=thief_number+1
            print(thief_number,'번째 도둑')
            
            while True:
                t.sleep(1)
                capture(skip_pixel)
                if 'SKIP' in word:
                    back_enter_rand=normal(0.6,0.1,1,0.3)
                    pag.press("enter",interval=back_enter_rand)
                    score=score+1
                    break
            break
        
        if sec>=300:
            pag.press("enter",interval=exit_esc_rand)
            print('매칭 및 서버 오류')
            break
        
    if score==macro_number+1:
        
        macro_time=t.time()-macro_start
        macro_time_hour=int(macro_time//3600)
        macro_time_minute=int((macro_time%3600)//60)
        macro_time_second=int((macro_time%3600)%60)
        
        print('매크로 완료')
        print('%s번 매크로 총 걸린시간: %s시간 %s분 %s초\n'%(macro_number,macro_time_hour,macro_time_minute,macro_time_second))

        f=open("C:/fallguysnick/log.txt", 'a')
        f.write('-----------------------------------------\n')
        
        f.write('매크로 시작 시간: %s\n'%now_first)
        now=t.strftime('%Y-%m-%d %H:%M:%S')
        f.write('매크로 종료 시간: %s\n'%now)
        f.write('도둑 횟수: %s\n'%thief_number)
        f.write('수호자 횟수: %s\n'%guardian_number)
        f.write('%s번 매크로 총 걸린시간: %s시간 %s분 %s초\n'%(macro_number,macro_time_hour,macro_time_minute,macro_time_second))
        f.write('-----------------------------------------\n')
        f.write('-----------------------------------------\n')
        f.close()
        break

if shutdown=='y':
    import os
    os.system('shutdown -s -f -t 100')
    print('컴퓨터가 곧 꺼집니다...')





















        





