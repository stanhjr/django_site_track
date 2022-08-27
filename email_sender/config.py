config = {
    'imports': ('email_sender.tasks',),
    'database_engine_options': {'echo': False},
    'worker_concurrency': 2,
    'task_acks_late': True,
    'task_annotations': {
        'email_sender.tasks.send_auction_win': {
            'queue': 'scheduled_emails'
        },
        'email_sender.tasks.send_mail_contact_us': {
            'queue': 'scheduled_emails'
        },

    },
    'accept_content': ['json', 'pickle', 'application/x-python-serialize'],
    'task_serializer': 'pickle',
    'result_serializer': 'pickle',
    'event_serializer': 'pickle',
    'result_expires': 7200,
    'task_compression': 'gzip',
    'result_compression': 'gzip',
    'task_default_queue': 'email_checker',
    'redis_max_connections': 2,
    'broker_transport_options': {
        'max_connections': 2
    },
    'broker_pool_limit': 2
}