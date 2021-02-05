from enum import Enum

class MsgArea(Enum):
    UPLOAD_CSV = "upload"

class Msgs:
    def __init__(self):
        self.master = {}

    def add_error(self, area, error_msg):
        if area not in self.master:
            self.master[area] = {}
        self.master[area]["Error"] = error_msg

    def add_info(self, area, info_msg):
        if area not in self.master:
            self.master[area] = {}
        self.master[area]["Info"] = info_msg

    def add_success(self, area, success_msg):
        if area not in self.master:
            self.master[area] = {}
        self.master[area]["Success"] = success_msg

    def get_all_messages(self):
        return self.master
