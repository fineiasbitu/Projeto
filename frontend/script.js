var produtos = [
    {
        imagem:'https://cf.shopee.com.br/file/9d7bb814b51ff7699407dd4faaab7de5',
        nome:'Mochila de costas Louis Vuitton',
        texto:'Mochila com design moderno e elegante.'
    },
    {
        imagem:'https://images-shoptime.b2w.io/produtos/4155146995/imagens/bolsa-cross-body-victoria-s-secret-v-quilt-shoulder-bag-preta-corrente/4155146995_1_large.jpg',
        nome:'Bolsa transversal Victoria Secrets branca',
        texto:'Bolsa ideal para todas as ocasiões.'
    },
    {
        imagem:'https://cf.shopee.com.br/file/95c9ab3ce265ee3dbd499a9d80ad2ba6',
        nome:'Bolsa transversal corrente Victor Hugo',
        texto:'Bolsa de alta qualidade com design arrojado e moderno.'
    },
    {
        imagem:'https://passoapasso.com/wp-content/uploads/2017/01/Bolsas-importadas-01.jpg',
        nome:'Bolsa tiracolo Louis Vuitton',
        texto:'Design e sofisticação.'
    }, {
        imagem:'https://cdn.fashiola.mx/L541594094/gucci-bolso-ophidia-gg-supreme.jpg',
        nome:'Bolsa transversal da Gucci',
        texto:'Bolsa de luxo da alta moda.'
    },
    {
        imagem:'https://images-na.ssl-images-amazon.com/images/I/A17ltad0vCL._UX500_.jpg',
        nome:'Bolsa Michael Kors',
        texto:'Bolsa MK luxo e sofisticação.',
    }
]

produtos.map((produto) => {
    document.getElementById('produtos').innerHTML += `
        <div class="produto">   
            <img src="${produto.imagem}">
            <div>
                <h2>${produto.nome}</h2>
                <hr>
                <p>${produto.texto}</p>
            </div>
            <a href="./tabela.html">Comprar</a>
        </div>
    `
        // O botão de comprar foi tirado da div interna
        // e jogado para a div .produto
})


