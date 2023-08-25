import zipfile
import time
import os
import random
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", action="store_true", required=False)

args = parser.parse_args()

banner = f"""
______                         _                    
| ___ \                       | |                   
| |_/ / ___ _ __ ___  ___ _ __| | _____ _ __        
| ___ \/ _ \ '__/ __|/ _ \ '__| |/ / _ \ '__|       
| |_/ /  __/ |  \__ \  __/ |  |   <  __/ |          
\____/ \___|_|  |___/\___|_|  |_|\_\___|_|                                                      
 _                                                  
| |                                                 
| |     ___  __ _  __ _  ___ _   _                  
| |    / _ \/ _` |/ _` |/ __| | | |                 
| |___|  __/ (_| | (_| | (__| |_| |                 
\_____/\___|\__, |\__,_|\___|\__, |                 
             __/ |            __/ |                 
            |___/            |___/                  
 _______         _____                _             
|___  (_)       /  __ \              | |            
   / / _ _ __   | /  \/_ __ __ _  ___| | _____ _ __ 
  / / | | '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
./ /__| | |_) | | \__/\ | | (_| | (__|   <  __/ |   
\_____/_| .__/   \____/_|  \__,_|\___|_|\_\___|_|   
        | |                                         
        |_|           

## Coded By https://github.com/Dawnn3619 ##
"""

print(banner)
print("### You Can Use -v/--verbose Parameter If You Want To Enable Verbose Mode ###")

now = time.localtime()
hour = now.tm_hour
minute = now.tm_min
second = now.tm_sec


def ZipBruteForce():
    while True:
        file_question = input("[*] Which File Do You Want To Crack?: ")
        print("\n[*] Checking Zip File...")
        try:
            with zipfile.ZipFile(file_question, 'r') as zip_file:
                file_list = zip_file.namelist()
                if file_list:
                    print("[*] The Zip File Found!\n")
                    break
        except zipfile.BadZipFile:
            print(f"[X] File is Not a Zip File!\n")
        except FileNotFoundError:
            print(f"[X] Zip File ({file_question}) Not Found!\n")
    while True:
        wordlist_question = input("[*] Wordlist Path: ")
        if os.path.exists(wordlist_question):
            print("[+] Wordlist File Found!\n")
            break
        else:
            print(f"[X] Wordlist File ({wordlist_question}) Not Found!\n")
    count = 1
    try:
        
        begining_time = time.time()
        print(f"[*] {hour:02d}:{minute:02d}:{second:02d} / Brute Force Started")
        with open(wordlist_question, 'rb') as text:
            password_found = False
            for entry in text.readlines():
                password = entry.strip()
                try:
                    with zipfile.ZipFile(file_question, 'r') as zf:
                        extract_dir = "extracted_data"
                        zf.extractall(pwd=password, path=extract_dir)
                        data = zf.namelist()[0]

                        data_size = zf.getinfo(data).file_size

                        print(f"\n[+] Password Found - {password.decode('utf8')}")
                        password_found = True
                        print(f"\n[*] Files In Zip File: {data}")
                        print(f"[*] Files Extracted To: {extract_dir}")
                        end_time = time.time()
                        process_time = end_time - begining_time
                except:
                    if args.verbose:
                        number = count
                        print(f"[{number}] Password Failed - {password.decode('utf8')}")
                        count += 1
                        pass
                    else:
                        pass
        if not password_found:
            print("\n[-] Password Not Found! Try Again With Another Wordlist")
            print(f"\n[*] Failed Empty Files Extracted To: {extract_dir}")
    except FileNotFoundError:
        print(f"[X] Wordlist File ({wordlist_question}) Not Found!")
    except:
        print("[X] There Was An Error!")
if __name__ == "__main__":
    ZipBruteForce()