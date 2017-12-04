const PythonShell = require('python-shell');
const path = require('path');
const bodyParser = require('body-parser');

exports.get = (req, res, next) => { 
    res.sendFile(path.join(__dirname, '../', '../public/views', 'index.html'));
};
exports.postFromPython = (req, res, next) => {
    var options = {
        args: [req.body.location.lat, req.body.location.lng], 
      };  
      PythonShell.run('../Exemplos/teste.py', options, function (err, results) {
          if (err) throw err;
          // results is an array consisting of messages collected during execution
          res.status(201).send({Resultado: results});
      });
};
