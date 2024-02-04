from win10toast import ToastNotifier
#Exibir uma notificação pop-up no Windows 10
import datetime
#Obter informações de data e hora

#Representa a data e hora atuais
data = datetime.datetime.now()
data = str(data)
#Cria um objeto ToastNotifier que será usado para exibir notificações
toast = ToastNotifier()
#Exibe a notificação: título, conteúdo e duração
toast.show_toast("Atualização de data e hora", data, duration=5)