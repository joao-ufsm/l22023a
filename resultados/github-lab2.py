import requests
import base64
import json
import csv
import sys
from datetime import datetime, timezone
import logging
import os
import subprocess
import shutil
from dotenv import load_dotenv

# oclint  --enable-clang-static-analyzer  -report-type html  t2.cpp  -- -Wall -g|sed 's:/home/jvlima/UFSM/l22023a/resultados/download/::g' > report.html


load_dotenv()

GITHUB_USER = os.getenv('GITHUB_USER')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

devoBaixar = True

geraComNomes = False

trabalhos = {
        "t1": {
                "dir": "T1",
                "finalizado": True,
                "github": "t1-grades-1680578092.csv",
                "data": datetime(2023, 4, 6, 23, 55).astimezone(tz=None),
                "testa": True,
                "entrada": "lados.in",
                "fonte": ["../../../entradas/t1/lados.in"],
                "resposta": "./entradas/t1/lados.out",
                "cols": 7
        },
        "t2": {
                "dir": "T2",
                "finalizado": True,
                "github": "t2-grades-1681390867.csv",
                "data": datetime(2023, 4, 14, 23, 55).astimezone(tz=None),
                "testa": True,
                "entrada": "campo.in",
                "fonte": ["../../../entradas/t2/campo.in"],
                "resposta": "./entradas/t2/campo.out",
                "valgrind": True,
                "cols": 8
        },
        "t3": {
                "dir": "T3",
                "finalizado": True,
                "github": "t3-grades-1681819942.csv",
                "data": datetime(2023, 4, 20, 23, 55).astimezone(tz=None),
                "testa": True,
                "entrada": "cartas.in",
                "fonte": ["../../../entradas/t3/cartas.in"],
                "resposta": "./entradas/t3/cartas.out",
                "valgrind": True,
                "cols": 8
        },
        "t4": {
                "dir": "T4",
                "finalizado": True,
                "github": "t4-grades-1682864320.csv",
                "data": datetime(2023, 5, 2, 23, 55).astimezone(tz=None),
                "testa": True,
                "entrada": "prev.in",
                "fonte": ["../../../entradas/t4/prev.in"],
                "resposta": "./entradas/t4/prev.out",
                "valgrind": True,
                "cols": 8
        },
        "t5": {
                "dir": "T5",
                "finalizado": True,
                "github": "t5-grades-1683166930.csv",
                "data": datetime(2023, 5, 9, 23, 55).astimezone(tz=None),
                "testa": True,
                "entrada": "teste1.in",
                "fonte": ["../../../entradas/t5/teste1.in"],
                "resposta": "./entradas/t5/teste1.out",
                "valgrind": True,
                "cols": 8
        },                                      
        "t6": {
                "dir": "T6",
                "finalizado": True,
                "github": "t6-grades-1684202711.csv",
                "data": datetime(2023, 5, 25, 23, 55).astimezone(tz=None),
                "testa": True,
                #"entrada": "teste1.in",
                #"fonte": ["../../../entradas/t5/teste1.in"],
                #"resposta": "./entradas/t5/teste1.out",
                "valgrind": True,
                "autoTeste" : True,
                "cols": 8
        },
        "t7": {
                "dir": "T7",
                "finalizado": True,
                "github": "t7-grades-1687128436.csv",
                "data": datetime(2023, 6, 22, 23, 55).astimezone(tz=None),
                "testa": True,
                #"entrada": "teste1.in",
                #"fonte": ["../../../entradas/t5/teste1.in"],
                #"resposta": "./entradas/t5/teste1.out",
                "principal": ["../../../entradas/t7/arvore.cpp"],
                "valgrind": True,
                "autoTeste" : True,
                "cols": 8
        },
        "t8": {
                "dir": "T8",
                "finalizado": False,
                "github": "t8-grades-1689078400.csv",
                "data": datetime(2023, 7, 17, 23, 55).astimezone(tz=None),
                "testa": True,
                #"entrada": "teste1.in",
                #"fonte": ["../../../entradas/t5/teste1.in"],
                #"resposta": "./entradas/t5/teste1.out",
                #"principal": ["../../../entradas/t7/arvore.cpp"],
                "valgrind": True,
                "autoTeste" : True,
                "cols": 8
        }                         
}

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(GITHUB_TOKEN)}

html_header="""<!DOCTYPE html><html><head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  text-align: center;
}
</style>
</head><body>
"""

