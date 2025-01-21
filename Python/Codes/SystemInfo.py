import machine
import os
import sys
import gc
print(f"Hello user!")
print(f"============")
# Информация о системе
print("System Info:")
print(f"============")
sys_info = os.uname()
print(f"OS: {sys_info.sysname}")
print(f"Machine: {sys_info.machine}")
print(f"Release: {sys_info.release}")
print(f"Version: {sys_info.version}")
print(f"Node Name: {sys_info.nodename}")
print(f"Python version: {sys.version}\n")

# Память
gc.collect()
print("Memory Info:")
print(f"Free memory: {gc.mem_free()} bytes")
print(f"Total memory: {gc.mem_alloc() + gc.mem_free()} bytes\n")

# Информация о чипе
chip_id = machine.unique_id()
print(f"Chip ID: {chip_id.hex()}")

# Температура процессора
try:
    temp = machine.temperature()  # Не на всех платах работает
    print(f"CPU Temperature: {temp} °C")
except AttributeError:
    print("CPU Temperature: Not available on this platform")
print(f"============")
