    import argparse
    import os
    from src.core import DiskSpaceManager

    def main():
        parser = argparse.ArgumentParser(description='Disk Space Manager')
        parser.add_argument('--analyze', action='store_true', help='Analyze disk space')
        parser.add_argument('--cleanup', action='store_true', help='Cleanup disk space')
        args = parser.parse_args()

        if args.analyze:
            manager = DiskSpaceManager()
            manager.analyze()
        elif args.cleanup:
            manager = DiskSpaceManager()
            manager.cleanup()

    if __name__ == '__main__':
        main()
