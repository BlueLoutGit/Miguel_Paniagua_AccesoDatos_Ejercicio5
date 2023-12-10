import subprocess


class JVDBClient:
    def __init__(self, exe_path = 'jvdb.exe'):
        # Obtener la ruta del ejecutable desde las variables de entorno
        self.exe_path = exe_path

    def insert(self, basededatos, collection, nombrearchivo, contenido):
        command  = f'{self.exe_path} insert "{basededatos}" "{collection}" "{nombrearchivo}" "{contenido}"'
        response = subprocess.run(command, shell=True)
        if response.returncode == 0:
            print('OK')
            return True
        else:
            print('KO')
            return False

    def select_file(self, basededatos, collection, nombrearchivo):
        command  = f'{self.exe_path} selectFile "{basededatos}" "{collection}" "{nombrearchivo}"'
        response = subprocess.run(command, shell=True)
        if response.returncode == 0:
            print('OK')
            return True
        else:
            print('KO')
            return False

    def select_collection(self, basededatos, collection):
        command  = f'{self.exe_path} selectCollection "{basededatos}" "{collection}"'
        response = subprocess.run(command, shell=True)
        if response.returncode == 0:
            print('OK')
            return True
        else:
            print('KO')
            return False
