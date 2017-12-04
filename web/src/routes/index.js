const express = require('express'); //importando o express para criar uma rota
const router = express.Router(); //criando uma rota com o express
const controller = require('../controllers/index');

router.get('/', controller.get);
router.post('/', controller.postFromPython);

module.exports = router; //exportando o modulo