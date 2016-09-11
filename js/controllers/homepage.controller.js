(function() {
    app.controller('homePageController', homePageController);

    function homePageController($http, $routeParams) {
	var homePage = this;
	homePage.message = "craig"
	$http.get('http://192.168.0.107:8000/craig')
                .success(function(data) {
                    console.log(data)
			homePage.message = data;
                })
    }
})();
