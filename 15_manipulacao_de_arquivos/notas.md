    write --> só aceita string

    conteudo = arquivo.write('\n'.join(alunos_com_virgula)) 

    JOIN --> juntou a lista ALUNOS_COM_VIRGULA em uma string só separando cada nome por lista usando o '\n' para quebrar a linha
caso queira pode separar por ',' somente trocando por '\n', ou seja: conteudo = arquivo.write(','.join(alunos_com_virgula)) 