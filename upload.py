"""
A script for making the program directories and files for a
variety of different contests.
"""

import sys

from cp_helper.judges.judge import Judge
from cp_helper.judges.atcoder import AtCoder
from cp_helper.judges.boj import Boj
from cp_helper.judges.codeforces import Codeforces
from cp_helper.judges.dmoj import Dmoj
from cp_helper.judges.fhc import Fhc


# for identifying the judge
IDENTIFIERS = [
    ('atcoder.jp', AtCoder),
    ('acmicpc.net', Boj),
    ('codeforces.com', Codeforces),
    ('dmoj.ca', Dmoj),
    ('facebook.com', Fhc),
]


def get_judge_class(problem_url):
    for url, JudgeClass in IDENTIFIERS:
        if url in problem_url:
            return JudgeClass
    return Judge


files = sys.argv[1:]
for filename in files:
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith(' * problem: '):
            problem_url = line[3:].split()[1].strip()
            break
    else:  # did not find the string " * problem: " in the file
        print(f'incompatible file {filename}; skipped')
        continue
    JudgeClass = get_judge_class(problem_url)
    JudgeClass.upload_solution(filename)
