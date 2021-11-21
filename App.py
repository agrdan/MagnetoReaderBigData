from mqtt.MqttClient import Mqtt
from threading import Thread
from time import sleep as delay
from model.MagnetoDTO import MagnetoDTO


class Main(Thread):

    def __init__(self, mqtt: Mqtt):
        Thread.__init__(self)
        self.mqtt = mqtt
        self.mqtt.start()

    def run(self):
        while (True):
            msg = self.mqtt.getFromQueue()
            if (msg is not None):
                topic, values = msg.split(";")
                magnetoValues = MagnetoDTO().serialize(values, False)
                print(magnetoValues.dump())
            delay(1)


if __name__ == '__main__':
    mqtt = Mqtt("lsm/data")
    main = Main(mqtt)
    main.start()
