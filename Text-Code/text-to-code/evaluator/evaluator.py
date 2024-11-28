# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.
import os
import logging
import argparse
from bleu import _bleu
import json

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description='Evaluate leaderboard predictions for code completion (line level).')
    parser.add_argument('--answers', '-a', required=True, help="filename of the labels, in json format.")
    parser.add_argument('--predictions', '-p', required=True, help="filename of the leaderboard predictions, in txt format.")
    args = parser.parse_args()

    preds = open(args.predictions, "r").readlines()
    gts = open(args.answers, "r").readlines()

    assert len(preds) == len(gts), f"Samples of predictions and answers are not equal, {len(preds)}: {len(gts)}"

    total = len(gts)
    EM = 0.0
    
    ground_truth_path = os.path.splitext(args.predictions)[0] + '-ground_truth.txt'
    logger.info(f'ground_truth_path: {ground_truth_path}')

    with open(ground_truth_path, "w") as wf:
        for pred, gt in zip(preds, gts):
            pred = pred.strip()
            gt = json.loads(gt)["code"]
            wf.write(gt+"\n")
            if pred.split() == gt.split():
                EM += 1

    bleu_score = round(_bleu(ground_truth_path, args.predictions), 2)
    logger.info(f"BLEU: {bleu_score}%, EM: {round(EM/total*100, 2)}%")

    scores = {
        "BLEU": bleu_score,
        "EM": round(EM / total * 100, 2)
    }

    # Change the extension to .json
    json_file_path = os.path.splitext(args.predictions)[0] + '-evaluation_results.json'

    # Write the dictionary to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(scores, json_file, indent=4)

    # Log the action
    logger.info(f"Scores written to {json_file_path}")


if __name__ == "__main__":
    main()
