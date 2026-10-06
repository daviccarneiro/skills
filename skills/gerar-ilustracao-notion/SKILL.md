---
name: gerar-ilustracao-notion
description: >-
  Gere ou adapte ilustrações editoriais minimalistas com personagens simples,
  contornos escuros arredondados, cores foscas e textura de papel, seguindo cinco
  referências visuais incluídas. Use quando o usuário invocar esta skill ou pedir
  essa família visual, inclusive como estética semelhante à do Notion. Permite
  variar tema, paleta, cenário e objetos mantendo o desenho consistente.
  Não se destina a fotografias, interfaces funcionais ou cópia de logos.
---

# Gerar-ilustração-Notion

Crie imagens novas na família visual das cinco referências incluídas. A fonte
de verdade são estas imagens, não uma interpretação genérica da marca Notion.
O nome da marca é apenas uma aproximação verbal: o conjunto tem cores quentes,
contornos fortes e textura impressa próprios. Não prometa reprodução idêntica.

## Antes de gerar

1. Leia [a análise visual](references/analise-visual.md) e inspecione as cinco
   imagens em `assets/` na primeira utilização da sessão. Resolva todos os
   caminhos a partir da pasta desta skill, nunca da conversa original.
2. Extraia do pedido tema, ação, personagens, paleta, formato e destino. Preencha
   o que faltar com os padrões abaixo; pergunte somente se faltar uma decisão
   indispensável. Um pedido para apenas preparar prompts não autoriza geração.
3. Escolha uma ou duas referências mais úteis para composição e traço. Use-as
   como entradas visuais no gerador disponível, quando suportado, explicando
   que são referências de estilo, não objetos ou profissões a copiar.
4. Use a ferramenta de geração/edição de imagens disponível e suas instruções
   atuais. Se a skill operacional `imagegen` estiver disponível, leia-a para
   executar a geração. Não dependa de caminhos de instalação ou de um provedor
   específico. Se não houver gerador, entregue o prompt preenchido e indique
   quais arquivos anexar; não apresente um prompt como imagem produzida.

## DNA visual a preservar

- Ilustração editorial 2D, formas fechadas e arredondadas, desenho limpo com
  ligeira organicidade. Contorno castanho muito escuro ou carvão, contínuo,
  espesso e de peso consistente; detalhes internos iguais ou um pouco mais finos.
- Adultos estilizados: cabeças moderadamente ampliadas, corpos compactos,
  ombros arredondados, braços de espessura plausível e mãos grandes o suficiente
  para ler os gestos. Não usar membros elásticos nem cabeças de bebê. A primeira
  referência de corpo inteiro sugere cerca de 5–6 cabeças de altura; é uma
  aproximação visual, não uma medida obrigatória para figuras recortadas.
- Olhos como pequenos pontos/ovais escuros; sobrancelhas em arcos curtos; nariz
  em curva ou pequeno ângulo; boca de poucos traços ou área escura simples.
  Cabelos e barbas em massas sólidas, sem fios individuais. Óculos simplificados.
- Expressões acolhedoras ou concentradas, gestos compreensíveis. Varie idade,
  gênero, pele, cabelo, roupa e acessórios mantendo a mesma gramática de desenho.
  Não introduza médico, jaleco ou computador se o novo tema não os justificar.
- Cores em áreas predominantemente planas, foscas e pouco saturadas; pequenas
  variações tonais de impressão são aceitáveis. Pouca modelagem de volume.
  Massas escuras em cabelo, contornos e algumas roupas equilibram áreas claras.
- Fundo claro com grão fino e discreto de papel, também perceptível nas áreas
  de cor. Aparência de impressão editorial suave, sem sujeira ou envelhecimento
  agressivo. A textura não deve prejudicar olhos, dedos ou limites dos objetos.
- Composição narrativa clara: uma ação principal, poses relacionadas e poucos
  objetos significativos. Vista frontal ou em três quartos, perspectiva simples,
  profundidade sugerida por sobreposição. Preserve respiro entre silhuetas.
- Preserve a lógica compositiva, não a disposição literal dos anexos: dupla
  com intervalo, comparação em dois campos, grupo em torno de uma atividade ou
  pessoa explicando algo. Adapte enquadramento e distribuição ao novo formato.

## Parâmetros variáveis

