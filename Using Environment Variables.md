# Environment Variable - dotenv package

- To work with environment variables, use the `python-dotenv` package. Here's the [link to docs](https://pypi.org/project/python-dotenv/).

- It reads the key-value pairs from a `.env` file and sets them as environment variables. To do this, we call the `load_env()` function.

- To access the environment variables, we use `os` module, which has a method: `os.environ.get('ENV_VAR_NAME')`.

- Here a sample `.env` file:

```
API_KEY="FOO"
DB_PASSWORD="BAR"
SECRET_KEY="fizzBuzz"
```

- In the python script, you would need to write the following code:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# accessing environment variables
print(os.environ.get('SECRET_KEY'))

```

- By default, the `.env` file has to be in the same directory as the script using the above code. You can use a `.env` file from a different directory as well, refer to the documentation or do a stackoverflow search.