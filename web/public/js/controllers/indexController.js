var app = angular.module('app',[]);
app.controller('indexController', function($scope, $http, $rootScope, $window) {
    $scope.teste = "lol";
    $rootScope.location = {}
    $scope.chama_python = function (){
        $http({
            url: 'http://localhost:3000',
            method: "POST",
            data: {location: $rootScope.location},
        })
        .then(function(response) {
            console.log(response);
        });
    }
});