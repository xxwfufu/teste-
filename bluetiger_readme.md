# 🛡️ BlueTiger-Tools v1.0

**Defensive Cybersecurity Toolkit - Blue Team Edition**

BlueTiger-Tools est un multi-outil de cybersécurité défensive conçu pour les équipes Blue Team. Inspiré des outils Red Team mais orienté protection et détection.

## 🎯 Fonctionnalités

### 🔍 Monitoring & Détection
- **Monitoring Réseau Temps Réel** - Surveillance des connexions suspectes
- **Analyse des Processus** - Détection de processus malveillants
- **Scanner de Ports** - Identification des ports ouverts dangereux
- **Détection de Menaces** - Reconnaissance de signatures de malwares

### 🛡️ Sécurité & Protection
- **Vérification d'Intégrité** - Contrôle des fichiers système critiques
- **Analyse des Logs** - Parsing et analyse des événements système
- **Alertes Automatiques** - Notifications en temps réel des incidents
- **Rapports de Sécurité** - Génération de rapports détaillés

### ⚙️ Configuration & Gestion
- **Configuration Flexible** - Paramètres personnalisables
- **Logs Détaillés** - Historique complet des événements
- **Interface Intuitive** - Menu coloré et navigation simple

## 🚀 Installation

### Prérequis
- Python 3.7+
- Système Windows/Linux/macOS
- Droits administrateur recommandés

### Installation Automatique (Windows)
```bash
# 1. Télécharger tous les fichiers dans un dossier
# 2. Double-cliquer sur install.bat
# 3. Lancer avec run.bat
```

### Installation Manuelle
```bash
# Cloner ou télécharger les fichiers
git clone [repository-url] bluetiger-tools
cd bluetiger-tools

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'outil
python main.py
```

## 📁 Structure du Projet

```
BlueTiger-Tools/
├── main.py              # Script principal
├── requirements.txt     # Dépendances Python
├── install.bat         # Installation Windows
├── run.bat             # Lancement rapide Windows
├── config.json         # Configuration (auto-généré)
├── bluetiger_logs.txt  # Logs (auto-généré)
└── README.md           # Documentation
```

## 🎮 Utilisation

### Menu Principal
```
1. 🔍 Monitoring Réseau Temps Réel
2. 📊 Analyse des Processus Système  
3. 🔒 Scanner de Ports Ouverts
4. 🛡️ Détection de Processus Suspects
5. 📁 Vérification d'Intégrité Fichiers
6. 📋 Analyse des Logs Système
7. ⚙️ Configuration
8. 📈 Rapport de Sécurité
9. ℹ️ Informations Système
0. 🚪 Quitter
```

### Exemples d'Usage

**Monitoring Réseau:**
- Surveillance continue des connexions
- Détection d'IPs suspectes
- Alertes sur ports dangereux (4444, 6666, 1337, etc.)

**Analyse de Processus:**
- Détection de processus suspects (nc.exe, mimikatz, etc.)
- Surveillance CPU/Mémoire élevée
- Identification d'activités malveillantes

**Scanner de Ports:**
- Scan des ports 1-1024
- Identification des services dangereux
- Alertes sur ports critiques (RDP, SSH, SMB, etc.)

## ⚙️ Configuration

Le fichier `config.json` permet de personnaliser:

```json
{
    "alerts_enabled": true,
    "log_file": "bluetiger_logs.txt",
    "scan_interval": 30,
    "monitored_ports": [22, 80, 443, 3389, 21, 25],
    "whitelist_ips": ["127.0.0.1", "::1"],
    "max_cpu_threshold": 80,
    "max_memory_threshold": 85
}
```

## 🚨 Détections Supportées

### Processus Suspects
- `nc.exe`, `netcat` - Outils de réseau
- `mimikatz` - Extraction de credentials
- `cmd.exe`, `powershell.exe` - Shells suspects
- Signatures de malwares connus

### Ports Dangereux
- **21** - FTP
- **22** - SSH  
- **23** - Telnet
- **135, 139, 445** - SMB/NetBIOS
- **1433** - SQL Server
- **3389** - RDP
- **4444, 6666, 1337** - Backdoors communes

### Activités Suspectes
- Connexions vers IPs externes
- Téléchargements suspects (wget, curl)
- Commandes PowerShell encodées
- Usage