res_erro = "ERRO"
res_ok = "OK"
res_atraso = "{}"
res_alerta = "{}"

html_footer="</body></html>"

def configuraLog():
        global logger
        logging.basicConfig(filename='analise.log', 
                format='%(asctime)s %(levelname)s %(message)s',             level=logging.DEBUG)
        logger = logging.getLogger("GITHUB")
        logger.setLevel(logging.DEBUG)
        logger.info("INICIA Analizando")


# Convert a github API call result to JSON object.
def githubRequest(url):
        logger.info(url)
        req = requests.get(url, headers=headers)
        if(req.ok):
                return json.loads(req.text or req.content)
        else:
                return None

def githubDownloadRequest(url):
        logger.info(url)
        req = requests.get(url, headers=headers)
        if(req.ok):
                return req.content
        else:
                return None

#def githubBuildURL():
#login = requests.get('https://api.github.com/search/repositories?q=github+api', headers=headers)
#line = githubRequest('https://api.github.com/user/repos')

def gitHubGetUsers(user, repo):
    usuarios = githubRequest('https://api.github.com/repos/{}/{}/contributors'.format(user, repo))
    for u in usuarios:
        print(u)

# https://github.com/pedrobms/lp2-2019b
#arquivos = githubRequest('https://api.github.com/repos/{}/{}/contents/{}'.format('pedrobms', 'lp2-2019b', '/'))
#for arq in arquivos:
#    print(arq.get('name'),arq.get('type'))

#gitHubGetUsers('pedrobms', 'lp2-2019b')

#r = requests.get('https://api.github.com/repos/django/django')
#if(r.ok):
#    repoItem = json.loads(r.text or r.content)
#    print("Django repository created: " + repoItem['created_at'])

def gitHubTestaCommits(user, repo, pasta):
        info = githubRequest('https://api.github.com/repos/{}/{}/commits?path={}'.format(user, repo, pasta))
        if info is None:
                logger.warning("nao achei commits {} {}".format(user, repo))
                return False, None
        if len(info) == 0:
                info = githubRequest('https://api.github.com/repos/{}/{}/commits?path={}'.format(user, repo, pasta.lower()))
        if len(info) == 0:
                logger.warning("nao encontrei infos de commits")
                return False, None
        return True, len(info)


# retorna quantos dias do 1o ao ultimo commit
def gitHubTestaDataInicio(user, repo, pasta):
        info = githubRequest('https://api.github.com/repos/{}/{}/commits?path={}'.format(user, repo, pasta))
        if info is None:
                #print("nada")
                return False, None
        if len(info) == 0:
                info = githubRequest('https://api.github.com/repos/{}/{}/commits?path={}'.format(user, repo, pasta.lower()))
        if len(info) == 0:
                logger.warning("nao encontrei infos")
                return False, None
        # apenas um commit
        if len(info) == 1:
                return True, res_alerta.format("nada")
        # dados do ultimo commit
        commit = info[0].get('commit')
        if commit is None:
                logger.warning("nao encontrei last commit")
                return False, None
        autor = commit.get('author')
        if autor is None:
                logger.warning("nao encontrei autor de last commit")
                return False, None
        if autor.get('date') is None:
                logger.warning("nao encontrei data de last commit")
                return False, None
        ultimo = datetime.strptime(autor.get('date'), "%Y-%m-%dT%H:%M:%SZ")
        # dados do 1o commit
        commit = info[-1].get('commit')
        if commit is None:
                logger.warning("nao encontrei 1o commit")
                return False, None
        autor = commit.get('author')
        if autor is None:
                logger.warning("nao encontrei autor de 1o commit")
                return False, None
        if autor.get('date') is None:
                logger.warning("nao encontrei data de 1o commit")
                return False, None
        primeiro = datetime.strptime(autor.get('date'), "%Y-%m-%dT%H:%M:%SZ")
        delta = ultimo - primeiro
        return True, str(delta)

