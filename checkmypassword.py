import requests
import hashlib
import sys

# returns api data from pwnedpassword.com 
# query_char is the hashed version of our password
def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/'+ query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes,hashes_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hashes_to_check:
      return count
  return 0


# actual password is converted into hahsed password
# sha1 is the hashing algorithm used
# encoding the password in utf-8 format is necessary before passing it to hashlib algorithm
# hexdigest returns a string in hexadecimal of hash object  
# string in uppercase is required hence .upper()is used
def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f"{count} matches found!")
    else:
      print("no matches")
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))