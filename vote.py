import csv
import time
import re


def validate_email(email):
    pattern = r'^[a-zA-Z][0-9]{2}43[0-9]{3}@ems\.niu\.edu\.tw$'
    username, domain = email.split('@')
    print(f'\r{username[:-3]}***@{domain} ->', end='')

    if re.match(pattern, email):
        return True
    else:
        return False


def read_csv(filename):
    expectations = []  # 新的陣列用於儲存'對112學年的資工系學會的期許'
    total_votes = 0  # 用於儲存總票數
    valid_votes = 0  # 用於儲存有效票數
    invalid_votes = 0  # 用於儲存無效票數
    candidate1 = 0  # 用於儲存'同意哪一組當選?'為'第一組'的票數
    candidate2 = 0  # 用於儲存'同意哪一組當選?'為'第二組'的票數
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            total_votes += 1

            if(validate_email(row['電子郵件地址'])):
                agreement = row['同意哪一組當選?']
                if agreement == '第一組候選人':
                    candidate1 += 1
                elif agreement == '第二組候選人':
                    candidate2 += 1
                valid_votes += 1
                print(f'「{agreement}」一票')
                # print('{agreement}一票')
            else:
                invalid_votes += 1
                print('「非會員無效票」一票')
                # print('無效票 一票')
            print(f'\r第一組票數:{candidate1}  第二組票數:{candidate2}  無效票數:{invalid_votes}', end='')
            expectation = row['對112學年的資工系學會的期許']
            if expectation != '':
                expectations.append(expectation)
            time.sleep(0.5)
    return [expectations, total_votes, valid_votes, invalid_votes, candidate1, candidate2]


first = 47 
second = 55
third = 47
fourth = 45
fifth = 2
r_first = 18
r_second = 12
r_third = 1
r_fourth = 3
total = first+second+third+fourth+fifth+r_first+r_second+r_third+r_fourth
threshold = total//3 + 1


print('第十五屆資工系正副會長選舉開票！')
print('----------------------------------------------')
time.sleep(1)

filename = 'data.csv'
expectations, total_votes, valid_votes, invalid_votes, candidate1, candidate2 = read_csv(filename)

print()
print('----------------------------------------------')
print('資訊工程學系年級人數：')
print(f'大一：{first}人  大二：{second}人  大三：{third}人  大四：{fourth}人  大五：{fifth}人')
print(f'碩一：{r_first}人  碩二：{r_second}人  碩三：{r_third}人  碩四：{r_fourth}人')
print(f'總人數：{total}人')
print(f'總投票數：{total_votes}')
print(f'無效票數：{invalid_votes}')
print(f'有效票數{valid_votes}人，佔總人數{round(valid_votes/(total)*100, 2)}%')
print()
if(valid_votes >= threshold):
    print('有效票數已達本會會員三分之一以上故投票有效：')
    print(f'我們恭喜{f"「第一組」獲得「{candidate1}」票" if candidate1 > candidate2 else f"「第二組」獲得「{candidate2}」票"}，當選第十五屆資訊工程學系正副會長')
else:
    print('有效票數未達本會會員三分之一以上故投票無效：')
    print('本次投票無效，請大家再接再厲！')

# print('----------------------------------------------')
# print('您們寶貴的意見我們都有看到：')
# for expectation in expectations:
#     print(expectation)