def gitHubTestaData(user, repo, prazo, pasta):
        info = githubRequest('https://api.github.com/repos/{}/{}/commits?path={}'.format(user, repo, pasta))
        if info is None:
                #print("nada")
                return False, None
        if len(info) == 0:
                info = githubRequest('https://api.github.com/repos/{}/{}/commits?path={}'.format(user, repo, pasta.lower()))
        if len(info) == 0:
                logger.warning("nao encontrei infos")
                return False, None
        commit = info[0].get('commit')
        if commit is None:
                logger.warning("nao encontrei commits")
                return False, None
        autor = commit.get('author')
        if autor is None:
                logger.warning("nao encontrei autor de commit")
                return False, None
        if autor.get('date') is None:
                logger.warning("nao encontrei data de commit")
                return False, None
        # 2022-04-29T01:34:42Z
        ultimo = datetime.strptime(autor.get('date'), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).astimezone(tz=None)
        if ultimo > prazo:
                #print(str(ultimo) + " prazo " + str(prazo) + " : " + autor.get('date'))
                #print(str(ultimo.replace(tzinfo=timezone.utc).astimezone(tz=None)))
                return False, (ultimo-prazo)
        return True, ultimo

def gitHubTestaPrivate(user, repo):
        info = githubRequest('https://api.github.com/repos/{}/{}'.format(user, repo))
        if info is None:
                return False
        if info.get('private') == None:
                return False
        return info['private'] 

def gitHubTestaPasta(user, repo, pasta):
        info = githubRequest('https://api.github.com/repos/{}/{}/contents/{}'.format(user, repo, "/"))
        if info is None:
                return False
        for a in info:
                nome = a.get('name') 
                if nome is not None:
                        nome = nome.upper()   
                if nome is not None and nome == pasta:
                        return True
        return False

def gitHubTestaColaboradores(user, repo):
        info = githubRequest('https://api.github.com/repos/{}/{}/collaborators'.format(user, repo))
        if info is None:
                return False
        try:
                colaboradores = [i.get('login') for i in info]
                # colaboradores.remove(user)
                colaboradores.remove('joao-lima')                
                if len(colaboradores) == 1:
                        return True
        except Exception as e: 
                logger.error("colaboradores: {}".format(str(e)))     
        return False

def testaAlunoCommits(a, pasta):
        teste, commits = gitHubTestaCommits("jvlima-ufsm", a['repo'], pasta)
        if teste == True:
                return str(commits)
        else:
                return res_erro

def testaAlunoDataInicio(a, pasta):
        teste, dias = gitHubTestaDataInicio("jvlima-ufsm", a['repo'], pasta)
        if teste == True:
                return dias
        else:
                return res_erro

def testaAlunoData(a, data, pasta):
        teste, data = gitHubTestaData("jvlima-ufsm", a['repo'], data, pasta)
        if teste == True:
                return res_ok
        else:
                return res_atraso.format(data)

def testaAlunoPasta(a, pasta):
        if gitHubTestaPasta(a['user'], a['repo'], pasta) == True:
                return res_ok
        else:
                return res_erro

def testaAlunoPrivado(a):
        if gitHubTestaPrivate(a['user'], a['repo']) == True:
                return res_ok
        else:
                return res_erro

def testaAlunoColaborador(a):
        if gitHubTestaColaboradores(a['user'], a['repo']) == True:
                return res_ok
        else:
                return res_erro


def githubLs(path, returnPaths=False):
        ''' Request via Github API the list of
        directories and files in some path
        returns files, directories        
        '''
        prefix = ''
        if returnPaths == True:
                prefix = path
        js = githubRequest(path)
        files = []
        dirs = []
        for f in js:
                if f['type'] == 'file':
                        files += [prefix + f['name']]
                elif f['type'] == 'dir':
                        dirs += [prefix + f['name']]
        return files, dirs

def urlJoin(head, tail):
   while len(head) > 0 and head[-1] == '/':
      head = head[:-1]
   while len(tail) > 0 and tail[0] == '/':
      tail = tail [1:]
   return head + '/' + tail


def listaArquivosAluno(a, pasta):
        def recursiveScanner(path):
                files, dirs = githubLs(path)
                for d in dirs:
                        for f in recursiveScanner(urlJoin(path, d)):
                                files += [d + '/' + f]
                return files
        url = 'https://api.github.com/repos/{}/{}/contents/{}'.format(a['user'],
                a['repo'], pasta)
        return recursiveScanner(url)

def filtraTodosArquivos(todos):
        arquivos = []
        if len(todos) == 0:
                return []
        for arquivo in todos:
                if arquivo.endswith('.cpp'):
                        arquivos += [arquivo]
                if arquivo.endswith('.h'):
                        arquivos += [arquivo]
                if arquivo.endswith('.hpp'):
                        arquivos += [arquivo]
                if arquivo == "Makefile":
                        arquivos += [arquivo]
        return arquivos


def formatGithubDownloadFile(user, repo, path):
        #"https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md
        url = 'https://raw.githubusercontent.com/{}/{}/'.format(user, repo)
