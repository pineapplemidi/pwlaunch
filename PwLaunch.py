from __future__ import absolute_import, print_function, unicode_literals

import Live
import io
import json
import sys

sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/ \
lib/python2.7/site-packages/')

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonElement import ButtonElement

RED_THIRD = 4
GREEN_FULL = 52
GREEN_BLINK = 100

class PwLaunch(ControlSurface):
    def __init__(self, c_instance):
        super(PwLaunch, self).__init__(c_instance)
        with self.component_guard():
            is_momentary = True
            config = self._open_config()
            self._session = self._setup_session(
                config['width'], config['height'])
            self._button_down = ButtonElement(is_momentary, 0, 0, 12)
            self._session.set_scene_bank_down_button(self._button_down)
            self._button_up = ButtonElement(is_momentary, 0, 0, 11)
            self._session.set_scene_bank_up_button(self._button_up)
            self._launch_button = ButtonElement(is_momentary, 0, 0, 81)
            clip_slot = self._session.scene(0).clip_slot(0)
            clip_slot.set_stopped_value(RED_THIRD)
            clip_slot.set_triggered_to_play_value(GREEN_BLINK)
            clip_slot.set_started_value(GREEN_FULL)
            clip_slot.set_launch_button(self._launch_button)
            self._stop_button = ButtonElement(is_momentary, 0, 0, 82)
            clip_stop_buttons = []
            clip_stop_buttons.append(self._stop_button)
            self._session.set_stop_track_clip_buttons(tuple(clip_stop_buttons))
            self.set_highlighting_session_component(self._session)

    def _open_config(self):
        with open('/users/berry/config.json') as f:
            data = json.load(f)
            self.log(json.dumps(data))
            return json.loads(json.dumps(data))

    def _setup_session(self, width, height):
        session = SessionComponent(width, height)
        session.set_offsets(0, 0)
        return session

    def log(self, message):
        log_str = 'LOG: ' + message + '\n'
        with io.open(
            "/users/berry/pwlaunch.txt",
                mode='w', encoding='utf-8') as f:
            f.write(log_str)
            f.close()
