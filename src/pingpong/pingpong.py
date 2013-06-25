from kaylee.project import Project, AUTO_PROJECT_MODE
from kaylee.errors import InvalidResultError

class PingPong(Project):

    def __init__(self, *args, **kwargs):
        super(PingPong, self).__init__(mode=AUTO_PROJECT_MODE, *args, **kwargs)
        self.tasks_count = kwargs['tasks_count']

        self.client_config.update({
            'pong_latency': kwargs['pong_latency']
        })
        self._tasks_counter = 0

    def __getitem__(self, task_id):
        return {
            'id' : task_id
        }

    def next_task(self):
        if self._tasks_counter < self.tasks_count:
            self._tasks_counter += 1
            return self[self._tasks_counter]
        else:
            return None

    def normalize_result(self, task_id, result):
        try:
            return int(result['pong'])
        except KeyError:
            raise InvalidResultError(result, '"pong" key was not found')
        except ValueError:
            raise InvalidResultError(result, 'The result is invalid.')

    def result_stored(self, task_id, data, storage):
        if len(storage) == self.tasks_count:
            self.completed = True
            self._announce_results(storage)

    def _announce_results(self, storage):
        print('{} ping-pongs with {}ms latency have been completed'
              .format(len(storage), self.client_config['pong_latency']))
