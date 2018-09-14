# Cálculo Numérico - Trabalho 1

# Sumário
- [Como rodar](#como-rodar)
- [Enunciado](#enunciado)
- [Instruções](#instru%C3%A7%C3%B5es) (para contribuidores)

# Como rodar
- Clonar ou fazer download do repositório
- Ir até a pasta do trabalho

` $ cd <caminho-da-pasta-de-downloads>/cn-uece `

- Criar virtualenv

` $ pip3 install virtualenv --user `

` $ python3 -m virtualenv venv `

- Configuar o ambiente

` $ source venv/bin/activate ` (comando necessário para todas as vezes que for acessar de uma nova aba do terminal)

` $ pip3 install -r requirements.txt `

- Baixar as dependências: Tkinter

` $ sudo dnf install python3-tkinter ` (Fedora)

` $ sudo apt install python3-tk ` (Debian/Ubuntu)

- Rodar o programa

` $ python3 main.py `

# Enunciado

![Enunciado do trabalho](https://i.imgur.com/Jskdr7w.png)

# Instruções

## Inicialmente
- Dar fork no [repositório oficial](https://github.com/warrior-graph/CN-UECE)
- Clonar seu novo repositório

` $ git clone https://github.com/<usuario>/CN-UECE `

- Adicionar o repositório oficial como remoto

` $ git remote add upstream https://github.com/warrior-graph/CN-UECE `

## Antes de fazer alterações
- Atualizar seu repositório com base no oficial

` $ git pull upstream master `

## Ao fazer alterações
- Adicionar arquivos alterados

` $ git add * `

- Adicionar a descrição do que foi alterado

` $ git commit -m "<descrição>" `

- Enviar alterações para o seu repositório

` $ git push origin master `

## Abrindo um pull request
- Ir no repositório oficial > pull requests > [new pull request](https://github.com/warrior-graph/CN-UECE/compare)
- Selecionar "compare across forks"
- Alterar o "head fork" e selecionar o branch, se as alterações não tiverem sido feitas no master
- "Create pull request"
- Descrever no título as alterações do fork em relação ao repositório oficial
- "Create pull request" de novo
- Esperar o merge :)
