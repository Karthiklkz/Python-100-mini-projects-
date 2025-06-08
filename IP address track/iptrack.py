import requests

def get_public_ip():
    return requests.get('https://api64.ipify.org').text

def track_ip(ip):
    url = f"http://ip-api.com/json/{ip}"  # or your chosen IP geolocation API
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'success':
        print(f"IP: {ip}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
    else:
        print("Could not fetch data. Check the IP address.")

public_ip = get_public_ip()
print("Tracking your public IP...")
track_ip(public_ip)
