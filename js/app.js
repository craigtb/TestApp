var app = angular.module('TestApp', ['ngRoute']);

app.config(function($routeProvider, $httpProvider) {
    $httpProvider.defaults.withCredentials = true;
    $routeProvider
        .when('/', {
            controller: 'pageController as page',
            templateUrl: 'page.html'
        })
        .otherwise({
            redirectTo: '/'
        })
});
