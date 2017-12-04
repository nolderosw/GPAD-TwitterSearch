const express = require('express'); //importando o express
const bodyParser = require('body-parser'); //importando o body parser para transformar o corpo da requisicao para um json
const mongoose = require('mongoose'); //instanciando o mongoose para gerenciar o mongodb
const path = require('path')

const app = express(); //criando um app com express
const router = express.Router(); //criando o sistema de rotas, para o usuario acessar a app a partir de uma url

//conectando com o banco de dados
mongoose.connect('mongodb://wesley150:147senha@ds125896.mlab.com:25896/teste_twitnode');

//carregando os models
// ex: const Product = require('./models/product');

//carrega as rotas
const testeRoute = require('./routes/teste');
const indexRoute = require('./routes/index');

app.use('/bower_components', express.static(path.join(__dirname, '../bower_components')))
app.use('/public', express.static(path.join(__dirname, '../public')))

app.use(bodyParser.json()); //todo conteudo do corpo da requisicao é convertido pra json
app.use(bodyParser.urlencoded({ extended: false })); //codificacao da url

//rotas paginas

//rotas serviços
app.use('/teste', testeRoute); //usando a rota route quando o usuario acessar '/'
app.use('/', indexRoute); //usando a rota route quando o usuario acessar '/'

module.exports = app; //exportando modulo