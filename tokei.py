import pygame
import math
import datetime
import sys

# Pygameの初期化
pygame.init()

# ウィンドウのサイズ設定
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("針時計")

# 色の定義
WHITE = (255, 255, 255) #白
BLACK = (0, 0, 0) #黒
RED = (255, 0, 0) #赤
GREEN = (0, 255, 0) #緑
BLUE = (0, 0, 255) #青

# 時計の中心点と半径
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 150

# 時計の針の長さ
HOUR_HAND_LENGTH = 80
MINUTE_HAND_LENGTH = 120
SECOND_HAND_LENGTH = 140

# クロック
clock = pygame.time.Clock()
fps = 60

# 時計のテクスチャ
circle_tokei = pygame.image.load("images/tokei.png")
second_hand_img = pygame.image.load("images/second_hand.png")
minute_hand_img = pygame.image.load("images/hand_1.png")
hour_hand_img = pygame.image.load("images/hand_1.png")

hour_hand_img = pygame.transform.scale(hour_hand_img, (HOUR_HAND_LENGTH // 2, HOUR_HAND_LENGTH*2))
minute_hand_img = pygame.transform.scale(minute_hand_img, (MINUTE_HAND_LENGTH // 2, MINUTE_HAND_LENGTH*2))
second_hand_img = pygame.transform.scale(second_hand_img, (4, SECOND_HAND_LENGTH*2))

# 時計の針を描画する関数
def draw_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=CENTER)
    screen.blit(rotated_image, new_rect)

# メインループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 画面を白で塗りつぶす
    screen.fill(WHITE)

    # 時計の外円を描画
    screen.blit(circle_tokei, (WIDTH // 2 - 227, HEIGHT // 2 - 170))

    # 現在の時刻を取得
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    
    # 角度を計算（12時を基準に反時計回りが正の方向）
    hour_angle = (hours + minutes / 60) * 30  # 1時間あたり30度
    minute_angle = (minutes + seconds / 60) * 6  # 1分あたり6度
    second_angle = seconds * 6  # 1秒あたり6度

    # 時計の針を描画
    draw_hand(hour_hand_img, hour_angle)
    draw_hand(minute_hand_img, minute_angle)
    draw_hand(second_hand_img, second_angle)

    # 画面の更新
    pygame.display.update()

    # フレームレートの設定
    clock.tick(fps)