# "dySxnIZZBRZp0VBUEiJXcmGYsZomC7"

import requests
import os
import sys

bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDcxMDA3Mzc1Njk4MjA5NjczNjMiLCJhdWQiOlsiaHR0cHM6Ly9kaXkucmVwaHJhc2UuYWkvYXV0aDAiLCJodHRwczovL3JlcGhyYXNlYWktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc5NzYzMTk5LCJleHAiOjE2Nzk4NDk1OTksImF6cCI6IjNLVTVqdkVxV0pCQ1VLblBYMjZvbmFTUHkzakozMEo0Iiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSByZWFkOnJlcGhyYXNlLmFpIGFsbDpkaXkgcmVhZDpyZXBocmFzZS5haSJ9.pnWxI2-3eL-kVMWEznoUbD59l0xac_LSg3p-7hJvR6ZpeX4bvlg0KxDUbP7Ke7dPskWqCfoX7IY43QcZnUPXv1MRUpQONgmSbzqeuvhSSWXcQ39HBCzuKxypXCCbIKJwy93SYF7_ZTr5LP-82HVetez8_YlGVORTww4NvZsIa4YHAzbbkQne_3Jdx2NP19y1j_huMy2lXpNYg2zWwht5WyoIFT0qo7rS6Ru43Pf2s74GhXqrSHiRBu8PbrwtCnZ89DIdxLvkaU7rqNmZYoyQUKeTDn7y_iLf65KspRctM1zH5nxdbDZP7N5cI1juNh2hxJFvV9NvsHVfqFc4C3rAtA"

campaign_id = "GcCf1NQc2SNlIZWIOrmWxaWfYPPXYV" # From previous script


url = f"https://personalized-brand.api.rephrase.ai/v2/campaign/GcCf1NQc2SNlIZWIOrmWxaWfYPPXYV/export"

headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
}

response = requests.post(url, headers=headers)

print(response.text)
