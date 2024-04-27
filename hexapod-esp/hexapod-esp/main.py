
import config

if config.HTTP_SERVER_ON:
    import controller
    controller.start()