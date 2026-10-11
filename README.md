# PortHawk 🦅

Un scanner de ports et de services écrit en Python

## À propos

PortHawk est un projet d'apprentissage

## Installation

Python 3.10 ou supérieur suffit.

```bash
git clone https://github.com/nathangrados/porthawk.git
cd porthawk
```

## Utilisation

```bash
python3 porthawk.py -t 127.0.0.1                    # ports 1-1024 par défaut
python3 porthawk.py -t localhost -p 1-9000          # plage de ports personnalisée
python3 porthawk.py -t 127.0.0.1 --timeout 0.5      # délai réduit par port
python3 porthawk.py -t 127.0.0.1 --threads 200      # plus de threads en parallèle
python3 porthawk.py -h                              # afficher l'aide
```

### Options

| Option | Description | Défaut |
|---|---|---|
| `-t`, `--target` | IP ou nom d'hôte à scanner (obligatoire) | |
| `-p`, `--ports` | Plage de ports, ex. `1-1000` | `1-1024` |
| `--timeout` | Délai maximal par port, en secondes | `1.0` |
| `--threads` | Nombre de threads en parallèle | `100` |

### Exemple de sortie

```
Scan de localhost (127.0.0.1)...
[+] Port 8000 ouvert
```