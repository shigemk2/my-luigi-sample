# tasks.py
# zsh
# PYTHONPATH='' luigi --local-scheduler --module tasks HelloWorld
# fish
# set -x PYTHONPATH '' ; luigi --local-scheduler --module tasks HelloWorld
import luigi

class HelloWorld(luigi.Task):
    def run(self):
        print('Hello, world!')
