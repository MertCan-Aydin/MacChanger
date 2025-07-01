# 🔧 MacChanger

Bu Python betiği, Linux sistemlerde bir ağ arayüzünün (örneğin `eth0`, `wlan0`) MAC adresini kolayca değiştirmenizi sağlar. Özellikle Kali Linux gibi pentest amaçlı kullanılan sistemlerde, MAC adresinizi gizlemek veya değiştirmek istediğinizde işe yarar.

---

## 🚀 Özellikler

- Belirli bir arayüzün MAC adresini istediğiniz gibi değiştirir.
- Mevcut MAC adresini otomatik olarak tespit eder.
- Başarılı olup olmadığını doğrular.
- Terminal üzerinden kolay kullanım sağlar.

---

## 🧠 Nasıl Çalışır?

1. Kullanıcıdan arayüz adı (`eth0`, `wlan0` gibi) ve yeni MAC adresi alınır.
2. `ifconfig` komutlarıyla ağ arayüzü geçici olarak kapatılır.
3. MAC adresi değiştirilir.
4. Arayüz tekrar açılır.
5. Yeni MAC adresi kontrol edilerek işlem doğrulanır.

---

## 🛠️ Gereksinimler

- Python 3
- Linux tabanlı bir sistem
- Root (yönetici) yetkileri

---

## 🔍 Kullanım

```bash
sudo python3 macChanger.py -i <arayüz_adı> -m <yeni_mac_adresi>
```

### Örnek:

```bash
sudo python3 macChanger.py -i eth0 -m 00:11:22:33:44:55
```

---

## 📦 Kod Hakkında

```python
def get_user_input():
    # argparse ile terminalden arayüz ve MAC bilgisi alınıyor
```

```python
def change_mac_address(interface, new_mac):
    # ifconfig ile arayüz kapatılır, MAC değiştirilir ve tekrar açılır
```

```python
def get_current_mac(interface):
    # Mevcut MAC adresi regex ile ifconfig çıktısından alınır
```

Kodun sonunda, mevcut MAC adresi kontrol edilerek işlem doğrulanır. Böylece kullanıcıya güvenli bir sonuç sunulur.

---

## 🧪 Güvenlik Notları

- MAC adresi değişikliği kalıcı değildir. Sistemi yeniden başlattığınızda eski haline dönebilir.
- Gerçek bir MAC adresi formatı kullandığınızdan emin olun. Örnek: `00:11:22:33:44:55`
- Bazı ağ kartları rastgele MAC adresi atamalarını desteklemez.

---
