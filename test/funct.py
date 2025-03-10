from command_struct import *
import struct
import serial

# Выделение бита для каждого параметра
def pack_control_data(control_data: ControlData) -> bytes:
    return struct.pack('<BBBhhhhhh', *control_data)


# Выделение бита для каждого параметра
def pack_cmd_execute_menu(cmd_execute_menu: CMD_EXECUTE_MENU) -> bytes:
    return struct.pack('<B', *cmd_execute_menu)



# Создание сообщения. Состоит из command_id и payload
def create_message(command_id: int, payload: bytes) -> Message:
    payload_size = len(payload)
    return Message(start_character=ord('>'),
                   command_id=command_id,
                   payload_size=payload_size,
                   header_checksum=(command_id + payload_size) % 256,
                   payload=payload,
                   payload_checksum=sum(payload) % 256)


def create_message2(command_id: int, payload: bytes) -> Message:
    payload_size = len(payload)
    return Message(start_character=ord('>'),
                   command_id=command_id,
                   payload_size=payload_size,
                   header_checksum=(command_id + payload_size) % 256,
                   payload=payload,
                   payload_checksum=sum(payload) % 256)


#
def pack_message(message: Message) -> bytes:
    message_format = '<BBBB{}sB'.format(message.payload_size)
    return struct.pack(message_format, *message)


def unpack_message(data: bytes, payload_size: int) -> Message:
    message_format = '<BBBB{}sB'.format(payload_size)
    return Message._make(struct.unpack(message_format, data))


def read_message(connection: serial.Serial, payload_size: int) -> Message:
    # 5 is the length of the header + payload checksum byte
    # 1 is the payload size
    response_data = connection.read(5 + payload_size)
    print('received response', response_data)
    return unpack_message(response_data, payload_size)


def rotate_gimbal():
    CMD_CONTROL = 67
    control_data = ControlData(roll_mode=0, roll_speed=0, roll_angle=0,
                               pitch_mode=0, pitch_speed=0, pitch_angle=0,
                               yaw_mode=1, yaw_speed=100, yaw_angle=90)
    # print('command to send:', control_data)
    packed_control_data = pack_control_data(control_data)
    # print('packed command as payload:', packed_control_data)
    message = create_message(CMD_CONTROL, packed_control_data)
    # print('created message:', message)
    packed_message = pack_message(message)
    # print('packed message:', packed_message)

    connection = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=10)
    print('send packed message:', packed_message)
    connection.write(packed_message)
    message = read_message(connection, 1)
    print('received confirmation:', message)
    print('confirmed command with ID:', ord(message.payload))


def on_motor(n):
    print("123")
    MOTOR_ON = 69
    cmd_execute_menu = CMD_EXECUTE_MENU(comm_n=n)
    print('command to send:', cmd_execute_menu)
    packed_cmd_execute_menu = pack_cmd_execute_menu(cmd_execute_menu)
    print('packed command as payload:', packed_cmd_execute_menu)
    message = create_message(MOTOR_ON, packed_cmd_execute_menu)
    print('created message:', message)
    packed_message = pack_message(message)
    print('packed message:', packed_message)
    connection = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=10)
    print('send packed message:', packed_message)
    connection.write(packed_message)


def yaw_motor_control(yaw):
    CMD_CONTROL = 67
    control_data = ControlData(roll_mode=0, roll_speed=0, roll_angle=0,
                               pitch_mode=0, pitch_speed=0, pitch_angle=0,
                               yaw_mode=2, yaw_speed=100, yaw_angle=yaw)
    # print('command to send:', control_data)
    packed_control_data = pack_control_data(control_data)
    # print('packed command as payload:', packed_control_data)
    message = create_message(CMD_CONTROL, packed_control_data)
    # print('created message:', message)
    packed_message = pack_message(message)
    # print('packed message:', packed_message)

    connection = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=10)
    print('send packed message:', packed_message)
    connection.write(packed_message)
    message = read_message(connection, 1)
    print('received confirmation:', message)
    print('confirmed command with ID:', ord(message.payload))


def pitch_motor_control(pitch, yaw):
    CMD_CONTROL = 67
    control_data = ControlData(roll_mode=2, roll_speed=500, roll_angle=pitch,
                               pitch_mode=2, pitch_speed=500, pitch_angle=0,
                               yaw_mode=2, yaw_speed=500, yaw_angle=yaw)
    # print('command to send:', control_data)
    print(yaw, pitch)
    packed_control_data = pack_control_data(control_data)
    # print('packed command as payload:', packed_control_data)
    message = create_message(CMD_CONTROL, packed_control_data)
    # print('created message:', message)
    packed_message = pack_message(message)
    # print('packed message:', packed_message)

    connection = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=10)
    print('send packed message:', packed_message)
    connection.write(packed_message)
    message = read_message(connection, 1)
    print('received confirmation:', message)
    print('confirmed command with ID:', ord(message.payload))




