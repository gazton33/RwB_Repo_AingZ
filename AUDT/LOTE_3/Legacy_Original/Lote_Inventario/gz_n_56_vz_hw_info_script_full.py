"""
Script AVANZADO para inventario de hardware y software en Windows.
- Extrae CPU, RAM, GPU, almacenamiento, red, sistema operativo, versiones de software instalado, dispositivos conectados y más.
- Ideal para auditoría técnica e integración en gemelos digitales.
- Exporta CSV y log markdown.

Dependencias principales: ``psutil``.
Dependencias opcionales: ``cpuinfo`` para detalles de CPU, ``GPUtil`` para GPUs,
``wmi`` y ``pywin32`` para información de software en Windows.
"""
import platform
import psutil
import socket
import csv
from datetime import datetime
import os

try:
    import cpuinfo
except ImportError:
    cpuinfo = None
try:
    import GPUtil
except ImportError:
    GPUtil = None
try:
    import wmi
except ImportError:
    wmi = None

fecha = datetime.now().strftime('%Y-%m-%d_%H-%M')

# 1. INFO GENERAL DEL SISTEMA
def info_sistema():
    datos = {
        'nombre_equipo': platform.node(),
        'sistema_operativo': platform.system(),
        'version_os': platform.version(),
        'release_os': platform.release(),
        'arquitectura': platform.machine(),
        'procesador': platform.processor() or (cpuinfo.get_cpu_info()['brand_raw'] if cpuinfo else 'N/A'),
        'ip_local': socket.gethostbyname(socket.gethostname()),
        'fecha_reporte': fecha,
    }
    return datos

# 2. CPU Y RAM
def info_cpu_ram():
    ram = psutil.virtual_memory()
    info = {
        'total_ram_gb': round(ram.total / (1024**3), 2),
        'ram_disponible_gb': round(ram.available / (1024**3), 2),
        'cpu_cores_logicos': psutil.cpu_count(),
        'cpu_cores_fisicos': psutil.cpu_count(logical=False),
    }
    return info

# 3. GPU
def info_gpu():
    if GPUtil:
        gpus = GPUtil.getGPUs()
        gpus_info = []
        for gpu in gpus:
            gpus_info.append(f"{gpu.name} ({gpu.memoryTotal}MB)")
        return {'gpus': '; '.join(gpus_info) if gpus_info else 'N/A'}
    return {'gpus': 'N/A'}

# 4. ALMACENAMIENTO
def info_disco():
    discos = psutil.disk_partitions()
    data = []
    for d in discos:
        try:
            usage = psutil.disk_usage(d.mountpoint)
            data.append(f"{d.device} ({round(usage.total/(1024**3), 1)}GB, libre: {round(usage.free/(1024**3), 1)}GB)")
        except:
            continue
    return {'almacenamiento': '; '.join(data)}

# 5. SOFTWARE INSTALADO (solo Windows, requiere wmi)
def software_instalado():
    softwares = []
    if wmi:
        c = wmi.WMI()
        for p in c.Win32_Product():
            try:
                name = p.Name
                version = p.Version or ''
                if name:
                    softwares.append(f"{name} {version}")
            except:
                continue
    else:
        # Alternativa: leer del registro (más rápido, menos completo)
        softwares.append('wmi no disponible: instalar con pip install wmi')
    return {'softwares': ' | '.join(softwares[:50]) + (' ...' if len(softwares)>50 else '')}

# 6. DISPOSITIVOS USB (opcional)
def dispositivos_usb():
    usb_list = []
    if wmi:
        c = wmi.WMI()
        for usb in c.Win32_USBHub():
            try:
                usb_list.append(usb.Name)
            except:
                continue
    return {'usb_dispositivos': ' | '.join(usb_list)}

# 7. RED
def info_red():
    addrs = psutil.net_if_addrs()
    nics = []
    for iface, lst in addrs.items():
        for l in lst:
            if l.family == 2:
                nics.append(f"{iface}: {l.address}")
    return {'redes': ' | '.join(nics)}

# 8. EXPORTAR CSV y MARKDOWN
def exportar_csv(info_dict, nombre='reporte_hw_gz_n56vz.csv'):
    with open(nombre, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for k, v in info_dict.items():
            writer.writerow([k, v])

def exportar_md(info_dict, nombre='reporte_hw_gz_n56vz.md'):
    with open(nombre, 'w', encoding='utf-8') as f:
        for k, v in info_dict.items():
            f.write(f'- **{k}:** {v}\n')

# INTEGRACIÓN GENERAL
def generar_reporte():
    datos = {}
    datos.update(info_sistema())
    datos.update(info_cpu_ram())
    datos.update(info_gpu())
    datos.update(info_disco())
    datos.update(info_red())
    datos.update(software_instalado())
    datos.update(dispositivos_usb())
    exportar_csv(datos, f'reporte_hw_gz_n56vz_{fecha}.csv')
    exportar_md(datos, f'reporte_hw_gz_n56vz_{fecha}.md')
    print('\nREPORTE RESUMIDO:')
    for k, v in datos.items():
        print(f'{k}: {v}')
    print(f"\nCSV exportado como reporte_hw_gz_n56vz_{fecha}.csv\nMarkdown: reporte_hw_gz_n56vz_{fecha}.md")

if __name__ == '__main__':
    generar_reporte()
