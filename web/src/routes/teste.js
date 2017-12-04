const express = require('express'); //importando o express para criar uma rota
const router = express.Router(); //criando uma rota com o express
const controller = require('../controllers/teste');

router.get('/', controller.get); //configurando uma primeira rota!!

module.exports = router; //exportando o modulo