import socket


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Retourne True si le port TCP est ouvert."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def scan(host: str, ports: range, timeout: float = 1.0) -> list[int]:
    """Scanne une plage de ports et retourne la liste des ports ouverts."""
    open_ports = []
    try : 
        for port in ports:
            if scan_port(host, port, timeout):
                open_ports.append(port)
    except KeyboardInterrupt :
        print("\n[!] Scan interrompu par l'utilisateur.")
    return open_ports


def resolvehost(host) : 
    # retourne l'IP, ou None si le nom est invalide
    try : 
        return socket.gethostbyname(host)
    except socket.gaierror :
        return None


def main(): 
    target = "127.0.0.1"

    ip = resolvehost(target)
    if ip is None :
        print(f"[!] Impossible de résoudre l'hôte : {target}")
        return

    print(f"Scan de {target}...")
    for port in scan(target, range(1, 65536)):
        print(f"[+] Port {port} ouvert")

if __name__ == "__main__":
    main()