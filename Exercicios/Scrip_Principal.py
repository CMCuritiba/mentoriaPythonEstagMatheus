# Script para gerar dados de pedidos do serviço de informação ao cidadão (SIC)

import psycopg2
import csv
from time import sleep
from csv import reader
import paramiko
from scp import SCPClient
import sys

# CSV & execução da query
"""
cur.execute(variavél)
rows = cur.fetchall()                
                
with open('spl.proposicao.csv', 'w', newline="") as csv_file: 
    arquivocsv = csv.writer(csv_file)    
    arquivocsv.writerow(rows)            
    
                    
    cur.close()       
    con.close() 
""" 

def header():
    print("==================================================================================")
    print("== Script para gerar dados de pedidos do serviço de informação ao cidadão (SIC) ==")
    print("==================================================================================")

# Conecxão com o Banco
con = psycopg2.connect (host = "cedro",
                        database = "pro",
                        user = "mgnt2020",
                        password = "camara")
cur = con.cursor()
"""
def connectdb():

    try:
        print("- Digite seu usuário:")
        user = input()
        print("==================================================================================")
        print("- Digite sua senha:")
        password = input()
        print("==================================================================================")


        con = psycopg2.connect (host = "cedro",
                            database = "pro",
                            user = "{}".format(user),
                            password = "{}".format(password))#.format(senha))
        cur = con.cursor()
    except ValueError:
        print("- Senha e(ou usuários incorretos)")
        connectdb()
"""


#Conexão SSH 
def createSSHClient():
    
    host = "cedro,"
    port = "5432"
    username = "mgnt2020"
    password = "camara"
    
    command = "ls"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    sftp_client=ssh.open_sftp()

    sftp_client.get('/home/mgnt2020/Downloads/MyRepository-main/Python/Script/script_download.csv','script_downloaded_file.csv')

    sftp_client.close()
    ssh.close() 

def main():
    
    header()
    try:
        date = int(input('- Digite a data desejada para extração: '))   
    
        def arquivos() -> None:
            try:
                print("==================================================================================")    
                print(" - Extrair arquivos anexos ?\n1 - Sim\n2 - Não")
                arq = int(input())
                

                if arq == 1:
                    
                    Aquery = """SELECT 
                                sa.pro_id AS ID, pro_resposta_pmc,
                                html2text(arq_nome) AS NOME_ARQUIVO,
                                html2text(pro_texto) AS TEXTO, 
                                pro_observacao AS OBSERVAÇÃO, pro_envio_protocolo AS ENVIO_PROTOCOLO,
                                pro_protocolada AS PROTOCOLADA,
                                pro_ultimo_tramite AS Data_Encerramento 
                                FROM spl.proposicao sp
                                INNER JOIN spl.arquivo sa
                                USING (pro_id)                                
                                WHERE sp.pro_ano={}  AND sp.tpr_id IN (118, 119)""".format(date)                            
                    
                    cur.execute(Aquery)
                    rows = cur.fetchall()               
                                    
                    with open('Arquivos.csv', 'w', newline="") as csv_file: 
                        arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='\n')    
                        arquivocsv.writerow(rows)                                
                            
                    proposicao()       

                elif arq == 2:                     
                    proposicao()
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

        def proposicao() -> None:
            
            try:
                print("==================================================================================")    
                print(" - Extrair somente pedidos \ recursos conclúidos ?\n1 - Sim\n2 - Não")
                prop = int(input())

                if prop == 1:
                    
                    Pquery = """SELECT
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
                    
                    cur.execute(Pquery)
                    rows = cur.fetchall()                
                                    
                    with open('Proposicao.csv', 'w', newline="") as csv_file: 
                        arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='\n')    
                        arquivocsv.writerow(rows)                                         
                

                    informacao()

                elif prop == 2:
                    informacao()

                else:
                    print("==================================================================================")
                    print("Digite uma opção válida..")
                    proposicao()
                    sleep(1) 
            except ValueError:
                print("==================================================================================")
                print("Digite uma opção válida..")
                proposicao()
                sleep(1)

                     
        
        def informacao() -> None:
            try:
                print("==================================================================================")    
                print(" - Extrair somente resposta final ?\n1 - Sim\n2 - Não")
                inf = int(input())     

                if inf == 1:

                    Iquery ="""SELECT 
                                i.inf_id,
                                html2text(i.inf_texto) AS Informação_Texto,
                                i.inf_data AS Informação_Data,
                                p.pro_resposta_pmc AS Resposta
                                FROM spl.informacao i
                                INNER JOIN spl.proposicao p 
                                JOIN spl.estado e USING (est_id)
                                JOIN spl.tipo_proposicao t ON 
                                    p.tpr_id = t.tpr_id
                                USING (pro_id)
                                WHERE pro_ano BETWEEN 2019 AND 2021
                                AND p.tpr_id IN (118, 119)
                                AND e.est_id BETWEEN 54 AND 59
                                """        
                    
                    cur.execute(Iquery)
                    rows = cur.fetchall()                
                                    
                    with open('InformaçãoFinal.csv', 'w', newline="") as csv_file: 
                        arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='\n')   
                        arquivocsv.writerow(rows)      
                                                    
                    
                    print("FIM..")            
                    main()

                elif inf == 2:
                    
                    Iquery2 = """SELECT * FROM spl.informacao limit 2"""        
                    
                    cur.execute(Iquery2)
                    rows = cur.fetchall()                
                                    
                    with open('Informação.csv', 'w', newline="") as csv_file: 
                        arquivocsv = csv.writer(csv_file, delimiter='\n', quotechar='\n')     
                        arquivocsv.writerow(rows)            
                                                        
                    cur.close()       
                    con.close()
                    
                    print("FIM..")

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

        arquivos()  
    except ValueError:
        print("==================================================================================")
        print("Digite uma opção válida..")
        main()
        sleep(1)  
             
     

if __name__ == "__main__":   
    main()

