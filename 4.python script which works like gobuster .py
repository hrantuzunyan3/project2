import requests
import sys

def main(target, wordlist_path):
    with open(wordlist_path, "r") as wordlist_file:
        wordlist = wordlist_file.read().splitlines()
        
    for word in wordlist:
        new_url = target + "/" + word.strip()
        response = requests.get(new_url)
        
        if response.status_code == 200:
            print(f"URL: {new_url}, status code {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <target_url> <wordlist_path>")
        sys.exit(1)
    
    target_url = sys.argv[1]
    wordlist_path = sys.argv[2]
    
    main(target_url, wordlist_path)
