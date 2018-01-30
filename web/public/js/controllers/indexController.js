var app = angular.module('app', []);
app.controller('indexController', function ($scope, $http, $rootScope, $window, $timeout) {
    $rootScope.location = {}
    $rootScope.radius_circle = 1000;
    $scope.twitters = [];
    var grafico_barra;
    var grafico_pie;
    $scope.pesquisando = false;

    $scope.muda_raio = function (value) {
        if (!value) {
            $rootScope.radius_circle = parseInt(1000);
        }
        else {
            $rootScope.radius_circle = parseInt(value);
        }
    }
    $scope.chama_botao = function() {
        $timeout( function(){
            $scope.$apply(function () {
                $scope.pesquisando = true;
            });
        }, 100);
    }
    $scope.chama_python = function () {
        $http({
            url: 'http://localhost:3000',
            method: "POST",
            data: { location: $rootScope.location, raio: $rootScope.radius_circle },
        })
            .then(function (response) {
                if (!response.data.Resultado) {
                    alert("Não foram encontrados Twitters!");
                }

                var data = String(response.data.Resultado[response.data.Resultado.length - 1]).replace('[', '').replace(']', '').split(',');
                /*
                for(var i = 0; i < response.data.Resultado[response.data.Resultado.length-1].length; i++){
                    data.push(response.data.Resultado[response.data.Resultado.length-1][i])
                }*/
                resposta_final = response.data.Resultado.splice(response.data.Resultado.length - 1, 1);
                $scope.twitters = response.data.Resultado;

                grafico_barra.data.datasets[0].data = data;

                grafico_barra.update();

                var data2 = data.splice(data.length-1,1);

                var data3 = [];

                for(var i = 0; i < data.length; i++){
                    data3.push(parseFloat(data[i]/data2*100).toFixed(2));
                }

                grafico_pie.data.datasets[0].data = data3;
                grafico_pie.update();
                $scope.pesquisando = false; 
            });
    }
    $(document).ready(function () {
        //grafico 1 (em barras)
        var ctx = document.getElementById("myChart").getContext('2d');
        var ctx2 = document.getElementById("myChart2").getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["Baixa", "Média", "Alta"],
                datasets: [
                    {
                        data: [],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(54, 162, 235, 1)',
                        ],
                        borderWidth: 1
                    }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                },
                legend: {
                    display: false
                },
                tooltips: {
                    callbacks: {
                        label: function (tooltipItem) {
                            return tooltipItem.yLabel;
                        }
                    }
                },
                title: {
                    display: true,
                    text: 'Twitters por chance de indicarem febre amarela'
                }
            }
        });

        var myPieChart = new Chart(ctx2,{
            type: 'pie',
            data: {
                labels: ["Baixa", "Média", "Alta"],
                datasets: [
                    {
                        data: [],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                        ],
                        borderColor: [
                            'rgba(255,99,132,1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(54, 162, 235, 1)',
                        ],
                        borderWidth: 1
                    }
                ]
            },
            options: {
                title: {
                    display: true,
                    text: 'Twitters por chance de indicarem febre amarela'
                },
                tooltips: {
                    mode: 'label',
                    callbacks: {
                        label: function(tooltipItem, data) {
                            return data['datasets'][0]['data'][tooltipItem['index']] + '%';
                        }
                    }
                }

            }
        });
        grafico_pie = myPieChart;
        grafico_barra = myChart;
    });
});