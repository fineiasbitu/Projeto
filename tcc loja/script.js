const botao = document.querySelector("#botao-carregar");
const tabela = document.querySelector("#tabela-produtos_loja");

botao.addEventListener("click", function () {
  carregarDados();
});
function carregarDados() {
    fetch("http://127.0.0.1:5000/todos")
      .then(function (resposta) {
        return resposta.json();
      })
      .then(function (listaprodutos_loja) {
        popularTabela(listaprodutos_loja);
      });
  }
  function popularTabela(listaprodutos_loja) {
    const tamanhoLista = listaprodutos_loja.length;
  
    for (let index = 0; index < tamanhoLista; index++) {
      const linha = document.createElement("tr");
  
      const id = document.createElement("td");
      const nome = document.createElement("td");
      const modelo = document.createElement("td");
      const cor = document.createElement("td");
      const tamanho = document.createElement("td");
      const quantidade = document.createElement("td");
      const preco = document.createElement("td");
  
      id.innerHTML = listaprodutos_loja[index][0];
      nome.innerHTML = listaprodutos_loja[index][1];
      modelo.innerHTML = listaprodutos_loja[index][2];
      cor.innerHTML = listaprodutos_loja[index][3];
      tamanho.innerHTML = listaprodutos_loja[index][4];
      quantidade.innerHTML = listaprodutos_loja[index][5];
      preco.innerHTML = listaprodutos_loja[index][6];
  
      linha.appendChild(id);
      linha.appendChild(nome);
      linha.appendChild(modelo);
      linha.appendChild(cor);
      linha.appendChild(tamanho);
      linha.appendChild(quantidade);
      linha.appendChild(preco);
      
      tabela.appendChild(linha);
    }
  }
  