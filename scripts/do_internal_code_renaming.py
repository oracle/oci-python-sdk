# USER_INFO in src/oraclebmc/base_client.py should be "Oracle-PythonSDK/{}-bmc".format(__version__)
# but when we copy the file from src/oci it is "Oracle-PythonSDK/{}".format(__version__)

with open('oraclebmc/src/oraclebmc/base_client.py', 'r') as f:
    original_content = f.read()

new_content = original_content.replace('"Oracle-PythonSDK/{}".format(__version__)', '"Oracle-PythonSDK/{}-bmc".format(__version__)')

with open('oraclebmc/src/oraclebmc/base_client.py', 'w') as f:
    f.write(new_content)