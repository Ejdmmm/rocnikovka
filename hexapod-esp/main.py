
import config

if config.HTTP_SERVER_ON:
    import controller
    controller.start()



from network import Pin, PWM
servo = PWM(Pin(13), freq=50)
servo.duty(20)
servo.duty(70)
servo.duty(120)
