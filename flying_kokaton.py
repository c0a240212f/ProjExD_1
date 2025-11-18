import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)  # 練習8
    kk_img = pg.transform.flip(pg.image.load("fig/3.png"), True, False)  # 練習3
    kk_rct = kk_img.get_rect()  # 練習10
    kk_rct.center = 300, 200  # 練習10
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 背景スクロール（x を 0..3199 でループ）
        x = tmr % 3200  # 練習5 -> 9
        screen.blit(bg_img, [-x, 0])         # 練習5
        screen.blit(bg_img2, [-x + 1600, 0]) # 練習8
        screen.blit(bg_img, [-x + 3200, 0])  # 練習9

        key_lst = pg.key.get_pressed()

        # デフォルトの横速度（背景と同じ速度で左に流れる）
        vx = -1

        # 右キーが押されていれば右に進む（要求どおり）
        if key_lst[pg.K_RIGHT]:
            vx = +1

        # 左キーが押されていれば左に進む（任意の補助）
        if key_lst[pg.K_LEFT]:
            vx = -1

        # 縦方向
        vy = 0
        if key_lst[pg.K_UP]:
            vy = -1
        elif key_lst[pg.K_DOWN]:
            vy = +1

        # move_ip を 1回だけ呼ぶ
        kk_rct.move_ip(vx, vy)

        screen.blit(kk_img, kk_rct)  # 練習4 -> 10
        pg.display.update()
        tmr += 1
        clock.tick(200)  # 練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
