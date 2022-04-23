
import sys

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

config_builder = ConfigBuilder()

config = config_builder.parse_config("./config.json")


if __name__ == "__main__":
    pass
