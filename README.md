# 📚 The Most Common Word

This project provides a Python function that identifies the most frequently occurring word in a given text and returns its count. It includes tests to validate its functionality, ensuring reliability and robustness.

## 🛠️ Features

- Extracts and counts words using **regular expressions** and Python's `Counter` class.
- Handles **case insensitivity**, **special characters**, and edge cases like empty text or ties.
- Fully tested with **pytest** and type-checked using **mypy**.


## 🔧 Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. To set up the environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:Kinetics20/the_most_common_word.git
   cd the_most_common_word
    ```

## Install Dependencies

To install Poetry, Mypy and Pytest on Linux or macOS, use the following command:

```bash
pipx install poetry
poetry add mypy
poetry add 'pytest==8.3.4'
```

## 🚀 Usage

The main function `most_common_word` analyzes a given text and returns the most frequent word.  
Example Code:

```python
from common_word import most_common_word

text = "Home is where I feel safe, but the house I grew up in will always be home to me."
result = most_common_word(text)
print(result)  # Output: ('home', 2)
```

## ✅ Tests

The project includes unit tests written using `pytest` to validate the function’s behavior.  
Run Tests:

```bash
pytest test_common_word.py -vv
```
### Test Results:

```bash
================================================================ test session starts =================================================================
platform linux -- Python 3.12.3, pytest-8.3.4
collected 6 items

test_common_word.py::test_most_common_word_basic PASSED                                                                                        
test_common_word.py::test_most_common_word_case_insensitivity PASSED                                                                           
test_common_word.py::test_most_common_word_empty_text PASSED                                                                                   
test_common_word.py::test_most_common_word_special_characters PASSED                                                                           
test_common_word.py::test_most_common_word_tie PASSED                                                                                          
test_common_word.py::test_most_common_word_single_word PASSED                                                                                  

================================================================= 6 passed in 0.02s ================================================================
```

## 🧪 Type Checking

Static typing was enforced with `mypy` for code clarity and safety.  
Run mypy:

```bash
mypy common_word.py
```
