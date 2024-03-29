# Algoritmos de Busca
* Resolover problemas usando os algoritmos de busca, os componentes para uma busca são "1- estado inicial, 2- estado final, 3- espaço de estados, 4- ações para passar de um estado para o outro, 5- solução que leva do estado inicial ate o final". Algoritmos de busca em inteligência artificial são técnicas computacionais que permitem encontrar soluções para problemas por meio da exploração sistemática de um espaço de busca, que é um conjunto de estados ou configurações possíveis. Esses algoritmos são fundamentais para resolver uma ampla variedade de problemas em IA, como encontrar caminhos em mapas, planejar trajetórias de robôs, otimizar recursos, entre outros. Ex: Encontrar a menor rota para ir de uma cidade até outra. Escolher qual a melhor jogada

![()](../../imagens/algoritmos_de_busca.PNG)

![()](../../imagens/componentes_problema.PNG)

### Heuristica
* Técnica que ajuda a resolver problemas complexos ou a tomar decisões informadas usando regras práticas, abordagens aproximadas ou regras simplificadas. Em algoritmos de busca, as heurísticas são usadas para estimar a qualidade de uma solução ou guiar o processo de busca na direção mais promissora, economizando tempo e recursos.

![()](../../imagens/heuristicas.PNG)

### Busca Gulosa
* A busca gulosa, também conhecida como busca heurística ou busca voraz, é um tipo de algoritmo de busca utilizado em inteligência artificial e em algoritmos de busca. Ela se caracteriza por tomar decisões baseadas apenas em informações locais e na busca pelo estado que parece ser o mais promissor no momento, sem considerar o futuro a longo prazo. Em outras palavras, a busca gulosa foca exclusivamente na maximização de uma heurística específica, ignorando potenciais consequências a longo prazo.

### Busca A Estrela (A*)
* O algoritmo A* (pronunciado "A estrela") é um algoritmo de busca informada que é amplamente usado em inteligência artificial e em uma variedade de aplicações de otimização, especialmente em problemas de busca de caminho, como jogos, robótica, planejamento de trajetórias e roteamento em redes. O A* é uma extensão da busca gulosa que combina a busca em largura com uma heurística para encontrar o caminho mais curto ou a solução mais eficiente para um problema.