# 🔧 MacChanger

This Python script allows you to easily change the MAC address of a network interface (e.g. `eth0`, `wlan0`) on Linux systems. This is especially useful in pentesting systems like Kali Linux when you want to hide or change your MAC address.

---

## 🚀 Features

- Changes the MAC address of a specific interface as desired.
- Automatically detects the current MAC address.
- Verifies whether it was successful or not.
- Provides easy operation via the terminal.

---

## 🧠 How does it work?

1. The interface name (`eth0`, `wlan0` etc.) and the new MAC address are obtained from the user.
2. The network interface is temporarily closed with `ifconfig` commands.
3. The MAC address is changed.
4. The interface is turned back on.
5. The operation is verified by checking the new MAC address.

---

## 🛠️ Requirements

- Python 3
- A Linux-based system
- Root (administrator) privileges

---

## 🔍 Usage

``bash
sudo python3 macChanger.py -i <interface_name> -m <new_mac_address>
```

### Example:

``bash
sudo python3 macChanger.py -i eth0 -m 00:11:22:33:44:55
```

---

## 📦 About Code

``python
def get_user_input():
    # get interface and MAC information from terminal with argparse
```

``python
def change_mac_address(interface, new_mac):
    # close the interface with ifconfig, change the MAC and reopen

``python
def get_current_mac(interface):
    # Get current MAC address with regex from ifconfig output
```

At the end of the code, the transaction is verified with checkin

Translated with DeepL.com (free version)
