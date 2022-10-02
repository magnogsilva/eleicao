cont_x = 0
cont_y = 0
cont_z = 0
branco = 0
nulo = 0
#votacao = False
escolha = False
print('='*12,'Início da Votação','='*12)
print('Suas opções são:')
while escolha == False:
    votacao = False
    while votacao == False:
        try:
            print('Candidato_X => 889','\nCandidato_Y => 847','\nCandidato_Z => 515','\nBranco => 0')
            voto = int(input('Digite o número do candidato da sua escolha: '))
            if voto == 889:
                cont_x += 1 
                votacao = True           
            elif voto == 847:
                cont_y += 1 
                votacao = True          
            elif voto == 515:
                cont_z += 1 
                votacao = True        
            elif voto == 0:
                branco += 1 
                votacao = True          
            else:
                nulo += 1
                votacao = True                       
        except:
            print('='*25)
            print('CANDIDATO INEXISTENTE!','\nVote novamente.')
            votacao = False
            print('='*25)
    print('='*25)
    print('Deseja finalizar a votação?')
    print('[Sim] => 1','\n[Não] => 2')
    escolha = int(input('Resposta: '))
    if escolha == 1:
        escolha = True
        votacao = True
    else:
        escolha = False
        votacao = False        
if cont_x > cont_y and cont_x > cont_z:
    vencedor = 'Candidato_x'
    mais_votos = cont_x
elif cont_y > cont_x and cont_y > cont_z:
    vencedor = 'Candidato_y'
    mais_votos = cont_y
elif cont_z > cont_x and cont_z > cont_y:
    vencedor = 'Candidato_z'
    mais_votos = cont_z
else:
    vencedor = 'empate'
br_nu = branco + nulo
print('='*25)
print('VENCEDOR')
if vencedor == 'empate':
    print('Houve um EMPATE!')
else:
    print('{} com {} voto(s).'.format(vencedor, mais_votos))
print('='*25)
print('RESULTADO FINAL DOS VOTOS')
print('='*25)
print('Candidato_x = {} voto(s).'.format(cont_x))
print('Candidato_y = {} voto(s).'.format(cont_y))
print('Candidato_z = {} voto(s).'.format(cont_z))
print('Brancos e Nulos = {} voto(s).'.format(br_nu))
