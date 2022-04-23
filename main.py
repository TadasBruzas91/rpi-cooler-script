
import sys
from time import sleep

try:
    from py_console import console
except:
    print(
        "'py-console' not found!!!\nTo install library run 'pip install py-console'")
    sys.exit()

try:
    from python_json_config import ConfigBuilder
except:
    console.error(
        "'python-json-config' not found!!!")
    console.warn("To install library run 'pip install python-json-config'")
    sys.exit()


if __name__ == "__main__":
    from cooler import FanController
    config_builder = ConfigBuilder()

    config = config_builder.parse_config("./config.json")

    fanController = FanController()
    try:
        fanController.set_high_temp_threshold(
            config.cooling_temp_threshold.high)
        fanController.set_low_temp_threshold(config.cooling_temp_threshold.low)
        fanController.start_lgpio()
        fanController.set_fan_output_pin(config.output.fan1)
        fanController.daemon = True
        fanController.start()
        while True:
            sleep(60)
    except KeyboardInterrupt:
        fanController.close_lgpio()
