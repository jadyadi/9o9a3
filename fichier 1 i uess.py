[build-system]
requires = ["setuptools>=45", "setuptools_scm[toml]>=6.2", "sip>=6.7.0"]
build-backend = "setuptools.build_meta"

[project]
name = "Assistant Personnel"
version = "0.1.41"
authors = [
    {name = "Jad, Saad", email = "jadelayadi54@gmail.com, mhanisaad95@gmail.com"},
]
description = "Assistant personnel de Jad et Saad"
readme = "README.md" # j'ai pas encore fait le readme
requires-python = ">=3.9"
classifiers = [
    "Development Status :: version finale",,
    "Systeme d'exploitation : windows",
    "Language de programmation :: Python :: 3",
    "Language de programmation :: Python :: 3.9",
    "Language de programmation :: Python :: 3.10",
    "Language de programmation :: Python :: 3.11",
    "Language de programmation :: Python :: 3.12",
]
dependencies = [
    "numpy==1.26.4",
    "PyQt5==5.15.11",
    "SpeechRecognition==3.10.4",
    "markdown==3.7",
    "pynput==1.7.7",
    "llama-cpp-python==0.3.1",
    "huggingface_hub==0.25.1",
    "openwakeword==0.6.0",
    "pyinstaller==6.10.0",
    "ffmpeg-python==0.2.0",
    "llama-index-core==0.12.0",
    "llama-index-readers-file==0.4.0",
    "llama-index-embeddings-huggingface==0.4.0",
    "docx2txt==0.8",
    "mistune==3.0.2",
    "paddlepaddle==2.6.2",
    "paddleocr==2.9.1",
    "whispercpp "
]
dynamic = []

[project.urls]
[project.scripts]
assistant-personnel = "assistant-personnel.main:main"

[tool.setuptools_scm]
write_to = "assistant-personnel/_version.py"

[tool.setuptools.packages.find]
where = ["."]
include = ["assistant-personnel*"]
exclude = ["tests*"]

[tool.setuptools.package-data]
"assistant-personnel.resources" = ["*.png", "*.onnx"]


[tool.black]
line-length = 100
target-version = ['py37']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''

[tool.pylint.master]
ignore-patterns = ["test_.*?py"]

[tool.pylint.format]
max-line-length = 100

[tool.pylint.messages_control]
disable = [
    "C0114",  # missing-module-docstring
    "C0116",  # missing-function-docstring
    "C0103",  # invalid-name
    "W0611",  # unused-import
    "W0612",  # unused-variable
    "W0613",  # unused-argument
    "W0621",  # redefined-outer-name
    "W0622",  # redefined-builtin
    "W0703",  # broad-except
    "R0801",  # duplicate-code
    "R0902",  # too-many-instance-attributes
    "R0903",  # too-few-public-methods
    "R0904",  # too-many-public-methods
    "R0913",  # too-many-arguments
]