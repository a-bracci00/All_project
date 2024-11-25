import psutil
import time
import signal
import subprocess

def check_teamviewer_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'teamviewer' or process.info['name'] == 'teamviewerd':
            return True
        return False

def open_taemviewer_terminal():
    cmd = 'teamviewer'
    subprocess.Popen(cmd, shell=True)

def signal_handler(sig, frame):
    print('\nScript terminato manualmente')
    exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        if not check_teamviewer_running():
            open_taemviewer_terminal()
        
        time.sleep((300))

if __name__ == '__main__':
    main()
