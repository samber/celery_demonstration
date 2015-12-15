from    __future__                      import absolute_import

from    ipaddress                       import IPv4Address

from    django.utils                    import timezone

from    scanner.jobs.models             import Credential
from    scanner.jobs.celery             import app
from    scanner.lib                     import ssh


@app.task(bind=True, ignore_result=True)
def                     fill_queue(self, params):
    print(params)
    for i in range(0, params["gap"]):
        # ip to scan
        hostname = IPv4Address(params["from"]) + i

        # quit when 255.255.255.255 + 1 == 0.0.0.0
        if hostname < IPv4Address(params["from"]):
            return

        test_credentials.delay({
            "hostname": hostname.exploded,
            "username": params["username"],
            "password": params["password"]
        })

    params["from"] = (IPv4Address(params["from"]) + params["gap"]).exploded
    fill_queue.delay(params)


@app.task(bind=True, ignore_result=True)
def                     test_credentials(self, credentials):
    if ssh.connect(credentials["hostname"], credentials["username"], credentials["password"]) is True:
        ssh.persist_valid_credential(credentials["hostname"], credentials["username"], credentials["password"])
    print(credentials["username"] + ":" + credentials["password"] + "@" + credentials["hostname"])




@app.task(bind=True, ignore_result=True)
def                     check_still_valid_credentials(self):
    servers = Credential.objects.all()
    for server in servers:
        if ssh.connect(server.hostname, server.username, server.password) is False:
            server.delete()

