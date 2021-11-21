from utils.JSONSerializator import JSONSerializator
from datetime import datetime as dt


class MagnetoDTO(JSONSerializator):

    def __init__(self):
        self.x = None
        self.y = None
        self.z = None

    def dump(self):
        return str("{};{};{};{}".format(dt.now().strftime("%H:%M:%S %Y-%m-%d"), self.x, self.y, self.z))
