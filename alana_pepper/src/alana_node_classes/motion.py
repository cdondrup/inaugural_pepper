from nao_interaction_msgs.srv import SetBreathEnabled, SetBreathEnabledRequest
from std_srvs.srv import Empty, EmptyRequest
import service_utils as su


def enable_breathing(enable):
    su.call_service(
        "/naoqi_driver/motion/set_breath_enabled",
        SetBreathEnabled,
        SetBreathEnabledRequest(
            chain_name=SetBreathEnabledRequest.ARMS,
            enable=enable
        )
    )


def wake_up():
    su.call_service(
        "/naoqi_driver/motion/wake_up",
        Empty,
        EmptyRequest()
    )


def rest():
    su.call_service(
        "/naoqi_driver/motion/rest",
        Empty,
        EmptyRequest()
    )