| Parâmetro | Padrão se omitido | Como variar |
|---|---|---|
| `tema` | O assunto do pedido | Educação, natureza, cultura, cotidiano, negócios etc. |
| `mensagem` | Uma ideia principal | Colaboração, contraste, descoberta, acolhimento etc. |
| `acao` | Interação simples e legível | Plantar, cozinhar, ler, planejar, consertar, conversar |
| `personagens` | 2–4 quando o pedido comportar um grupo | Quantidade, aparência, roupas, gestos e relações |
| `cenario` | Fundo claro e poucos indícios espaciais | Interior, exterior, oficina, biblioteca, jardim etc. |
| `objetos` | 1–3 objetos essenciais | Trocar o vocabulário inteiro conforme o tema |
| `paleta` | Creme, areia, ocre, castanho escuro | 3–5 famílias cromáticas; neutros e tons de pele adicionais conforme necessário |
| `acento` | Opcional, azul-petróleo dessaturado | Uma cor de destaque subordinada à ação |
| `composicao` | Grupo em atividade compartilhada | Dupla, comparação, cena coletiva, personagem isolado |
| `formato` | Paisagem 3:2 | Quadrado, retrato, banner; recompor sem esticar |
| `area_livre` | Respiro ao redor das cabeças | Especificar região para título inserido depois |
| `textura` | Fina e discreta | Reduzir ou elevar levemente sem ocultar o traço |
| `fundo` | Claro e opaco | Transparente se solicitado; manter textura dentro das formas |
| `cantos` | Retos | Arredondados somente quando desejado para o uso final |
| `texto` | Nenhum | Somente o texto exato solicitado |
| `continuidade` | Mesma família visual | Se personagem recorrente, conservar referência e ficha de aparência |

As paletas devem ser definidas por função: fundo claro, contorno escuro, base,
acento e pele. Mudar para azul ou lilás não significa tingir todas as peles.
Valores hexadecimais são alvos aproximados em geração, não garantia de cor exata.
Se o usuário pedir cores vivas, adapte-as mantendo o acabamento fosco, contraste
do traço e hierarquia de cores. Uma paleta nova não muda desenho nem anatomia.

## Prompt-base

Substitua todos os campos entre chaves pelo pedido resolvido. Remova campos
inaplicáveis. Se usar referências visuais, nomeie os anexos efetivamente enviados.

```text
Crie uma ilustração editorial 2D original sobre {tema}, comunicando {mensagem}.
Cena: {personagens} realizando {acao} em {cenario}, com {objetos}.
Composição: {composicao}, enquadramento {formato}, com {area_livre}.

Siga a linguagem visual das referências anexadas: contornos contínuos escuros,
espessos, arredondados e de peso consistente; formas simples e orgânicas;
personagens de proporções adultas estilizadas, cabeças moderadamente grandes,
rostos com olhos pequenos ovais, sobrancelhas curtas, nariz e boca simplificados;
cabelos em massas sólidas; mãos simplificadas e gestos claros. Preserve esse
traço, a escala relativa dos detalhes e a construção das figuras ao trocar o tema.

Use cores predominantemente planas e foscas, contraste por massas escuras,
profundidade discreta por sobreposição e perspectiva simples. Paleta por função:
{paleta}. Acento: {acento}. Fundo: {fundo}. Textura: {textura}, semelhante a papel
impresso de granulação fina, inclusive nos preenchimentos, sem borrar contornos.
Clima humano e acolhedor; uma ação principal e objetos reduzidos ao essencial.
Acabamento dos cantos: {cantos}. Texto: {texto}.

As referências orientam estilo e composição, não o assunto. Use exclusivamente
os personagens, objetos e contexto da cena descrita; não herde símbolos de
medicina, odontologia ou tecnologia sem relação com o tema solicitado.

Evite fotografia, render 3D, luz cinematográfica, brilho plástico, gradientes
volumétricos, anatomia realista detalhada, olhos de anime, proporções chibi,
membros exageradamente longos, line art fino, vetorial estéril sem textura,
rabiscos, aquarela escorrida, hachuras densas, ruído grosseiro, excesso de objetos,
logos ou textos não solicitados, mãos fundidas e membros extras.
```

Para prompts sem entradas visuais, remova a menção a anexos e conserve a descrição
completa. Informe que a fidelidade fica menos ancorada. Para ferramentas sem
campo de negativos, mantenha os anti-padrões no próprio prompt.

## Continuidade e revisão

Em séries, reutilize a mesma referência de estilo, papéis da paleta, peso do
contorno e escala dos rostos. Para um personagem recorrente, registre cabelo,
rosto, pele, roupa, acessórios e proporções; use uma imagem aprovada dele como
referência adicional quando possível. Sem isso, não garanta identidade exata.

Inspecione a imagem gerada antes de concluir:

- A nova cena e os objetos correspondem ao tema, sem herança médica automática?
- Contorno, rostos e proporções continuam compatíveis com os anexos?
- Cores foscas, grão fino e fundo atendem ao pedido sem excesso de volume?
- A ação se entende, os gestos são plausíveis e silhuetas não se confundem?
- O enquadramento preserva áreas livres e não corta mãos ou rostos sem intenção?
- Há logos, texto indesejado, membros extras ou objetos fundidos?

Se houver desvio claro, faça uma correção dirigida preservando as partes boas.
Após até duas correções sem resolver, apresente a limitação específica em vez
de repetir indefinidamente. Pedidos explícitos de novas iterações podem continuar.
Entregue a imagem e uma indicação breve da paleta/cena; exponha o prompt completo
se solicitado. Não afirme ter validado visualmente o que não conseguiu abrir.

Leia [exemplos de uso](references/exemplos.md) quando precisar de variações de
paleta, composição ou continuidade; não use seus temas como padrões obrigatórios.
