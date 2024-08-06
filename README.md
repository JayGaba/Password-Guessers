# Password Guessing Tools

## Description

This repository contains tools for performing password guessing attacks on various services. The tools included are:

1. **SSH Password Guesser**: Attempts to guess the SSH login password using a list of possible passwords.
2. **FTP Password Guesser**: Attempts to guess the FTP login password using a list of possible passwords.
3. **HTTP Form Password Guesser**: Attempts to guess passwords for HTML login forms using a list of possible passwords.

## Features

- **Multi-threaded**: Uses multiple threads to speed up the guessing process.
- **Configurable**: Allows users to specify various parameters such as the number of threads, success messages, and more.
- **Versatile**: Supports different protocols and methods, including SSH, FTP, and HTTP forms.
- **Efficient**: Optimized to handle large lists of passwords efficiently.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/JayGaba/Password-Guessers.git
   cd Password-Guessers
   ```

3. **Install dependencies:**
   Ensure you have Python installed. Install the required libraries using requirements.txt:
   ``` 
   pip install -r requirements.txt
   ```
## Usage

### SSH Password Guesser

1. **Prepare a password list**: Place your password list in the wordlists directory and name it password_list.
2. **Run the SSH password guesser**:
   
   ```
   python guesser.py <hostname> <username> ssh
   ```

### FTP Password Guesser

1. **Prepare a password list**: Place your password list in the wordlists directory and name it password_list.
2. **Run the FTP password guesser**:
   
   ```
   python guesser.py <hostname> <username> ftp
   ```

### HTTP Form Password Guesser

1. **Prepare a password list**: Place your password list in the wordlists directory and name it password_list.
2. **Run the HTTP form password guesser**:
   
   ```
   python http_guesser.py -u <url> -d <data> -m <method> -f <field> -s <success_message> -t <threads>
   ```
## Example

### SSH Password Guesser
```
python guesser.py 192.168.1.10 root ssh
```
### FTP Password Guesser
```
python guesser.py 192.168.1.10 root ftp
```
### HTTP Form Password Guesser
```
python http_guesser.py -u http://example.com/login -d "username=admin&password=PASSWORD" -m POST -f password -s "welcome" -t 10
```
## Requirements

- Python 3.x
- paramiko
- ftplib
- requests

## Future Enhancements

- Implement better error handling and logging.
- Improve the performance of the guessing algorithms.
- Add more configuration options and improve the user interface.


