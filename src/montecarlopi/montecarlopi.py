from kaylee.project import Project, AUTO_PROJECT_MODE
from kaylee.errors import InvalidResultError

class MonteCarloPi(Project):

    def __init__(self, *args, **kwargs):
        super(MonteCarloPi, self).__init__(mode=AUTO_PROJECT_MODE, *args, **kwargs)
        self.client_config.update({
            'alea_script'   : kwargs['alea_script'],
            'random_points' : kwargs['random_points']
        })
        self.tasks_count = kwargs['tasks_count']
        self._tasks_counter = 0

    def __getitem__(self, task_id):
        return { 'id' : task_id }

    def next_task(self):
        if self._tasks_counter < self.tasks_count:
            self._tasks_counter += 1
            return self[self._tasks_counter]
        else:
            return None

    def normalize_result(self, task_id, data):
        try:
            return data['pi']
        except KeyError:
            raise InvalidResultError(data, '"pi" key was not found')

    def result_stored(self, task_id, data, storage):
        if len(storage) == self.tasks_count:
            self.completed = True
            self._announce_results(storage)

    def _announce_results(self, storage):
        mid_pi = (sum(res[0] for res in storage.values()) / len(storage))
        print('The  value of PI computed by the Monte-Carlo method is: {}'
              .format(mid_pi))
