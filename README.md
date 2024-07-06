# NTLM-Stealer-PDF

This repository contains a script to generate a PDF file with an embedded link that connects to an SMB share. This is typically used in penetration testing to capture NTLM hashes when the PDF is opened.

## Installation of required library
```
pip install reportlab
```

## Usage
```
python ntlmpdf.py
```

## Features
Generates a PDF file with a clickable link to an SMB share.
The link text is prominently displayed in red for better visibility.
Suitable for use in penetration testing scenarios with proper authorization.

