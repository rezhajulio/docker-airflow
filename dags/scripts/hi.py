import cowsay
import click


@click.command()
@click.option('--name', prompt='Your name', default="Cow")
def main(name):
    print(cowsay.cow(f"Hi, I am {name}. Nice to meet you!"))


if __name__ == "__main__":
    main()