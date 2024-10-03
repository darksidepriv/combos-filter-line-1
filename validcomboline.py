import re
import os

# Regex untuk validasi email
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def is_valid_email_password(line):
    """Memvalidasi apakah sebuah baris memiliki format email:password."""
    if ':' not in line:
        return False
    
    email, password = line.split(':', 1)  # Pisahkan bagian email dan password
    email = email.strip()
    password = password.strip()
    
    # Cek apakah email valid dan password tidak kosong
    if re.match(EMAIL_REGEX, email) and len(password) > 0:
        return True
    return False

def validate_file(input_file, valid_file, error_file, debug=False):
    """Memfilter file untuk baris yang valid dan tidak valid."""
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(valid_file, 'w', encoding='utf-8') as valid_out, \
         open(error_file, 'w', encoding='utf-8') as error_out:
        
        for line in infile:
            line = line.strip()
            if is_valid_email_password(line):
                valid_out.write(line + '\n')
                if debug:
                    print(f"VALID: {line}")
            else:
                error_out.write(line + '\n')
                if debug:
                    print(f"INVALID: {line}")

    print(f"\nProses selesai! Baris valid disimpan di '{valid_file}', baris yang tidak valid di '{error_file}'.")

def main():
    print("=== Aplikasi Validasi Email:Password ===")


    input_file = input("Masukkan nama file yang akan divalidasi (contoh: data.txt): ")
    

    if not os.path.exists(input_file):
        print(f"File '{input_file}' tidak ditemukan. Pastikan nama file benar.")
        return
    

    valid_file = 'emailpassword_valid.txt'
    error_file = 'errorline.txt'


    debug_mode = input("Aktifkan mode debug? (y/n): ").lower() == 'y'


    validate_file(input_file, valid_file, error_file, debug=debug_mode)

if __name__ == "__main__":
    main()
