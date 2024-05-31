

### func request_api_data() : 
- returns api data from pwnedpassword.com 
- query_char is the hashed version of our password

### func get_password_leaks_count():
- splits the api response.text into lines using splitlines()
- stores them as tuples (\<hash_code\>,\<count\>) in a list
- matches the password and find its count

### func pwned_api_check():
- actual password is converted into hahsed password
- sha1 is the hashing algorithm used
- encoding the password in utf-8 format is necessary before passing it to hashlib algorithm
- hexdigest returns a string in hexadecimal of hash object  
- string in uppercase is required hence .upper()is used
- response and tail are passed on to get_password_leaks_count()
