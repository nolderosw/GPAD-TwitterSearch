//importação de pacotes
const app = require('../src/app'); //está em um arquivo separado na pasta src
const debug = require('debug')('nodestr:server');
const http = require('http');

//criando uma porta para o servidor escutar
const port = normalizePort(process.env.PORT || '3000');
app.set('port', port); //setando a porta para a aplicação a partir da função normalize port

const server = http.createServer(app); //criando um servidor a partir do app do express

server.listen(port); //fazendo com que o servidor escute a porta que foi setada
server.on('error', onError); //quando acontecer algum erro chame a função onError
server.on('listening', onListening);
console.log('API rodando na porta' + port); //dando um log pra dizer que o server rodou tudo ok!

function normalizePort(val){ //função que verifica se a prota 3000 está disponível
    const port = parseInt(val,10);

    if(isNaN(port)){
        return val;
    }

    if(port >= 0){
        return port;
    }

    return false;
}

function onError(error){ //função para verificar se teve algum erro ao iniciar o servidor, nesse caso erro de privilegio ou de porta ja usada!
    if (error.syscall !== 'listen'){
        throw error;
    }

    const bind = typeof port === 'string' ? 'Pipe ' + port : 'Port ' + port;

    switch(error.code){
        case 'EACCES':
            console.error(bind + ' requires elevated privileges');
            process.exit(1);
            break;
        case 'EADDRINUSE':
            console.error(bind + ' is alredy in use');
            process.exit(1);
            break;
        default:
            throw error;
    }
}

function onListening(){ //função para colher informações do servidor e startar o debug!
    const addr = server.address();
    const bind = typeof addr === 'string' ? 'pipe ' + addr : 'port ' + addr.port;

    debug('Listening on '+ bind);
}
