"""
A script for making the program directories and files for a
variety of different contests.
"""


from argparse import ArgumentParser

from cp_helper.judges.judge import Judge
from cp_helper.judges.atcoder import AtCoder
from cp_helper.judges.boj import Boj
from cp_helper.judges.codeforces import Codeforces
from cp_helper.judges.dmoj import Dmoj
from cp_helper.judges.fhc import Fhc


judges = dict(
    ac=AtCoder,
    boj=Boj,
    cf=Codeforces,
    dmoj=Dmoj,
    fhc=Fhc,
)

parser = ArgumentParser(description='Make files for Competitive Programming.')
parser.add_argument(
    '-j', '--judge',
    help='the judge to make files for',
    choices=judges.keys(),
    type=str.lower,
)
parser.add_argument(
    '-c', '--contest',
    help='set contest prefix',
    type=str,
)
parser.add_argument(
    '-n',
    help='the number of files to make',
    dest='count',
    type=int,
)
parser.add_argument(
    '-s', '--suffixes',
    help='the suffixes, separated by commas',
    type=str,
)
parser.add_argument(
    '-p', '--problem',
    help='make one file, e.g. for solving out of a contest',
    type=str,
)
# parser.add_argument(
#     '-r', '--range',
#     help='make a range of problems',
#     type=str,
# )

args = parser.parse_args()

try:
    JudgeClass = judges[args.judge]
except KeyError:
    JudgeClass = Judge
# print(JudgeClass)

if args.contest:
    if hasattr(JudgeClass, 'download_contest'):
        JudgeClass.download_contest(args.contest)
    elif args.count is not None:
        JudgeClass.make_contest_files(args.contest, num_problems=args.count)
    else:
        assert args.suffixes is not None
        suffixes = args.suffixes.split(',')
        JudgeClass.make_contest_files(
            args.contest, problem_id_suffixes=suffixes)
else:
    assert args.problem is not None
    JudgeClass.write_template(args.problem)
