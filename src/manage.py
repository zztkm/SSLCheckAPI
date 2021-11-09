import argparse


def runserver():
    from app import app
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", port=8080)


# コマンドライン引数パーサー
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# サブコマンド: runserver
parser_runserver = subparsers.add_parser("runserver")
parser_runserver.set_defaults(handler=runserver)

if __name__ == "__main__":
    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler()
    else:
        parser.print_help()
