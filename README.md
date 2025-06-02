# basic login system

using bcrypt library implemented a basic login system.

<img width="239" alt="Screenshot 2025-06-02 at 7 37 38 PM" src="https://github.com/user-attachments/assets/38352f80-9ed0-4884-9e85-3574e2bab68c" />

The password is hashed using bcrypt algorithm with random generated salt. The password is one that you are seeing in the above image, otherwise knowing the password is computationally not feasible. but yes in code you can see the given hashed password, and extract salt and cost factor from it.
