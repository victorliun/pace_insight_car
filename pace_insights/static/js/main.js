(function(){
    var app = angular.module('finnacialOptions', [])

    .controller('CompareFormController', ['$scope', '$http', 
        function($scope, $http){
        $scope.carmakes = [];
        $scope.carModels = [];
        $scope.carVersions = [];
        $scope.compCtrl.hp = {};
        $scope.compCtrl.pcp = {};
        $scope.compCtrl.lease = {};
        $scope.compCtrl.loan = {};
        var params = {'format': 'json'};
        $http.get('/depreciation/carmakes/', { params: params }
            ).success(
            function(response) { 
                // console.log(response[0]);
                $scope.carmakes = response;
                $scope.carMake = response[0];
                $scope.updateCarModel(response[0]);
            }).error(
                function(failure) { console.log("failed :(", failure); }
        );
        $scope.updateCarModel = function(car_make){
            var _new_param = {'format': 'json', 'car_make': car_make['id']};
            $http.get('/depreciation/carmodels/', { params: _new_param}).
            success(function (data) {
                $scope.carModels = data;
                $scope.carModel = data[0];
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
                $scope.carVersion = data[0];
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
                // console.log(data);
                $scope.depreciation = data[0];
                $scope.compCtrl.depreciationId = $scope.depreciation['id'];
                var d = $scope.depreciation['year_0_mock'];
                $scope.compCtrl.totalPrice = parseInt(d.replace(',','').replace('£',''));
                var last_price = parseInt($scope.depreciation['year_4_mock']
                    .replace(',','').replace('£',''));
                $scope.compCtrl.pcp.ballon_value = Math.round(last_price * 0.9);
            }).
            error(
                function(failure) { console.log("failed :(", failure); }
            );
        };

        $scope.submit = function(){
            // console.log($scope.compCtrl);
            var params = $scope.compCtrl;
            $scope.submitted = true;
            if ($scope.compareForm.$invalid)
                return false;
            $http.get('/depreciation/api/get-graph-data', {params: params})
            .success(function(data){
                // console.log(data);
                angular.element(document.querySelectorAll("div.payGraph")).html('');
                create_graph(data);
                $scope.compCtrl.showGraph = 'True';
                $scope.result = data;
                $scope.submitted = false;
            }).
            error(
                function(failure) { console.log("failed :(", failure); }
            );
        };
        $scope.$watch('compCtrl.extraPrice', function(newValue, oldValue) {
          $scope.compCtrl.lease.extras = newValue;
        });

        $scope.sortByTotalCost = function(val){
            return val["Total Cost for Comparison"];
        };

    }]);



})();