from msal import ConfidentialClientApplication
import requests
import json

# =========================
# Azure App Registration
# =========================

TENANT_ID = "30441bb7-6714-4898-affe-230b17c4704c"
CLIENT_ID = "3c8a6773-e5af-4ac3-b636-2342f167a11e"
CLIENT_SECRET = "Put Scret here"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

# =========================
# Authenticate
# =========================

app = ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

token = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" not in token:
    print("Authentication Failed")
    print(token)
    exit()

headers = {
    "Authorization": f"Bearer {token['access_token']}",
    "Content-Type": "application/json"
}

# =========================
# Create User
# =========================
user_data = {
    "accountEnabled": True,
    "displayName": "John Dan",
    "mailNickname": "johndan",
    "userPrincipalName": "johndan@speedoflightengineering.onmicrosoft.com",
    "passwordProfile": {
        "forceChangePasswordNextSignIn": True,
        "password": "TempPassword123!"
    },
    "department": "Sales",
    "jobTitle": "Sales Executive"
}

response = requests.post(
    "https://graph.microsoft.com/v1.0/users",
    headers=headers,
    json=user_data
)

if response.status_code == 201:
    print("User Created Successfully")
else:
    print(response.text)
    exit()

user_id = response.json()["id"]

# =========================
# Add User to Group
# =========================
GROUP_ID = "2a658fec-74a1-4417-8687-10d30b764d37"

group_payload = {
    "@odata.id":
    f"https://graph.microsoft.com/v1.0/directoryObjects/{user_id}"
}

response = requests.post(
    f"https://graph.microsoft.com/v1.0/groups/{GROUP_ID}/members/$ref",
    headers=headers,
    json=group_payload
)

if response.status_code == 204:
    print("User Added to Group")
else:
    print(response.text)

print("Onboarding Complete")


