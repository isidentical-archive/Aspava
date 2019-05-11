from django_cron import CronJobBase, Schedule
from social.utils import quit_evality

class RenewEvalityCron(CronJobBase):
    RUN_EVERY_MINS = 1 

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'social.cronjobs.RenewEvalityCron'

    def do(self):
        quit_evality()
