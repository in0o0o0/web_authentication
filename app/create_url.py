def create_url(secret,user,qr_size,):
    uri = pyotp.totp.TOTP(secret).provisioning_uri(user, issuer_name="Doku Wiki")
    url = 'https://chart.googleapis.com/chart?chs={0}&cht=qr&chl={1}'.format(qr_size,uri);
    return url
