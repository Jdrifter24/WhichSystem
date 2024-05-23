import subprocess
import re

def get_ttl(ip_address):
    proc = subprocess.Popen(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = out.split()
    if len(out) >= 13:
        out = out[12].decode('utf-8')
        ttl = re.findall(r"\d{1,3}", out)
        if ttl:
            return int(ttl[0])
    return None

def identify_os(ttl_value):
    if ttl_value is not None:
        if ttl_value >= 127:
            return "Windows"
        elif ttl_value == 64:
            return "Linux"
    return "Desconocido"

def main():
    ip = input("Introduce la dirección IP: ")
    ttl_value = get_ttl(ip)
    if ttl_value:
        os_type = identify_os(ttl_value)
        print(f"El TTL para {ip} es {ttl_value}.")
        print(f"El sistema operativo probable es: {os_type}")
    else:
        print(f"No se pudo obtener el TTL para {ip}")

if __name__ == "__main__":
    main()
