# Prompt e parâmetros

Consulte ao preparar uma geração ou edição nesta família visual.

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
