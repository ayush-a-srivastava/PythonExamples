import platform
import psutil
import cpuinfo
import wmi

print(f'Architecture: {platform.architecture()}')
print(f'Network name: {platform.node()}')
print(f'Operating System: {platform.platform()}')
print(f'Processor Name: {platform.processor()}')

my_cpuinfo = cpuinfo.get_cpu_info()
print(f'Full CPU Name: {my_cpuinfo['brand_raw']}')
print(f'Total RAM:  {psutil.virtual_memory().total/1024 /1024 / 1024:0.2f} GB')

pc = wmi.WMI()
os_info = pc.Win32_OperatingSystem()[0]
print(os_info)
print(pc.Win32_Processor()[0].name)
print(pc.Win32_VideoController()[0].name)