from dotenv import load_dotenv
import os
load_dotenv(r"C:\Users\ShreyasBilikereShant\Downloads\.env")
temp = os.getenv("exception_emails")
print(type(temp))
#out=temp.split(',')
print(temp)
