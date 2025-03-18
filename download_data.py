import click


@click.command()
@click.argument('experiment', type=click.STRING)
def download_data(experiment):
    pass
    # Download data for the given experiment

if __name__ == '__main__':
    download_data()