import os
import subprocess

# Run the 'chainlit create-secret' command
result = subprocess.run(['chainlit', 'create-secret'], stdout=subprocess.PIPE)

# Extract the secret from the output
secret = result.stdout.decode('utf-8').split('\n')[1]

# Write the secret to the .env file
with open('.env', 'a') as f:
    f.write(secret + '\n')

print("Secret written to .env file.")