#        branch = githubGet('branch')
        branch = None
        if branch == None: branch = 'master'
        url += branch + '/' + path
        return url

def githubDownload(a, path):
        locais = []
        if not isinstance(path, list):
                path = [path]
        for i in path:
                logger.info('downloading ' + i + '...')
                url = formatGithubDownloadFile(a['user'], a['repo'], i)
                basename = os.path.basename(i)
                dirname = os.path.dirname(i).upper()
                userdir = a['matricula']
                alvo = os.path.join(os.path.join('download', userdir, dirname, basename))
                if devoBaixar == True:
                        try:
                                os.makedirs(os.path.join('download', userdir, dirname))
                        except: pass
                        conteudo = githubDownloadRequest(url)
                        with open(alvo, 'wb') as fhandle:
                                fhandle.write(conteudo)
                locais += [alvo]
        return locais

def baixaArquivosAluno(a):
#        try:
        todos = listaArquivosAluno(a, '/')
        if len(todos) == 0:
                return []
        logger.info("Todos os arquivos de {}: {}".format(a['nome'], str(todos)))
        arquivos = filtraTodosArquivos(todos)
        logger.info("Filtro dos arquivos de {}: {}".format(a['nome'], str(arquivos)))
        locais = githubDownload(a, arquivos)
        logger.info("Arquivos baixados de {}: {}".format(a['nome'], str(locais)))
#        except Exception as e:
#                logger.error("download: {}".format(str(e)))
        return locais

def baixaArquivosAlunoPorClone(a, trab):
        logger.info("Download: {} {}".format(trab['dir'], a.get('nome')))
        atual = os.getcwd()
        if a.get('repo') is None:
                logger.info("URL vazia: {}".format(a['nome']))
        try:
                if os.path.exists(os.path.join(atual, 'download', trab['dir'], a['matricula'])):
                        alvo = os.path.join(atual, 'download', trab['dir'], a['matricula'])
                        os.chdir(alvo)
                        os.system("git pull")
                else:
                        os.system("git clone git@github.com:jvlima-ufsm/{0} download/{1}/{2}".format(a['repo'], trab['dir'], a['matricula']))
        except Exception as e: 
                logger.error("download: {}".format(str(e)))     
        finally:
                os.chdir(atual)
        #os.system("git clone git@github.com:jvlima-ufsm/{0} download/{0}".format(a['repo']))
 #       except Exception as e:
 #               logger.error("download: {}".format(str(e)))
        
def testaAlunoResposta(a, trab):
        atual = os.getcwd()
        rel = None
        retorno = None
        try:
                #alvo = os.path.join(atual, 'download', a['matricula'], trab['dir'])
                alvo = os.path.join(atual, 'download', trab['dir'], a['matricula'])
                os.chdir(alvo)
                if trab.get('fonte') is not None:
                        for f in trab['fonte']:
                                shutil.copy( f, "." )
                executar = [ './a.out' ]
                if trab.get('argumento') is not None:
                        executar.append(trab['argumento'])
                logger.info("Executando em {}".format(alvo))
                #rel = os.popen(cmd).readlines()
                entrada = None
                if trab.get('entrada') is not None:
                        entrada = open(trab['entrada'])
                #retorno = subprocess.check_output(executar, stderr=subprocess.STDOUT, stdin=entrada, timeout=5)
                retorno = subprocess.run(executar, stdin=entrada, timeout=5, capture_output=True)
                rel = retorno.stdout.decode("utf-8")
                if trab.get('autoTeste') is not None:                
                        rel = rel + "\nERRORS:\n" + retorno.stderr.decode("utf-8") 
                #with subprocess.Popen(executar, stdout=subprocess.PIPE, stdin=entrada) as proc:
                #        rel = proc.stdout.read().decode("utf-8") 
                # cria diretorio de saida
        except Exception as e: 
                logger.error("executor: {}".format(str(e)))     
        finally:
                os.chdir(atual)
        # se matricula vazia
        if a.get('matricula') is None:
                return ""
        # diretorio dos relatorios
        dir_rel = os.path.join('relatorios', a['matricula'], trab['dir'] )
        try:
                os.makedirs(dir_rel)
        except: pass
        if rel is None:
                return res_erro
        alvo_saida = os.path.join(dir_rel, 'saida.txt')                
        # o programa nao gera um saida.txt         
        if trab.get("geraSaida") is None:                
                with open(alvo_saida, 'w') as fhandle:
                        fhandle.write(rel)
        # faz a comparacao
        if trab.get('resposta') is not None:
                try:
                        if trab.get("geraSaida") is not None:
                                orig = os.path.join(atual, 'download', a['repo'], 'saida.txt')
                                if os.path.exists(orig) == False:
                                        return res_erro
                                shutil.copy(orig, alvo_saida)
                        executar = "diff -c {} {}".format(alvo_saida, trab['resposta'])
                        cmd = executar.split()
                        logger.info("Diferenca em {}".format(alvo_saida))
                        #rel = os.popen(cmd).readlines()
                        with subprocess.Popen(cmd, stdout=subprocess.PIPE) as proc:
                                rel = proc.stdout.read().decode("utf-8") 
                # cria diretorio de saida
                except Exception as e: 
                        logger.error("executor: {}".format(str(e)))     
                if len(rel) == 0:
                        return res_ok
                # retorna erros
                alvo_rel = os.path.join(dir_rel, 'resposta.txt')
                with open(alvo_rel, 'w') as fhandle:
                        fhandle.write(rel)
                return "[VER](./{})".format(alvo_rel)
        elif trab.get('autoTeste') is not None:                
                logger.info("RETCODE {}".format(retorno.returncode))
                if retorno.returncode != 0:
                        return "erro ({}/7)".format(retorno.returncode)
                else:
                        return res_ok
        else:
                return res_alerta.format('nada')
        return ""

