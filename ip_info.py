import requests
import json
from termcolor import colored

class IPInfo:
    def __init__(self, output_handle):
        self.output_handle = output_handle

    def get_ip_info(self, ip):
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = json.loads(response.content)

        if data["status"] == "success":
            result = f"{ip},{data['country']},{data['regionName']},{data['city']}"
            return result
        else:
            print(colored(f"Failed to retrieve information for IP: {ip}", "red"))
            return None

    def process_ip_list(self, input_file):
        with open(input_file, "r") as ip_file:
            for line in ip_file:
                ip = line.strip()
                result = self.get_ip_info(ip)
                if result:
                    print(result)
                    if self.output_handle:
                        self.output_handle.write(result + "\n")
                        self.output_handle.flush()
