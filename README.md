## Brute-Force Login Simulator

A Python-based Brute-Force Login Simulator to demonstrate the mechanics of brute-force attacks on login systems. This tool uses a hardcoded username and password and attempts to “guess” the password from a list of potential passwords.

	⚠️ Warning: This script is for educational purposes only. Unauthorized use of brute-force techniques is illegal. Use only on systems you own and are authorized to test.

## Features

	•	Simulated Brute-Force Attack: Attempts to guess a target password from a list.
	•	Customizable Password List: Easily change the list of attempted passwords by editing passwords.txt.
	•	Progress Feedback: Shows each login attempt and the result.

## Project Structure

Brute-Force-Login-Simulator/
├── brute_force_simulator.py  # Main script for the brute-force simulation
└── passwords.txt             # List of passwords to try

## Requirements

	•	Python 3.6+

## Installation

	1.	Clone the Repository:

git clone https://github.com/yourusername/Brute-Force-Login-Simulator.git
cd Brute-Force-Login-Simulator


	2.	Verify Dependencies:
This script only uses standard Python libraries, so no additional installations are required.

Usage

	1.	Set the Target Username and Password (optional):
Open brute_force_simulator.py and edit the following lines to set the target credentials:

TARGET_USERNAME = "admin"           # The username to simulate attacking
TARGET_PASSWORD = "supersecret"      # The correct password to simulate finding


	2.	Update Password List (optional):
Open passwords.txt and add your own test passwords, one per line. The script will attempt each password in the order listed.
	3.	Run the Simulator:

python brute_force_simulator.py


	4.	Example Output:

Attempting brute-force on username 'admin'...
Attempt 1: Trying password '1234'
Attempt 2: Trying password 'password'
...
[SUCCESS] Login successful with password 'supersecret' after 7 attempts!



Explanation

The simulator attempts each password from passwords.txt until it either finds the correct password or exhausts the list. A small delay is added between attempts to mimic real-world conditions.

Example passwords.txt

1234
password
letmein
qwerty
admin123
guest
supersecret

Notes and Limitations

	•	Educational Use Only: This simulator is intended to provide an understanding of brute-force attacks for educational purposes.
	•	Simple Simulation: This is a basic brute-force simulation, without network access or login forms. It only demonstrates brute-force logic in Python.
	•	Modify to Expand: You can expand this tool by adding multiple usernames, logging outputs to a file, or adjusting delays between attempts.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Use this README to guide users through the purpose, usage, and limitations of the Brute-Force Login Simulator.
