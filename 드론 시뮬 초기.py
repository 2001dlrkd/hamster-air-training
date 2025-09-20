import pygame
import sys

# 초기화
pygame.init()
pygame.joystick.init()

# 조이스틱 연결 확인
if pygame.joystick.get_count() == 0:
    print("조이스틱이 연결되지 않았습니다!")
    sys.exit()
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"조이스틱 연결됨: {joystick.get_name()}")

# 화면 크기
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("라디오마스터 2D 드론 (상하좌우)")

# 색상
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# 드론 설정
drone_size = 40
drone_x, drone_y = WIDTH // 2, HEIGHT // 2
speed = 5

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 스틱 입력 (왼쪽 스틱만 사용)
    axis_x = joystick.get_axis(0)  # 좌우
    axis_y = joystick.get_axis(1)  # 상하

    # 이동 (Y축은 위아래 방향 반전 필요할 수 있음)
    drone_x += axis_x * speed
    drone_y += axis_y * speed

    # 화면 경계 제한
    drone_x = max(0, min(WIDTH - drone_size, drone_x))
    drone_y = max(0, min(HEIGHT - drone_size, drone_y))

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (drone_x, drone_y, drone_size, drone_size))
    pygame.display.flip()

    clock.tick(60)
