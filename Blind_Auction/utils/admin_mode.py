import json

SETTINGS_FILE = './utils/admin_setting.json'
with open(SETTINGS_FILE,'r') as f:
    settings = json.load(f)
    people_number = settings.get('people_number')
    min_price = settings.get('min_price')
    password = settings.get('password')

# main.py에서 세팅이 변경될 시 다시 해당 변수를 로딩하기 위한 함수
def load_settings():
    global people_number, min_price, password
    with open(SETTINGS_FILE,'r') as f:
        settings = json.load(f)
        people_number = settings.get('people_number')
        min_price = settings.get('min_price')
        password = settings.get('password')
    
# 비밀번호 변경함수
def password_change():
    global settings
    while True:
        new_password = input("Please enter new password: ")
        password_check = input("Please reenter new password: ")
        
        if new_password != password_check:
            print("Password change failed.")
        else:
            print("Password change success!")
            settings['password'] = new_password
            
            with open(SETTINGS_FILE, 'w') as f:
                json.dump(settings, f)
            break      

# 입찰자 수, 최저 입찰 금액 세팅
def admin_set():
    global settings
    new_people_num = int(input("Please enter new people_num: "))
    new_min_price = int(input("Please enter new min_pirce: "))
    settings['people_number'] = new_people_num
    settings['min_price'] = new_min_price
    
    with open(SETTINGS_FILE,'w') as f:
        json.dump(settings, f)