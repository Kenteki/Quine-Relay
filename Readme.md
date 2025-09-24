# Ouroboros Quine-relay
This repository contains a **3-language (Python → Ruby → Lua → Python)** Ouroboros Quine-relay.

The repository was created as a task for an internship at the company **Itransition**.

## What is a Quine?
A quine is a computer program that takes no input and produces a copy of its own source code as its only output.  
The standard terms for these programs in computability theory and computer science literature are "self-replicating programs", "self-reproducing programs", and "self-copying programs".  

Source: [Wikipedia](https://en.wikipedia.org/wiki/Quine_(computing)).

## Requirements

To execute this repository, you need the following pre-installed libraries:

 ```
Python <sup>3.13.7</sup>
Ruby <sup>3.4.6</sup>
Lua <sup>5.1.5</sup>
 ```

## Installation

### For Windows

Get Python from the official [website](https://www.python.org/downloads/windows/)  
Get Ruby from the official [website](https://rubyinstaller.org/)  
Get LuaBinaries from the official [website](https://luabinaries.sourceforge.net/)  

Don't forget to **add .exe to PATH** in Windows environment variables.  
You can also check in PowerShell if everything is installed correctly:

```
python --version
ruby --version
lua -v
```

After each command, you should receive a response with your current version.

### For Linux

Use the following commands in Bash:

```
sudo apt update
sudo apt install python3.13 python3.13-venv python3-pip
sudo apt install ruby-full
sudo apt install lua5.1
```

After that, check the versions to make sure everything is installed properly:

```
python3 --version
ruby --version
lua -v
```


# Execution

## Powershell:

```
python scipt.py > script.rb
ruby script.rb > script.lua
lua script.lua > answer.py
```

As a result, the final output file will be identical to the first file.  
To check differences, you can use the `diff` tool:

> diff script.py answer.py

If PowerShell outputs nothing, it means the files are identical (byte-to-byte).

**Note:** Windows by default saves files with encoding **UTF-16 with BOM**, which some execution libraries do not support.  
To avoid this, it is recommended to save output files with an additional parameter:

> | Out-File -FilePath filename -Encoding utf8NoBOM

Where `filename` is the file name with the required extension.  

Example:

> py test.py | Out-File -FilePath filename -Encoding utf8NoBOM

## Bash:

Execution is the same as in PowerShell:

```
python scipt.py > script.rb
ruby script.rb > script.lua
lua script.lua > answer.py
```

To compare files:

> diff script.py answer.py


# How the program works

The array **data** contains the template of code for each language.  
Then, a few `for` loops take specific lines in the array using variables **a, b, c, sep**:  

- **a, b, c** — define the range of elements in the array  
- **sep** — ASCII code of the separator symbol (",")  

Variables **q, space, separator** contain ASCII codes for quotes, space, and separators.  
Through loops, the program generates the next required code and inserts separators, spaces, and quotes accordingly.

# Documentation and Additional Information

## Additional Information

The **test** folder in the repository contains output files so you can check them without manually downloading and executing the program.  

Video demonstration: [streamable](https://streamable.com/rqlay4)

## Documentation

- [Wikipedia](https://drcabana.org/)
- [Drcabana](https://drcabana.org/)
- [Esoteric.codes](https://esoteric.codes/blog/the-128-language-quine-relay/)