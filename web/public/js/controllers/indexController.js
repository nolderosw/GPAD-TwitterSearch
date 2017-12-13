var app = angular.module('app',[]);
app.controller('indexController', function($scope, $http, $rootScope, $window) {
    $rootScope.location = {}
    $rootScope.radius_circle = 1000;
    $scope.twitters = [];
    $scope.chama_python = function (){
        $http({
            url: 'http://localhost:3000',
            method: "POST",
            data: {location: $rootScope.location, raio: $rootScope.radius_circle},
        })
        .then(function(response) {
            console.log(response.data.Resultado);
            $scope.twitters = response.data.Resultado;
        });
    }
    $scope.muda_raio = function (value){
        if(!value){
            $rootScope.radius_circle = parseInt(1000);
        }
        else{
            $rootScope.radius_circle = parseInt(value);
        }
    }
});