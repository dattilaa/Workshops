def send_sms(text) -> str:
    return text if len(text) <= 160 else text[:160]

print(send_sms(input()))