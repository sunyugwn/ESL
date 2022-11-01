#모듈 불러오기
import pygame as pg   #화면 띄움
import time           #시간 측정

#pygame 초기화
pg.init()

############################함수########################
#게임 끄기
def close_screen():
    for event in pg.event.get():
        if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            global close_screen
            close_screen = True

#초기화
def reset():
    global start_time
    start_time = time.time()

#글씨 쓰기
def make_text(font, text, color, x, y, tf, center):
    t = font.render(text, tf, color)
    if center == True:
        t_rect = t.get_rect()
        t_rect.centerx = x
        t_rect.centery = y
        return screen.blit(t, t_rect)
    
    return screen.blit(t, (x, y))


########################초기설정#############################
#화면
screen_size = [1920, 1080]   #화면 크기(일반 컴퓨터에서 전체화면)
screen = pg.display.set_mode(screen_size, pg.FULLSCREEN)   #스크린 만들기

#폰트
credit_font = pg.font.Font('font/MonoplexKR-Text.ttf', 124)              #크레딧 폰트
big_font = pg.font.Font('font/SuseongBatang.ttf', 64)                    #큰 폰트(안내 등)
name_font = pg.font.Font('font/SuseongBatang.ttf', 36)                   #이름 폰트
text_font = pg.font.Font('font/MonoplexKRNerd-light.ttf', 22)            #기본 폰트
mission_font = pg.font.Font('font/나눔손글씨 노력하는 동희.ttf', 48)       #미션 폰트

#fps 설정
clock = pg.time.Clock()
fps = 60


################메인###############
#












##############닫기##################
#pygame 종료
pg.quit()
#프로그램 종료
import sys
sys.exit()