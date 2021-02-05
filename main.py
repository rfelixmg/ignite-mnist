from argparse import ArgumentParser
import os

from gsync.sync import gsutil_sync

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def sync_dataset(args):

	# data set dir in the server
	dataset_dir = f'{args.basedir}/'

	# sync from google cloud
	gsutil_sync(
        push=False,
        bucket_name='aiml-dst-ids',
        file_system_root=dataset_dir,
        folder_name='experiments',
        bucket_prefix_folder='rfelix')

	# treat data, if zip's etc...


def main(args):

	print("[main.start] of the program")
	if args.save_file:
		 with open(f'{args.basedir}//test/hello.text', 'w') as file_handler:
		 	file_handler.write("Hello world from file!\n")
	else:
		 with open(f'{args.basedir}/hello.text', 'r') as file_handler:
		 	lines = file_handler.readlines()
		 	_ = [print(f) for f in lines]

	sync_dataset(args)

	print("[end.start] of the program")



if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument(
        "--save_file",
        type=str2bool,
        default=True,
        help="Saving file",
    )
    parser.add_argument(
        "--basedir",
        type=str,
        default='/tmp',
        help="Saving file",
    )

    main(parser.parse_args())

