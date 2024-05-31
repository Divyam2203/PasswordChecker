

func request_api_data() : 
# returns api data from pwnedpassword.com 
# query_char is the hashed version of our password

func pwned_api_check():
# actual password is converted into hahsed password
# sha1 is the hashing algorithm used
# encoding the password in utf-8 format is necessary before passing it to hashlib algorithm
# hexdigest returns a string in hexadecimal of hash object  
# string in uppercase is required hence .upper()is used
