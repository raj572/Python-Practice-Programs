from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID" : "aghohjAYlFljn3d8S7N5jGJ87KbEGmwsmnfiFxlnfpg58tYiGlghfVMg3_aoiM3l1Eeo3Q.",
    "__Secure-1PSIDTS" : "sidts-CjIBSAxbGeaZX46kGvjC3xby2us20Xv7e6nykNx7oM3JKsSVYgW9iPBTcbBvs4OH35pFlBAA",
    "__Secure-1PSIDCC" : "APoG2W-mMfYo0W07k7a4s1nrZpnHgWeFRRqXDdhR2Wx9iTEt-1UqB8c52hfZzi8Xb-Kg-WzsBH5J"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input("Enter Your Query : ")
    Reply = bard.get_answer(Query)['content']
    print(Reply)
