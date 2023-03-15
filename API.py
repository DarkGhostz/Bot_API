from flask import Flask,  request
import json



app = Flask(__name__)



animes = [
    {
        'id': 11,
        'titulo': 'Attack on Titan',
        'autor': ' Hajime Isayama',
        'sobre': 'Os seres humanos se depararam com a repentina aparição dos Titãs no distrito de Shiganshina após mais de um século de paz. Eren Yeager, Mikasa Ackerman-sua irmã adotiva- e seu amigo de infância, Armin Arlert, testemunham o aparecimento de uma Titã de 60 metros, o Titã Colossal, e outro menor, o Titã Blindado, que abrem uma brecha na muralha Maria. Os Titãs, em seguida, invadem a cidade e fazem uma carnificina, incluindo a morte da mãe de Eren, que é devorada diante de seus olhos. Ele então decide se vingar e matar todos os Titãs, entrando para Divisão de Exploração'

    },
    {
        'id': 10,
        'titulo': 'One Piece',
        'autor': 'Echiro Oda',
        'sobre': 'A série foca em Monkey D. Luffy, um jovem feito de borracha, que, inspirado em seu ídolo de infância, o poderoso pirata Shanks, o Ruivo, parte em uma jornada do mar do East Blue para encontrar o tesouro mítico, o One Piece, e proclamar-se o Rei dos Piratas.'

    },
    {
        'id': 9,
        'titulo': 'Pokemon',
        'autor': 'Satoshi Tajiri',
        'sobre': 'O nome Pokémon é uma abreviação da marca japonesa Pocket Monsters (ポケットモンスター Poketto Monsutā?). O termo Pokémon, além de se referir a própria franquia Pokémon, também se refere às mais de 900 espécies de ficção que aparecem na mídia de Pokémon. A palavra "Pokémon" é usada no singular e plural para o nome individual de cada espécie; a gramática correta é "um Pokémon" e "muitos Pokémon", bem como "um Pikachu" e "muitos Pikachu". (no entanto, em Pokémon Red, Blue e Yellow, alguns NPCs se referiam a Clefairy e Diglett no plural, mostrando "CLEFAIRYs" and "DIGLETTs", respectivamente. Isso foi arrumado em FireRed e LeafGreen.)'

    },
    {
        'id': 8,
        'titulo': 'Naruto',
        'autor': 'Masashi Kishimoto',
        'sobre': 'Naruto (ナルト) é uma série de mangá escrita e ilustrada por Masashi Kishimoto, que conta a história de Naruto Uzumaki, um jovem ninja que constantemente procura por reconhecimento e sonha em se tornar Hokage, o ninja líder de sua vila.'

    },
    {
        'id': 7,
        'titulo': 'One Punch-Man',
        'autor': ' pseudónimo One',
        'sobre': 'A história se passa em cidades japonesas fictícias, especialmente na chamada de Cidade Z, onde aparecem com grande frequência seres monstruosos que causam vários desastres. Após treinar durante três anos, Saitama, o protagonista, se tornou um herói não oficial incrivelmente forte que derrota monstros ou outros vilões com um único soco. No entanto, devido à sua força esmagadora, Saitama tornou-se entediado e está constantemente tentando encontrar adversários mais fortes que podem lutar de igual contra ele.\n\Em seus combates, ele conhece novos amigos, inimigos e o seu próprio discípulo, o ciborgue Genos, onde posteriormente os dois entram na Associação dos Heróis, a fim de se tornarem heróis oficiais e ganharem reconhecimento e respeito por todos os seus esforços para manter as cidades a salvo. Apesar de derrotar seres extremamente fortes que até mesmo os maiores heróis da Associação são incapazes de derrotar, Saitama é desrespeitado devido a sua aparência física simples, e alguns o acusam de ser um herói falsificado. Apenas um pequeno número de indivíduos reconhecem seu incrível talento e humildade com os outros.'

    },
    {
        'id': 6,
        'titulo': 'Boku no Hero Academia',
        'autor': ' Kōhei Horikoshi',
        'sobre': 'Em um mundo onde 80 porcento da população mundial possuem super poderes, o tímido estudante Midoriya Izuku teve a infelicidade de nascer sem poderes.Cap. 1 Grande fã do sorridente All Might, o herói conhecido como o símbolo da paz, Izuku, sofre com a frustração de saber que jamais terá uma individualidade especial para que possa se tornar, assim como seu grande ídolo, em um defensor dos fracos e oprimidos.\nMesmo sofrendo bullying por seus amigos de escola, como o arrogante Katsuki, o garoto nunca abandonou o herói existente dentro de si. Gentil e generoso, ele está sempre pronto a ajudar quem precisa.\nPorém, um inesperado encontro irá mudar o destino de Izuku. Destino esse que o levará a ingressar no tão sonhado colégio U.A., instituição para onde os grandes heróis vão estudar e treinar. A partir daí, as cortinas de uma fantástica aventura repleta de personagens cativantes e temerosos vilões se abrem para o jovem Midoriya.'

    },
    {
        'id': 5,
        'titulo': 'Dragon Ball ',
        'autor': 'Akira Toriyama',
        'sobre': 'A história de Dragon Ball começa com Son Goku, um garoto ingênuo e puro com cauda de macaco e uma força extraordinária. Ele mora sozinho após a morte de seu avô adotivo em uma montanha chamada Paozu. Um dia ele conhece Bulma, uma garota muito inteligente da cidade, que estava em busca das sete Esferas do Dragão. Persuadido, Goku concorda em ajudar Bulma a encontrar as Esferas. Os dois partem em uma longa jornada, durante a qual eles fazem muitos amigos. Depois, Goku passa por um treinamento com Kame-Sennin, onde o garoto Kuririn se torna seu parceiro, e participa de vários torneios mundiais de artes marciais. No curso de seu crescimento e seu desenvolvimento, ele enfrenta inúmeros inimigos, incluindo Piccolo,[2] que depois se torna seu aliado.[3] Quando jovem adulto, Goku se casa com Chi-Chi, cumprindo uma promessa feita por ele quando ambos eram crianças, e possui seu primeiro filho chamado Gohan.\n Goku acaba descobrindo que pertence à raça extraterrestre Saiyajin, e que foi enviado à Terra quando criança para conquistar o planeta.\n Pouco depois de sua chegada, no entanto, ele tinha sofrido um ferimento na cabeça, perdendo desta forma a memória da missão e sua natureza agressiva. No entanto, o jovem decide continuar a defender seu planeta adotado do ataque de inimigos cada vez mais difíceis, incluindo o príncipe dos sayajins Vegeta, que depois também se torna seu aliado.\n Desta forma, juntamente com sua família e seus amigos, Goku luta contra inimigos como Freeza, Cell, Boo, entre outros, se tornando o protetor da Terra e todo o universo.'

    },
    {
        'id': 4,
        'titulo': 'Classroom of the Elite ',
        'autor': 'Shōgo Kinugasa',
        'sobre': 'Em um futuro não muito distante, o governo japonês estabeleceu a Tokyo Metropolitan Advanced Nurturing School, dedicada a instruir e formar a geração de pessoas que sustentarão o país no futuro. Os alunos recebem um alto grau de liberdade a fim de imitar a vida real o mais próximo possível.\nA história segue a perspectiva de Ayanokōji Kiyotaka, um garoto quieto e despretensioso que não é bom em fazer amizades e prefere manter distância. Ele é um estudante de classe D, que é onde a escola despeja seus alunos inferiores. Depois de encontrar Suzune Horikita e Kikyō Kushida, duas outras alunas de sua turma, a situação de Ayanokōji começa a mudar.'

    },
    {
        'id': 3,
        'titulo': 'DrStone',
        'autor': ' Riichiro Inagaki',
        'sobre': 'Taiju, um típico estudante japonês, diz a seu amigo Senku, que ama a ciência, que ele está finalmente prestes a confessar a Yuzuriha, com quem ele esteve secretamente apaixonado por cinco anos. Encontrando-se debaixo de uma árvore de cânfora nos terrenos da escola, assim como Taiju está prestes a confessar, uma luz brilhante aparece no céu. Taiju empurra Yuzuriha para a árvore para protegê-la, mas a luz de repente petrifica toda a humanidade, com todos os humanos na Terra se transformando em pedra. A maioria dos humanos começa a perder sua consciência enquanto todos os vestígios de civilização decaem, mas Taiju continua vivo enquanto os anos progridem por sua motivação de libertar a si mesmo e a Yuzuriha. Eventualmente, Taiju se liberta da pedra e encontra uma mensagem esculpida na árvore que o leva a descobrir que Senku também escapou da pedra, mantendo sua consciência viva contando há quanto tempo ele foi petrificado. Assim, Taiju descobre que a data é agora 5 de outubro de 5738.'

    },
    {
        'id': 2,
        'titulo': 'GENJITSU SHUGI YUUSHA NO OUKOKU SAIKENKI',
        'autor': 'Dojyomaru',
        'sobre': ' Ó, HERÓI!\n\nQuando Kazuya Souma é inesperadamente transportado para outro mundo, ele sabe que as pessoas esperam um herói. Mas a ideia de heroísmo de Souma é mais prática do que a maioria - ele quer reconstruir a economia decadente da nova terra em que se encontrou! Noivo da princesa e repentinamente colocado no trono, este herói realista deve reunir pessoas talentosas para ajudá-lo a colocar o país de pé novamente - não por meio de guerra ou aventura, mas com reforma administrativa!'

    },
    {
        'id': 1,
        'titulo': 'Bleach',
        'autor': ' Tite Kubo',
        'sobre': 'Ichigo Kurosaki é um estudante de 15 anos que tem uma estranha capacidade de ver, tocar e falar com espíritos de pessoas mortas. Numa noite, Ichigo encontra uma shinigami (adaptado na dublagem brasileira como "Ceifeiro de Almas") — personificação japonesa do deus da morte — chamada Rukia Kuchiki, e esta se surpreende por ele poder vê-la. A conversa entre os dois é interrompida pela aparição de um Hollow, entidade espiritual maligna. Rukia é gravemente ferida ao tentar proteger Ichigo, e então, como último recurso, ela decide transferir parte de seus poderes a ele, para que este então pudesse enfrentar o Hollow de igual para igual e proteger sua família. Ichigo acidentalmente acaba absorvendo os poderes de Rukia por completo devido ao seu poder espiritual, e assim consegue vencer facilmente o espírito maligno. No dia seguinte, Rukia aparece na escola de Ichigo, como uma humana de aparência normal, usando um gigai (material que permite os espíritos poderem conviver no mundo humano sendo vistos e podendo tocar objetos). Ela informa que devido ao fato de Ichigo ter absorvido seus poderes, ela não poderia voltar ao mundo pós-morte (Soul Society ou Sociedade das Almas em português) até recuperar totalmente sua força de shinigami.'
    }

]
#Obter todos animes
@app.route('/animes',methods=['GET'])
def obter_animes():
    return json.dumps(animes, indent=4)

#Obter anime por id
@app.route('/animes/<int:id>',methods=['GET'])
def obter_id(id):
    for anime in animes:
        if anime.get('id') == id:
            return json.dumps(animes, indent=4)
        

#Editar anime por id
@app.route('/animes/<int:id>',methods=['PUT'])        
def editar_anime(id):
    anime_alterado = request.get_json()
    for indice,anime in enumerate(animes):
        if anime.get('id') == id:
            animes[indice].update(anime_alterado)
            return json.dumps(animes[indice], indent=4)


#incluir anime        
@app.route('/animes',methods=['POST']) 
def incluir_anime():
    novo_anime = request.get_json()
    animes.append(novo_anime)
    return json.dumps(animes, indent=4)

#excluir anime 
@app.route('/animes/<int:id>',methods=['DELETE'])
def excluir_anime(id):
    for indice, anime in enumerate(animes):
        if anime.get('id') == id:
           del animes[indice]
    return json.dumps(animes, indent=4)       



app.run(port=5000,host='localhost',debug=True)