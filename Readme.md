<h1> API Times Brasileiros</h1>

<img src="https://a4.espncdn.com/combiner/i?img=%2Fi%2Fleaguelogos%2Fsoccer%2F500%2F85.png">
<h2> Descrição: </h2>
<p> 
Esta API utiliza o modelo arquitetural REST e é capaz de fornecer dados sobre os títulos da atual
elite do futebol brasileiro.
</p>

<h2> Status </h2>
<p> Finalizado </p>

<h2> Como acessar: </h2>

<ol>
<li> Clone o repostório.</li>
<li> Abra um editor de código python (Pycharm por exemplo).</li>
<li>Execute o arquivo main.py</li>
<li>
Após isto ele vai liberar um link http. Copie o link, adicione  
'/times' no final do link e cole no navegador.
</li>
* Você também pode utilizar este link para fazer requisições.
</ol>

<h2> Endpoints</h2>
<ul>
<li> 
http://seu-host/times (Retorna o número de títulos estaduais, nacionais e
continentais da atual Série A do campeonato brasileiro)
</li>

<li>
http://seu-host/times/estaduais (Retorna apenas o número de títulos estaduais)
</li>

<li>
http://seu-host/times/nacionais (Retorna apenas o número de títulos nacionais, como a
Copa do Brasil, o Brasileiro e a Supercopa do Brasil)
</li>

<li>
http://seu-host/times/continentais (Retorna apenas o número de títulos continentais, como a 
Libertadores, a Sul-Americana e a Recopa)
</li>

<Li>
http://seu-host/times/total (Retorna os valores de todos os endpoints anteriores)
</li>

</ul>


<h2> Detalhes </h2>
<p> É contado apenas os títulos de capeonatos que ainda existem.</p>
<h2>Técnicas e Tecnologias </h2>
<ul>
<li>Python</li>
<li>Criação e integração de API RESTful</li>
<li>Manipulação de dados de planilha Excel</li>
</ul>


<h2>Autores</h2>
<ul>
<li>Felipe Vieira da Silva</li>
</ul>
<h2> Licenças</h2>
<ul>

<li>MIT LICENSE</li>
</ul>