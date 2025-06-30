import subprocess
import argparse
import re


def get_user_input():
    parser = argparse.ArgumentParser(description="MAC adresi değiştirici")
    parser.add_argument("-i", "--interface", required=True, help="Değiştirilecek ağ arayüzü (örnek: eth0)")
    parser.add_argument("-m", "--mac", required=True, help="Yeni MAC adresi (örnek: 00:11:22:33:44:55)")
    return parser.parse_args()


def change_mac_address(interface, new_mac):
    print(f"[+] {interface} arayüzü kapatılıyor...")
    subprocess.call(["ifconfig", interface, "down"])
    print(f"[+] MAC adresi {new_mac} olarak ayarlanıyor...")
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    print(f"[+] {interface} arayüzü tekrar açılıyor...")
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    output = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    if mac_address:
        return mac_address.group(0)
    return None


# Ana akış
print("🔧 MacChanger başlatıldı...")
args = get_user_input()

change_mac_address(args.interface, args.mac)
current_mac = get_current_mac(args.interface)

if current_mac.lower() == args.mac.lower():
    print(f"[✓] Başarılı! MAC adresi {current_mac} olarak değiştirildi.")
else:
    print(f"[✗] Hata! MAC adresi değiştirilemedi. Şu anki MAC: {current_mac}")