def testaAlunoCompilador(a, trab):
        #res = filter(lambda x : trab['dir'] in x or trab['dir'].lower() in x, arquivos )
        #alvos = list(res)
#        if len(alvos) == 0:
#                logger.warning("Nenhum arquivo de {} {}".format(a['nome'], trab['dir']))
#                return "", False
        logger.info("COMPILADOR Arquivos trabalho {} de {}".format(trab['dir'], a['nome'] ))
        atual = os.getcwd()
        rel = None
        try:
                #alvo = os.path.join(atual, 'download', a['matricula'], trab['dir'])
                #alvo = os.path.join(atual, 'download', a['repo'])
                alvo= os.path.join(atual, 'download', trab['dir'], a['matricula'])
                os.chdir(alvo)
                fontes = [f for f in os.listdir('.') if f.endswith('.cpp')]
                if trab.get('principal') is not None:
                        for c in trab['principal']:
                                shutil.copy(c, ".")
                        fontes = [os.path.basename(f) for f in trab['principal'] if f.endswith('.cpp')]
                # se nao tem arquivo CPP no diretorio
                if len(fontes) == 0:
                        logger.warning("Nenhum arquivo de {} {}".format(a['nome'], a['repo']))
                        os.chdir(atual)
                        return "", False
                logger.info("COMPILADOR compilando {} de {}: {}".format(trab['dir'], a['nome'], fontes ))                        
                compilador = 'g++ -Wall -std=c++11 -g'.split()
                compilador += fontes
                if trab.get('libs') is not None:
                        compilador += trab['libs'].split()
                logger.info("Compilando em {}".format(alvo))
                os.system("rm -f a.out")
                #rel = os.popen(cmd).readlines()
                with subprocess.Popen(compilador, stderr=subprocess.PIPE) as proc:
                        rel = proc.stderr.read().decode("utf-8") 
                # cria diretorio de saida
        except Exception as e: 
                logger.error("g++: {}".format(str(e)))     
        finally:
                os.chdir(atual)
        # se matricula vazia
        if a.get('matricula') is None:
                return "", True
        # escreve relatorio
        dir_rel = os.path.join('relatorios', a['matricula'], trab['dir'] )
        try:
                os.makedirs(dir_rel)
        except: pass
        if len(rel) == 0:
                return res_ok, True
        # retorna erros
        alvo_rel = os.path.join(dir_rel, 'compilador.txt')
        with open(alvo_rel, 'w') as fhandle:
                fhandle.write(rel)
        return "[VER](./{})".format(alvo_rel), True

