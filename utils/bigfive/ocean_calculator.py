import requests
from collections import Counter
import re


def get_form_build_id(r):

    regex = r'<input type="hidden" name="form_build_id" value="(.*)" \/>(\s)*<input type="hidden" name="form_id" value="webform_client_form_17315" \/>'

    matches = re.finditer(regex, r, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            m = match.group(groupNum)
            if len(m) > 5:
                return m
    return None


url = "https://www.truity.com/test/big-five-personality-test"
headers = {'Referer': 'https://www.truity.com/test/big-five-personality-test', }
files = []


def get_form():
    response = requests.request("GET", url)
    return response.text

def part_1(responses):
    payload = responses
    payload['form_id'] = 'webform_client_form_17315'

    response = requests.request("POST", url, headers=headers, data=payload, files=payload)

    return response.text

def part_2(form_build_id, responses):
    payload = responses
    payload['form_id'] = 'webform_client_form_17315'
    payload['form_build_id'] = form_build_id
    payload['details[sid]'] = ''
    payload['details[page_num]'] = '2'
    payload['details[page_count]'] = '4'
    payload['details[finished]'] = '0'
    payload['url'] = ''
    payload['op'] = 'Next Page >'
    payload['submitted[pagebreak]'] = 'pagebreak'

    response = requests.request("POST", url, headers=headers, data=payload, files=payload)

    return response.text

def part_3(form_build_id, responses):

    payload = responses
    payload['form_id'] = 'webform_client_form_17315'
    payload['form_build_id'] = form_build_id
    payload['details[sid]'] = ''
    payload['details[page_num]'] = '3'
    payload['details[page_count]'] = '4'
    payload['details[finished]'] = '0'
    payload['url'] = ''
    payload['op'] = 'Next Page >'
    payload['submitted[pagebreak]'] = 'pagebreak 2'

    response = requests.request("POST", url, headers=headers, data=payload, files=payload)

    return response.text


def part_4(form_build_id):
    payload = {'form_id': 'webform_client_form_17315',
               'form_build_id': form_build_id,
               'submitted[age]': '',
               'submitted[gender]': 'null',
               'submitted[education]': 'null',
               'submitted[children]': '',
               'details[sid]': '',
               'details[page_num]': 0,
               'details[page_count]': 0,
               'details[finished]': 0,
               'url': '',
               'op': 'Score it!',
               'submitted[pagebreak_4]': 'pagebreak'}

    response = requests.request("POST", url, headers=headers, data=payload, files=payload)

    return response.text


def get_ocean(result):
    regex = r"\"dataset\":{\"\":\[{\"name\":\"O\",\"value\":(.*)},{\"name\":\"C\",\"value\":(.*)},{\"name\":\"E\",\"value\":(.*)},{\"name\":\"A\",\"value\":(.*)},{\"name\":\"N\",\"value\":(.*)}\]}}}\)"
    matches = re.finditer(regex, result, re.MULTILINE)

    r = []

    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            r.append(match.group(groupNum))

    return r

def score_ocean(questionnarie):

    response_1 = {'submitted[a1]': 0,
                  'submitted[c1]': 0,
                  'submitted[e1]': 0,
                  'submitted[n1]': 0,
                  'submitted[o1]': 0,
                  'submitted[a2]': 0,
                  'submitted[c2]': 0,
                  'submitted[e2]': 0,
                  'submitted[n2]': 0,
                  'submitted[o2]': 0,
                  'submitted[a3]': 0,
                  'submitted[c3]': 0,
                  'submitted[e3]': 0,
                  'submitted[n3]': 0,
                  'submitted[o3]': 0,
                  'submitted[a4]': 0,
                  'submitted[c4]': 0,
                  'submitted[e4]': 0,
                  'submitted[n4]': 0,
                  'submitted[o4]': 0}


    response_2 = {'submitted[a5]': 0,
                  'submitted[c5]': 0,
                  'submitted[e5]': 0,
                  'submitted[n5]': 0,
                  'submitted[o5]': 0,
                  'submitted[a6]': 0,
                  'submitted[c6]': 0,
                  'submitted[e6]': 0,
                  'submitted[n6]': 0,
                  'submitted[o6]': 0,
                  'submitted[a7]': 0,
                  'submitted[c7]': 0,
                  'submitted[e7]': 0,
                  'submitted[n7]': 0,
                  'submitted[o7]': 0,
                  'submitted[a8]': 0,
                  'submitted[c8]': 0,
                  'submitted[e8]': 0,
                  'submitted[n8]': 0,
                  'submitted[o8]': 0}

    response_3 = {'submitted[o_word_1]': 0,
                    'submitted[c_word_1]': 0,
                    'submitted[e_word_1]': 0,
                    'submitted[a_word_1]': 0,
                    'submitted[n_word_1]': 0,
                    'submitted[o_word_2]': 0,
                    'submitted[c_word_2]': 0,
                    'submitted[e_word_2]': 0,
                    'submitted[a_word_2]': 0,
                    'submitted[n_word_2]': 0,
                    'submitted[o_word_3]': 0,
                    'submitted[c_word_3]': 0,
                    'submitted[e_word_3]': 0,
                    'submitted[a_word_3]': 0,
                    'submitted[n_word_3]': 0,
                    'submitted[o_word_4]': 0,
                    'submitted[c_word_4]': 0,
                    'submitted[e_word_4]': 0,
                    'submitted[a_word_4]': 0,
                    'submitted[n_word_4]': 0,
                    }

    c = 0

    for key, value in response_1.items():
        response_1[key] = questionnarie[c] + 1 
        c += 1

    for key, value in response_2.items():
        response_2[key] = questionnarie[c] + 1 
        c += 1

    for key, value in response_3.items():
        response_3[key] = 1 #questionnarie[c] + 1 
        c += 1

    print(list(response_1.values()) + list(response_2.values()) + list(response_3.values()))

    p1 = part_1(response_1)
    p1_r = get_form_build_id(p1)

    #print(p1_r)

    p2 = part_2(p1_r, response_2)
    p2_r = get_form_build_id(p2)

    #print(p2_r)

    p3 = part_3(p2_r, response_3)
    p3_r = get_form_build_id(p3)

    #print(p3_r)

    p4 = part_4(p3_r)

    l = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness" , "Neuroticism"]


    return zip(l, get_ocean(p4))


if __name__ == "__main__":
    questionnarie = [4, 4, 3, 0, 4, 1, 3, 1, 0, 2, 4, 3, 2, 0, 2, 4, 4, 0, 1, 3, 3, 4, 3, 0, 4, 2, 1, 0, 3, 0, 2, 0, 2, 2, 0, 0, 0, 1, 4, 2, 4, 4, 2, 4, 2, 4, 0, 1, 4, 2, 4, 4, 3, 3, 0, 1, 4, 3, 4, 2]

    q = "2  4   4   4   3   4   4   4   3   4   0   0   4   4   0   0   4   0   0   4   4   4   0   0   4   4   0   0   0   0   4   0   0   0   0   4   0   0   0   0   4   4   0   0   3   4   4   2   3   3   4   3   3   4   4   2   0   0   4   4"
    questionnarie = list(map(int,q.split()))
    print(dict(score_ocean(questionnarie)))

