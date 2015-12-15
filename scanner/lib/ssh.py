
import paramiko, base64

from django.conf import settings

from scanner.jobs.models import Credential


def connect(hostname, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, port=22, username=username, password=password, timeout=settings.SSH_TIMEOUT)

        if _is_connected(client) is False:
            return False

        client.close()
        return True
    except:
        return False

def _is_connected(client):
    transport = client.get_transport() if client else None
    return transport and transport.is_active()

def persist_valid_credential(hostname, username, password):
    Credential.objects.create(
        hostname=hostname,
        username=username,
        password=password,
    )
