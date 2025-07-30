#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BlueTiger-Tools v1.0
Multi-Tool pour la Cybersécurité Défensive (Blue Team)
Créé comme alternative défensive aux outils Red Team

Fonctionnalités:
- Monitoring réseau temps réel
- Analyse de logs et détection d'anomalies  
- Scanner de vulnérabilités système
- Détection de processus suspects
- Vérification d'intégrité fichiers
- Génération de rapports sécurité
"""

import os
import sys
import json
import time
import psutil
import socket
import hashlib
import datetime
import subprocess
from pathlib import Path
from colorama import init, Fore, Back, Style

# Initialisation des couleurs
init(autoreset=True)

class BlueTigerTools:
    def __init__(self):
        self.version = "1.0"
        self.banner = f"""
{Fore.BLUE}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  {Fore.WHITE}██████╗ ██╗     ██╗   ██╗███████╗████████╗██╗ ██████╗ ███████╗{Fore.BLUE}║
║  {Fore.WHITE}██╔══██╗██║     ██║   ██║██╔════╝╚══██╔══╝██║██╔════╝ ██╔════╝{Fore.BLUE}║  
║  {Fore.WHITE}██████╔╝██║     ██║   ██║█████╗     ██║   ██║██║  ███╗█████╗  {Fore.BLUE}║
║  {Fore.WHITE}██╔══██╗██║     ██║   ██║██╔══╝     ██║   ██║██║   ██║██╔══╝  {Fore.BLUE}║
║  {Fore.WHITE}██████╔╝███████╗╚██████╔╝███████╗   ██║   ██║╚██████╔╝███████╗{Fore.BLUE}║
║  {Fore.WHITE}╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚══════╝{Fore.BLUE}║
║                                                              ║
║               {Fore.CYAN}🛡️  DEFENSIVE CYBERSECURITY TOOLKIT  🛡️{Fore.BLUE}              ║
║                         {Fore.WHITE}Version {self.version} - Blue Team{Fore.BLUE}                       ║
╚══════════════════════════════════════════════════════════════╝
        """
        
        self.config_file = "config.json"
        self.load_config()
        
    def load_config(self):
        """Charge la configuration"""
        default_config = {
            "alerts_enabled": True,
            "log_file": "bluetiger_logs.txt",
            "scan_interval": 30,
            "monitored_ports": [22, 80, 443, 3389, 21, 25],
            "whitelist_ips": ["127.0.0.1", "::1"],
            "max_cpu_threshold": 80,
            "max_memory_threshold": 85
        }
        
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                self.config = default_config
                self.save_config()
        except:
            self.config = default_config
            
    def save_config(self):
        """Sauvegarde la configuration"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Impossible de sauvegarder la config: {e}")

    def log_event(self, message, level="INFO"):
        """Enregistre les événements"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        try:
            with open(self.config["log_file"], 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except:
            pass
            
        # Affichage console avec couleurs
        color = Fore.GREEN if level == "INFO" else Fore.YELLOW if level == "WARNING" else Fore.RED
        print(f"{color}[{level}] {message}")

    def display_menu(self):
        """Affiche le menu principal"""
        print(self.banner)
        print(f"{Fore.CYAN}┌─────────────────────────────────────────────────────────────┐")
        print(f"│                    {Fore.WHITE}MENU PRINCIPAL{Fore.CYAN}                         │")
        print(f"├─────────────────────────────────────────────────────────────┤")
        print(f"│  {Fore.GREEN}1.{Fore.WHITE} 🔍 Monitoring Réseau Temps Réel                    {Fore.CYAN}│")
        print(f"│  {Fore.GREEN}2.{Fore.WHITE} 📊 Analyse des Processus Système                   {Fore.CYAN}│")
        print(f"│  {Fore.GREEN}3.{Fore.WHITE} 🔒 Scanner de Ports Ouverts                       {Fore.CYAN}│")
        print(f"│  {Fore.GREEN}4.{Fore.WHITE} 🛡️  Détection de Processus Suspects                {Fore.CYAN}│")
        print(f"│  {Fore.GREEN}5.{Fore.WHITE} 📁 Vérification d'Intégrité Fichiers              {Fore.CYAN}│")
        print(f"│  {Fore.GREEN}6.{Fore.WHITE} 📋 Analyse des Logs Système                       {Fore.CYAN}│")
        print(f"│  {Fore.GREEN}7.{Fore.WHITE} ⚙️  Configuration                                  {Fore.CYAN}│")
        print(f"│  {Fore.GREEN}8.{Fore.WHITE} 📈 Rapport de Sécurité                            {Fore.CYAN}│")
        print(f"│  {Fore.GREEN}9.{Fore.WHITE} ℹ️  Informations Système                          {Fore.CYAN}│")
        print(f"│  {Fore.RED}0.{Fore.WHITE} 🚪 Quitter                                        {Fore.CYAN}│")
        print(f"└─────────────────────────────────────────────────────────────┘")

    def network_monitor(self):
        """Monitoring réseau en temps réel"""
        print(f"\n{Fore.BLUE}[NETWORK MONITOR] Démarrage du monitoring réseau...")
        self.log_event("Démarrage du monitoring réseau")
        
        try:
            print(f"{Fore.CYAN}Surveillance des connexions actives (Ctrl+C pour arrêter):\n")
            
            while True:
                connections = psutil.net_connections(kind='inet')
                suspicious_found = False
                
                for conn in connections:
                    if conn.status == 'ESTABLISHED' and conn.raddr:
                        remote_ip = conn.raddr.ip
                        remote_port = conn.raddr.port
                        local_port = conn.laddr.port
                        
                        # Vérification IP suspecte (pas dans whitelist)
                        if remote_ip not in self.config["whitelist_ips"]:
                            if remote_port in [4444, 6666, 1337, 31337]:  # Ports suspects
                                print(f"{Fore.RED}⚠️  CONNEXION SUSPECTE: {remote_ip}:{remote_port} -> Port local {local_port}")
                                self.log_event(f"Connexion suspecte détectée: {remote_ip}:{remote_port}", "WARNING")
                                suspicious_found = True
                            else:
                                print(f"{Fore.GREEN}✓ Connexion normale: {remote_ip}:{remote_port} -> Port local {local_port}")
                
                if not suspicious_found:
                    print(f"{Fore.GREEN}✓ Aucune connexion suspecte détectée")
                
                time.sleep(self.config["scan_interval"])
                os.system('cls' if os.name == 'nt' else 'clear')
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[INFO] Monitoring arrêté par l'utilisateur")
            self.log_event("Monitoring réseau arrêté")

    def analyze_processes(self):
        """Analyse des processus système"""
        print(f"\n{Fore.BLUE}[PROCESS ANALYZER] Analyse des processus en cours...")
        
        suspicious_processes = ['nc.exe', 'netcat', 'cmd.exe', 'powershell.exe', 'mimikatz']
        high_cpu_processes = []
        high_memory_processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                proc_info = proc.info
                
                # Vérification processus suspects
                if any(susp in proc_info['name'].lower() for susp in suspicious_processes):
                    print(f"{Fore.RED}⚠️  PROCESSUS SUSPECT: {proc_info['name']} (PID: {proc_info['pid']})")
                    self.log_event(f"Processus suspect détecté: {proc_info['name']} PID:{proc_info['pid']}", "WARNING")
                
                # Vérification usage CPU élevé
                if proc_info['cpu_percent'] > self.config["max_cpu_threshold"]:
                    high_cpu_processes.append((proc_info['name'], proc_info['pid'], proc_info['cpu_percent']))
                
                # Vérification usage mémoire élevé
                if proc_info['memory_percent'] > self.config["max_memory_threshold"]:
                    high_memory_processes.append((proc_info['name'], proc_info['pid'], proc_info['memory_percent']))
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Affichage des processus gourmands
        if high_cpu_processes:
            print(f"\n{Fore.YELLOW}[CPU] Processus avec usage CPU élevé:")
            for name, pid, cpu in high_cpu_processes[:5]:
                print(f"  • {name} (PID: {pid}) - CPU: {cpu:.1f}%")
        
        if high_memory_processes:
            print(f"\n{Fore.YELLOW}[MEMORY] Processus avec usage mémoire élevé:")
            for name, pid, memory in high_memory_processes[:5]:
                print(f"  • {name} (PID: {pid}) - Mémoire: {memory:.1f}%")

    def port_scanner(self):
        """Scanner de ports ouverts"""
        print(f"\n{Fore.BLUE}[PORT SCANNER] Scan des ports locaux...")
        
        open_ports = []
        dangerous_ports = [21, 22, 23, 25, 53, 135, 139, 445, 1433, 3389, 5432]
        
        for port in range(1, 1024):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex(('127.0.0.1', port))
            
            if result == 0:
                open_ports.append(port)
                color = Fore.RED if port in dangerous_ports else Fore.GREEN
                risk = "RISQUE ÉLEVÉ" if port in dangerous_ports else "Normal"
                print(f"{color}Port {port}: OUVERT - {risk}")
                
                if port in dangerous_ports:
                    self.log_event(f"Port dangereux ouvert détecté: {port}", "WARNING")
            
            sock.close()
        
        print(f"\n{Fore.CYAN}Total ports ouverts: {len(open_ports)}")
        self.log_event(f"Scan ports terminé - {len(open_ports)} ports ouverts")

    def detect_suspicious_processes(self):
        """Détection avancée de processus suspects"""
        print(f"\n{Fore.BLUE}[THREAT DETECTION] Recherche de menaces...")
        
        # Signatures de malwares courants
        malware_signatures = [
            'wannacry', 'conficker', 'zeus', 'trojan', 'keylogger',
            'ransomware', 'cryptolocker', 'emotet', 'trickbot'
        ]
        
        threats_found = 0
        
        for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
            try:
                proc_info = proc.info
                
                # Vérification nom du processus
                if any(malware in proc_info['name'].lower() for malware in malware_signatures):
                    print(f"{Fore.RED}🚨 MALWARE DÉTECTÉ: {proc_info['name']} (PID: {proc_info['pid']})")
                    threats_found += 1
                
                # Vérification ligne de commande suspecte
                if proc_info['cmdline']:
                    cmdline = ' '.join(proc_info['cmdline']).lower()
                    if any(word in cmdline for word in ['download', 'wget', 'curl', 'powershell -enc']):
                        print(f"{Fore.YELLOW}⚠️  ACTIVITÉ SUSPECTE: {proc_info['name']} - Commande: {cmdline[:50]}...")
                        
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        if threats_found == 0:
            print(f"{Fore.GREEN}✓ Aucune menace détectée")
        else:
            print(f"{Fore.RED}🚨 {threats_found} menace(s) potentielle(s) détectée(s)")
            self.log_event(f"{threats_found} menaces détectées", "CRITICAL")

    def file_integrity_check(self):
        """Vérification d'intégrité des fichiers système importants"""
        print(f"\n{Fore.BLUE}[FILE INTEGRITY] Vérification de l'intégrité...")
        
        important_files = [
            "/etc/passwd", "/etc/shadow", "/etc/hosts",  # Linux
            "C:\\Windows\\System32\\drivers\\etc\\hosts",  # Windows
            "C:\\Windows\\System32\\config\\SAM"
        ]
        
        for file_path in important_files:
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.sha256(f.read()).hexdigest()
                    
                    print(f"{Fore.GREEN}✓ {file_path}")
                    print(f"  SHA256: {file_hash[:32]}...")
                    
                except Exception as e:
                    print(f"{Fore.RED}❌ Erreur lecture {file_path}: {e}")

    def system_info(self):
        """Informations système complètes"""
        print(f"\n{Fore.BLUE}[SYSTEM INFO] Informations système:")
        print(f"{Fore.CYAN}═" * 60)
        
        # Informations système
        uname = os.uname() if hasattr(os, 'uname') else None
        if uname:
            print(f"{Fore.WHITE}Système: {uname.sysname} {uname.release}")
            print(f"Machine: {uname.machine}")
        
        # CPU et Mémoire
        print(f"CPU: {psutil.cpu_count()} cœurs - Usage: {psutil.cpu_percent()}%")
        memory = psutil.virtual_memory()
        print(f"Mémoire: {memory.percent}% utilisée ({memory.used // 1024**3}GB / {memory.total // 1024**3}GB)")
        
        # Réseau
        net_stats = psutil.net_io_counters()
        print(f"Réseau: {net_stats.bytes_sent // 1024**2}MB envoyés, {net_stats.bytes_recv // 1024**2}MB reçus")
        
        # Disque
        disk = psutil.disk_usage('/')
        print(f"Disque: {disk.percent}% utilisé ({disk.used // 1024**3}GB / {disk.total // 1024**3}GB)")

    def run(self):
        """Lance l'interface principale"""
        while True:
            try:
                self.display_menu()
                choice = input(f"\n{Fore.WHITE}Votre choix: {Fore.GREEN}")
                
                if choice == '1':
                    self.network_monitor()
                elif choice == '2':
                    self.analyze_processes()
                elif choice == '3':
                    self.port_scanner()
                elif choice == '4':
                    self.detect_suspicious_processes()
                elif choice == '5':
                    self.file_integrity_check()
                elif choice == '6':
                    print(f"{Fore.YELLOW}[INFO] Fonctionnalité d'analyse de logs en développement")
                elif choice == '7':
                    print(f"{Fore.YELLOW}[INFO] Interface de configuration en développement")
                elif choice == '8':
                    print(f"{Fore.YELLOW}[INFO] Génération de rapport en développement")
                elif choice == '9':
                    self.system_info()
                elif choice == '0':
                    print(f"{Fore.GREEN}Merci d'avoir utilisé BlueTiger-Tools! 🛡️")
                    break
                else:
                    print(f"{Fore.RED}Choix invalide!")
                
                input(f"\n{Fore.WHITE}Appuyez sur Entrée pour continuer...")
                os.system('cls' if os.name == 'nt' else 'clear')
                
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Arrêt demandé par l'utilisateur")
                break
            except Exception as e:
                print(f"{Fore.RED}Erreur: {e}")

if __name__ == "__main__":
    print(f"{Fore.BLUE}Initialisation de BlueTiger-Tools...")
    app = BlueTigerTools()
    app.run()