#def testaAlunoValgrind(a, trab, arquivos):
#        return ""
def testaAlunoValgrind(a, trab):
        atual = os.getcwd()
        rel = None
        if a.get('matricula') is None:
                return ""
        dir_rel = os.path.join( atual,'relatorios', a['matricula'], trab['dir'] )
        try:
                os.makedirs(dir_rel)
        except: pass
        alvo_saida = os.path.join(dir_rel, 'valgrind.txt')
        try:
                #alvo = os.path.join(atual, 'download', a['matricula'], trab['dir'])
                alvo = os.path.join(atual, 'download', trab['dir'], a['matricula'])
                os.chdir(alvo)
                # testa arquivo binario
                if os.path.exists("./a.out") == False:
                        os.chdir(atual)
                        return res_erro
                # entrada
                if trab.get('fonte') is not None:
                        for f in trab['fonte']:
                                shutil.copy( f, ".")
                executar = 'valgrind -q --leak-check=full ./a.out'
                cmd = executar.split()

                #if trab.get('argumento') is not None:
                #        executar.append(trab['argumento'])
                logger.info("Valgrind em {}".format(alvo))
                entrada = None
                if trab.get('entrada') is not None:
                        entrada = open(trab['entrada'])
                rel_valgrind = open(alvo_saida, 'w')
                output =  subprocess.check_output(cmd, stderr=rel_valgrind, stdin=entrada, timeout=5)
                rel_valgrind.close()
                #rel = rel_valgrind.read().decode("utf-8") 
                #with subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE) as proc:
                #        rel = proc.stderr.read().decode("utf-8") 
                # cria diretorio de saida
        except Exception as e: 
                logger.error("valgrind: {}".format(str(e)))     
        finally:
                os.chdir(atual)
        # le relatorio todo para ver conteudo
        rel_valgrind = open(alvo_saida)
        rel = rel_valgrind.read()
        # diretorio dos relatorios
        if rel is None:
                return res_erro
        if len(rel) == 0:
                return res_ok
        alvo_rel = os.path.join('relatorios', a['matricula'], trab['dir'], 'valgrind.txt' )
        #alvo_saida = os.path.join(dir_rel, 'valgrind.txt')
        #with open(alvo_saida, 'w') as fhandle:
        #        fhandle.write(rel)
        return "[VER](./{})".format(alvo_rel)

def testaAlunoCppcheck(a, trab):
        logger.info("CHECK Arquivos trabalho {} de {}".format(trab['dir'], a['nome'] ))
        atual = os.getcwd()
        rel = None
        fontes = []
        try:
                cmd = 'cppcheck --enable=all --suppress=missingIncludeSystem'.split()
                #alvo = os.path.join(atual, 'download', a['matricula'], trab['dir'])
                alvo = os.path.join(atual, 'download', trab['dir'], a['matricula'])
                os.chdir(alvo)
                # diretorio vazio?
                fontes = [f for f in os.listdir('.') if f.endswith('.cpp')]
                if trab.get('principal') is not None:
                        for c in trab['principal']:
                                if os.path.basename(c) in fontes:
                                        fontes.remove( os.path.basename(c) )
                logger.info("cppcheck fontes {}".format(alvo))
                # roda
                logger.info("cppcheck em {}".format(fontes))
                #rel = os.popen(cmd).readlines()
                if len(fontes) > 0:
                        cmd += fontes
                        with subprocess.Popen(cmd, stderr=subprocess.PIPE) as proc:
                                rel = proc.stderr.read().decode("utf-8") 
                # cria diretorio de saida
        except Exception as e: 
                logger.error("cppcheck: {}".format(str(e)))     
        finally:
                os.chdir(atual)

        # se nao tem arquivo CPP no diretorio
        if len(fontes) == 0:
                logger.warning("cppcheck nenhum arquivo de {} {}".format(a['nome'], a['repo']))
                return res_erro

        # se matricula vazia
        if a.get('matricula') is None:
                return ""

        # escreve relatorio
        dir_rel = os.path.join('relatorios', a['matricula'], trab['dir'] )
        try:
                os.makedirs(dir_rel)
        except: pass
        if len(rel) == 0:
                return res_ok
        # retorna erros
        alvo_rel = os.path.join(dir_rel, 'cppcheck.txt')
        with open(alvo_rel, 'w') as fhandle:
                fhandle.write(rel)
        return "[VER](./{})".format(alvo_rel)

