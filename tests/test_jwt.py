from app.security import create_access_token

token = create_access_token(
    {
        "sub": "gowtham123"
    }
)

print(token)