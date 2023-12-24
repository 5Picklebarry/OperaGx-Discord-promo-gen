# made by 5picklebarry.

import requests
import time
import random
import string
from colorama import Fore, Style
import ctypes

import os

os.system("")

Fore.RESET


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def set_cmd_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


def print_header():
    header = """
  (  ____ \(  ____ )\__   __/(  ____ \| \    /\( \      (  ____ \(  ___ \ (  ___  )(  ____ )(  ____ )|\     /|
  | (    \/| (    )|   ) (   | (    \/|  \  / /| (      | (    \/| (   ) )| (   ) || (    )|| (    )|( \   / )
  | (____  | (____)|   | |   | |      |  (_/ / | |      | (__    | (__/ / | (___) || (____)|| (____)| \ (_) / 
  (_____ \ |  _____)   | |   | |      |   _ (  | |      |  __)   |  __ (  |  ___  ||     __)|     __)  \   /  
        ) )| (         | |   | |      |  ( \ \ | |      | (      | (  \ \ | (   ) || (\ (   | (\ (      ) (   
  /\____) )| )      ___) (___| (____/\|  /  \ \| (____/\| (____/\| )___) )| )   ( || ) \ \__| ) \ \__   | |   
  \______/ |/       \_______/(_______/|_/    \/(_______/(_______/|/ \___/ |/     \||/   \__/|/   \__/   \_/    
"""
    header_lines = header.split("\n")
    max_length = max(len(line) for line in header_lines)
    centered_header = [line.center(max_length) for line in header_lines]

    print(
        f"{Fore.RED}\n".join(centered_header)
        + f"\n\nMade by 5picklebarry{Style.RESET_ALL}\n"
    )


if __name__ == "__main__":
    set_cmd_title("5picklebarrys opera gen")

    print_header()

    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    headers = {
        "authority": "api.discord.gx.games",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.opera.com",
        "referer": "https://www.opera.com/",
        "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
    }

    session = requests.Session()
    token_count = 0

    try:
        while True:
            partner_user_id = generate_random_string(64)
            data = {"partnerUserId": partner_user_id}

            response = session.post(url, headers=headers, json=data)

            if response.status_code == 200:
                token = response.json().get("token")
                if token:
                    token_count += 1
                    token_url = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
                    with open("codes.txt", "a") as file:
                        file.write(token_url + "\n")
                    clear_console()
                    print_header()
                    print(
                        f"{Fore.GREEN}A token (x{token_count}) was saved to the codes.txt file.{Style.RESET_ALL}"
                    )
                else:
                    print("Token not found in the response.")
            else:
                clear_console()
                print_header()
                print(
                    f"{Fore.RED}Request failed with status code {response.status_code}.{Style.RESET_ALL}"
                )
                print(f"Error message: {response.text}")

    except KeyboardInterrupt:
        print("Process interrupted.")
    except SystemExit:
        print("System exited.")
    except Exception as e:
        clear_console()
        print_header()
        print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")
    finally:
        session.close()