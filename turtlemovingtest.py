import pygame 
import turtle 
import time 


pygame.init() 
pygame.joystick.init() 
joystick = pygame.joystick.Joystick(0) 
joystick.init() 

num_axes = joystick.get_numaxes()
print("축 개수:", num_axes)


t = turtle.Turtle()
t.shape("turtle") 
t.penup()
t.speed(1)
screen = turtle.Screen()
screen.title("조이스틱 터틀 제어")


while True:
    pygame.event.pump()
    
    
    x_axis = joystick.get_axis(0)  
    if abs(x_axis) > 0.1:         
        t.right(x_axis * 10)       
    
    
    y_axis = joystick.get_axis(1)  
    if abs(y_axis) > 0.1:
        t.forward(-y_axis * 10)    

    time.sleep(0.05)

     

 
