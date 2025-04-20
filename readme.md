# Python Banking App 
Made by - Riddesh Saboo , ZuberKhan Pathan and Arjun Singh
A simple banking system built in Python using Tkinter for GUI and SQLite for storage. 
This app includes features like user registration, login, balance management, QR code generation and scanning for unique user identification.

## Project Structure

.
├── accounts/qr/           # Stores generated QR codes
├── dashboard_page.py      # User dashboard interface
├── db_helper.py           # SQLite helper for database operations
├── deposit_page.py        # Handles deposits
├── login_page.py          # User login system
├── main.py                # Main entry point to launch the app
├── pay_page.py            # Payment to friend system
├── qr_generator.py        # QR code generator module
├── qr_scanner.py          # QR code scanner using webcam
├── register_page.py       # New user registration logic
├── transactions_page.py   # Shows user’s transaction history
├── withdraw_page.py       # Handles withdrawals
├── customers.db           # SQLite DB file (excluded from Git)


## Features

- User Registration & Login  
- Deposit & Withdraw Money  
- Send Money to Friends (with balance update for both accounts)(using Qr or manually) 
- View Transaction History  
- QR Code Generation upon registration of the User  
- QR Code Scanning  
- All data stored securely in SQLite  


## Dependencies

Install required libraries via:

```bash
pip install -r requirements.txt

requirements.txt contains:

qrcode==8.1
pillow==11.2.1
opencv-python==4.11.0.86
pyzbar==0.1.9
numpy==2.2.4


Running the App
	1.	Clone the repo:

        git clone https://github.com/riddeshsaboo/banking-application
        cd banking-application


	2.	Install dependencies:

        pip install -r requirements.txt


	3.	Launch the app:

        python main.py



QR Code System
	•	Generates a unique QR for each registered user.
	•	Stored in accounts/qr/USERNAME.png.  (USERNAME == PRN of the user)
	•	Can be scanned later for instant login and transactions.


GitHub Notes

Excluded files/folders (via .gitignore):
	•	__pycache__/
	•	*.db
	•	accounts/qr/*.png
	•	lib/, bin/, and venv-related files

Author

Developed by Riddesh Saboo

