import pygame
import sys

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("조이스틱이 연결되지 않았습니다!")
    sys.exit()
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"조이스틱 연결됨: {joystick.get_name()}")

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("라디오마스터 2D 드론 (이미지 버전)")

WHITE = (255, 255, 255)

# 이미지 로드
image_path = "C:\hamsterair\drone.png"
try:
    drone_img = pygame.image.load(image_path)
except:
    print("이미지를 불러올 수 없습니다!")
    sys.exit()

# 크기 조정
drone_size = 80
drone_img = pygame.transform.scale(drone_img, (drone_size, drone_size))

# 드론 위치
drone_x, drone_y = 350, 500   #원래는 100,100
speed = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    axis_x = joystick.get_axis(0)  
    axis_y = -joystick.get_axis(1)  

    drone_x += axis_x * speed
    drone_y += axis_y * speed

    drone_x = max(0, min(WIDTH - drone_size, drone_x))
    drone_y = max(0, min(HEIGHT - drone_size, drone_y))

    screen.fill(WHITE)
    screen.blit(drone_img, (drone_x, drone_y))
    pygame.display.flip()
    clock.tick(60)
