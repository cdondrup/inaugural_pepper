import service_utils as su
from nao_interaction_msgs.srv import SetTrackerTarget, SetTrackerTargetRequest
from nao_interaction_msgs.srv import StartTracker, StartTrackerRequest
from std_srvs.srv import Empty, EmptyRequest


def start(id):
    su.call_service(
        "/naoqi_driver/tracker/register_target",
        SetTrackerTarget,
        SetTrackerTargetRequest(target=SetTrackerTargetRequest.PEOPLE, values=[id])
    )
    su.call_service(
        "/naoqi_driver/tracker/track",
        StartTracker,
        StartTrackerRequest(target=StartTrackerRequest.PEOPLE)
    )


def stop():
    su.call_service(
        "/naoqi_driver/tracker/stop_tracker",
        Empty,
        EmptyRequest()
    )
    su.call_service(
        "/naoqi_driver/tracker/unregister_all_targets",
        Empty,
        EmptyRequest()
    )
