(function() {
     
var pj = kl.pj;
     

pj.init = function(app_config) {
    pj.config = app_config;
    kl.include(app_config.alea_script, kl.project_imported.trigger);
};
     

pj.process_task = function(task) {
    var random = new Alea(task.id);
    var counter = 0;
    for (var i = 0; i < pj.config.random_points; i++) {
        var x = random();
        var y = random();
        if (x * x + y * y <= 1) {
            counter += 1;
        }
    }
    var pi = 4 * counter / pj.config.random_points;

    kl.task_completed.trigger({pi: pi});
};     

}());
