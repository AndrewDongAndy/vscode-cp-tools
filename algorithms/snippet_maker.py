"""
For creating the snippets file.

This script doesn't care about the formatting (e.g. tabs) of the output file.
"""

import os

# directories to ignore when making snippets
IGNORE_DIRS = [
    'unfinished',
]

# files to write JSON to
OUTPUT_FILES = [
    # 'snippets.json',
    os.path.join('..', '.vscode', 'algorithms.code-snippets'),
]

# order might matter
REPLACEMENTS = [
    ('\\', '\\\\'),
    ('"', '\\"'),
]


def render_snippet(snippet: str, tab_trigger: str, description: str, scope='cpp') -> str:
    for old, new in REPLACEMENTS:
        snippet = snippet.replace(old, new)
    separated = snippet.split('\n')
    while separated[-1] == '':
        separated.pop()
    result = ','.join(f'"{s}"' for s in separated)
    return f'''
    "{description}": {{
        "scope": "{scope}",
        "prefix": "{tab_trigger}",
        "body": [{result}],
        "description": "{description}",
    }}
    '''
    # note: `"scope": "cpp"` is hard-coded!


def main():

    snippet_strings: list[str] = []
    for subdir, dirs, files in os.walk('.'):
        for filename in files:
            if filename == os.path.basename(__file__):
                # don't make this script file into a snippet!
                continue

            filename_no_ext, ext = os.path.splitext(filename)
            if ext != '.cpp':
                continue

            # if the subdirectory contains any of the IGNORE_DIRS as a substring,
            # don't process this file
            if any(subdir.find(ignore_dir) != -1 for ignore_dir in IGNORE_DIRS):
                continue

            trigger = filename_no_ext.replace('_', '').lower()
            description = filename_no_ext.replace('_', ' ').title()

            filepath = subdir + os.sep + filename
            with open(filepath) as g:
                snippet = g.read()  # read whole snippet

                # check for tabs
                if snippet.find('\t') != -1:
                    print(f'file includes tabs: {filename}')
                    snippet = snippet.replace('\t', '  ')  # code indentation

                result = render_snippet(snippet, trigger, description)
                snippet_strings.append(result)


    all_snippets = ','.join(snippet_strings)
    output = f'{{{all_snippets}}}'

    for filename in OUTPUT_FILES:
        with open(filename, 'w') as f:
            f.write(output)


if __name__ == '__main__':
    main()
