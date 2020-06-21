"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
download = float(input('Informe o tamanho do Download em (MB):\n'))
link = float(input('Informe o tamnho do link de internet em (Mbps):\n'))

taxa = link / 8
velocidade = download / taxa

if velocidade >= 60:
    print('Seu download terminar em {:.2f} Minutos.'.format(velocidade / 60))
else:
    print('Seu download terminar em {:.2f} Segundos.'.format(velocidade))



