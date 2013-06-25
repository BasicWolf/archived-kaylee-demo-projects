pj = kl.pj

pj.init = (app_config) ->
    pj.config = app_config
    kl.project_imported.trigger()
    return

pj.process_task = (task) ->
    kl.util.after(pj.config.pong_latency, () ->
        kl.task_completed.trigger({pong: task.id}))
    return