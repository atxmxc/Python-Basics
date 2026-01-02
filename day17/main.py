# using api keys, environmental variables and making an api tool thats safe to distribute.
# DISCLAMER: NEVER PUT YOUR API KEYS IN YOUR CODE OR REPO
# we set the key using env variables
'$env:AP_KEY="your_key"'
# we can read the ket as well using the os library
import os
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("Missing Variable")
    raise SystemExit
