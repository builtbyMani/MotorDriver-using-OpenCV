import socket

# --- SETTINGS ---
# TYPE THE EXACT IP SHOWN ON YOUR OLED SCREEN HERE:
ESP_IP = "10.91.152.162"  
ESP_PORT = 4210

print(f"Sending test to {ESP_IP}...")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cmd = input("Type RUN or STOP and hit Enter: ")
    sock.sendto(cmd.encode(), (ESP_IP, ESP_PORT))
    print(f"Sent {cmd}")