
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('model', type=str, help='Type of model')
    parser.add_argument('--verbose', action='store_true')

    args = parser.parse_args()
    main(args)