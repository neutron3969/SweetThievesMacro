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
error_ratio=[0.5391,0.375,0.1016,0.0486]
connection_ratio=[0.3961,0.4736,0.0711,0.0264]
defend_ratio=[0.3047,0.8542,0.0781,0.0312]


rule_pixel=pixel(rule_ratio)
skip_pixel=pixel(skip_ratio)
error_pixel=pixel(error_ratio)
connection_pixel=pixel(connection_ratio)
defend_pixel=pixel(defend_ratio)


pag.FAILSAFE = False

print('모니터 해상도: %sx%s'%(width,height))
macro_number=int(input('수호자가 탈주 한 도둑 횟수(숫자만): '))
shutdown=input('매크로 후 컴퓨터를 종료할려면 \'y\' 입력: ')

print('3초 후 시작합니다...')
t.sleep(1)
print('2초 후 시작합니다...')
t.sleep(1)
print('1초 후 시작합니다...')
t.sleep(1)


score=1
score2=0
macro_start=t.time()

guardian_number=0
thief_number=0
not_run_number=0
connection_number=0
error_number=0

degrading_start=t.time()
now_first=t.strftime('%Y-%m-%d %H:%M:%S')

f=open("C:/fallguysnick/log.txt", 'a')
f.write('==============================\n')
f.write('도둑 예상 횟수: %s번\n'%(macro_number))
f.close()
while True:
    f=open("C:/fallguysnick/log.txt", 'a')
    print('-----------------------------------------')
    print(score,'번째 달도')
    
    now=t.strftime('%Y-%m-%d %H:%M:%S')
    f.write('-----------------------------------------\n')
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
        capture(defend_pixel)

        if 'Defend' in word:
            guardian_number=guardian_number+1
            print(guardian_number,'번째 수호자')
            print('재시작')
            back_enter_rand=normal(1,0.1,1,0.3)
            pag.press("esc",interval=back_enter_rand)
            back_enter_rand=normal(0.6,0.1,1,0.3)
            pag.press("enter",interval=back_enter_rand)
            score=score+1
            break

        if 'Steal' in word:
            thief_number=thief_number+1
            print(thief_number,'번째 도둑')

            thief_start=t.time()
            while True:
                t.sleep(1)
                capture(skip_pixel)
                if 'SKIP' in word:
                    back_enter_rand=normal(0.6,0.1,1,0.3)
                    pag.press("enter",interval=back_enter_rand)
                    score=score+1
                    score2=score2+1
                    break
                
                thief_sec=t.time()-thief_start
                if thief_sec>=50:
                    pag.press("esc",interval=back_enter_rand)
                    back_enter_rand=normal(0.8,0.1,1,0.3)
                    pag.press("s",interval=back_enter_rand)
                    back_enter_rand=normal(0.8,0.1,1,0.3)
                    pag.press("s",interval=back_enter_rand)
                    back_enter_rand=normal(0.8,0.1,1,0.3)
                    pag.press("s",interval=back_enter_rand)
                    back_enter_rand=normal(0.8,0.1,1,0.3)
                    pag.press("enter",interval=back_enter_rand)




                    print('수호자 안 나감')
                    not_run_number=not_run_number+1
                    score=score+1
                    break
            break
        
        capture(connection_pixel)
        if 'Connection' in word:
            print('Connection Error')
            score=score+1
            connection_number=connection_number+1
            break

        sec=t.time()-start
        if sec>=180:
            back_enter_rand=normal(0.6,0.1,1,0.3)
            pag.press("esc",interval=back_enter_rand)
            back_enter_rand=normal(0.6,0.1,1,0.3)
            pag.press("enter",interval=back_enter_rand)
            print('매칭 및 서버 오류')
            score=score+1
            error_number=error_number+1
            break
    f=open("C:/fallguysnick/log.txt", 'a')
    run_number=thief_number-not_run_number
    f.write('도둑: %s (탈주O: %s, 탈주X: %s), 수호자: %s\n'%(thief_number,run_number,not_run_number,guardian_number))
    f.write('Connection Error: %s, 매칭 및 서버 오류: %s\n'%(connection_number,error_number))
    f.close()
        
    if score2==macro_number:
        break


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
f.close()

        
if shutdown=='y':
    import os
    os.system('shutdown -s -f -t 100')
    print('컴퓨터가 곧 꺼집니다...')
