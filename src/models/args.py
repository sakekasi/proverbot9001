#!/usr/bin/env python3

import argparse
from typing import List, Dict, Any

from tokenizer import Tokenizer, tokenizers
from context_filter import get_context_filter

from torch import optim

optimizers = {
    "SGD": optim.SGD,
    "Adam": optim.Adam,
}
def add_std_args(parser : argparse.ArgumentParser,
                 default_values : Dict[str, Any] = {}) -> None:
    parser.add_argument("scrape_file")
    parser.add_argument("save_file")
    parser.add_argument("--num-epochs", dest="num_epochs", type=int,
                        default=default_values.get("num-epochs", 20))
    parser.add_argument("--batch-size", dest="batch_size", type=int,
                        default=default_values.get("batch-size", 256))
    parser.add_argument("--max-length", dest="max_length", type=int,
                        default=default_values.get("max-length", 100))
    parser.add_argument("--max-tuples", dest="max_tuples", type=int,
                        default=default_values.get("max-tuples", None))
    parser.add_argument("--print-every", dest="print_every", type=int,
                        default=default_values.get("print-every", 5))
    parser.add_argument("--hidden-size", dest="hidden_size", type=int,
                        default=default_values.get("hidden-size", 128))
    parser.add_argument("--learning-rate", dest="learning_rate", type=float,
                        default=default_values.get("learning-rate", .7))
    parser.add_argument("--epoch-step", dest="epoch_step", type=int,
                        default=default_values.get("epoch-step", 10))
    parser.add_argument("--gamma", dest="gamma", type=float,
                        default=default_values.get("gamma", 0.8))
    parser.add_argument("--num-encoder-layers", dest="num_encoder_layers", type=int,
                        default=default_values.get("num-encoder-layers", 3))
    parser.add_argument("--num-decoder-layers", dest="num_decoder_layers", type=int,
                        default=default_values.get("num-decoder-layers", 3))
    parser.add_argument("--num-keywords", dest="num_keywords", type=int,
                        default=default_values.get("num-keywordes", 60))
    parser.add_argument("--tokenizer", choices=list(tokenizers.keys()), type=str,
                        default=default_values.get("tokenizer",
                                                   list(tokenizers.keys())[0]))
    parser.add_argument("--optimizer",
                        choices=list(optimizers.keys()), type=str,
                        default=default_values.get("optimizer",
                                                   list(optimizers.keys())[0]))
    parser.add_argument("--context-filter", dest="context_filter", type=str,
                        default=default_values.get("context-filter",
                                                   "goal-changes%no-args"))

def start_std_args(description : str, default_values : Dict[str, Any] = {}) \
    -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    add_std_args(parser, default_values)
    return parser

def take_std_args(args : List[str], description : str,
                  default_values : Dict[str, Any] = {}) -> argparse.Namespace:
    return start_std_args(description, default_values).parse_args(args)