def testaAlunoOclint(a, trab):
        logger.info("CHECK Arquivos trabalho {} de {}".format(trab['dir'], a['nome'] ))
        atual = os.getcwd()
        rel = None
        fontes = []
        try:
                #oclint  --enable-clang-static-analyzer  -report-type html  t2.cpp  -- -Wall -g|sed 's:/home/jvlima/UFSM/l22023a/resultados/download/::g' > report.html
                cmd = 'oclint  --enable-clang-static-analyzer  -report-type html'.split()
                
                #alvo = os.path.join(atual, 'download', a['matricula'], trab['dir'])
                alvo = os.path.join(atual, 'download', trab['dir'], a['matricula'])
                os.chdir(alvo)
                # diretorio vazio?
                fontes = [f for f in os.listdir('.') if f.endswith('.cpp')]
                if trab.get('principal') is not None:
                        for c in trab['principal']:
                                if os.path.basename(c) in fontes:
                                        fontes.remove( os.path.basename(c) )
                                #shutil.copy(c, ".")
                logger.info("oclint fontes {}".format(alvo))
                # roda
                logger.info("oclint em {}".format(fontes))
                #rel = os.popen(cmd).readlines()
                if len(fontes) > 0:
                        cmd += fontes
                        cmd += "-- -Wall -g".split()
                        with subprocess.Popen(cmd, stdout=subprocess.PIPE) as proc:
                                rel = proc.stdout.read().decode("utf-8") 
                # cria diretorio de saida
        except Exception as e: 
                logger.error("oclint: {}".format(str(e)))     
        finally:
                os.chdir(atual)

        # se nao tem arquivo CPP no diretorio
        if len(fontes) == 0:
                logger.warning("oclint nenhum arquivo de {} {}".format(a['nome'], a['repo']))
                return res_erro

        # se matricula vazia
        if a.get('matricula') is None:
                return ""

        # rel vazio
        if len(rel) == 0:
                return res_ok

        rel = rel.replace("/home/jvlima/UFSM/l22023a/resultados/download/", "")

        # escreve relatorio
        dir_rel = os.path.join('relatorios', a['matricula'], trab['dir'] )
        try:
                os.makedirs(dir_rel)
        except: pass
        # retorna erros
        alvo_rel = os.path.join(dir_rel, 'report.html')
        with open(alvo_rel, 'w') as fhandle:
                fhandle.write(rel)
        return "[VER](./{})".format(alvo_rel)

def geraEntradasVazias():
        table = ""
        table += "    | "
        table += "    | "
        # trabalhos
        for tx, value in trabalhos.items():        
                # pasta
                table += " |"
                # commits
                table += " | "
                # resposta
                table += " | "
                table += " | "
                # cppcheck
                table += " | "
                # valgrind
                if value.get("valgrind") is not None:
                        table += " | "
                # data
                table += " | "
                # inicio (dias de trabalho)
                table += " | "
        table += "  | \n"
        return table

def testaReposAlunos(alunos, trab, file_html):
        table = ""
        #table += "    <td>{0}</td>\n".format(column.strip())
        for a in alunos:
                print("Gerando para " + a['nome'] + "...")
                table += "| "
                if geraComNomes == True:
                        table += " {0} | ".format(a['nome'].strip())
                # matricula
                if a.get('matricula') is None:
                        table += " - | "
                else:
                        table += " {0} | ".format(a['matricula'].strip())
                        
                # repositorio
                if a.get('repo') is None:
                        table += geraEntradasVazias()
                        continue

                # baixa arquivos
                baixaArquivosAlunoPorClone(a, trab)
                # privado
                #saida = testaAlunoPrivado(a)
                #table += "    <td>{0}</td>\n".format(saida.strip())
                # colaboradores
                #saida = testaAlunoColaborador(a)
                #table += "    <td>{0}</td>\n".format(saida.strip())
                
                # trabalhos
                #for tx, value in trabalhos.items():        
                # pasta
                #saida = testaAlunoPasta(a, tx)
                #table += "    <td>{0}</td>\n".format(saida.strip())
                # commits
                saida = testaAlunoCommits(a, "/")
                table += " {0} | ".format(saida.strip())
                # resposta
                saida, res = testaAlunoCompilador(a, trab)
                table += " {0} | ".format(saida.strip())
                if trab.get("testa") == True:
                        if res == True:
                                saida = testaAlunoResposta(a, trab)
                                table += " {0} | ".format(saida.strip())
                        else:
                                table += "  | "
                else:
                        table += "  | "
                # cppcheck
                saida = testaAlunoOclint(a, trab)
                table += "  {0} | ".format(saida.strip())
                # valgrind
                if trab.get("valgrind") is not None:
                        if trab['valgrind'] == True:
                                saida = testaAlunoValgrind(a, trab)
                                table += " {0} | ".format(saida.strip())
                        else:
                                table += " | "
                # data
                saida = testaAlunoData(a, trab["data"], "/")
                table += " {0} | ".format(saida.strip())
                # inicio (dias de trabalho)
                saida = testaAlunoDataInicio(a, "/")
                table += " {0} | ".format(saida.strip())
                table += "\n"
        #table += "</table>"
        file_html.writelines(table) 


