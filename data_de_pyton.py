import locale
from datetime import datetime, timedelta

# Define o locale para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Data em formato string
data_str = "2 de julho de 2025"

# Converte para datetime.date
data_verificar = datetime.strptime(data_str, "%d de %B de %Y").date()


data_base = datetime.now().date()


inicio = data_base
fim = data_base + timedelta(days=2)

# Verificação
if inicio <= data_verificar <= fim:
    print("A data está dentro do intervalo de 2 dias.")
else:
    print("A data está fora do intervalo de 2 dias.")

# Para visualização
print(f"Hoje: {data_base}, Intervalo: {inicio} até {fim}, Data a verificar: {data_verificar}")
