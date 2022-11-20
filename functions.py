import time,sys,os

def normalize(value,old_min,old_max,new_min,new_max):
    return new_min + (new_max - new_min) * ((value - old_min) / (int(old_max) - int(old_min)))

def read(dictionary_key):
    return str(dictionary_key).strip("[']")

def exit_program(message):
    print(message)
    os._exit(1)
