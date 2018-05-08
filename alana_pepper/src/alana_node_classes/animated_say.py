import service_utils as su
from nao_interaction_msgs.srv import Say, SayRequest


def say(text):
    su.call_service(
        "/naoqi_driver/animated_speech/say",
        Say,
        SayRequest(text=text)
    )
