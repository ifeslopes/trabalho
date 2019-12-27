# Trabalho
#### Técnicas de Programação – Trabalho 1


Uma empresa deseja usar técnicas de aprendizado de máquina para fazer classificação
automática de mamografias. Para isso ela irá usar uma base de dados que contém imagens de
mamografias e as análises realizadas por um médico. Os nomes das imagens e as análises estão
salvas em um arquivo com formato CSV (comma separated values – valores separados por
vírgula):

![imagem](https://github.com/ifeslopes/trabalho/blob/master/Captura%20de%20tela%20de%202019-12-26%2021-43-55.png)

Uma visualização melhor desses arquivos pode ser obtida o MS Excel ou usando o BrOffice Calc: 

![imagem](https://github.com/ifeslopes/trabalho/blob/master/Captura%20de%20tela%20de%202019-12-26%2021-44-26.png)

### Colunas com informações interessantes:

• patient_id: contém o identificador único do paciente. Alguns pacientes possuem mais de
uma anormalidade, então eles podem aparecer mais de uma vez na tabela.
• pathology: o resultado principal da análise. Anomalias classificadas como câncer são
classificadas como malignas (MALIGNANT). Anomalias que não são câncer, mas precisam de
acompanhamento são classificadas como benignas (BENIGN). Anomalias que não são câncer
e não precisam de acompanhamento, são classificadas como benignas sem retorno
(BENIGN_WITHOUT_CALLBACK).
• Left or right breast: representa qual seio (esquerdo ou direito) foi avaliado.
• image view: indicam o tipo de exame que foi realizado. Podem ser CC e MLO.
• breast_density: densidade do seio que é indicativo de que a paciente precisa ser
acompanhada.
• mass shape: Forma da amostra.
• mass margins: Tipo de borda da amostra.
• image file path: contém o caminho onde a foto da mamografia se encontra no computador.

### Atividades do Trabalho:
• Ler o arquivo de entrada: 5 pontos
• Escrever arquivos de saída: 5 pontos
• Salvar em um arquivo “relatorio.txt” o número de linhas e o porcentual do total dos valores
das coluna breast_density, pathology, mass margin e mass shape (ver exemplo abaixo) - 10:

### Exemplo (não relacionado ao arquivo de entrada do site):
breast_density:
- 1: 10 (10%)
- 2: 30 (30%)
- 3: 40 (40%)
- 4: 10 (10%)
- 5: 10 (10%)
pathology:
- MALIGN: 70 (70%)
- BENIGN: 20 (20%)
- BENIGN_WITHOUT_CALLBACK: 10 (10%)


• Salvar um arquivo “script.txt” com uma lista de comandos que permitam renomear usando
o comando MOVE as imagens (coluna “image file path”) para o formato
<numero_incremental>_<patient_id>_<left or right>_<image view>_pathology.dcm. O
arquivo de ter um comando por linha. – 5 pontos
  
### Exemplo de arquivo scripts.txt:
Linha Conteúdo
1
MOVE
MassTraining_P_00001_LEFT_CC/1.3.6.1.4.1.9590.100.1.2.422112722213189649807611434612
228974994/1.3.6.1.4.1.9590.100.1.2.342386194811267636608694132590482924515/0000
00.dcm 0001_P_00001_LEFT_CC_MALIGNANT.dcm
2
MOVE
MassTraining_P_00001_LEFT_MLO/1.3.6.1.4.1.9590.100.1.2.3194789993119714424261853535
60182990988/1.3.6.1.4.1.9590.100.1.2.359308329312397897125630708681441180834/00
0000.dcm 0002_P_00001_LEFT_MLO_MALIGNANT.dcm
…
