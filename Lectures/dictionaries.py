'''
customer = {
    "name": "Dabin Im",
    "age": 29,
    "is_verified": True
}

print(customer["name"])
# print(customer["Name"])           # Error: 파이썬은 대소문자 구별한다
# print(customer["birthdate"])      # Error: customer dictionary 에 존재하지 않은 key 이다.

print(customer.get("name"))         # 해당 key에 존재하는 value을 가져온다. 즉 print(customer["name"])와 같은 역할을 함
print(customer.get("birthdate"))    # 단, print(customer["birthdate"]) 는 다르게 오류를 던지지 않음
                                    # 결과 : None (이유: birthdate 라는 key가 존재하지 않기에 오류를 대신하여 None 이라는 결과를 보여준다.) 


customer.get("birthdate", "Dec 16 1991") # 다음과 같이 명시적으로 value 값을 지정할 수 있다.

# 또한 customer dictionary 에 값을 변경하거나 저장할 수 있다.
customer["name"] = "Jack Smith"         # value 변경 = update
customer["birthdate"] = "Jan 1 1980"    # key-value 추가 = add

print(customer)
'''

# Simple Quiz
#region
#digits_mapping = {
#    "1" : "One",
#    "2" : "Two",
#    "3" : "Three",
#    "4" : "Four"
#}

#numbers = input("Phone: ")
#text = ""
## method 1
#'''
#for number in numbers:
#    text += digits_mapping[number] + " "
#'''

## method 2
#for ch in numbers:
#    text += digits_mapping.get(ch, "!") + " "

#print(text)
#endregion

message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😔"
}
text = ""
for word in words:
    text += emojis.get(word, word) + " "

print(text)