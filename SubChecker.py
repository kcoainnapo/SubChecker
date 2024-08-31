import argparse
import requests
import os

# Define colors for output
GREEN = '\033[0;32m'
RED = '\033[0;31m'
RESET = '\033[0m'  # No Color

# Set up argument parser
parser = argparse.ArgumentParser(description="Check subdomains for HTTP/HTTPS availability.")
parser.add_argument("-f", "--file", required=True, help="File containing subdomains.")
parser.add_argument("--only-up", action="store_true", help="Save only 'Up' domains to a file.")
parser.add_argument("--only-down", action="store_true", help="Save only 'Down' domains to a file.")
parser.add_argument("--only-http", action="store_true", help="Check only HTTP.")
parser.add_argument("--only-https", action="store_true", help="Check only HTTPS.")
args = parser.parse_args()

# Default to both protocols if neither --only-http nor --only-https is specified
check_http = not args.only_https
check_https = not args.only_http

# File prompts
if not args.only_down:
    up_file = input("Enter a name for the file containing ONLINE domains: ")
if not args.only_up:
    down_file = input("Enter a name for the file containing OFFLINE domains: ")

# Path to the file containing subdomains
subdomains_file = args.file

# Check if the subdomains file exists
if not os.path.isfile(subdomains_file):
    print(f"Subdomains file not found: {subdomains_file}")
    exit(1)

# Read subdomains from the file into a list
subdomains = []
with open(subdomains_file, 'r') as file:
    for line in file:
        subdomain = line.strip()
        subdomains.append(subdomain)

# Function to check subdomain
def check_subdomain(subdomain, protocol):
    url = f"{protocol}://{subdomain}"
    try:
        response = requests.get(url, timeout=4)
        print(f"{url}... {GREEN}Up - {response.status_code}{RESET}")
        if not args.only_down:
            with open(up_file, 'a') as up:
                up.write(f"{url}\n")  # Write full URL with protocol
    except requests.RequestException:
        print(f"{url}... {RED}Down - Request Error{RESET}")
        if not args.only_up:
            with open(down_file, 'a') as down:
                down.write(f"{url}\n")  # Write full URL with protocol

# Loop through each subdomain and check it
for subdomain in subdomains:
    if check_http:
        check_subdomain(subdomain, "http")
    if check_https:
        check_subdomain(subdomain, "https")
