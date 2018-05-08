#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import urllib2
import json
import random
import alana_node_classes.motion as motion
import alana_node_classes.asr as asr
import alana_node_classes.animated_say as animated_say
import alana_node_classes.behaviour_manager as behaviour_manager
from alana_node_classes.config import Config
from end_of_speech.msg import EndOfSpeech


class AlanaNode(object):
    def __init__(self, name):
        rospy.loginfo("Starting {} ...".format(name))
        rospy.on_shutdown(self.on_shutdown)
        self.conf = Config(rospy.get_param("~conf"))
        self.speaking_app = rospy.get_param("~mummer_speaking_app")
        self.listening_app = rospy.get_param("~mummer_listening_app")
        motion.wake_up()
        motion.enable_breathing(True)
        rospy.Subscriber("/end_of_speech/eos", EndOfSpeech, self.callback)
        asr.enable(True)
        behaviour_manager.toggle_behaviour(self.listening_app)
        rospy.loginfo("{} started ...".format(name))

    def callback(self, msg):
        asr.enable(False)
        print self.listening_app
        print self.speaking_app
        behaviour_manager.toggle_behaviour(self.speaking_app)
        print "RECEIVED", msg

        found = False
        for k, v in self.conf.concepts.items():
            # print "Concept", k
            for keyword in v:
                if keyword in msg.final_utterance:
                    # print keyword, k
                    found = True
                    try:
                        behaviour_manager.start_behaviour(self.conf.applications[k])
                        behaviour_manager.wait_for_behaviour(self.conf.applications[k])
                    except KeyError:
                        # print self.conf.precanned_text[k]
                        animated_say.say(random.choice(self.conf.precanned_text[k]))
                    finally:
                        break

        if not found:
            question = urllib2.quote(msg.final_utterance.encode('UTF-8'))
            call_url = "http://35.168.209.123:5000/?q={question}&sid=MUMMER&cs=1.0".format(question=question)
            print call_url
            try:
                answer = urllib2.urlopen(call_url, timeout=10.).read()
            except:
                return
            answer = json.loads(answer)
            print "ANSWER", answer

            animated_say.say(answer[1])

        asr.enable(True)
        behaviour_manager.toggle_behaviour(self.listening_app)

    def on_shutdown(self):
        asr.enable(False)


if __name__ == "__main__":
    rospy.init_node("alana_node")
    a = AlanaNode(rospy.get_name())
    rospy.spin()
