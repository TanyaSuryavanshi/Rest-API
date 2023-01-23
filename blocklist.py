"""
blocklist.py

This file just contains the blocklist of the JWT tokens. It will be imported by
app and the logout resource so that tokens can be added to the blocklist when the
user logs out.
"""
# when we restarts the app, the blocklist gets deleted.Previous JWTs now work until their expiry date.
# so we can use redis for this.

BLOCKLIST = set()