# Instruções

## Inicialmente
- Dar fork no repositório oficial
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
