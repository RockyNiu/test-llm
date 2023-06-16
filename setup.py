from pathlib import Path
from setuptools import setup, find_packages


NAME = 'test-llm'
DESCRIPTION = 'A repo to test LLM'

URL = 'https://github.com/RockyNiu/test-llm'
AUTHOR = 'Lei Niu'
EMAIL = 'lei.niu.ny@gmail.com'
REQUIRES_PYTHON = '>=3.9.0'

for line in open('__init__.py'):
    line = line.strip()
    if '__version__' in line:
        context = {}
        exec(line, context)
        VERSION = context['__version__']

HERE = Path(__file__).parent

try:
    with open(HERE / "README.md", encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

REQUIRED = [i.strip() for i in open(HERE / 'requirements.txt') if not i.startswith('#')]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author_email=EMAIL,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    url=URL,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
)
