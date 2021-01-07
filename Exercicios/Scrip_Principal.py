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

"""
header()
print("Digite seu login:")
login = input()
print("==================================================================================")
print("Digite sua senha:")
senha = input()
"""

# Conecxão com o Banco
con = psycopg2.connect (host = "cedro",
                        database = "pro",
                        user = "mgnt2020",
                        password = "camara")#.format(senha))
cur = con.cursor()

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
    date = int(input('- Digite a data desejada para extração: '))    
       
    def arquivos():

        print("==================================================================================")    
        print(" - Extrair arquivos anexos ?\n1 - Sim\n2 - Não")
        arq = int(input())

        if arq == 1:
            
            Aquery = """SELECT arq_nome, arq_tipo, pro_ultimo_tramite
                        FROM spl.arquivo
                        CROSS JOIN spl.proposicao
                        WHERE spl.proposicao.pro_ano={}""".format(date)
                    
            
            cur.execute(Aquery)
            rows = cur.fetchall()               
                            
            with open('Arquivos.csv', 'w', newline="") as csv_file: 
                arquivocsv = csv.writer(csv_file)    
                arquivocsv.writerow(rows)                                
                      
            proposicao()       

        elif arq == 2:
            proposicao()
        else:
            print("==================================================================================")
            print("Digite uma opção válida..") 
            arquivos()
            sleep(1)

    def proposicao():

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
                arquivocsv = csv.writer(csv_file)    
                arquivocsv.writerow(rows)                                         
        

            informacao()

        elif prop == 2:
            informacao()

        else:
            print("==================================================================================")
            print("Digite uma opção válida..")
            proposicao()
            sleep(1)          
    
    def informacao():
        print("==================================================================================")    
        print(" - Extrair somente resposta final ?\n1 - Sim\n2 - Não")
        inf = int(input())     

        if inf == 1:

            Iquery ="""SELECT * FROM spl.apoio limit 3"""        
            
            cur.execute(Iquery)
            rows = cur.fetchall()                
                            
            with open('InformaçãoFinal.csv', 'w', newline="") as csv_file: 
                arquivocsv = csv.writer(csv_file)    
                arquivocsv.writerow(rows)      
                                            
            
            print("FIM..")            
            main()

        elif inf == 2:
            
            Iquery2 = """SELECT * FROM spl.informacao limit 2"""        
            
            cur.execute(Iquery2)
            rows = cur.fetchall()                
                            
            with open('Informação.csv', 'w', newline="") as csv_file: 
                arquivocsv = csv.writer(csv_file)    
                arquivocsv.writerow(rows)            
                                                
            cur.close()       
            con.close()
            
            print("FIM..")
            main()
        else:    
            print("==================================================================================")
            print("Digite uma opção válida..")
            return informacao()
            sleep(1)

    arquivos()           
     

if __name__ == "__main__":        
    main()
