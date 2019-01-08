totp = pyotp.TOTP("DBからユーザのsecretを取得")

if totp.verify("ユーザから送られてきたコードを取得"):
    "認証成功時の処理"
else:
    "認証失敗時の処理"
