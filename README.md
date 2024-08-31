# Subchecker
SubChecker is a Python script designed to check the availability of subdomains using both HTTP and HTTPS protocols. 
It saves the results of the checks to separate files for online and offline domains.

Features : 
- Check Subdomains: Test the availability of subdomains using HTTP and/or HTTPS.
- Output Files: Save results in separate files for online and offline domains.
- Customizable Checks: Specify which protocols to check (HTTP, HTTPS) and which results to save.

Requirements : 
- Python 3.6 or higher
- "requests" library

# Installation
Clone the Repository:

    git clone https://github.com/kcoainnapo/subchecker.git
  
Ensure you have Python 3 and pip installed, then install the required libraries:

    pip install requests

# Options
    -f, --file (Required): Path to the file containing the subdomains to check.
    --only-up: Save only online domains to a file specified by the user.
    --only-down: Save only offline domains to a file specified by the user.
    --only-http: Check only the HTTP protocol.
    --only-https: Check only the HTTPS protocol.

# Example

1.Check both HTTP and HTTPS, save results to both files:

    python3 subchecker.py -f subdomains.txt

This will prompt you to enter filenames for both online and offline domains.


2.Check only HTTP, save only online domains to up.txt:

    python3 subchecker.py -f subdomains.txt --only-http --only-up

    
3.Check both protocols but save only offline domains to down.txt:

    python3 subchecker.py -f subdomains.txt --only-http --only-down


4.Check both protocols and save only online domains to up.txt:

    python3 subchecker.py -f subdomains.txt --only-http --only-up

