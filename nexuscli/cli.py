import click


@click.group()
def cli():
    pass


from nexuscli import profiles, auth, orgs, projects, resources, views, schemas, acls
