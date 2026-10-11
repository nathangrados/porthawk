import socket
import argparse





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

def parse_ports(port_str : str) -> range:
    """Convertit '1-1000' en range(1,1001)."""
    try : 
        start, end = port_str.split("-")
        start, end = int(start), int(end)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Format invalide : '{port_str}' (attendu : 1-1000)")
    if not (1 <= start <= end <= 65535) :
        raise argparse.ArgumentTypeError("Les ports doivent être compris entre 1 et 65535, et début <= fin.")

    return range(start, end + 1)

def parse_args() -> argparse.Namespace :
    parser = argparse.ArgumentParser(description = "PortHawk : scanner de ports TCP")
    parser.add_argument("-t", "--target", required = True, help="IP ou nom d'hôte à scanner")
    parser.add_argument("-p", "--ports", type = parse_ports, default = parse_ports("1-1024"), help="Plage de ports, ex 1-1000 (défaut : 1-1024)")
    parser.add_argument("--timeout", type=float, default = 1.0, help = "Délai par port en secondes (défault : 1.0)")
    return parser.parse_args()

def main():
    args = parse_args()
    print(vars(args))

    ip = resolvehost(args.target)
    if ip is None :
        print(f"[!] Impossible de résoudre l'hôte : {args.target}")
        return

    print(f"Scan de {args.target}...")
    for port in scan(args.target, args.ports, args.timeout):
        print(f"[+] Port {port} ouvert")

if __name__ == "__main__":
    main()