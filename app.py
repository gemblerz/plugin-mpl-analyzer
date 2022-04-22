import argparse
import logging

from waggle.plugin import Plugin

def run(args):
    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S')
    with Plugin() as plugin:
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-debug', dest='debug',
        action='store_true', default=False,
        help='Debug flag')
    parser.add_argument(
        '-stream', dest='stream',
        action='store', default="camera",
        help='ID or name of a stream, e.g. sample')
    parser.add_argument(
        '-object', dest='object',
        action='append',
        help='Object name to count')
    parser.add_argument(
        '-all-objects', dest='all_objects',
        action='store_true', default=False,
        help='Consider all registered objects to detect')
    parser.add_argument(
        '-model', dest='model',
        action='store', default='coco_ssd_resnet50_300_fp32.pth',
        help='Path to model')
    parser.add_argument(
        '-image-size', dest='image_size',
        action='store', default=300, type=int,
        help='Input image size')
    parser.add_argument(
        '-confidence-level', dest='confidence_level',
        action='store', default=0.4,
        help='Confidence level [0. - 1.] to filter out result')
    parser.add_argument(
        '-continuous', dest='continuous',
        action='store_true', default=False,
        help='Flag to run this plugin forever')
    parser.add_argument(
        '-interval', dest='interval',
        action='store', default=0, type=int,
        help='Inference interval in seconds')
    parser.add_argument(
        '-sampling-interval', dest='sampling_interval',
        action='store', default=-1, type=int,
        help='Sampling interval between inferencing')
    run(parser.parse_args())
