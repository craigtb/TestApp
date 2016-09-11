var app = angular.module('TestApp', ['ngRoute']);

app.config(function($routeProvider, $httpProvider) {
    $httpProvider.defaults.withCredentials = true;
    $routeProvider
        .when('/', {
            controller: 'homePageController as homePage',
            templateUrl: 'homepage.html'
        })
        .otherwise({
            redirectTo: '/'
        })
});
