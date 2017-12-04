const express = require('express'); //importando o express para criar uma rota
const router = express.Router(); //criando uma rota com o express
const controller = require('../controllers/index');
const path = require('path');

router.get('/', function(req, res, next) {
    res.sendFile(path.join(__dirname, '../', '../public/views', 'index.html'));
  });

module.exports = router; //exportando o modulo