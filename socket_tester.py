import asyncio
from bleak import BleakClient, BleakScanner
import socket
#Replace with your device's MAC address
DEVICE_MAC = 'D8:3A:DD:5F:D3:10'

#UUIDs
SERVICE_UUID = '12345678-1234-5678-1234-56789abcdef0'
CHAR_UUID = 'abcdef01-1234-5678-1234-56789abcdef0'

async def main():
    # Discover devices
    devices = await BleakScanner.discover()
    for device in devices:
        if device.address == DEVICE_MAC:
            print(f"Found device: {device.name} with address {device.address}")

    async with BleakClient(DEVICE_MAC) as client:
        print(f"Connected to {DEVICE_MAC}")

    #Read the characteristic value
        value = await client.read_gatt_char(CHAR_UUID)
    data = value.decode('utf-8')
    HOST = "127.0.0.1"
    PORT = 18735

    # create socket and connect
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((HOST, PORT))

    # send data
    cs.sendall(data)

    # wait for a result
    data = cs.recv(1024)
    print("result: ", data)
    cs.close()
#Run the event loop
asyncio.run(main())