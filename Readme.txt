Alternative Public-Key Encryption System
Overview
This project implements a simple public-key encryption system using a novel method of key generation and encryption. It allows users to generate key pairs, encrypt a message, and decrypt a ciphertext. The system is based on integer sequences and modular arithmetic, with Python handling all the encryption and decryption processes.

Prerequisites
Python 3.6+: Ensure you have Python installed on your system. You can download it from here.


How to Run the System
Download The file and save it in a folder of your choice:


Navigate to the Project Directory: Open your terminal (Command Prompt or PowerShell on Windows, or Terminal on macOS/Linux), and navigate to the directory where the crypto_system.py file is located.

cd path/to/your/project
Run the Program: In the terminal, execute the Python script by running:

python crypto_system.py

This will launch the system and prompt you to input a message.

Input a Message:

After running the script, you will be asked to input a message (up to 8 characters) to be encrypted.
Example:

Enter a message (up to 8 characters): hello
Encryption and Decryption:

The system will generate a public-private key pair, encrypt the provided message, and then decrypt it back to the original message.
You will see output showing the binary message, the encrypted ciphertext, and the decrypted message.
Example output:



Public Key: [2341, 4982, 9871, 19742, 39484, 78968, 157936, 315872]
Private Key (e, q, w): ([127, 255, 511, 1023, 2047, 4095, 8191, 16383], 32771, 17)

Enter a message (up to 8 characters): hello
Binary message to encrypt: [0, 1, 1, 0, 1, 0, 1, 1]
Encrypted message (ciphertext): 457892
Decrypted binary message: [0, 1, 1, 0, 1, 0, 1, 1]
Decrypted message as text: k


How to Test the System
To test the system:

Run the program using python crypto_system.py.
Enter any message (up to 8 characters) when prompted.
The program will encrypt and decrypt your message, and display the results in both binary and textual formats.
You can repeat this process with different inputs to test various messages and observe how the encryption system behaves.