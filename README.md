# Password Security Checker

This command-line application (CLI) helps you assess the strength of your passwords by checking them against known compromised passwords in the Have I Been Pwned (HIBP) Pwned Passwords database. It leverages secure hashing and k-anonymity to protect your privacy.

## Features:

- **Checks password strength**: Identifies if your password has been exposed in data breaches using the Pwned Passwords API.
- **Secure hashing**: Hashes your password using a cryptographically secure algorithm (e.g., SHA-256) before sending a portion of the hash to the API, ensuring your password itself is never transmitted.
- **Privacy-focused**: Utilizes k-anonymity to protect user privacy. Only the first few characters of the hash are sent to the API, making it impossible to reconstruct the original password.

## Function Discriptions:

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


## Contributing

Feel free to fork this repository and contribute improvements. Pull requests are welcome!
