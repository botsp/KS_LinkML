import os
import sys

def serve():
    os.system(r'C:\Users\kevin\AppData\Local\Programs\Python\Python312\Scripts\mkdocs.exe serve')

def build():
    os.system(r'C:\Users\kevin\AppData\Local\Programs\Python\Python312\Scripts\mkdocs.exe build')

def deploy():
    os.system(r'C:\Users\kevin\AppData\Local\Programs\Python\Python312\Scripts\mkdocs.exe gh-deploy')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build.py [serve|build|deploy]")
    else:
        command = sys.argv[1]
        if command == "serve":
            serve()
        elif command == "build":
            build()
        elif command == "deploy":
            deploy()
        else:
            print(f"Unknown command: {command}")