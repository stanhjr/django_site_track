"""
Hello dear friend, I know that the code looks terrible, there were reasons for that

if you need help with the project, you can write to me on this email stanhjrpower@gmail.com
"""

from email_sender.tasks import app


if __name__ == "__main__":
    argv = [
        'worker',
        '-B',
        '--loglevel=DEBUG',
        '--without-heartbeat',
        '--without-mingle',
        '--without-gossip',
        '--queues=scheduled_emails,contact_us'
    ]
    app.worker_main(argv)