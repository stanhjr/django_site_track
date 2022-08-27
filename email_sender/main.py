"""This module contains src worker start script for scheduled_updates domain."""

from email_sender.tasks import app


if __name__ == "__main__":
    argv = [
        'worker',
        '-B',
        '--loglevel=DEBUG',
        '--without-heartbeat',
        '--without-mingle',
        '--without-gossip',
        '--queues=scheduled_emails'
    ]
    app.worker_main(argv)