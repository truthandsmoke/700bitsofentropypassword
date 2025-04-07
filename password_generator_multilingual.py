#!/usr/bin/env python3
import random
import string
import math
import sys
import os

def create_standard_pool():
    """Creates a standard pool of 94 ASCII characters"""
    return string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def create_extended_pool():
    """Creates an expanded character pool using Unicode from multiple languages for maximum entropy"""
    standard_pool = create_standard_pool()
    extended_chars = []
    
    # European scripts and extensions
    extended_chars.extend([chr(i) for i in range(0x00A1, 0x00FF)])  # Latin-1 Supplement
    extended_chars.extend([chr(i) for i in range(0x0100, 0x017F)])  # Latin Extended-A
    extended_chars.extend([chr(i) for i in range(0x0180, 0x024F)])  # Latin Extended-B
    extended_chars.extend([chr(i) for i in range(0x1E00, 0x1EFF)])  # Latin Extended Additional
    extended_chars.extend([chr(i) for i in range(0x0250, 0x02AF)])  # IPA Extensions
    extended_chars.extend([chr(i) for i in range(0x0370, 0x03FF)])  # Greek and Coptic
    extended_chars.extend([chr(i) for i in range(0x0400, 0x04FF)])  # Cyrillic
    extended_chars.extend([chr(i) for i in range(0x0500, 0x052F)])  # Cyrillic Supplement
    
    # Middle Eastern and African scripts
    extended_chars.extend([chr(i) for i in range(0x0590, 0x05FF)])  # Hebrew
    extended_chars.extend([chr(i) for i in range(0x0600, 0x06FF)])  # Arabic
    extended_chars.extend([chr(i) for i in range(0x0750, 0x077F)])  # Arabic Supplement
    extended_chars.extend([chr(i) for i in range(0x08A0, 0x08FF)])  # Arabic Extended-A
    extended_chars.extend([chr(i) for i in range(0x0700, 0x074F)])  # Syriac
    extended_chars.extend([chr(i) for i in range(0x0780, 0x07BF)])  # Thaana (Maldivian)
    extended_chars.extend([chr(i) for i in range(0x07C0, 0x07FF)])  # NKo
    extended_chars.extend([chr(i) for i in range(0x1200, 0x137F)])  # Ethiopic (sample)
    
    # South and Southeast Asian scripts
    extended_chars.extend([chr(i) for i in range(0x0900, 0x097F)])  # Devanagari (Hindi, Sanskrit)
    extended_chars.extend([chr(i) for i in range(0x0980, 0x09FF)])  # Bengali
    extended_chars.extend([chr(i) for i in range(0x0A00, 0x0A7F)])  # Gurmukhi (Punjabi)
    extended_chars.extend([chr(i) for i in range(0x0A80, 0x0AFF)])  # Gujarati
    extended_chars.extend([chr(i) for i in range(0x0B00, 0x0B7F)])  # Oriya
    extended_chars.extend([chr(i) for i in range(0x0B80, 0x0BFF)])  # Tamil
    extended_chars.extend([chr(i) for i in range(0x0C00, 0x0C7F)])  # Telugu
    extended_chars.extend([chr(i) for i in range(0x0C80, 0x0CFF)])  # Kannada
    extended_chars.extend([chr(i) for i in range(0x0D00, 0x0D7F)])  # Malayalam
    extended_chars.extend([chr(i) for i in range(0x0D80, 0x0DFF)])  # Sinhala
    extended_chars.extend([chr(i) for i in range(0x0E00, 0x0E7F)])  # Thai
    extended_chars.extend([chr(i) for i in range(0x0E80, 0x0EFF)])  # Lao
    extended_chars.extend([chr(i) for i in range(0x1000, 0x109F)])  # Myanmar
    extended_chars.extend([chr(i) for i in range(0x1780, 0x17FF)])  # Khmer
    
    # East Asian scripts (samples to keep pool manageable)
    extended_chars.extend([chr(i) for i in range(0x3040, 0x309F)])  # Hiragana
    extended_chars.extend([chr(i) for i in range(0x30A0, 0x30FF)])  # Katakana
    extended_chars.extend([chr(i) for i in range(0x3130, 0x318F)])  # Hangul Compatibility Jamo
    extended_chars.extend([chr(i) for i in range(0x3400, 0x3500)])  # CJK Unified Ideographs Extension A (sample)
    extended_chars.extend([chr(i) for i in range(0x4E00, 0x4F00)])  # CJK Unified Ideographs (sample)
    extended_chars.extend([chr(i) for i in range(0xAC00, 0xAD00)])  # Hangul Syllables (sample)
    
    # Symbols and other scripts
    extended_chars.extend([chr(i) for i in range(0x2000, 0x206F)])  # General Punctuation
    extended_chars.extend([chr(i) for i in range(0x20A0, 0x20CF)])  # Currency Symbols
    extended_chars.extend([chr(i) for i in range(0x2100, 0x214F)])  # Letterlike Symbols
    extended_chars.extend([chr(i) for i in range(0x2150, 0x218F)])  # Number Forms
    extended_chars.extend([chr(i) for i in range(0x2190, 0x21FF)])  # Arrows
    extended_chars.extend([chr(i) for i in range(0x2200, 0x22FF)])  # Mathematical Operators
    extended_chars.extend([chr(i) for i in range(0x25A0, 0x25FF)])  # Geometric Shapes
    extended_chars.extend([chr(i) for i in range(0x2600, 0x26FF)])  # Miscellaneous Symbols
    extended_chars.extend([chr(i) for i in range(0x2700, 0x27BF)])  # Dingbats
    
    # Filter out control characters, whitespace, and non-printable characters
    filtered_chars = []
    for c in extended_chars:
        try:
            if c.isprintable() and not c.isspace():
                filtered_chars.append(c)
        except:
            # Skip characters that cause issues
            pass
    
    # Combine with standard pool
    return standard_pool + ''.join(filtered_chars)

