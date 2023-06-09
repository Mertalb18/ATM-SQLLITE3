import sqlite3 as sql

conn = sql.connect("atmserver.db")
cursor = conn.cursor()

def newTable():
    cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
        accountName TEXT,
        accountPassword TEXT,
        accountBalance INTEGER,
        accountDept INTEGER)""")
    conn.commit()


def newAccount(accountName, accountPassword, accountBalance, accountDept):

    cursor.execute("insert into accounts values(?, ?, ?, ?)", (accountName, accountPassword, accountBalance, accountDept))
    conn.commit()


def getAll():
    cursor.execute("select * from accounts")
    accountList = cursor.fetchall()
    return accountList


def getAccount(accountName):
    cursor.execute(f"select * from accounts where accountName = '{accountName}'")
    accountByName = cursor.fetchone()
    return accountByName


def getPassword(accountPassword):
    cursor.execute("select * from accounts where accountPassword = ?", (accountPassword))
    accountByPassword = cursor.fetchone()
    return accountByPassword


def updatePassword(accountName, newPassword):
    cursor.execute("update accounts set accountPassword = ? where accountName = ?", (newPassword, accountName))
    conn.commit()


def updateBalance(accountName, newBalance):
    cursor.execute("update accounts set accountBalance = ? where accountName = ?", (newBalance, accountName))
    conn.commit()


def updateDept(accountName, newDept):
    cursor.execute("update accounts set accountDept = ? where accountName = ?", (newDept, accountName))
    conn.commit()


def deleteAccount(accountName):
    cursor.execute("delete from accounts where accountName = ?", (accountName,))
    conn.commit()


def deleteTable():
    cursor.execute("drop table accounts")
    print("Tablo silindi.")