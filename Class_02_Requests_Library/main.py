import requests # type: ignore    
# for download => pip install types-requests


# #1. Get request => ki hai hamne khud ki bnai hui api se
# res = requests.get("https://testing-api-fast.vercel.app/")

# print(res.json()) # ['Taha', 'Raza', 'Ali']



#<-------------------------------------------------------------------------------------->
#2. Post request => ki hai hamne data create karne ke liye.

# Url = "https://testing-api-fast.vercel.app/"

# my_body = {
#   "name": "Azlaan"
# }

# res_post = requests.post(Url, json=my_body)



#<-------------------------------------------------------------------------------------->
#3. Put request => ki hai hamne data update karne ke liye.

# old_name = "Azlaan"

# my_put_body = {
#   "name": "Awais"
# }

# res_put = requests.put(f"{Url}/{old_name}", json=my_put_body)
# print(res_put.json())


#<-------------------------------------------------------------------------------------->
#3. Delete request => ki hai hamne data delete karne ke liye.

Url = "https://testing-api-fast.vercel.app/"

try:
    del_name = "Awais"

    res_delete = requests.delete(f"{Url}data/{del_name}")

    print("status_code:", res_delete.status_code)
    print("\n")
    print("headers:", res_delete.headers)
    print("\n")
    print("text str type:", res_delete.text)
    print("\n")
    print("json list type:", res_delete.json())

except Exception as e:
    print("You have an error in your api request", e)