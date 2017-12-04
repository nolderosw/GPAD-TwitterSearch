const express = require('express'); //importando o express para criar uma rota
const router = express.Router(); //criando uma rota com o express
const controller = require('../controllers/index');
const path = require('path');
const PythonShell = require('python-shell');

router.get('/', function(req, res, next) {
    res.sendFile(path.join(__dirname, '../', '../public/views', 'index.html'));
});

router.get('/getPython', function(req, res, next) {
  var options = {
    args: ['Hello', 'World']
  };  
  PythonShell.run('../Exemplos/teste.py', options, function (err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      res.send({Resultado: results});
    });
});

module.exports = router; //exportando o modulo