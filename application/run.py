from config.DBConfig import DBConfig  # Importa a configuração do banco de dados
from controller.exame_controller import ExameController
from controller.paciente_controller import PacienteController
from controller.medico_controller import MedicoController
from view.Interface_Usuario import InterfaceUsuario
from view.splash_screen import SplashScreen
import time

if __name__ == "__main__":
    # Criação do SplashScreen e exibição inicial
    splash_screen = SplashScreen()
    print(splash_screen.get_updated_screen())  # Exibe o SplashScreen inicial
    time.sleep(4)  # Pausa para exibir o SplashScreen por 4 segundos

    # Criação da conexão com o banco de dados usando a classe DBConfig
    db_config = DBConfig()  # Instancia a classe DBConfig
    db = db_config.get_db()  # Obtém a conexão com o banco de dados

    # Criação dos controladores, passando a conexão com o banco de dados
    exame_controller = ExameController(db)  # Passa db para o controlador
    paciente_controller = PacienteController(db)  # Passa db para o controlador

    # Passa db e exame_controller ao criar o MedicoController
    # Passa db e exame_controller para o controlador
    medico_controller = MedicoController(db, exame_controller)

    # Instância a Interface do Usuário com os controladores e o SplashScreen
    interface_usuario = InterfaceUsuario(
        exame_controller, paciente_controller, medico_controller, splash_screen)

    # Inicia o menu principal
    interface_usuario.menu_principal()
