function verificar(){
    var data = new Date()
    var ano  = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res  = document.querySelector('div#res')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('[ERRO!] Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var gênero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            gênero = 'Homem'
            if (idade >= 0 && idade < 10) {
                // CRIANÇA
                img.setAttribute('src', 'foto-crianca-m.png')
            } else if (idade < 21){
                // JOVEM
                img.setAttribute('src', 'foto-jovem-m.png')
            }  else if (idade < 50){
                // ADULTO
                img.setAttribute('src', 'foto-adulto-m.png')
            } else {
                // IDOSO
                img.setAttribute('src', 'foto-idoso-m.png')
            }
        } else if (fsex[1].checked) {
            gênero = 'Mulher'                        
            if (idade >= 0 && idade < 10) {
                // CRIANÇA
                img.setAttribute('src', 'foto-crianca-f.png')
            } else if (idade < 21){
                // JOVEM
                img.setAttribute('src', 'foto-jovem-f.png')
            }  else if (idade < 50){
                // ADULTO
                img.setAttribute('src', 'foto-adulto-f.png')
            } else {
                // IDOSO
                img.setAttribute('src', 'foto-idoso-f.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos.`
        res.appendChild(img)
    }
}