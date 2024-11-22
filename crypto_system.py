import random
from math import gcd

class CryptoSystem:
    def __init__(self, n):
        self.n = n
        self.public_key = None
        self.private_key = None

    def generate_increasing_sequence(self):
        """Generates sequence where each element is greater than sum of previous elements."""
        sequence = []
        current_sum = 0
        for _ in range(self.n):
            next_val = random.randint(current_sum + 1, 2 * current_sum + 10)
            sequence.append(next_val)
            current_sum += next_val
        return sequence

    def is_prime(self, n):
        """Checks if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_prime(self, min_value):
        """Generates prime number greater than min_value."""
        candidate = min_value + 1
        while not self.is_prime(candidate):
            candidate += 1
        return candidate

    def mod_inverse(self, a, m):
        """Calculates modular multiplicative inverse."""
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        _, x, _ = extended_gcd(a, m)
        return (x % m + m) % m

    def generate_keys(self):
        """Generates public and private key pair."""
        e = self.generate_increasing_sequence()
        q = self.generate_prime(2 * e[-1])
        while True:
            w = random.randint(2, q-1)
            if gcd(w, q) == 1:
                break
        h = [(w * e_i) % q for e_i in e]
        self.public_key = h
        self.private_key = (e, q, w)
        return h, (e, q, w)

    def encrypt(self, message):
        """Encrypts a binary message."""
        if len(message) != self.n:
            raise ValueError(f"Message must be {self.n} bits long")
        if not self.public_key:
            raise ValueError("Generate keys first")
        c = sum(h_i * m_i for h_i, m_i in zip(self.public_key, message))
        return c

    def decrypt(self, ciphertext):
        """Decrypts a ciphertext back to a binary message."""
        if not self.private_key:
            raise ValueError("Generate keys first")
        e, q, w = self.private_key
        w_inv = self.mod_inverse(w, q)
        c_prime = (ciphertext * w_inv) % q
        message = []
        for e_i in reversed(e):
            if c_prime >= e_i:
                message.insert(0, 1)
                c_prime -= e_i
            else:
                message.insert(0, 0)
        return message

def get_binary_message():
    """Prompts the user for a message and converts it to a binary list."""
    message = input("Enter a message (up to 8 characters): ").strip()
    if len(message) > 8:
        raise ValueError("Message length must not exceed 8 characters.")
    
    binary_message = []
    for char in message:
        binary_rep = format(ord(char), '08b')  # Convert each character to binary (8 bits)
        binary_message.extend([int(bit) for bit in binary_rep])

    return binary_message[:8] 

def binary_to_string(binary_message):
    """Converts a binary message back to a string."""
    chars = []
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        chars.append(chr(int(''.join(map(str, byte)), 2)))
    return ''.join(chars)

if __name__ == "__main__":
    
    crypto = CryptoSystem(8)

    
    public_key, private_key = crypto.generate_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key (e, q, w): {private_key}")

  
    binary_message = get_binary_message()
    print(f"Binary message to encrypt: {binary_message}")

   
    ciphertext = crypto.encrypt(binary_message)
    print(f"Encrypted message (ciphertext): {ciphertext}")

   
    decrypted_message = crypto.decrypt(ciphertext)
    print(f"Decrypted binary message: {decrypted_message}")

    
    decrypted_text = binary_to_string(decrypted_message)
    print(f"Decrypted message as text: {decrypted_text}")
