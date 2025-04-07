# Multilingual Password Generator

An offline powerful, high-entropy password generator supporting multiple languages and scripts for maximum security.

## Features

- Generates passwords of various lengths (16, 32, 64, 128, 256 characters)
- Three different character pools for varied security requirements:
  - **Standard ASCII** (94 characters)
  - **Extended Unicode** (5900+ characters)
  - **Multilingual** (15 different writing systems with guaranteed language diversity)
- Ultra-high entropy passwords (700+ bits for 64-character passwords)
- Ensures numeric diversity (64-character passwords always contain at least 4 digits)
- Beautiful formatting for longer passwords
- No external dependencies - runs with Python standard library

## Supported Languages/Scripts

The generator includes characters from 15 different writing systems:

- **Western**: Latin, Extended Latin (European), Greek, Cyrillic (Russian)
- **Middle Eastern/African**: Arabic, Hebrew, Ethiopic
- **South Asian**: Devanagari (Hindi), Bengali, Tamil
- **Southeast Asian**: Thai
- **East Asian**: Chinese, Japanese (Hiragana/Katakana), Korean (Hangul)

## Installation

1. Ensure you have Python 3.6 or later installed
2. Download the script: `password_generator_multilingual.py`
3. No additional packages required!

## Usage

Run the script from the command line:

```bash
python password_generator_multilingual.py
```

The script will generate and display passwords of various lengths (16, 32, 64, 128, 256 characters) using all three character pools.

## Understanding Entropy

Password strength is measured in bits of entropy:

- **Standard ASCII pool (64 chars)**: ~420 bits
- **Extended Unicode pool (64 chars)**: ~800 bits (exceeds the 700+ bits requirement)
- **Multilingual pool (64 chars)**: ~725 bits

For comparison:
- A typical 8-character password has ~40 bits of entropy
- Modern encryption (AES-256) uses 256 bits
- These passwords have entropy levels suitable for the most security-critical applications

## Example Output

```
Standard pool size: 94 characters
Extended pool size: 5923 characters

Languages available: 15
  Arabic: 247 characters
  Bengali: 96 characters
  Chinese/Japanese/Korean Ideographs: 256 characters
  Cyrillic (Russian, Bulgarian, etc.): 255 characters
  Devanagari (Hindi, Sanskrit): 127 characters
  Ethiopic: 358 characters
  Greek: 134 characters
  Hebrew: 88 characters
  Japanese Hiragana: 92 characters
  Japanese Katakana: 95 characters
  Korean Hangul: 256 characters
  Latin (English, Spanish, French, etc.): 51 characters
  Extended Latin (European languages): 399 characters
  Tamil: 72 characters
  Thai: 87 characters

Entropy for a 64-character password using extended pool: 802.06 bits

== 64-character passwords ==

Standard ASCII (419.49 bits):
CM(a!P6fe_nhzeUxmv@l:Ri1?FxdWFvMG=6l6_`*`""_*<46PjVmIS=rux[x\r6[

Extended Unicode (802.06 bits):
·ኟǫʎۭɒ걀Ṉኀ୫걥่Ừ7ỦȺŢब⇼㓥곢♳י♉今➹ຯℓ⋳えɣ၉ޜ义ङ乘㑝ູȚ⇥Ę♔ಽƎࣱႃ㑤ޯޠẀấ丽ឥ6)丧乾ሙȕばഊ△؉く

Multilingual (726.50 bits):
ম௰곛׃ƧヺψঢŻ临উௐউ临ூ곮丫ūҤヅעٷ90Šy业8オ갫乏aЧRӸҤঊ곃걢겝书京곝Т仴ْf乳னசڅץӀ4乭Ϻ亲ͶўnزP乄×
```

## Security Considerations

- Use the multilingual or extended Unicode pools for maximum security
- The entropy levels provided are theoretical maximums
- For critical applications, passwords of 64 characters or longer are recommended
- Store these passwords in a secure password manager

## License

This project is released under the MIT License - see the LICENSE file for details.

Bitcoin
bitcoin:1FH3yda1povxot1nY9jZYoS4ZSjVQUx9t7

Bitcoin:3NnbEapmFAPDEJ9W8WXm4g8x3mWuub6qZ5

Ethereum
0x7316FB87Ee1DEA2F41A0Da41E3948dda65948b16

0x4d04CEe3FfFe959F6DDE2A0b678fC1146fb052f3

SOL
5CbPgKffMCDRsQsAXxm5vUJpy9HuLxg5HByKbfFszqEH

Zelle
https://enroll.zellepay.com/qr-codes?data=ewogICJuYW1lIiA6ICJOQVRIQU4gQVNTQUYiLAogICJhY3Rpb24iIDogInBheW1lbnQiLAogICJ0b2tlbiIgOiAiKDkyNSkgNDUwLTk1NTAiCn0=

PayPal
https://www.paypal.com/qrcodes/p2pqrc/WFEUVNJPT35CY

Cashapp 
$beggarbillionaire


## Author

Created with security and internationalization in mind. 
