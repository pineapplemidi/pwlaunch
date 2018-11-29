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


class PwLaunch(ControlSurface):

    def __init__(self, c_instance):
        super(PwLaunch, self).__init__(c_instance)
        with self.component_guard():
            is_momentary = True
            config = self._open_config()
            self._session = self._setup_session(config['width'], config['height'])
            self._button_down = ButtonElement(is_momentary, 0, 0, 12)
            self._session.set_scene_bank_down_button(self._button_down)
            self._button_up = ButtonElement(is_momentary, 0, 0, 11)
            self._session.set_scene_bank_up_button(self._button_up)
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
            "/users/berry/somefile.txt",
                mode='w', encoding='utf-8') as f:
            f.write(log_str)
            f.close()
