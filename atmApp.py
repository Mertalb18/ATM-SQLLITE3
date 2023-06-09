# ATM Para Çekme
from atmDatabase import *

# ! ATM func start
def atm():
    newTable()
    tries = 3
    # ! Welcome start
    while True:
        print(f"""Hoşgeldiniz, lütfen sisteme giriş yapın. Eğer kayıtlı değilseniz lütfen kayıt olun.
        1- Kullanıcı Girişi
        2- Yeni Kayıt
        3- Çıkış Yap""")

        login = input("Seçiminiz: ")
        # ! Login start
        if login == "1":
            while True:
                tries -= 1
                username = input("Kullanıcı adınızı giriniz: ").lower()
                password = input("Şifrenizi giriniz: ")
                accountCheck = getAccount(username)

                if accountCheck == None:
                    print("Kullanıcı bulunamadı.")
                    continue

                accountName = accountCheck[0]
                accountPassword = accountCheck[1]
                accountBalance = accountCheck[2]
                accountDept = accountCheck[3]

                if username == "" and password == "":
                    print("Kullanıcı adı veya şifre boş bırakılamaz")

                elif username == accountName and password == accountPassword:
                        print("Giriş Yapıldı.")
                        # ! Menu start
                        while True:
                            print("""\nİşlemler:
    1- Para Çekme
    2- Para Yatırma
    3- Para Gönderme
    4- Şifre Değişikliği
    5- Bakiye Sorgulama
    6- Borç Yatırma
    7- Borç Sorgulama
    8- Çıkış""")

                            transaction = input("\nYapmak istediğiniz işlemin numarasını giriniz: ")

                            if transaction == "1": # Money withdraw
                                print(f"Güncel Bakiyeniz: {accountBalance}")

                                while True:
                                    try:
                                        withdraw = int(input("Çekmek istediğiniz tutarı giriniz: "))

                                        if withdraw > accountBalance:
                                            print("Yetersiz bakiye.")

                                        elif withdraw == 0:
                                            print("Çekmek istediğiniz tutar '0' dan büyük olmalıdır.")

                                        else:
                                            accountBalance -= withdraw
                                            updateBalance(accountName, accountBalance)
                                            print(f"Çekilen tutar: {withdraw}. Kalan Bakiye: {accountBalance}")
                                            break

                                    except:
                                        print("Bir sayı girmeniz gerekiyor.")

                            elif transaction == "2": # Money deposit
                                print(f"Güncel Bakiyeniz: {accountBalance}")

                                while True:
                                    try:
                                        deposit = int(input("Yatırmak istediğiniz tutarı giriniz: "))

                                        if deposit > 0:
                                            accountBalance += deposit
                                            updateBalance(accountName, accountBalance)
                                            print(f"Yatırılan tutar: {deposit}. Yeni Bakiye: {accountBalance}")
                                            break

                                    except:
                                        print("Bir sayı girmeniz gerekiyor.")

                            elif transaction == "3": # Money transfer
                                print(f"Güncel Bakiyeniz: {accountBalance}")
                                
                                while True:
                                    try:
                                        while True:
                                            transfer = int(input("Göndermek istediğiniz miktarı giriniz: "))
                                            if transfer == 0:
                                                print("Göndermek istediğiniz tutar '0' dan büyük olmalıdır.")

                                            else:
                                                transferName = input("Göndermek istediğiniz hesap adını giriniz: ")
                                                recieverName = getAccount(transferName)
                                                
                                                if recieverName == None:
                                                    print("Kullanıcı bulunamadı.")
                                                    continue

                                                transferName = recieverName[0]
                                                transferBalance = recieverName[2]

                                            if transferName == "":
                                                print("Lütfen geçerli bir alıcı hesap adı giriniz.")

                                            else:
                                                print(f"{transferName} hesabına {transfer} para gönderme işlemini onaylıyor musunuz?")

                                                while True:
                                                    approve = input("E/H: ").lower()
                                                    if approve == "e" and accountBalance > transfer:
                                                        accountBalance -= transfer
                                                        transferBalance += transfer
                                                        updateBalance(accountName,accountBalance)
                                                        updateBalance(transferName,transferBalance)
                                                        print(f"{transferName} hesabına {transfer} gönderildi. Güncel bakiyeniz {accountBalance}")
                                                        break

                                                    elif approve == "h":
                                                        print("İşlem iptal ediliyor.")
                                                        break

                                                    else:
                                                        print("Geçersiz işlem")
                                                        
                                                break
                                        break
                                    except:
                                        print("Bir sayı girmeniz gerekiyor.")

                            elif transaction == "4": # Password change
                                while True:
                                    password = input("Şifrenizi Giriniz: ")
                                    
                                    if password == accountPassword:
                                        while True:
                                            newPassword = input("Yeni şifrenizi giriniz: ")
                                            newPasswordCheck = input("Yeni şifrenizi tekrar giriniz: ")

                                            if len(newPassword) == 4:
                                                if newPassword == newPasswordCheck:
                                                    updatePassword(accountName, newPassword)
                                                    print("Şifreniz değiştirilmiştir.")
                                                    break

                                                else:
                                                    print("Şifreler uyuşmuyor.")

                                            else:
                                                print("Şifre uzunluğu 4 karakterden oluşmalıdır.")
                                                
                                        break
                                    else:
                                        print("Girilen şifre hatalıdır.")

                            elif transaction == "5": # Balance display
                                print(f"Güncel bakiyeniz: {accountBalance}")

                            elif transaction == "6": # Dept payment
                                print(f"Bakiyeniz: {accountBalance} TL")
                                print(f"Borcunuz: {accountDept} TL")

                                while True:
                                    try:
                                        payment = int(input("Ödemek istediğiniz miktarı giriniz: "))

                                        if payment > 0:
                                            if accountBalance >= payment:
                                                accountBalance -= payment
                                                accountDept -= payment
                                                updateBalance(accountName, accountBalance)
                                                updateDept(accountName, accountDept)
                                                print(f"Borcunuz ödendi. Kalan borcunuz {accountDept} TL. Yeni bakiyeniz {accountBalance} TL")
                                                break

                                            else:
                                                print("Yetersiz bakiye.")
                                    
                                    except:
                                        print("Bir sayı girmeniz gerekiyor.")

                            elif transaction == "7": # Dept display
                                print(f"Güncel borcunuz: {accountDept} TL")


                            elif transaction == "8": # Menu exit
                                print("Çıkış yapılıyor.")
                                break
                        # ! Menu end
                elif tries == 0:
                    print("Hesabınız bloke edildi.")
                    break

                else:
                    print("Kullanıcı Adı veya Şifre hatalı")

                break
        # ! Login end
        # ! Register start
        elif login == "2":
            while True:
                accountName = input("Kullanıcı adınızı giriniz: ")
                accountCheck = getAccount(accountName)

                if accountCheck != None:
                    print("Bu kullanıcı zaten mevcut.")
                    continue

                if len(accountName) < 4:
                    print("Kullanıcı adı en az 4 karakterli olmalıdır.")

                else:
                    while True:
                        newPassword = input("Şifrenizi giriniz: ")
                        newPasswordCheck = input("Şifrenizi tekrar giriniz: ")

                        if len(newPassword) == 4:
                            if newPassword == newPasswordCheck:
                                accountPassword = newPassword
                                newAccount(accountName, accountPassword, 0, 5000)
                                print("Kaydınız tamamlanmıştır.")
                                break

                            else:
                                print("Şifreler uyuşmuyor.")

                        else:
                            print("Şifre uzunluğu 4 karakterden oluşmalıdır.")

                    break
        # ! Register end
        # ! Shutdown start
        elif login == "3":
            print("Çıkış yapıldı.")
            break
        # ! Shutdown end
        else:
            print ("Hatalı giriş.")
    # ! Welcome end
# ! ATM func end
atm()