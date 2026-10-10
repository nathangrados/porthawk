import socket


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Retourne True si le port TCP est ouvert."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def scan(host: str, ports: range, timeout: float = 1.0) -> list[int]:
    """Scanne une plage de ports et retourne la liste des ports ouverts."""
    open_ports = []
    for port in ports:
        if scan_port(host, port, timeout):
            open_ports.append(port)
    return open_ports


if __name__ == "__main__":
    target = "127.0.0.1"
    print(f"Scan de {target}...")
    for port in scan(target, range(1, 9000)):
        print(f"[+] Port {port} ouvert")