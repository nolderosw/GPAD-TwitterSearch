exports.get = (req, res, next) => { 
   res.status(200).send({ //enviando uma resposta para a requisição, 200 quer dizer que foi tudo ok
        title: "Node Store API",
        version: "0.0.2"
    })
}
