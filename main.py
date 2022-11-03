import os
from Class.classExample import classExample
from dotenv import load_dotenv

load_dotenv()

#!Utilize a externsão better comments para esses comentarios
#* Exemplo 2
#? Exemplo 3
#TODO Exemplo 4 

if __name__ == "__main__":
    print(os.getenv("VARIABLE"))
    object = classExample(1)
    object.consoleParam()