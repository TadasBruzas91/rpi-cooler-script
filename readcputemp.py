import psutil
from python_json_config import ConfigBuilder

config_builder = ConfigBuilder()
config = config_builder.parse_config("./config.json")

cpu_temp_sensors = config.cpu_temp_sensors


def get_cpu_temp():
    temp_sensors = psutil.sensors_temperatures()
    for temp_sensor in temp_sensors:
        if temp_sensor in cpu_temp_sensors:
            size = len(temp_sensors[temp_sensor])
            all_values = 0
            for values in temp_sensors[temp_sensor]:
                all_values += values[1]
            result = "{:.1f}".format(all_values / size)
            return float(result)
