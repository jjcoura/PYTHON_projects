function carregar() {
    var bicho = document.getElementById('txtani').value.toLowerCase();
    var img = document.getElementById('imagem');

    if (bicho === 'cachorro' || bicho === 'cao' || bicho === 'toto' || bicho === 'totó' || bicho === 'cão') {
        // Cachorro
        img.src = 'ft-cao.png';
        document.body.style.backgroundColor = '#c2734a';
    } else if (bicho === 'gato' || bicho === 'bichano' || bicho === 'cat' || bicho === 'gata') {
        // Gato
        img.src = 'ft-gato.png'
        document.body.style.backgroundColor = '#9e9283';
    } else if (bicho === 'porco' || bicho === 'leitão' || bicho === 'leitao' || bicho === 'suíno' || bicho === 'porca' || bicho === 'leitoa' || bicho === 'suino') {
        // Porco
        img.src = 'ft-porco.png'
        document.body.style.backgroundColor = '#e0909d'
    } else {
        // BICINHO NÃO ENCONTRADO!!!
        img.src = 'imagem-nao-encontrada.png';
        document.body.style.backgroundColor = '#f5f5f5';
    }
}