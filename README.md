# FUTURE_CS_03
# 🔐 Secure File Sharing System (AES Encryption)
## 📌 Project Overview

This project demonstrates a Secure File Sharing System built using Python Flask.
The system allows users to upload files, which are then encrypted using AES encryption (Fernet) and stored securely.
Files can later be decrypted and downloaded safely through the web interface.

This project simulates real-world secure file transfer requirements used in corporate, healthcare, legal and SOC environments.

___

## 🛠️ Tools & Technologies Used

Python Flask – Backend Web Framework

PyCryptodome (AES via Fernet) – Encryption & Decryption

HTML / CSS – Frontend UI

Git & GitHub – Version Control

GitHub Codespaces – Cloud Development Environment

___

## 🔐 Features Implemented

Secure File Upload

Files are uploaded through a Flask web form.

AES Encryption (Fernet)

Each uploaded file is encrypted before being saved.

Encryption is performed using a secure key stored in secret.key.

Encrypted File Storage

All uploaded files are stored as .enc inside the /uploads directory.

Secure File Download

When the user downloads, the file gets decrypted automatically.

Simple UI for File Handling

Minimal, clean HTML-based upload & download interface.

Key Management

A Fernet encryption key is generated once and reused securely.

___

## 📁 Project Structure
FUTURE_CS_03/
│
├── app.py                # Main Flask application
├── encryption.py         # AES encryption & decryption logic
├── secret.key            # AES encryption key
├── requirements.txt      # Python package dependencies
├── uploads/              # Encrypted uploaded files
├── decrypted_*           # Temporary decrypted output files
└── README.md             # Project documentation
___

## ▶️ How to Run the Project
1. Install Dependencies
pip install -r requirements.txt
2. Run the Flask App
python app.py
3. Open in Browser
http://127.0.0.1:5000/

___


## 🔒 Security Overview
AES Encryption (Fernet)

Uses AES-128 in CBC mode internally.

Includes HMAC-SHA256 for message integrity.

Ensures files remain confidential and tamper-proof.

Key Handling

A single AES key is generated and stored in secret.key.

Only the server has access to this key.

Files cannot be decrypted without this key.

Secure Transfer

Encrypted files ensure safe storage and downloading.

___

## 🎯 Skills Gained

Flask backend web development

Practical AES encryption

Secure file handling

Cryptography fundamentals

GitHub project management

___

## 📦 Final Deliverables

✔ Complete GitHub repository

✔ Clean, documented code

✔ Professional README.md

✔ Architecture diagram

✔ Security explanation

✔ Walkthrough video (to be recorded by you)

___

## 👤 Author

Pinemula Arun Kumar
Future Interns Program