def geraHeadersHTML(trab, file_html):        
        #table = "<table style=\"width:100%\">\n"
        #table += "  <tr>\n"
        #table += "    <th></th>\n"
        #if geraComNomes == True:
        #        table += "    <th></th>\n"                
        #table += "    <th colspan=2>{0}</th>\n".format("GitHub")
        #for tx, value in trabalhos.items():
        #table += "    <th colspan={}>{}</th>\n".format(trab.get('cols'), trab["dir"])
        #table += "    <th colspan=3>{0}</th>\n".format("T1")
        #table += "  </tr>\n"

        table = "| "
        linha = ""
        if geraComNomes == True:
                table += " {0} | ".format("Nome")        
                linha += "|---"
        table += " {0} |".format("Matrícula")        
        linha += "|---"
        #table += "    <th>{0}</th>\n".format("Priv.")
        #table += "    <th>{0}</th>\n".format("Usrs.")               
        # trabalhos
        #for tx, value in trabalhos.items():
        #table += "    <th>{0}</th>\n".format("Dir.")
        table += " {0} |".format("Commits")
        linha += "|---"
        table += " {0} | ".format("GCC")
        linha += "|---"
        table += " {0} | ".format("RES")
        linha += "|---"
        table += " {0} | ".format("Análise")
        linha += "|---"
        if trab.get("valgrind") is not None:
                table += " {0} | ".format("Valgrind")
                linha += "|---"
        table += " {0} | ".format("Data")
        linha += "|---"
        table += " {0} | ".format("Duração")
        linha += "|---"
        table += "\n"
        linha += "|\n"
        # escreve texto
        #file_html.writelines(html_header)
        texto = "# {}\n".format(trab["dir"])
        agora = datetime.now()
        texto += "Última atualização: **{}**\n\n".format(agora)
        file_html.writelines(texto)
        file_html.writelines(table)
        file_html.writelines(linha)

def geraHeadersHTMLIndex(file_html):        
        # escreve texto
        #file_html.writelines(html_header)
        agora = datetime.now()
        texto = "Última atualizacão: **{}**\n".format(agora)
        file_html.writelines(texto)
        #texto = "\n"
        #file_html.writelines(texto)

def readAlunosMatriculados():
   output = {}
   with open('alunos_ELC1067_TCC2.csv', 'rt') as fhandle:
      reader = csv.reader(fhandle, delimiter=',')
      next(reader) # pula cabecalho
      for row in reader:
        output[ row[0] ] = row[1]
   #
   with open('alunos_ELC1067_TSI1.csv', 'rt') as fhandle:
      reader = csv.reader(fhandle, delimiter=',')
      next(reader) # pula cabecalho
      for row in reader:
        output[ row[0] ] = row[1]           
   return output        

def readReposFromCsv(matriculados, trab):
   output = []
   with open(trab.get("github"), 'rt') as fhandle:
      reader = csv.reader(fhandle, delimiter=',')
      next(reader) # pula cabecalho
      for row in reader:
        entry = {
            'nome': row[4],
            'matricula': matriculados.get(row[4]),
            'repo': row[6].replace("https://github.com/jvlima-ufsm/","")
        }
 #       if len(row[5]) > 0:
 #               segments = entry['url'].split('/')
 #               entry['user'] = segments[1]
 #               entry['repo'] = segments[2]
        output += [entry]
        logger.info("{} {} {}".format(entry.get('matricula'), entry.get('url'), entry.get('nome')))
   output = sorted(output, key=lambda x:x.get('matricula'))        
   return output

def principal():
        configuraLog()
        file_index = open("README.md", "w")
        geraHeadersHTMLIndex(file_index)
        matriculados = readAlunosMatriculados()
        texto = ""
        for tx, value in trabalhos.items():  
                if value["finalizado"] == False:
                        fileout = open("{}.md".format(tx), "w")      
                        geraHeadersHTML(value, fileout)
                        alunos = readReposFromCsv(matriculados, value)
                        testaReposAlunos(alunos, value, fileout)
                        #fileout.writelines(html_footer)
                        fileout.close()
                texto += "- [{}](./{})\n".format(value.get("dir"), "{}.md".format(tx))
        texto += "\n"
        file_index.writelines(texto)
        file_index.close()

if __name__ == "__main__":
        principal()
