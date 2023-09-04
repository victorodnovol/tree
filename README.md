# Tree

## Description

A simple script for listing folder contents as a tree structure. It has functionality similar to the `tree` command in linux
You may also use CLI options to make script execute system command or check access rights of an object like `stat` command

## Usage

    python tree.py [OPTIONS] [PATH]
    Run the script with selected parameter and `home` path
    Follow the prompts to select the path for processing
    Type `exit` when you're done

## Features

    Recursively traverses the specified folder and its subfolders
    Generates a tree structure based on the file names and directories
    Outputs the tree in a human-readable format
    Checks access rights of an given object
    Executes `bash` requested command on given path
    Generated trees are auto-saved to current folder as a text files

## Options

    -h, --help: Displays help message
    -s, `path`, execute shell command at `path`
    -c, `path`, check access rights of an object at `path`
    -t, `path`, show folder contents at given `path` as a tree

## Examples

Set current working directory to PWD and generate a tree for a user-prompted folder:

    bash $ python tree.py -t .

Set current working directory to `/path/to/directory` and ask user for a subfolder to generate a tree:

    bash $ python tree.py -t /path/to/directory

Set current working directory to `~/cats/names` and ask user for a command to execute:

    bash $ python tree.py -s ~/cats/names

Set current working directory to `~/cats/pictures` and ask user for an object to check:

    bash $ python tree.py -c ~/cats/pictures

## Contributing

Pull requests and issues are welcome! To contribute, fork the repository, make your changes, and submit a pull request.

## License

MIT License

Copyright (c) 2023 Victor Odnovol

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
This license allows anyone to use, modify, and distribute the software freely, as long as they include the copyright and license notice in their copies. The license also prohibits the use of the software in any way that is harmful or unethical.
