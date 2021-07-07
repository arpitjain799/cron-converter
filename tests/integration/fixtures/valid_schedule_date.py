valid_schedules = [
  {
    'schedule': '* * * * *',
    'prev_prev': '2020-02-08T09:30:00',
    'prev': '2020-02-08T09:31:00',
    'now': '2020-02-08T09:32:00',
    'next': '2020-02-08T09:32:00',
    'next_next': '2020-02-08T09:33:00'
  },
  {
    'schedule': '* * * * *',
    'prev_prev': '2020-02-08T09:31:00',
    'prev': '2020-02-08T09:32:00',
    'now': '2020-02-08T09:32:15',
    'next': '2020-02-08T09:33:00',
    'next_next': '2020-02-08T09:34:00',
  },
  {
    'schedule': '0 0 * * *',
    'prev_prev': '2020-02-03T00:00:00',
    'prev': '2020-02-04T00:00:00',
    'now': '2020-02-05T00:00:00',
    'next': '2020-02-05T00:00:00',
    'next_next': '2020-02-06T00:00:00'
  },
  {
    'schedule': '0 0 * * *',
    'prev_prev': '2020-02-04T00:00:00',
    'prev': '2020-02-05T00:00:00',
    'now': '2020-02-05T00:00:01',
    'next': '2020-02-06T00:00:00',
    'next_next': '2020-02-07T00:00:00'
  },
  {
    'schedule': '*/5 * * * *',
    'prev_prev': '2020-02-08T09:25:00',
    'prev': '2020-02-08T09:30:00',
    'now': '2020-02-08T09:32:15',
    'next': '2020-02-08T09:35:00',
    'next_next': '2020-02-08T09:40:00',
  },
  {
    'schedule': '30 1 * * *',
    'prev_prev': '2020-12-30T01:30:00',
    'prev': '2020-12-31T01:30:00',
    'now': '2020-12-31T09:32:15',
    'next': '2021-01-01T01:30:00',
    'next_next': '2021-01-02T01:30:00'
  },
  {
    'schedule': '30 1 * * *',
    'prev_prev': '2020-02-27T01:30:00',
    'prev': '2020-02-28T01:30:00',
    'now': '2020-02-28T09:32:15',
    'next': '2020-02-29T01:30:00',
    'next_next': '2020-03-01T01:30:00'
  },
  {
    'schedule': '30 1 * * *',
    'prev_prev': '2021-02-27T01:30:00',
    'prev': '2021-02-28T01:30:00',
    'now': '2021-02-28T09:32:15',
    'next': '2021-03-01T01:30:00',
    'next_next': '2021-03-02T01:30:00'
  },
  {
    'schedule': '30 1 1 * *',
    'prev_prev': '2020-01-01T01:30:00',
    'prev': '2020-02-01T01:30:00',
    'now': '2020-02-08T09:32:00',
    'next': '2020-03-01T01:30:00',
    'next_next': '2020-04-01T01:30:00'
  },
  {
    'schedule': '* * * 1 *',
    'prev_prev': '2020-01-31T23:58:00',
    'prev': '2020-01-31T23:59:00',
    'now': '2020-02-08T09:32:00',
    'next': '2021-01-01T00:00:00',
    'next_next': '2021-01-01T00:01:00'
  },
  {
    'schedule': '30 1 * 1 *',
    'prev_prev': '2020-01-30T01:30:00',
    'prev': '2020-01-31T01:30:00',
    'now': '2020-10-31T09:32:00',
    'next': '2021-01-01T01:30:00',
    'next_next': '2021-01-02T01:30:00'
  },
  {
    'schedule': '30 1 1 1 *',
    'prev_prev': '2019-01-01T01:30:00',
    'prev': '2020-01-01T01:30:00',
    'now': '2020-02-08T09:32:00',
    'next': '2021-01-01T01:30:00',
    'next_next': '2022-01-01T01:30:00'
  },
  {
    'schedule': '30 1 * * SAT',
    'prev_prev': '2020-12-12T01:30:00',
    'prev': '2020-12-19T01:30:00',
    'now': '2020-12-25T09:32:00',
    'next': '2020-12-26T01:30:00',
    'next_next': '2021-01-02T01:30:00'
  },
  {
    'schedule': '30 1 * * MON-FRI',
    'prev_prev': '2020-12-30T01:30:00',
    'prev': '2020-12-31T01:30:00',
    'now': '2020-12-31T09:32:00',
    'next': '2021-01-01T01:30:00',
    'next_next': '2021-01-04T01:30:00'
  },
  {
    'schedule': '1-30/10 * * * MON-FRI',
    'prev_prev': '2020-02-05T09:11:00',
    'prev': '2020-02-05T09:21:00',
    'now': '2020-02-05T09:32:00',
    'next': '2020-02-05T10:01:00',
    'next_next': '2020-02-05T10:11:00'
  },
  {
    'schedule': '* * * * MON-FRI',
    'prev_prev': '2020-02-04T23:58:00',
    'prev': '2020-02-04T23:59:00',
    'now': '2020-02-05T00:00:00',
    'next': '2020-02-05T00:00:00',
    'next_next': '2020-02-05T00:01:00'
  },
  {
    'schedule': '*/10 * * * MON-FRI',
    'prev_prev': '2020-02-05T09:10:00',
    'prev': '2020-02-05T09:20:00',
    'now': '2020-02-05T09:30:00',
    'next': '2020-02-05T09:30:00',
    'next_next': '2020-02-05T09:40:00'
  },
  {
    'schedule': '* 6 * * 1',
    'prev_prev': '2013-02-04T06:58:00',
    'prev': '2013-02-04T06:59:00',
    'now': '2013-02-08T09:32:15',
    'next': '2013-02-11T06:00:00',
    'next_next': '2013-02-11T06:01:00'
  },
  {
    'schedule': '* 6 * * 1',
    'prev_prev': '2013-02-04T06:58:00+00:00',
    'prev': '2013-02-04T06:59:00+00:00',
    'now': '2013-02-08T09:32:15+00:00',
    'next': '2013-02-11T06:00:00+00:00',
    'next_next': '2013-02-11T06:01:00+00:00'
  },
  {
    'schedule': '* 6 * * 1',
    'prev_prev': '2013-02-04T06:58:00+02:00',
    'prev': '2013-02-04T06:59:00+02:00',
    'now': '2013-02-08T09:32:15+02:00',
    'next': '2013-02-11T06:00:00+02:00',
    'next_next': '2013-02-11T06:01:00+02:00'
  }
]

valid_schedules_timezone = [
  {
    'schedule': '10 1 * 6 *',
    'timezone': 'Etc/UTC'
  },
  {
    'schedule': '10 1 * 6 *',
    'timezone': 'Europe/Rome'
  },
  {
    'schedule': '10 1 * 6 *',
    'timezone': 'America/New_York'
  }
]
