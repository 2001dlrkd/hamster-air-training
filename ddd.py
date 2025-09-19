import pygame

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick name: {joystick.get_name()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of hats: {joystick.get_numhats()}")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")

        elif event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")

        elif event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value:.2f}")

        elif event.type == pygame.JOYHATMOTION:
            print(f"Hat {event.hat} moved to {event.value}")

pygame.quit()
