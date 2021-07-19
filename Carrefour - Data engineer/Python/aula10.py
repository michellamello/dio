#Manipulação de datas e horários

from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = print(data_atual.strftime('%a, %d/%m/%Y'))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))


def trabalhando_com_datetime():
    data_horario = datetime.now()
    print(data_horario.strftime('%d/%m/%y %H:%M:%S'))
    print(data_horario.day)
    print(data_horario.year)
    print(data_horario.hour)
    print(data_horario.minute)
    print(data_horario.date())
    print(data_horario.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_horario.weekday()])
    data_criada = datetime(1986, 2, 6, 15, 30, 20)
    print(data_criada)
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)

    nova_data = data_convertida - timedelta(days=365, hours=10, minutes=15)

    print(nova_data)

trabalhando_com_date()
trabalhando_com_time()
trabalhando_com_datetime()
