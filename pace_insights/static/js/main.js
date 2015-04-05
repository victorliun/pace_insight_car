(function(){
    var app = angular.module('finnacialOptions', [])

    .controller('CompareFormController', ['$scope', '$http', function($scope, $http){
        $scope.carmakes = [];
        $scope.carModels = [];
        $scope.carVersions = [];
        var params = {'format': 'json'};
        $http.get('/depreciation/carmakes/', { params: params }
            ).success(
            function(response) { 
                console.log(response[0]);
                $scope.carmakes = response;
                $scope.compCtrl.carMake = response[0];
                $scope.updateCarModel(response[0]);
            }).error(
                function(failure) { console.log("failed :(", failure); }
        );
        $scope.updateCarModel = function(car_make){
            var _new_param = {'format': 'json', 'car_make': car_make['id']};
            $http.get('/depreciation/carmodels/', { params: _new_param}).
            success(function (data) {
                $scope.carModels = data;
                $scope.compCtrl.carModel = data[0];
                $scope.updateCarVersion(data[0]);
            }).
            error(
                function(failure) { console.log("failed :(", failure); }
            );
        };

        $scope.updateCarVersion = function(car_model){
            var _new_param = {'format': 'json', 'car_model': car_model['id']};
            $http.get('/depreciation/carversions/', { params: _new_param}).
            success(function (data) {
                $scope.carVersions = data;
                $scope.compCtrl.carVersion = data[0];
                $scope.updateDepreciation(data[0]);
            }).
            error(
                function(failure) { console.log("failed :(", failure); }
            );
        };

        $scope.updateDepreciation = function(car_version){
            var _new_param = {'format': 'json', 'car_version': car_version['id']};
            $http.get('/depreciation/depreciations/', { params: _new_param}).
            success(function (data) {
                console.log(data);
                $scope.depreciation = data[0];
            }).
            error(
                function(failure) { console.log("failed :(", failure); }
            );
        };

        $scope.submit = function(){
            console.log($scope);
        }
    }]);


})();