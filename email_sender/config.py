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
        'email_sender.tasks.send_reset_password_link_to_email': {
            'queue': 'scheduled_emails'
        },
        'email_sender.tasks.send__make_offer_mail': {
            'queue': 'scheduled_emails'
        },
        'email_sender.tasks.send_registration_link_to_email': {
            'queue': 'scheduled_emails'
        },
        'email_sender.tasks.send_win_auction_mail': {
                    'queue': 'scheduled_emails'
                },

    },
    'accept_content': ['json', 'application/x-python-serialize'],
    'task_serializer': 'json',
    'result_serializer': 'json',
    'event_serializer': 'json',
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
