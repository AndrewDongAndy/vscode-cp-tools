# vscode-cp-workspace
A set of VSCode-integrated tools for competitive programmers.

## Functionality
VSCode Competitive Programming Tools enables users to:
- Easily test C++ solutions concurrently to find bugs more quickly
- Manage algorithm snippets for importing in solutions (currently only supports C++ snippets)
- Quickly create contest files with a default template and downloading sample input
- Upload solutions to your GitHub repository

## Prerequisites
You must have:
- a version of Python compatible with Python 3.9.6; and
- the [multi-command](https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command) VSCode extension.

## Usage

Note: to add a (global) keybinding to VSCode, use `Ctrl+Shift+P` and search for "Open Keyboard Shortcuts (JSON)". Of course, you may change the hotkeys shown here to whichever hotkey combination you prefer.

Add the following keybindings to your `keybindings.json`:
```
{
  "key": "alt+s",
  "command": "cp.buildAndRun",
  "when": "editorTextFocus && resourceExtname == .cpp",
},
{
  "key": "alt+t",
  "command": "editor.action.insertSnippet",
  "when": "editorTextFocus && resourceExtname == .cpp",
},
{
  "key": "alt+u",
  "command": "cp.upload",
  "when": "editorTextFocus",
},
```

### New File Creation
In the command line, run `python make_files.py -h` to view the arguments you can use. The currently supported judges are:
<!-- TODO: add links -->
- AtCoder
- Baekjoon Online Judge
- Codeforces
- Don Mills Online Judge
- Facebook Hacker Cup

Currently, downloading sample input only works for AtCoder, Baekjoon Online Judge, and Codeforces. Moreover, downloading data from protected pages, such as AtCoder problems during a contest, is not supported.

### Program Execution
- For convenience, add the following keybinding:
  - If your default terminal is not set to Command Prompt, you will need to modify the `cp.buildAndRun` command in the `.vscode/settings.json` file.
- To run your code, press alt+s in a solution file.

### Book Code
- Place book code in the `algorithms/` directory. It is fine to organize by folders within `algorithms/`.
- Compile the `.vscode/algorithms.code-snippets` file by running the `snippet_maker.py` file in the `algorithms/` directory.
  - Re-run the `snippet_maker.py` script each time book code is added, modified, or removed.
- With your cursor in a solution file, use the hotkey (alt+t by default). You will see a searchable menu of all VSCode snippets you defined in the `algorithms/` directory.

#### Advanced Usage
- For extra productivity, you can add VSCode snippet-specific "code" in your book code .cpp files such as tabstops, placeholders, choices, and variables. Read more about these constructs [here](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_snippet-syntax).

### Uploading Files
- Create a `.env` file under the `cp_helper` directory and add your `GITHUB_USERNAME` and a `GITHUB_TOKEN`. For example:
```
GITHUB_USERNAME=AndrewDongAndy
GITHUB_TOKEN=ghp_arandomstringofletters
```
- The upload destination for each judge can be configured in each judge file under `cp_helper/judges`.

## TODO
- Make VSCode CP Tools work with any language
