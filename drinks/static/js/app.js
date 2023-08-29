let app = angular.module("fnbApp", []);
app.controller("mainCtrl", function($scope, $http) {
    $scope.items = $http.get('http://localhost:8000/api/food/1').then(function(data){
        $scope.items = data;
    });

})
//     $scope.items = []

//     $scope.getItems = function(){
//         $http.get('http://localhost:8000/drinks/').then(function(data){
//             $scope.items = data;
//         });
//     }
// }