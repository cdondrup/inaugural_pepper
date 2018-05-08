from std_srvs.srv import Empty, EmptyRequest
import service_utils as su


def enable(enable):
    su.call_service(
        "/mummer_asr/resume" if enable else "/mummer_asr/pause",
        Empty,
        EmptyRequest()
    )
