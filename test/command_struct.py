from collections import namedtuple

# Структура команд для управления
ControlData = namedtuple(
    'ControlData',
    'roll_mode pitch_mode yaw_mode roll_speed roll_angle pitch_speed pitch_angle yaw_speed yaw_angle')
# Структура системной команды
CMD_EXECUTE_MENU = namedtuple(
    'CMD_EXECUTE_MENU',
    'comm_n')
Message = namedtuple(
    'Message',
    'start_character command_id payload_size header_checksum payload payload_checksum')

