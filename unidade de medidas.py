valor = float(input("Digite um valor para converter: "))
medidas = str(input('escolha uma das medida:'  ' milhas '  ' polegadas '  ' pes '  ' metros '  ' quilometros '  ' centimetros : '))

if medidas==('milhas'):
    print("O valor de milhas para polegadas é",valor*63360, "para pes é", valor*5280, 'para metros é' ,valor*1609, 'em quilometros é',valor*1.609,"e em  centimetros é",valor*160900, '.' )
elif medidas==('polegadas'):  
    print('O valor de polegadas para milhas é',valor/63360, 'para pes é', valor/12, 'para metros é' ,valor/39.37, 'em quilometros é',valor/39370,"e em  centimetros é",valor*2.54, '.' )
elif medidas==('pes'):
    print('O valor de pes para milhas é',valor/5280, 'para polegada é',valor*12, 'para metros é aproximadamente',valor/3.281,'em quilometros é',valor/3281,'e em centimetros é',valor*30.48, '.')
elif medidas==('metros'):
    print('O valor de metros para milhas é aproximadamente ',valor/1609, 'para polegadas é',valor*39.37, 'para pes é aproximadamente',valor*3.281, 'em quilometro é',valor/1000,'e em centimetros',valor*100,'.') 
elif medidas==('quilometros'):
    print("O valor de quilometros para milhas é aproximadamente",valor/1,609, 'para polegada é aproximadamente',valor*39370,'para pes é',valor*3281, 'em metros é',valor*1000,'e em centimetros é',valor*100000, '.')
elif medidas==('centimetros'):
    print("O valor de centimetros para milhas é aproximadamente",valor/160900, 'para polegadas é ',valor/2.54,'para pes é ',valor/30.48,'em metros é',valor/100, 'e em quilometros',valor/100000,'.')
else: 
    print("Impossivel realizar alguma coversão veja se você utilizou alguma unidade errada")