import qrcode
import sys

def main_url():
    url = sys.argv[2]
    if not url:
        print("Inserisci un URL valido")
    img = qrcode.make(url)
    img.show()

def main_wifi():
    if sys.argv[2].upper() == "WPA" or sys.argv[2].upper() == "WEP":
        encr = sys.argv[2].upper()
        ssid = sys.argv[3]
        pswd = sys.argv[4]
        string = f"WIFI:T:{encr};S:{ssid};P:{pswd};;"
        img = qrcode.make(string)
        img.show()
    elif sys.argv[2].upper() == "NOPASS":
        encr = "nopass"
        ssid = sys.argv[3]
        string = f"WIFI:T:{encr};S:{ssid};P:;;"
        img = qrcode.make(string)
        img.show()
        

if __name__ == "__main__":
    try:
        if sys.argv[1].upper() == "WIFI":
            main_wifi()
        elif sys.argv[1].upper() == "URL":
            main_url()
        else:
            print("\nUtilizzo dello script:\n url2qr.py WIFI ENCRYPTION SSID PASSWORD (es. WPA/WEP/NOPASS MyWifi Password123)\n url2qr.py URL  http://sitoweb.com")
    except IndexError as errore:
        print("\nUtilizzo dello script:\n url2qr.py WIFI ENCRYPTION SSID PASSWORD (es. WPA/WEP/NOPASS MyWifi Password123)\n url2qr.py URL  http://sitoweb.com")