def calculate_entropy(password_length, pool_size):
    """Calculates entropy in bits for a password"""
    return password_length * math.log2(pool_size)

def generate_password(length, character_pool):
    """Generates a random password of the specified length"""
    return ''.join(random.SystemRandom().choice(character_pool) for _ in range(length))

def generate_password_with_digits(length, character_pool, min_digits=3):
    """Generates a password with at least the specified number of digits"""
    # First create a random password
    password = generate_password(length, character_pool)
    
    # Count the number of digits
    digit_count = sum(1 for c in password if c.isdigit())
    
    # If we already have enough digits, return the password
    if digit_count >= min_digits:
        return password
    
    # Otherwise, replace random characters with digits until we have enough
    digits = string.digits
    non_digit_positions = [i for i in range(length) if not password[i].isdigit()]
    
    # Convert to a list for modification
    password_list = list(password)
    
    # Add necessary digits
    for _ in range(min_digits - digit_count):
        if non_digit_positions:
            position = random.choice(non_digit_positions)
            password_list[position] = random.choice(digits)
            non_digit_positions.remove(position)
    
    return ''.join(password_list)

def generate_mixed_language_password(length, language_samples, min_languages=3):
    """Generates a password with characters from multiple language samples"""
    # Ensure we have enough languages
    if len(language_samples) < min_languages:
        raise ValueError(f"Need at least {min_languages} language samples")
    
    # Select a random subset of languages to include (at least min_languages)
    num_languages = random.randint(min_languages, len(language_samples))
    lang_codes = list(language_samples.keys())
    selected_languages = random.sample(lang_codes, num_languages)
    
    # Create a pool from the selected languages
    pool = []
    for lang in selected_languages:
        pool.extend(language_samples[lang])
    
    # Add digits and basic punctuation to ensure they're available
    pool.extend(string.digits)
    pool.extend("!@#$%^&*()-_=+[]{}|;:,.<>?")
    
    # Generate the password
    password = generate_password(length, pool)
    
    # Ensure we have at least one character from each selected language
    password_list = list(password)
    
    # Check if we need to insert language-specific characters
    for lang in selected_languages:
        # Check if this language is already represented
        if not any(c in language_samples[lang] for c in password):
            # Replace a random character with one from this language
            position = random.randint(0, length-1)
            lang_char = random.choice(language_samples[lang])
            password_list[position] = lang_char
    
    # For 64-char passwords, ensure at least 4 digits
    if length == 64:
        digit_count = sum(1 for c in password_list if c.isdigit())
        if digit_count < 4:
            # Add more digits
            digit_positions = random.sample(range(length), 4 - digit_count)
            for pos in digit_positions:
                password_list[pos] = random.choice(string.digits)
    
    return ''.join(password_list)

