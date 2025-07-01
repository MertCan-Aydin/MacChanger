# 🔧 MacChanger  

This Python script allows you to easily change the MAC address of a network interface (e.g., `eth0`, `wlan0`) on Linux systems. It is particularly useful for privacy or penetration testing purposes, such as on Kali Linux, where you may want to spoof or randomize your MAC address.  

---  

## 🚀 Features  

- Changes the MAC address of a specified interface to your desired value.  
- Automatically detects the current MAC address.  
- Verifies whether the change was successful.  
- Provides a simple command-line interface.  

---  

## 🧠 How It Works?  

1. Takes the interface name (e.g., `eth0`, `wlan0`) and the new MAC address as user input.  
2. Temporarily disables the network interface using `ifconfig`.  
3. Changes the MAC address.  
4. Re-enables the interface.  
5. Verifies the new MAC address to confirm the change.  

---  

## 🛠️ Requirements  

- Python 3  
- A Linux-based system  
- Root (administrator) privileges  

---  

## 🔍 Usage  

```bash  
sudo python3 macChanger.py -i <interface_name> -m <new_mac_address>  
```  

### Example:  

```bash  
sudo python3 macChanger.py -i eth0 -m 00:11:22:33:44:55  
```  

---  

## 📦 About the Code  

```python  
def get_user_input():  
    # Uses argparse to get interface and MAC address from the terminal  
```  

```python  
def change_mac_address(interface, new_mac):  
    # Uses ifconfig to disable the interface, change MAC, and re-enable it  
```  

```python  
def get_current_mac(interface):  
    # Extracts the current MAC address from ifconfig output using regex  
```  

At the end of the script, the new MAC address is checked to confirm the change, ensuring a reliable result for the user.  

---  

## 🧪 Security Notes  

- MAC address changes are **not permanent**. Rebooting the system may revert it to the original.  
- Ensure the new MAC address follows a valid format (e.g., `00:11:22:33:44:55`).  
- Some network cards may not support random MAC address assignments.  

---  
