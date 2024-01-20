# Project Title

This is a brief description of what this project does and the technologies used. This project includes a Python script for sending emails (`emailer.py`), a text file containing the email message (`message.txt`), and a `.gitignore` file for ignoring certain files in Git.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- Any text editor

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository to your local machine.
URL: https://github.com/dasrecord/marketing_automation.git

2. Create a `config.ini` file in the project directory. This file should contain your email settings. Here's an example of what it should look like:

```ini
[Email]
MY_ADDRESS = your-email@example.com
PASSWORD = your-email-password
```
3. Add your contact list file to the project directory.
EXAMPLE: msj_leads.csv

4. Run `emailer.py` to send emails.

## Additional Notes
You may need to set up "Sign in with app passwords" on your gmail.
URL: https://support.google.com/accounts/answer/185833?hl=en

## Built With

- Python3

## Authors

- Prasenjit Das - Initial work