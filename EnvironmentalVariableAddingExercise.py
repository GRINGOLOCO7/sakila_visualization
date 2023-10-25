import os

custom_message = os.getenv('CUSTOM_MESSAGE', 'Default Message')
print(custom_message)