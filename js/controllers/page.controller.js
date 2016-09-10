(function() {
    app.controller('pageController', pageController);

    function pageController($http, $routeParams) {
	var page = this;
	page.message = "craig"
	$http.get('http://192.168.0.107:8000/craig')
                .success(function(data) {
                    console.log(data)
			page.message = data;
                })
    }
})();
