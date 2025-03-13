import logging
import random

FORMAT = "%(levelname)s - %(message)s"

class BatterySimulation:
    def __init__(self, logger):
        self.logger = logger

    def simulate_last_hour(self):
        """Метод для симуляции данных"""

        for minute in range(1, 60 + 1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.logger.debug("{0} C".format(temperature))
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning("{0} C".format(temperature))
            elif temperature > 35:
                self.logger.critical("{0} C".format(temperature))
            else:
                raise Exception("Temperature out of range.")


def main():
    logger = logging.getLogger("battery_temperature")
    handler = logging.FileHandler("battery_temperature.log", mode="w")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    battery_simulation = BatterySimulation(logger)
    battery_simulation.simulate_last_hour()


if __name__ == "__main__":
    print("I prefer to be a module")
    main()
else:
    print("I like to be a module")