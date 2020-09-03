import requests

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


def part_1(form_build_id):
    payload = {'submitted[a1]': '2',
               'submitted[c1]': '2',
               'submitted[e1]': '2',
               'submitted[n1]': '2',
               'submitted[o1]': '2',
               'submitted[a2]': '3',
               'submitted[c2]': '3',
               'submitted[e2]': '3',
               'submitted[n2]': '3',
               'submitted[o2]': '3',
               'submitted[a3]': '4',
               'submitted[c3]': '4',
               'submitted[e3]': '4',
               'submitted[n3]': '4',
               'submitted[o3]': '4',
               'submitted[a4]': '1',
               'submitted[c4]': '1',
               'submitted[e4]': '1',
               'submitted[n4]': '1',
               'submitted[o4]': '1',
               'form_id': 'webform_client_form_17315'}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text


def part_2(form_build_id):
    payload = {'submitted[a5]': '2',
               'submitted[c5]': '2',
               'submitted[e5]': '2',
               'submitted[n5]': '2',
               'submitted[o5]': '2',
               'submitted[a6]': '3',
               'submitted[c6]': '3',
               'submitted[e6]': '3',
               'submitted[n6]': '3',
               'submitted[o6]': '3',
               'submitted[a7]': '4',
               'submitted[c7]': '4',
               'submitted[e7]': '4',
               'submitted[n7]': '4',
               'submitted[o7]': '4',
               'submitted[a8]': '1',
               'submitted[c8]': '1',
               'submitted[e8]': '1',
               'submitted[n8]': '1',
               'submitted[o8]': '1',
               'form_id': 'webform_client_form_17315',
               'form_build_id': form_build_id,
               'details[sid]': '',
               'details[page_num]': '2',
               'details[page_count]': '4',
               'details[finished]': '0',
               'url': '',
               'op': 'Next Page >',
               'submitted[pagebreak]': 'pagebreak'}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text


def part_3(form_build_id):
    payload = {'submitted[a_word_1]': '2',
               'submitted[c_word_1]': '2',
               'submitted[e_word_1]': '2',
               'submitted[n_word_1]': '2',
               'submitted[o_word_1]': '2',
               'submitted[a_word_2]': '3',
               'submitted[c_word_2]': '3',
               'submitted[e_word_2]': '3',
               'submitted[n_word_2]': '3',
               'submitted[o_word_2]': '3',
               'submitted[a_word_3]': '4',
               'submitted[c_word_3]': '4',
               'submitted[e_word_3]': '4',
               'submitted[n_word_3]': '4',
               'submitted[o_word_3]': '4',
               'submitted[a_word_4]': '4',
               'submitted[c_word_4]': '4',
               'submitted[e_word_4]': '4',
               'submitted[n_word_4]': '4',
               'submitted[o_word_4]': '5',
               'form_id': 'webform_client_form_17315',
               'form_build_id': form_build_id,
               'details[sid]': '',
               'details[page_num]': '3',
               'details[page_count]': '4',
               'details[finished]': '0',
               'url': '',
               'op': 'Next Page >',
               'submitted[pagebreak_2]': 'pagebreak 2'}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text


def part_4(form_build_id):
    payload = {'form_id': 'webform_client_form_17315',
               'form_build_id': form_build_id,
               'submitted[age]': '',
               'submitted[gender]': 'null',
               'submitted[education]': 'null',
               'submitted[children]': '',
               'details[sid]': '',
               'details[page_num]': '4',
               'details[page_count]': '4',
               'details[finished]': '0',
               'url': '',
               'op': 'Score it!',
               'submitted[pagebreak_4]': 'pagebreak'}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

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


build_id = get_form_build_id(get_form())


p1 = part_1(build_id)
p1_r = get_form_build_id(p1)

# print(p1)
print(p1_r)


p2 = part_2(p1_r)
p2_r = get_form_build_id(p2)

# print(p2)
print(p2_r)


p3 = part_3(p2_r)
p3_r = get_form_build_id(p3)

# print(p3)
print(p3_r)

p4 = part_4(p3_r)
# print(p4)

print(get_ocean(p4))