def get_language_samples():
    """Creates samples of characters from different languages/scripts"""
    language_samples = {
        # Western languages
        "Latin": [chr(i) for i in range(0x0041, 0x007A) if chr(i).isalpha()],
        "Latin_Extended": [chr(i) for i in range(0x00C0, 0x024F) if chr(i).isprintable()],
        "Greek": [chr(i) for i in range(0x0370, 0x03FF) if chr(i).isprintable()],
        "Cyrillic": [chr(i) for i in range(0x0400, 0x04FF) if chr(i).isprintable()],
        
        # Middle Eastern and African
        "Hebrew": [chr(i) for i in range(0x0590, 0x05FF) if chr(i).isprintable()],
        "Arabic": [chr(i) for i in range(0x0600, 0x06FF) if chr(i).isprintable()],
        "Ethiopic": [chr(i) for i in range(0x1200, 0x137F) if chr(i).isprintable()],
        
        # South and Southeast Asian
        "Devanagari": [chr(i) for i in range(0x0900, 0x097F) if chr(i).isprintable()],
        "Bengali": [chr(i) for i in range(0x0980, 0x09FF) if chr(i).isprintable()],
        "Tamil": [chr(i) for i in range(0x0B80, 0x0BFF) if chr(i).isprintable()],
        "Thai": [chr(i) for i in range(0x0E00, 0x0E7F) if chr(i).isprintable()],
        
        # East Asian
        "Hiragana": [chr(i) for i in range(0x3040, 0x309F) if chr(i).isprintable()],
        "Katakana": [chr(i) for i in range(0x30A0, 0x30FF) if chr(i).isprintable()],
        "Hangul": [chr(i) for i in range(0xAC00, 0xAD00) if chr(i).isprintable()],
        "CJK": [chr(i) for i in range(0x4E00, 0x4F00) if chr(i).isprintable()],
    }
    
    # Filter out any empty lists
    return {k: v for k, v in language_samples.items() if v}

def get_language_name(code):
    """Returns a full language name from a language code"""
    language_names = {
        "Latin": "Latin (English, Spanish, French, etc.)",
        "Latin_Extended": "Extended Latin (European languages)",
        "Greek": "Greek",
        "Cyrillic": "Cyrillic (Russian, Bulgarian, etc.)",
        "Hebrew": "Hebrew",
        "Arabic": "Arabic",
        "Ethiopic": "Ethiopic",
        "Devanagari": "Devanagari (Hindi, Sanskrit)",
        "Bengali": "Bengali",
        "Tamil": "Tamil",
        "Thai": "Thai",
        "Hiragana": "Japanese Hiragana",
        "Katakana": "Japanese Katakana",
        "Hangul": "Korean Hangul",
        "CJK": "Chinese/Japanese/Korean Ideographs",
    }
    return language_names.get(code, code)

def format_password(password, length):
    """Formats a password for display based on its length"""
    if length <= 64:
        return password
    elif length <= 128:
        # Split into 2 lines of 64 characters
        return password[:64] + "\n" + password[64:]
    else:
        # Split into chunks of 64 characters
        chunks = [password[i:i+64] for i in range(0, len(password), 64)]
        return "\n".join(chunks)

def main():
    # Create character pools
    standard_pool = create_standard_pool()
    extended_pool = create_extended_pool()
    
    # Get language samples
    language_samples = get_language_samples()
    
    # Display information about the character pools
    print(f"Standard pool size: {len(standard_pool)} characters")
    print(f"Extended pool size: {len(extended_pool)} characters")
    print(f"\nLanguages available: {len(language_samples)}")
    for lang_code in sorted(language_samples.keys()):
        print(f"  {get_language_name(lang_code)}: {len(language_samples[lang_code])} characters")
    
    # Calculate entropy for a 64-character password from the extended pool
    entropy_64 = calculate_entropy(64, len(extended_pool))
    print(f"\nEntropy for a 64-character password using extended pool: {entropy_64:.2f} bits")
    
    # Password lengths to generate
    lengths = [16, 32, 64, 128, 256]
    
    # Generate passwords for each length
    print("\nGenerating passwords of different lengths:")
    
    for length in lengths:
        print(f"\n== {length}-character passwords ==")
        
        # Standard ASCII password
        standard_password = generate_password(length, standard_pool)
        standard_entropy = calculate_entropy(length, len(standard_pool))
        print(f"\nStandard ASCII ({standard_entropy:.2f} bits):")
        print(format_password(standard_password, length))
        
        # Extended Unicode password (with digits for 64-char)
        if length == 64:
            extended_password = generate_password_with_digits(length, extended_pool, min_digits=4)
        else:
            extended_password = generate_password(length, extended_pool)
        extended_entropy = calculate_entropy(length, len(extended_pool))
        print(f"\nExtended Unicode ({extended_entropy:.2f} bits):")
        print(format_password(extended_password, length))
        
        # Multilingual password with mixed scripts
        mixed_password = generate_mixed_language_password(length, language_samples, min_languages=5)
        # Estimate entropy (conservatively)
        mixed_pool_size = sum(len(chars) for chars in language_samples.values())
        mixed_entropy = calculate_entropy(length, mixed_pool_size)
        print(f"\nMultilingual ({mixed_entropy:.2f} bits):")
        print(format_password(mixed_password, length))

if __name__ == "__main__":
    main() 