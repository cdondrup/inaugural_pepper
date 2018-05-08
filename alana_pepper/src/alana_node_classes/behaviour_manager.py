import rospy
import service_utils as su
from nao_interaction_msgs.srv import BehaviorManagerControl, BehaviorManagerControlRequest
from nao_interaction_msgs.srv import BehaviorManagerInfo, BehaviorManagerInfoRequest


def start_behaviour(name):
    su.call_service(
        "/naoqi_driver/behaviour_manager/start_behaviour",
        BehaviorManagerControl,
        BehaviorManagerControlRequest(name=name)
    )


def stop_behaviour(name):
    su.call_service(
        "/naoqi_driver/behaviour_manager/stop_behaviour",
        BehaviorManagerControl,
        BehaviorManagerControlRequest(name=name)
    )


def toggle_behaviour(name):
    try:
        start_behaviour(name)
    except:
        pass
    try:
        stop_behaviour(name)
    except:
        pass


def wait_for_behaviour(name):
    while not rospy.is_shutdown():
        if name not in su.call_service(
                "/naoqi_driver/behaviour_manager/get_running_behaviors",
                BehaviorManagerInfo,
                BehaviorManagerInfoRequest()
        ).behaviors:
            return
        else:
            rospy.sleep(.01)
