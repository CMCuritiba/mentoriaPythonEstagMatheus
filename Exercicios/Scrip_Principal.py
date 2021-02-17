# Script para gerar dados de pedidos do serviço de informação ao cidadão (SIC)

import psycopg2
import csv
from time import sleep
from csv import reader
import paramiko
from scp import SCPClient
import sys

def header():
    print("==================================================================================")
    print("== Script para gerar dados de pedidos do serviço de informação ao cidadão (SIC) ==")
    print("==================================================================================")

# Conecxão com o Banco

con = psycopg2.connect (host = "cedro",
                        database = "pro",
                        user = "mgnt2020",#.format(user),
                        password = "camara")#.format(password))
cur = con.cursor()

def main():

    def sqla():
        query = """SELECT 
            sa.arq_id AS ID_ARQUIVO,
            sp.pro_id AS ID_PROPOSICAO,
            inf_id AS ID_INFORMACAO,
            to_char(sp.pro_protocolada, 'DD/MM/YYYY HH24:MI') AS Data,
            sp.pro_codigo AS CODIGO_ARQUIVO,
            sa.arq_tipo AS TIPO_ARQUIVO,
            html2text(sa.arq_nome) AS NOME_ARQUIVO,
            se.est_nome AS Situação                                                                              
            FROM spl.arquivo sa
            INNER JOIN spl.proposicao sp                                
            USING (pro_id)
            JOIN spl.estado se USING (est_id)                                       
            WHERE sp.pro_ano={}
            AND sp.tpr_id IN (118, 119)
            AND se.est_id BETWEEN 54 AND 59""".format(date)

        cur.execute(query)
        rows = cur.fetchall()             
                        
        with open('Arquivos.csv', 'w', newline="") as csv_file: 
            arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='|')    
            arquivocsv.writerow(rows)

    def sqlaa():
        querya = """SELECT 
            sa.arq_id AS ID_ARQUIVO,
            sp.pro_id AS ID_PROPOSICAO,
            inf_id AS ID_INFORMACAO,
            to_char(sp.pro_protocolada, 'DD/MM/YYYY HH24:MI') AS Data,
            sp.pro_codigo AS CODIGO_ARQUIVO,
            sa.arq_tipo AS TIPO_ARQUIVO,
            html2text(sa.arq_nome) AS NOME_ARQUIVO,
            se.est_nome AS Situação                                                                              
            FROM spl.arquivo sa
            INNER JOIN spl.proposicao sp                                
            USING (pro_id)
            JOIN spl.estado se USING (est_id)                                       
            WHERE sp.pro_ano={}
            AND sp.tpr_id IN (118, 119)""".format(date)

        cur.execute(querya)
        rows = cur.fetchall()             
                        
        with open('Arquivos.csv', 'w', newline="") as csv_file: 
            arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='|')    
            arquivocsv.writerow(rows)

                        
    def sqlp():
        query2 = """SELECT
        p.pro_id AS ProId,
        to_char(p.pro_protocolada, 'DD/MM/YYYY HH24:MI') AS Data,
        CASE t.tpr_id
            WHEN 118 THEN 'Pedido de Informação'
            WHEN 119 THEN 'Recurso'
        END AS Tipo,
        p.pro_codigo AS CodigoPedido,
        spl.codigo_proposicao(p.pro_id_alvo) AS CodigoRecurso,
        html2text(p.pro_sumula) AS Assunto,
        html2text(p.pro_texto) AS Texto,
        to_char(p.pro_ultimo_tramite, 'DD/MM/YYYY HH24:MI') AS DataEncerramento,
        e.est_nome AS Situação,
        '' AS ArquivoAnexo
    FROM spl.proposicao p
        JOIN spl.tipo_proposicao t ON 
            p.tpr_id = t.tpr_id
        JOIN spl.estado e USING (est_id)
    WHERE p.tpr_id IN (118, 119)
        AND pro_ano={}
        AND e.est_id BETWEEN 54 AND 59
    ORDER BY Data DESC""" .format(date)

        cur.execute(query2)
        rows = cur.fetchall()                
                    
        with open('Proposição.csv', 'w', newline="") as csv_file: 
            arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='|')    
            arquivocsv.writerow(rows)

    def sqlpp():
        pquery2 = """SELECT
        p.pro_id AS ProId,
        to_char(p.pro_protocolada, 'DD/MM/YYYY HH24:MI') AS Data,
        CASE t.tpr_id
            WHEN 118 THEN 'Pedido de Informação'
            WHEN 119 THEN 'Recurso'
        END AS Tipo,
        p.pro_codigo AS CodigoPedido,
        spl.codigo_proposicao(p.pro_id_alvo) AS CodigoRecurso,
        html2text(p.pro_sumula) AS Assunto,
        html2text(p.pro_texto) AS Texto,
        to_char(p.pro_ultimo_tramite, 'DD/MM/YYYY HH24:MI') AS DataEncerramento,
        e.est_nome AS Situação,
        '' AS ArquivoAnexo
    FROM spl.proposicao p
        JOIN spl.tipo_proposicao t ON 
            p.tpr_id = t.tpr_id
        JOIN spl.estado e USING (est_id)
    WHERE p.tpr_id IN (118, 119)
        AND pro_ano={}    
    ORDER BY Data DESC""" .format(date)    
        
        cur.execute(pquery2)
        rows = cur.fetchall()                
                        
        with open('Proposição.csv', 'w', newline="") as csv_file: 
            arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='|')    
            arquivocsv.writerow(rows)  

    def sqlif():
        query3 ="""SELECT
            p.pro_id AS ID,
            i.inf_id AS ID_INFORMAÇÃO,
            i.inf_final AS INFORMAÇÃO_FINAL,
            to_char(p.pro_data_final, 'DD/MM/YYYY HH24:MI') AS DATA_FINAL
            FROM spl.informacao i
            INNER JOIN spl.proposicao p
            JOIN spl.estado e USING (est_id)
            JOIN spl.tipo_proposicao t ON 
            p.tpr_id = t.tpr_id
            USING (pro_id)
            WHERE pro_ano={}
            AND p.tpr_id IN (118, 119)
            AND e.est_id BETWEEN 54 AND 59
            """.format(date)
                        
        cur.execute(query3)
        rows = cur.fetchall()                
                        
        with open('InformaçãoFinal.csv', 'w', newline="") as csv_file: 
            arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='|')   
            arquivocsv.writerow(rows)  

    def sqli():
        Iquery4 = """SELECT
                    p.pro_id, 
                    i.inf_id,                        
                    to_char(i.inf_data, 'DD/MM/YYYY HH24:MI') AS Informação_Data,
                    html2text(i.inf_texto) AS Informação_Texto,
                    html2text(p.pro_sumula) AS Assunto
                    FROM spl.informacao i
                    INNER JOIN spl.proposicao p 
                    JOIN spl.estado e USING (est_id)
                    JOIN spl.arquivo a USING(pro_id)
                    JOIN spl.tipo_proposicao t ON 
                    p.tpr_id = t.tpr_id
                    USING (pro_id)
                    WHERE pro_ano= {}
                    AND p.tpr_id IN (118, 119)
                    AND e.est_id BETWEEN 54 AND 59""".format(date)           

        cur.execute(Iquery4)
        rows = cur.fetchall()                
                        
        with open('Informação.csv', 'w', newline="") as csv_file: 
            arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='|')    
            arquivocsv.writerow(rows)   
    
    header()
    try:
        date = int(input('- Digite a data desejada para extração: '))        
        
        def arquivos():
            try: 
                print("==================================================================================")   
                print(" - Extrair arquivos anexos ?\n1 - Sim\n2 - Não")
                a = int(input())             
                
                if a == 1:
                    arquivos == True
                    sqla()                   
                    proposicao()

                elif a == 2:
                    arquivos == False                                                   
                    a = ()             
                    proposicao
                    sleep(1)
                    
                else:
                    print("==================================================================================") 
                    print("Digite uma opção válida..")
                    arquivos()
                    sleep(1)

            except ValueError:
                print("==================================================================================") 
                print("Digite uma opção válida..") 
                arquivos()
                sleep(1)            

        def proposicao(a):#Arrumar para receber duas funções e trabalhar
            try:
                print("==================================================================================")    
                print(" - Extrair somente pedidos \ recursos conclúidos ?\n1 - Sim\n2 - Não")
                p = int(input())

                if p == 1:
                    proposicao == True
                    sqlp()
                    informacao()

                elif p == 2:          
                    proposicao == False   
                    sqlpp()
                    informacao()
                                    
                           
                
                else:
                    print("==================================================================================")
                    print("Digite uma opção válida..")
                    proposicao()
                    sleep(1)
                                
                

                    
            except ValueError:
                print("==================================================================================")
                print("Digite uma opção válida..")
                
                sleep(1)
                       
                    
    
        def informacao() -> None:
            try:
                print("==================================================================================")    
                print(" - Extrair somente resposta final ?\n1 - Sim\n2 - Não")
                inf = int(input())     

                if inf == 1:
                    sqlif()                                        
                    print("FIM..")            
                    main()

                elif inf == 2:
                    sqli()                                                                                                
                    print("FIM..")
                    main()

                else:    
                    print("==================================================================================")
                    print("Digite uma opção válida..")
                    informacao()
                    sleep(1)
            except ValueError:
                print("==================================================================================")
                print("Digite uma opção válida..")
                informacao()
                sleep(1)     
            
        if date < 2018:
            print("==================================================================================")   
            print("Digite uma data válida..")
            main()
        else:
            arquivos()
          
        
    except ValueError:
        print("==================================================================================")
        print("Apenas números devem ser computados..")
        main()
        sleep(1)  
             
    cur.close()       
    con.close()

if __name__ == "__main__":   
    main()
